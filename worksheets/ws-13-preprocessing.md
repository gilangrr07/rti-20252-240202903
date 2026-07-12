# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG (Versi Notebook)

Dataset           : Ulasan aplikasi Gojek berbahasa Indonesia (Kaggle, kolom content & sentiment)
Jumlah data awal  : 100.000 (setelah stratified sampling 50.000 positif + 50.000 negatif dari dataset penuh)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Data terlalu pendek setelah stemming | 2.777 dari 100.000 (2.8%) | Listwise deletion (dibuang dari korpus) | Ulasan tersisa hanya 1-2 token setelah stopword removal & stemming, tidak informatif untuk TF-IDF |
| Missing/kosong pada kolom content | Ditangani oleh dropna() di kedua versi (notebook & script) | Listwise deletion | Baris tanpa teks tidak bisa diproses |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Case folding | content (teks ulasan) | Seluruh teks diubah ke huruf kecil | Menyamakan token "Bagus" dan "bagus" |
| Cleansing | content | Hapus simbol, angka, URL, karakter non-alfabet | Mengurangi noise token yang tidak bermakna |
| Stopword removal | content | 757 kata dari daftar stopword Bahasa Indonesia (NLTK) | Menghilangkan kata fungsi (dan, yang, di, ke, dll.) yang tidak diskriminatif |
| Stemming | content | Sastrawi (mengembalikan ke kata dasar) | Menyatukan variasi morfologis ("mengecewakan" → "kecewa") |

Normalization:
  Metode    : Tidak ada normalisasi numerik konvensional — transformasi utama adalah TF-IDF Vectorizer (max_features=5.000)
  Alasan    : TF-IDF secara inheren menghasilkan bobot ternormalisasi [0,1] per dokumen (L2 norm default scikit-learn).
  Parameter : TF-IDF di-fit HANYA pada data training (X_train), lalu ditransformasikan ke X_test

Leakage Check:
  [X] Parameter TF-IDF (vocabulary, IDF weights) dihitung dari training set saja, di kedua versi eksperimen
  [X] Train-test split (80:20, random_state tetap) dilakukan SEBELUM fit TF-IDF
  [~] Cleansing/stemming pada versi notebook dilakukan SEBELUM split — secara ketat ini bukan data leakage, tapi tetap perlu dicatat sebagai keputusan desain

Jumlah data akhir : Notebook — 97.223 baris (setelah cleaning); Script multi-run — 100.000 baris (tanpa cleaning morfologis)
Script tersedia   : [X] Ya → sentimen_gojek.ipynb (versi lengkap dengan preprocessing) dan multi_run_experiment.py (versi tanpa preprocessing linguistik)
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Ulasan terlalu pendek setelah stemming | 2.777 dari 100.000 (2,78%) | Listwise deletion | < 5%, tidak informatif secara semantik untuk TF-IDF (di bawah 1-2 token efektif) |
| Baris content kosong/NaN | Ditangani di tahap load (dropna) | Listwise deletion | Tidak bisa divectorisasi tanpa teks |

**Jumlah data sebelum cleaning:** 100.000
**Jumlah data setelah cleaning:** 97.223 (versi notebook)
**Persentase data yang hilang/berubah:** 2,78%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Fitur teks (setelah TF-IDF) | 0 – 1 per term-doc weight | Sparse, right-skewed (banyak nilai 0) | Tidak relevan (bukan numerik konvensional) | TF-IDF weighting + L2 norm (bawaan scikit-learn) | TF-IDF sudah menghasilkan bobot ternormalisasi antar-dokumen; normalisasi tambahan (min-max/z-score) tidak diperlukan dan berisiko merusak sparsity |
| waktu_latih_detik (metadata log) | 0.13s – 152s | Right-skewed (RF jauh lebih lambat) | Ya (RF training time bervariasi) | Tidak perlu dinormalisasi | Ini metadata eksekusi, bukan fitur model — dilaporkan apa adanya di tabel hasil (WS-12), bukan dinormalisasi |

