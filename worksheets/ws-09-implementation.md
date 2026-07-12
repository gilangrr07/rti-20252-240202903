# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel Core i5-12450H, 8 Core / 12 Thread, 2.0 GHz (Boost 4.4 GHz)
  RAM     : 8 GB DDR4
  GPU     : NVIDIA RTX 2050 4GB GDDR6 (tersedia namun tidak digunakan karena eksperimen berjalan pada CPU-only)
  Storage : 512GB PCIe® NVMe™ TLC M.2 SSD

Software:
  OS        : Windows 11 Home 64-bit
  Runtime   : Python 3.10.12
  Framework : ____________________

Dependencies:
| Library      | Version | Sumber | Hash/Checksum |
| ------------ | ------- | ------ | ------------- |
| scikit-learn | 1.3.2   | pip    | -             |
| pandas       | 2.1.1   | pip    | -             |
| numpy        | 1.24.3  | pip    | -             |
| nltk         | 3.8.1   | pip    | -             |
| PySastrawi   | 1.0.1   | pip    | -             |
| matplotlib   | 3.8.0   | pip    | -             |


Konfigurasi:
  Config file     : config.json
  Random seed     : 42
  Hyperparameters : - TF-IDF max_features = 5000
                    - TF-IDF ngram_range = (1,1)
                    - Naïve Bayes alpha = 1.0
                    - Random Forest n_estimators = 100
                    - Test size = 20%

Reproducibility Check:
  [X] Dependency terdokumentasi (requirements.txt / lock file)
  [X] Seed ditetapkan di semua level (Python, NumPy, framework)
  [X] Config di version control
  [X] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | *Intel Core i5-12450H, 8 Core / 12 Thread* |
| RAM | *8 GB DDR4* |
| GPU | *NVIDIA RTX 2050 4GB GDDR6 (tidak digunakan)* |
| OS | *Windows 11 Home 64-bit* |
| Runtime | *Python 3.10.12* |
| Framework | *scikit-learn, pandas, numpy, NLTK, PySastrawi, matplotlib* |
| Random Seed | *42* |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| *scikit-learn* | *1.3.2* | *TF-IDF, Naïve Bayes, Random Forest, evaluasi model* |
| *pandas* | *2.1.1* | *Membaca dan mengolah dataset Kaggle* |
| *numpy* | *1.24.3* | *Operasi numerik dan pengaturan seed* |
| *NLTK* | *3.8.1* | *Stopword removal Bahasa Indonesia* |
| *PySastrawi* | *1.0.1* | *Stemming Bahasa Indonesia* |
| *matplotlib* | *3.8.0* | *Visualisasi confusion matrix dan hasil eksperimen* |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | *42* | *Accuracy, Precision, Recall, F1-Score* | — |
| 2 | *42* | Accuracy, Precision, Recall, F1-Score | [X] Ya / [ ] Tidak |
| 3 | *42* | Accuracy, Precision, Recall, F1-Score | [X] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability:
> - **Thermal throttling** — CPU/GPU overheating pada run berturut-turut → clock speed turun → waktu eksekusi berubah
> - **Background process** — antivirus scan, update OS, atau cloud sync aktif saat run berlangsung
> - **Cache dari run sebelumnya** — hasil tersimpan di memori/disk sehingga run berikutnya tidak menjalankan komputasi penuh
> - **Random state tidak dikontrol di semua level** — Python seed di-set, tapi NumPy/PyTorch/TensorFlow punya seed independen

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [X] Random seed di-set di semua level
- [X] Tidak ada background process yang mengganggu
- [X] Cache dibersihkan antar-run
- [X] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Perbandingan Algoritma Naïve Bayes dan Random Forest untuk Analisis Sentimen Ulasan Aplikasi Gojek Berbahasa Indonesia Menggunakan TF-IDF

## 1. Environment
> OS      : Windows 11 Home 64-bit
  CPU     : Intel Core i5-12450H
  RAM     : 8 GB DDR4
  GPU     : NVIDIA RTX 2050 4GB (tidak digunakan)
  Storage : 512GB PCIe® NVMe™ TLC M.2 SSD
  Python  : 3.10.12
  Seed    : 42

## 2. Installation
> pip install -r requirements.txt
  python -c "import nltk; nltk.download('stopwords')"

## 3. Data
> Sumber : Dataset ulasan aplikasi Gojek berbahasa    Indonesia dari Kaggle.
  Format : CSV
  Kolom utama :
  - content (ulasan)
  - sentiment (label sentimen)
  Ukuran :
  ±100.000 ulasan

## 4. Execution
> python main.py --config config.json

## 5. Configuration
> {
 "seed": 42,
 "test_size": 0.2,
 "tfidf_max_features": 5000,
 "tfidf_ngram_range": [1,1],
 "rf_n_estimators": 100,
 "nb_alpha": 1.0
}

## 6. Expected Output
> results/evaluation_results.csv
  results/confusion_matrix_nb.png
  results/confusion_matrix_rf.png

    Output:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  Naïve Bayes

  - Accuracy
  - Precision
  - Recall
  - F1-Score
  Random Forest
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [X] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Eksperimen telah dirancang untuk mencapai repeatability karena seluruh parameter utama dikunci menggunakan config file dan random seed yang konsisten. Namun, reproducibility penuh masih memerlukan repository Git yang dapat diakses publik, file requirements.txt yang telah dihasilkan dari environment aktual, dokumentasi dataset Kaggle yang digunakan, serta hasil eksperimen nyata sebagai referensi bagi peneliti lain yang ingin mereplikasi penelitian.
