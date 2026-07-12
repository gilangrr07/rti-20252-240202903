# Tahap 1 — Perancangan Desain Eksperimen & Arsitektur Pipeline

**Status:** Selesai

---

## 1. Komponen Sistem

1. **Dataset Loader** — membaca dataset publik Kaggle (ulasan aplikasi Gojek berbahasa Indonesia), memverifikasi kelengkapan dan distribusi label sentimen.
2. **Preprocessing Module** — pipeline seragam: case folding, cleansing (hapus simbol/angka/URL), stopword removal (NLTK Bahasa Indonesia), stemming (Sastrawi). Mengunci variabel kontrol (CV) preprocessing agar identik pada kedua kondisi algoritma.
3. **TF-IDF Vectorizer** — ekstraksi fitur (`max_features=5000`), di-fit **hanya pada data latih** untuk mencegah data leakage, lalu dipakai mentransformasi data uji.
4. **Classifier (swappable)** — komponen yang menjadi variabel independen (IV): Multinomial Naïve Bayes (`alpha=1.0`) atau Random Forest (`n_estimators=100`), keduanya dari scikit-learn.
5. **Evaluator** — menghitung accuracy, precision, recall, F1-score (average='weighted') via `classification_report`/`confusion_matrix`, menghasilkan variabel dependen (DV).

## 2. Alur Eksekusi Pipeline (Per Run)

```
Dataset mentah (Kaggle) → verifikasi label
  │
  ├─ Preprocessing (case folding → cleansing → stopword removal → stemming Sastrawi)
  │     └─ Cache hasil preprocessing (v2) agar tidak perlu diulang tiap replikasi
  │
  ├─ Stratified sampling per-seed (50k positif + 50k negatif dari korpus bersih)
  │
  ├─ Train-test split (80:20, random_state=seed, stratify=y)
  │
  ├─ TF-IDF Vectorizer — fit HANYA pada data latih, transform data uji
  │
  ├─ Classifier (swap: Naive Bayes ATAU Random Forest, parameter dikunci default)
  │
  └─ Evaluator → accuracy/precision/recall/F1 + confusion matrix → log JSON per run
```

Catatan: pada eksplorasi awal (notebook, single-run seed=42), seluruh langkah di atas dijalankan satu kali sebagai referensi pipeline. Pada tahap multi-run, langkah yang sama diulang 5 kali (seed berbeda) untuk tiap algoritma, menghasilkan 10 run per versi skrip.

**Fail-safe pipeline**: berbeda dari sistem produksi, pipeline ini bersifat riset — tidak ada mekanisme fail-closed/fail-open real-time. Penanganan anomali berfokus pada validasi otomatis (nilai metrik harus dalam [0,100], ditandai di field `anomali` pada log) dan investigasi manual pasca-eksekusi (lihat Tahap 3/4), bukan pemulihan otomatis saat run berjalan.

## 3. Skema Data (analog "skema database")

### 3.1 Struktur Dataset

```
gojek_labeled.csv
├── content         TEXT    -- teks ulasan mentah
└── sentiment       TEXT    -- label: 'positif' / 'negatif'

gojek_labeled_clean.csv (cache hasil preprocessing, dihasilkan v2)
├── content         TEXT
├── content_clean   TEXT    -- hasil case folding+cleansing+stopword+stemming
└── sentiment       TEXT
```

### 3.2 Struktur Log Eksperimen (JSON per run)

```json
{
  "run_id": "run-NB-01-v2",
  "timestamp": "2026-07-12T01:32:04.558394",
  "skenario": "NB",
  "seed": 42,
  "n_sample": 100000,
  "test_size": 0.2,
  "tfidf_max_features": 5000,
  "preprocessing": "case_folding+cleansing+stopword_removal+sastrawi_stemming",
  "metric_average": "weighted",
  "accuracy": 89.20,
  "precision": 89.61,
  "recall": 89.20,
  "f1_score": 89.18,
  "waktu_latih_detik": 0.3694,
  "confusion_matrix": {"TN": 9423, "FP": 577, "FN": 1582, "TP": 8418},
  "anomali": "NONE",
  "catatan": ""
}
```

Field `preprocessing` dan `metric_average` ditambahkan pada versi v2 sebagai bagian dari perbaikan transparansi metodologi (lihat Tahap 3).

## 4. Keputusan Teknis (Final)

1. **Mode eksperimen**: dua versi skrip (`v1` tanpa preprocessing, `v2` dengan preprocessing lengkap) — bukan by design sejak awal, melainkan hasil revisi setelah anomali ditemukan (lihat Tahap 3). Keduanya dipertahankan untuk memungkinkan analisis sensitivitas.
2. **Algoritma**: Multinomial Naïve Bayes vs Random Forest Classifier, keduanya dari scikit-learn, parameter default (tanpa tuning manual) untuk menghindari bias yang menguntungkan salah satu algoritma.
3. **Ekstraksi fitur**: TF-IDF Vectorizer, `max_features=5000`, `ngram_range=(1,1)`.
4. **Sumber data**: dataset publik Kaggle — dipilih karena stabil dan dapat direplikasi ulang oleh peneliti lain, tidak bergantung pada scraping mandiri yang rentan perubahan kebijakan API.
5. **Seed replikasi**: 5 nilai pre-determined (42, 123, 456, 789, 2024), ditentukan sebelum eksekusi (bukan dipilih setelah melihat hasil).
6. **Lingkungan eksekusi**: Google Colab untuk eksplorasi notebook; lokal (VS Code, Windows) untuk skrip multi-run.