"""
multi_run_experiment.py
=======================
Jalankan script ini di VS Code (folder RTI/) untuk menghasilkan
5 run eksperimen NB vs RF dengan seed berbeda.

Struktur folder yang dibutuhkan:
RTI/
├── Dataset/
│   └── gojek_labeled.csv
├── results/
│   └── (output akan disimpan di sini)
└── multi_run_experiment.py

Cara jalankan:
  python multi_run_experiment.py

Output:
  results/log_NB_run{01-05}.json
  results/log_RF_run{01-05}.json
  results/semua_hasil.csv
  results/rekap_statistik.csv
"""

import random
import time
import json
import os
import warnings
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# KONFIGURASI — ubah sesuai kebutuhan
# ─────────────────────────────────────────────────────────────────────────────
CONFIG = {
    "data_path"        : r"Dataset/gojek_labeled.csv",
    "results_dir"      : "results",
    "n_sample"         : 100000,        # total sampel (50k pos + 50k neg)
    "test_size"        : 0.2,           # 80:20 split
    "tfidf_max_features": 5000,
    "tfidf_ngram_range": (1, 1),
    "nb_alpha"         : 1.0,
    "rf_n_estimators"  : 100,
    "rf_max_depth"     : None,
    # 5 seed yang sudah ditentukan sebelum eksperimen
    "seeds"            : [42, 123, 456, 789, 2024],
}

os.makedirs(CONFIG["results_dir"], exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# LOAD & SAMPLING DATA
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 60)
print("MULTI-RUN EXPERIMENT: Naive Bayes vs Random Forest")
print("Dataset: Ulasan Aplikasi Gojek (Bahasa Indonesia)")
print("=" * 60)

print(f"\n[LOAD] Membaca dataset dari {CONFIG['data_path']} ...")
df_raw = pd.read_csv(CONFIG["data_path"])
print(f"       Total baris awal  : {len(df_raw):,}")

# Hapus content kosong
df_raw = df_raw.dropna(subset=["content"])
df_raw = df_raw[df_raw["content"].str.strip() != ""]
print(f"       Setelah cleaning  : {len(df_raw):,}")
print(f"       Positif           : {(df_raw['sentiment']=='positif').sum():,}")
print(f"       Negatif           : {(df_raw['sentiment']=='negatif').sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# FUNGSI SAMPLING STRATIFIED (seed-dependent)
# ─────────────────────────────────────────────────────────────────────────────
def get_sample(df, n_total, seed):
    """Stratified random sampling: n_total/2 per kelas."""
    n_per_class = n_total // 2
    pos = df[df["sentiment"] == "positif"].sample(n=n_per_class, random_state=seed)
    neg = df[df["sentiment"] == "negatif"].sample(n=n_per_class, random_state=seed)
    sample = pd.concat([pos, neg]).sample(frac=1, random_state=seed).reset_index(drop=True)
    return sample

# ─────────────────────────────────────────────────────────────────────────────
# FUNGSI SATU RUN EKSPERIMEN
# ─────────────────────────────────────────────────────────────────────────────
def run_experiment(algo_name, clf, seed, run_num):
    """Jalankan satu run eksperimen dan kembalikan dict hasil + simpan log JSON."""

    # Set seed global
    random.seed(seed)
    np.random.seed(seed)

    # Sampling
    df_sample = get_sample(df_raw, CONFIG["n_sample"], seed)
    X = df_sample["content"].astype(str).values
    y = df_sample["sentiment"].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=CONFIG["test_size"],
        random_state=seed,
        stratify=y
    )

    # TF-IDF (fit HANYA pada training set)
    tfidf = TfidfVectorizer(
        max_features=CONFIG["tfidf_max_features"],
        ngram_range=CONFIG["tfidf_ngram_range"]
    )
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf  = tfidf.transform(X_test)

    # Training + timing
    t_start = time.time()
    clf.fit(X_train_tfidf, y_train)
    t_train = round(time.time() - t_start, 4)

    # Prediksi & metrik
    y_pred = clf.predict(X_test_tfidf)
    acc  = round(accuracy_score(y_test, y_pred) * 100, 2)
    pre  = round(precision_score(y_test, y_pred, average="weighted", zero_division=0) * 100, 2)
    rec  = round(recall_score(y_test, y_pred, average="weighted", zero_division=0) * 100, 2)
    f1   = round(f1_score(y_test, y_pred, average="weighted", zero_division=0) * 100, 2)
    cm   = confusion_matrix(y_test, y_pred, labels=["negatif", "positif"])

    result = {
        "run_id"       : f"run-{algo_name.replace(' ','')}-{run_num:02d}",
        "timestamp"    : datetime.now().isoformat(),
        "skenario"     : algo_name,
        "seed"         : seed,
        "n_sample"     : CONFIG["n_sample"],
        "test_size"    : CONFIG["test_size"],
        "tfidf_max_features": CONFIG["tfidf_max_features"],
        "accuracy"     : acc,
        "precision"    : pre,
        "recall"       : rec,
        "f1_score"     : f1,
        "waktu_latih_detik": t_train,
        "confusion_matrix": {
            "TN": int(cm[0][0]),
            "FP": int(cm[0][1]),
            "FN": int(cm[1][0]),
            "TP": int(cm[1][1]),
        },
        "anomali"      : "NONE",
        "catatan"      : ""
    }

    # Validasi range metrik
    for k in ["accuracy","precision","recall","f1_score"]:
        if not (0 <= result[k] <= 100):
            result["anomali"] = f"RANGE ERROR: {k}={result[k]}"

    # Simpan log JSON
    log_name = f"log_{algo_name.replace(' ','_')}_run{run_num:02d}.json"
    log_path = os.path.join(CONFIG["results_dir"], log_name)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    return result

