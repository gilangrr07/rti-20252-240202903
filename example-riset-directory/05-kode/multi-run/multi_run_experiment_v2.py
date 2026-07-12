"""
multi_run_experiment_v2.py
===========================
Versi REVISI dari multi_run_experiment.py — menambahkan pipeline preprocessing
lengkap (case folding, cleansing, stopword removal NLTK, stemming Sastrawi)
SEBELUM sampling & split, agar konsisten dengan notebook sentimen_gojek.ipynb
dan dengan proposal (bagian E.2 — variabel kontrol preprocessing).

Perubahan dari versi lama:
  1. Preprocessing (case folding -> cleansing -> stopword removal -> stemming)
     diterapkan SEKALI ke seluruh dataset mentah, di-cache ke CSV supaya tidak
     perlu stemming ulang setiap kali script dijalankan (stemming lambat).
  2. Sampling & split dilakukan pada teks yang SUDAH bersih (content_clean),
     bukan teks mentah.
  3. Baris yang jadi kosong setelah preprocessing dibuang (sama seperti notebook).
  4. Metrik precision/recall/f1 tetap dihitung dengan average='weighted' (bukan
     binary pos_label seperti notebook) supaya definisi metrik konsisten di
     seluruh 10 run -- perbedaan definisi metrik dengan notebook dicatat
     eksplisit di dokumentasi, BUKAN disembunyikan.

Struktur folder yang dibutuhkan (sama seperti versi lama):
RTI/
├── Dataset/
│   └── gojek_labeled.csv
├── results/
│   └── (output v2 akan disimpan di sini, terpisah dari hasil lama)
└── multi_run_experiment_v2.py

Cara jalankan:
  python multi_run_experiment_v2.py

Catatan: run pertama akan lebih lambat (~5-15 menit) karena melakukan stemming
Sastrawi ke seluruh dataset. Hasil preprocessing di-cache ke
Dataset/gojek_labeled_clean.csv sehingga run berikutnya (jika script dijalankan
ulang) langsung memakai cache dan jauh lebih cepat.

Output:
  results/log_NB_run{01-05}_v2.json
  results/log_RF_run{01-05}_v2.json
  results/semua_hasil_v2.csv
  results/rekap_statistik_v2.csv
"""

import random
import time
import json
import os
import re
import warnings
import numpy as np
import pandas as pd
from datetime import datetime

import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# KONFIGURASI
# ─────────────────────────────────────────────────────────────────────────────
CONFIG = {
    "data_path"         : r"Dataset/gojek_labeled.csv",
    "data_clean_cache"  : r"Dataset/gojek_labeled_clean.csv",
    "results_dir"       : "results",
    "n_sample"          : 100000,
    "test_size"         : 0.2,
    "tfidf_max_features": 5000,
    "tfidf_ngram_range" : (1, 1),
    "nb_alpha"          : 1.0,
    "rf_n_estimators"   : 100,
    "rf_max_depth"      : None,
    "seeds"             : [42, 123, 456, 789, 2024],
}