**Apakah normalisasi diperlukan untuk fitur?** [ ] Ya [X] Tidak
**Justifikasi:**
> TF-IDF Vectorizer dari scikit-learn sudah menghasilkan representasi vektor yang ternormalisasi secara internal (L2 norm per dokumen), dan kedua model (MultinomialNB, RandomForestClassifier) tidak sensitif terhadap skala fitur dengan cara yang sama seperti model berbasis jarak (mis. KNN, SVM dengan kernel RBF), sehingga normalisasi tambahan tidak diperlukan.

**Leakage check:**
- [X] Parameter TF-IDF dihitung dari training set saja
- [X] Transformasi diterapkan ke test set setelah train-test split, bukan sebelum

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY — Versi Notebook (pipeline lengkap, referensi metode di proposal)
1. Dataset: Ulasan aplikasi Gojek berbahasa Indonesia (Kaggle)
2. Data awal: 100.000 baris, 1 fitur teks (content) + 1 label (sentiment)
3. Cleaning:
   - Missing values: ditangani saat load (dropna pada content)
   - Ulasan terlalu pendek pasca-stemming: 2.777 kasus, listwise deletion
   - Duplikat: tidak dilaporkan eksplisit di notebook — perlu ditambahkan sebagai langkah validasi lanjutan
4. Transformation: case folding → cleansing (simbol/angka/URL) → stopword removal (NLTK, 757 kata) → stemming (Sastrawi)
5. Normalisasi: TF-IDF Vectorizer (max_features=5.000), parameter di-fit dari training set (80% data)
6. Data akhir: 97.223 baris, 5.000 fitur TF-IDF
7. Leakage check: [X] Lulus (TF-IDF fit hanya pada train, split sebelum vectorization)

PREPROCESSING SUMMARY — Versi Script multi_run_experiment.py (5-run, dipakai untuk WS-10 s.d. WS-14)
1. Dataset: sama (Kaggle, gojek_labeled.csv)
2. Data awal: 100.000 baris per run (di-sample dari dataset yang SUDAH dipreprocessing sekali secara global)
3. Cleaning: dropna pada content + pembuangan baris content_clean kosong pasca-preprocessing (sama seperti notebook)
4. Transformation: case folding → cleansing (simbol/angka/URL) → stopword removal (NLTK) → stemming (Sastrawi) — identik dengan notebook, di-cache di gojek_labeled_clean.csv
5. Normalisasi: TF-IDF Vectorizer (max_features=5.000) di atas content_clean, parameter di-fit dari training set tiap run
6. Data akhir: 100.000 baris di-sample per run dari korpus yang sudah bersih
7. Leakage check: [X] Lulus — TF-IDF fit hanya di training, DAN pipeline preprocessing kini sesuai proposal E.2 dan identik dengan notebook
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Yang terjadi di penelitian ini justru kebalikannya: bukan over-processing, melainkan under-processing yang tidak disadari pada versi v1 — script multi_run_experiment.py sempat melewatkan seluruh tahap linguistik (cleansing, stopword removal, stemming) yang sudah dirancang dan dijustifikasi di proposal serta dijalankan di notebook eksplorasi awal. Setelah diperbaiki (v2) dan di-re-run, dampaknya terkonfirmasi nyata: gap accuracy RF-NB menyusut dari 1.71 poin menjadi 0.45 poin. Ini pengingat konkret bahwa preprocessing bukan detail implementasi yang bisa diabaikan saat menulis ulang kode (misalnya saat membuat script otomatisasi terpisah dari notebook) — setiap kali pipeline ditulis ulang, perlu ada cross-check eksplisit bahwa semua tahap yang dijanjikan di metode benar-benar dieksekusi, karena selisih sekecil apapun dalam preprocessing bisa mengubah besaran efek yang dilaporkan di skripsi.