# ─────────────────────────────────────────────────────────────────────────────
# EKSEKUSI SEMUA RUN
# ─────────────────────────────────────────────────────────────────────────────
all_results = []
seeds = CONFIG["seeds"]

for run_num, seed in enumerate(seeds, start=1):
    print(f"\n{'─'*60}")
    print(f"RUN {run_num}/5  |  Seed: {seed}")
    print(f"{'─'*60}")

    # Naive Bayes
    print(f"  [NB]  Training Naive Bayes (MultinomialNB)...")
    nb_clf = MultinomialNB(alpha=CONFIG["nb_alpha"])
    nb_res = run_experiment("NB", nb_clf, seed, run_num)
    all_results.append(nb_res)
    print(f"         Acc:{nb_res['accuracy']}%  Pre:{nb_res['precision']}%  "
          f"Rec:{nb_res['recall']}%  F1:{nb_res['f1_score']}%  "
          f"t={nb_res['waktu_latih_detik']}s  Anomali:{nb_res['anomali']}")

    # Random Forest
    print(f"  [RF]  Training Random Forest (n_estimators={CONFIG['rf_n_estimators']})...")
    rf_clf = RandomForestClassifier(
        n_estimators=CONFIG["rf_n_estimators"],
        max_depth=CONFIG["rf_max_depth"],
        random_state=seed,
        n_jobs=-1   # paralelisasi — pakai semua core agar lebih cepat
    )
    rf_res = run_experiment("RF", rf_clf, seed, run_num)
    all_results.append(rf_res)
    print(f"         Acc:{rf_res['accuracy']}%  Pre:{rf_res['precision']}%  "
          f"Rec:{rf_res['recall']}%  F1:{rf_res['f1_score']}%  "
          f"t={rf_res['waktu_latih_detik']}s  Anomali:{rf_res['anomali']}")

# ─────────────────────────────────────────────────────────────────────────────
# SIMPAN SEMUA HASIL KE CSV
# ─────────────────────────────────────────────────────────────────────────────
df_all = pd.DataFrame(all_results)
csv_all_path = os.path.join(CONFIG["results_dir"], "semua_hasil.csv")
df_all.to_csv(csv_all_path, index=False)
print(f"\n[SAVED] semua_hasil.csv ({len(df_all)} baris)")

# ─────────────────────────────────────────────────────────────────────────────
# REKAP STATISTIK (mean ± std per algoritma)
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("REKAP STATISTIK (mean ± std, N=5 per algoritma)")
print(f"{'='*60}")

rekap_rows = []
for algo in ["NB", "RF"]:
    df_algo = df_all[df_all["skenario"] == algo]
    row = {"algoritma": algo, "n_runs": len(df_algo)}
    for metrik in ["accuracy","precision","recall","f1_score","waktu_latih_detik"]:
        mean_val = round(df_algo[metrik].mean(), 2)
        std_val  = round(df_algo[metrik].std(), 2)
        row[f"{metrik}_mean"] = mean_val
        row[f"{metrik}_std"]  = std_val
        unit = "s" if metrik == "waktu_latih_detik" else "%"
        print(f"  {algo} | {metrik:<22}: {mean_val} ± {std_val} {unit}")
    rekap_rows.append(row)

df_rekap = pd.DataFrame(rekap_rows)
rekap_path = os.path.join(CONFIG["results_dir"], "rekap_statistik.csv")
df_rekap.to_csv(rekap_path, index=False)
print(f"\n[SAVED] rekap_statistik.csv")

# ─────────────────────────────────────────────────────────────────────────────
# SELISIH ANTAR ALGORITMA
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("SELISIH RF vs NB (mean)")
print(f"{'='*60}")
nb_row = df_rekap[df_rekap["algoritma"] == "NB"].iloc[0]
rf_row = df_rekap[df_rekap["algoritma"] == "RF"].iloc[0]
for metrik in ["accuracy","precision","recall","f1_score"]:
    selisih = round(rf_row[f"{metrik}_mean"] - nb_row[f"{metrik}_mean"], 2)
    arah = "RF unggul" if selisih > 0 else "NB unggul"
    print(f"  {metrik:<22}: {selisih:+.2f}%  ({arah})")

print(f"\n{'='*60}")
print("SELESAI. Cek folder results/ untuk semua output.")
print(f"{'='*60}")