os.makedirs(CONFIG["results_dir"], exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# PREPROCESSING — identik dengan sentimen_gojek.ipynb
# ─────────────────────────────────────────────────────────────────────────────
nltk.download("stopwords", quiet=True)
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stop_words_id = set(stopwords.words("indonesian"))

def preprocess(text):
    """
    Pipeline preprocessing (SAMA PERSIS dengan notebook):
    1. Case folding      — ubah ke huruf kecil
    2. Cleansing         — hapus URL, angka, simbol, karakter non-alfabet
    3. Stopword removal  — hapus stopword Bahasa Indonesia (NLTK)
    4. Stemming          — reduksi ke bentuk dasar (Sastrawi)
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words_id]
    tokens = [stemmer.stem(t) for t in tokens]
    return " ".join(tokens)

# ─────────────────────────────────────────────────────────────────────────────
# LOAD & PREPROCESS DATA (dengan cache)
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 60)
print("MULTI-RUN EXPERIMENT v2: Naive Bayes vs Random Forest")
print("Dengan preprocessing lengkap (case folding, cleansing,")
print("stopword removal, stemming Sastrawi)")
print("=" * 60)

if os.path.exists(CONFIG["data_clean_cache"]):
    print(f"\n[CACHE] Memuat data yang sudah dipreprocessing dari {CONFIG['data_clean_cache']} ...")
    df_raw = pd.read_csv(CONFIG["data_clean_cache"])
    print(f"        Total baris (cached) : {len(df_raw):,}")
else:
    print(f"\n[LOAD] Membaca dataset mentah dari {CONFIG['data_path']} ...")
    df_raw = pd.read_csv(CONFIG["data_path"])
    df_raw = df_raw.dropna(subset=["content"])
    df_raw = df_raw[df_raw["content"].str.strip() != ""]
    print(f"       Total baris awal (setelah drop kosong) : {len(df_raw):,}")

    print(f"\n[PREPROCESS] Menjalankan case folding -> cleansing -> stopword removal -> stemming ...")
    print(f"             (estimasi 5-15 menit tergantung ukuran data & CPU)")
    t0 = time.time()
    df_raw["content_clean"] = df_raw["content"].apply(preprocess)
    elapsed = time.time() - t0
    print(f"[PREPROCESS] Selesai dalam {elapsed/60:.1f} menit")

    n_before = len(df_raw)
    df_raw = df_raw[df_raw["content_clean"].str.strip() != ""].reset_index(drop=True)
    n_after = len(df_raw)
    print(f"[PREPROCESS] Baris dibuang karena kosong pasca-preprocessing: {n_before - n_after:,} "
          f"({(n_before-n_after)/n_before*100:.2f}%)")
    print(f"[PREPROCESS] Total baris setelah preprocessing: {n_after:,}")

    df_raw.to_csv(CONFIG["data_clean_cache"], index=False)
    print(f"[CACHE] Data bersih disimpan ke {CONFIG['data_clean_cache']} untuk run berikutnya")

print(f"\n       Positif : {(df_raw['sentiment']=='positif').sum():,}")
print(f"       Negatif : {(df_raw['sentiment']=='negatif').sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# SAMPLING STRATIFIED (seed-dependent) — pada content_clean, bukan content mentah
# ─────────────────────────────────────────────────────────────────────────────
def get_sample(df, n_total, seed):
    n_per_class = n_total // 2
    pos = df[df["sentiment"] == "positif"].sample(n=n_per_class, random_state=seed)
    neg = df[df["sentiment"] == "negatif"].sample(n=n_per_class, random_state=seed)
    sample = pd.concat([pos, neg]).sample(frac=1, random_state=seed).reset_index(drop=True)
    return sample

# ─────────────────────────────────────────────────────────────────────────────
# SATU RUN EKSPERIMEN
# ─────────────────────────────────────────────────────────────────────────────
def run_experiment(algo_name, clf, seed, run_num):
    random.seed(seed)
    np.random.seed(seed)

    df_sample = get_sample(df_raw, CONFIG["n_sample"], seed)
    X = df_sample["content_clean"].astype(str).values   # <-- pakai teks BERSIH
    y = df_sample["sentiment"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=CONFIG["test_size"], random_state=seed, stratify=y
    )

    tfidf = TfidfVectorizer(
        max_features=CONFIG["tfidf_max_features"],
        ngram_range=CONFIG["tfidf_ngram_range"]
    )
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf  = tfidf.transform(X_test)

    t_start = time.time()
    clf.fit(X_train_tfidf, y_train)
    t_train = round(time.time() - t_start, 4)

    y_pred = clf.predict(X_test_tfidf)
    acc  = round(accuracy_score(y_test, y_pred) * 100, 2)
    pre  = round(precision_score(y_test, y_pred, average="weighted", zero_division=0) * 100, 2)
    rec  = round(recall_score(y_test, y_pred, average="weighted", zero_division=0) * 100, 2)
    f1   = round(f1_score(y_test, y_pred, average="weighted", zero_division=0) * 100, 2)
    cm   = confusion_matrix(y_test, y_pred, labels=["negatif", "positif"])

    result = {
        "run_id"       : f"run-{algo_name.replace(' ','')}-{run_num:02d}-v2",
        "timestamp"    : datetime.now().isoformat(),
        "skenario"     : algo_name,
        "seed"         : seed,
        "n_sample"     : CONFIG["n_sample"],
        "test_size"    : CONFIG["test_size"],
        "tfidf_max_features": CONFIG["tfidf_max_features"],
        "preprocessing": "case_folding+cleansing+stopword_removal+sastrawi_stemming",
        "metric_average": "weighted",
        "accuracy"     : acc,
        "precision"    : pre,
        "recall"       : rec,
        "f1_score"     : f1,
        "waktu_latih_detik": t_train,
        "confusion_matrix": {
            "TN": int(cm[0][0]), "FP": int(cm[0][1]),
            "FN": int(cm[1][0]), "TP": int(cm[1][1]),
        },
        "anomali"      : "NONE",
        "catatan"      : ""
    }

    for k in ["accuracy","precision","recall","f1_score"]:
        if not (0 <= result[k] <= 100):
            result["anomali"] = f"RANGE ERROR: {k}={result[k]}"

    log_name = f"log_{algo_name.replace(' ','_')}_run{run_num:02d}_v2.json"
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

    print(f"  [NB]  Training Naive Bayes (MultinomialNB)...")
    nb_clf = MultinomialNB(alpha=CONFIG["nb_alpha"])
    nb_res = run_experiment("NB", nb_clf, seed, run_num)
    all_results.append(nb_res)
    print(f"         Acc:{nb_res['accuracy']}%  Pre:{nb_res['precision']}%  "
          f"Rec:{nb_res['recall']}%  F1:{nb_res['f1_score']}%  "
          f"t={nb_res['waktu_latih_detik']}s  Anomali:{nb_res['anomali']}")

    print(f"  [RF]  Training Random Forest (n_estimators={CONFIG['rf_n_estimators']})...")
    rf_clf = RandomForestClassifier(
        n_estimators=CONFIG["rf_n_estimators"],
        max_depth=CONFIG["rf_max_depth"],
        random_state=seed,
        n_jobs=-1
    )
    rf_res = run_experiment("RF", rf_clf, seed, run_num)
    all_results.append(rf_res)
    print(f"         Acc:{rf_res['accuracy']}%  Pre:{rf_res['precision']}%  "
          f"Rec:{rf_res['recall']}%  F1:{rf_res['f1_score']}%  "
          f"t={rf_res['waktu_latih_detik']}s  Anomali:{rf_res['anomali']}")

# ─────────────────────────────────────────────────────────────────────────────
# SIMPAN HASIL
# ─────────────────────────────────────────────────────────────────────────────
df_all = pd.DataFrame(all_results)
csv_all_path = os.path.join(CONFIG["results_dir"], "semua_hasil_v2.csv")
df_all.to_csv(csv_all_path, index=False)
print(f"\n[SAVED] semua_hasil_v2.csv ({len(df_all)} baris)")

rekap_rows = []
for algo in ["NB", "RF"]:
    df_algo = df_all[df_all["skenario"] == algo]
    row = {"algoritma": algo, "n_runs": len(df_algo)}
    for metrik in ["accuracy","precision","recall","f1_score","waktu_latih_detik"]:
        row[f"{metrik}_mean"] = round(df_algo[metrik].mean(), 2)
        row[f"{metrik}_std"]  = round(df_algo[metrik].std(), 2)
    rekap_rows.append(row)

df_rekap = pd.DataFrame(rekap_rows)
rekap_path = os.path.join(CONFIG["results_dir"], "rekap_statistik_v2.csv")
df_rekap.to_csv(rekap_path, index=False)
print(f"[SAVED] rekap_statistik_v2.csv")

print(f"\n{'='*60}")
print("SELESAI. Bandingkan results/semua_hasil_v2.csv (dgn preprocessing)")
print("dengan results/semua_hasil.csv (versi lama, tanpa preprocessing).")
print(f"{'='*60}")
