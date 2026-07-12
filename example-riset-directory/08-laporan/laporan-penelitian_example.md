# Laporan Penelitian

**Judul:** Perbandingan Algoritma Naïve Bayes dan Random Forest untuk Analisis Sentimen Ulasan Aplikasi Gojek Berbahasa Indonesia Menggunakan TF-IDF

**Peneliti:** Mohamad Gilang Rizki Riomdona (240202903)
**Dosen Pengampu:** Helmi Bahar Alim, S.Kom., M.Kom
**Target Publikasi:** Jurnal terindeks SINTA 3 atau lebih tinggi, bidang informatika/ilmu komputer Bahasa Indonesia
**Status Penelitian:** WS-09 s.d. WS-15 selesai; naskah jurnal telah disusun ([07-manuskrip/naskah-jurnal.md](naskah-jurnal.md)); menyisakan finalisasi format submission

---

## 1. Ringkasan Eksekutif

Penelitian ini merancang dan mengevaluasi secara empiris perbandingan performa **Naïve Bayes (NB)** dan **Random Forest (RF)** dalam klasifikasi sentimen ulasan aplikasi Gojek berbahasa Indonesia menggunakan TF-IDF sebagai ekstraksi fitur. Evaluasi dilakukan melalui eksperimen terkontrol: satu pipeline klasifikasi dengan dua kondisi algoritma (Kondisi A = Naïve Bayes, Kondisi B = Random Forest), diuji pada dataset publik Kaggle (100.000 ulasan, 50.000 positif + 50.000 negatif) dengan **5 replikasi** (seed berbeda: 42, 123, 456, 789, 2024) per algoritma — total **10 run** — menggunakan pipeline preprocessing seragam (case folding, cleansing, stopword removal NLTK, stemming Sastrawi) dan pengukuran accuracy, precision, recall, F1-score, serta waktu latih.

**Temuan utama:**

- Random Forest **secara konsisten mengungguli** Naïve Bayes pada seluruh 5 replikasi tanpa kecuali (accuracy 89,59% ± 0,18 vs 89,14% ± 0,19, selisih 0,45 poin).
- Signifikansi statistik **bergantung pada uji yang dipilih**: paired t-test menyatakan signifikan (p=0,0047), sedangkan Wilcoxon signed-rank test — yang lebih tepat karena distribusi accuracy Random Forest melanggar asumsi normalitas (Shapiro-Wilk p=0,0069) — menyatakan marginal (p=0,0625).
- **Random Forest ~89× lebih lambat dilatih** dibanding Naïve Bayes (28,52 detik vs 0,32 detik per run), sebuah trade-off akurasi vs biaya komputasi yang perlu dipertimbangkan pada implementasi praktis.
- Ditemukan **temuan metodologis penting**: implementasi awal skrip eksperimen multi-run (versi 1) tidak menyertakan tahap preprocessing linguistik akibat kelalaian saat menulis ulang kode dari notebook eksplorasi. Setelah dikonfirmasi dan diperbaiki (versi 2), gap performa RF-NB menyusut dari **1,71 poin** (tanpa preprocessing) menjadi **0,45 poin** (dengan preprocessing) — bukti kuantitatif bahwa kesimpulan komparasi algoritma sensitif terhadap keputusan preprocessing.

Seluruh kode sumber, data eksperimen, worksheet analisis, dan naskah tersedia pada dokumen-dokumen terkait (lihat §7 Lampiran untuk peta artefak).

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang

Gojek merupakan platform super-app dengan puluhan juta pengguna aktif di Indonesia yang mengumpulkan ribuan ulasan pengguna setiap harinya di Google Play Store. Ulasan-ulasan ini mengandung opini, keluhan, dan apresiasi yang berpotensi besar sebagai sumber intelijen bisnis, namun membacanya secara manual tidak memungkinkan pada skala tersebut. Analisis sentimen otomatis berbasis machine learning menjadi solusi yang relevan, dengan Naïve Bayes dan Random Forest sebagai dua algoritma yang paling umum digunakan untuk klasifikasi teks Bahasa Indonesia — namun performa keduanya dilaporkan tidak konsisten antar-studi (gap akurasi RF terhadap NB berkisar 1–24 poin tergantung domain), dan belum ada studi yang membandingkan keduanya secara terkontrol khusus pada ulasan aplikasi Gojek.

### 2.2 Rumusan Masalah

1. Apakah Random Forest menghasilkan performa klasifikasi sentimen yang lebih baik dibandingkan Naïve Bayes menggunakan TF-IDF pada dataset ulasan aplikasi Gojek berbahasa Indonesia, berdasarkan accuracy, precision, recall, dan F1-score?
2. Seberapa besar dan seberapa konsisten selisih performa tersebut di seluruh replikasi (seed) yang diuji?
3. Bagaimana signifikansi statistik dari selisih performa tersebut, dengan mempertimbangkan asumsi distribusi data (normalitas)?
4. Sejauh mana keputusan preprocessing (pipeline linguistik Bahasa Indonesia) memengaruhi besaran gap performa antara kedua algoritma?

### 2.3 Tujuan Penelitian

Detail tujuan & kontribusi: lihat [proposal-penelitian.md](proposal-penelitian.md) bagian D dan F, serta [naskah-jurnal.md](naskah-jurnal.md) §1 Pendahuluan.

---

## 3. Metodologi dan Pelaksanaan

Penelitian dilaksanakan dalam 7 tahap (WS-09 s.d. WS-15). Bagian ini merangkum implementasi dan verifikasi setiap tahap; detail teknis lengkap ada pada dokumen worksheet yang dirujuk.

### 3.1 WS-09 — Experimental Design & Setup

**Status: Selesai.** Dirancang controlled comparison experiment dengan satu variabel independen (jenis algoritma: NB vs RF), satu variabel dependen (performa klasifikasi via 4 metrik), dan variabel kontrol yang dikunci (dataset, preprocessing, TF-IDF, split, environment). Artifact dipetakan ke 5 modul: Dataset Loader (mengunci CV data), Preprocessing (mengunci CV preprocessing), TF-IDF Vectorizer (mengunci CV ekstraksi fitur), Classifier (IV, dapat ditukar antara NB/RF), dan Evaluator (menghasilkan DV).

Detail & diagram: [arsitektur-dan-skema.md](arsitektur-dan-skema.md).

### 3.2 WS-10 — Execution Plan & Data Collection

**Status: Selesai — 10 run (2 versi) telah dijalankan.** Disusun execution plan untuk 10 run (5 seed × 2 algoritma) dengan seed pre-determined sebelum eksekusi, dan format data logging JSON terstruktur per run (identitas, konfigurasi, hasil metrik, confusion matrix, status anomali) — bukan sekadar output terminal yang di-copy-paste.

**Eksekusi versi 1** (`multi_run_experiment.py`): dijalankan 07/07/2026 20:53–20:57, 10 run, seluruhnya tanpa crash (`anomali=NONE`).
**Eksekusi versi 2, revisi** (`multi_run_experiment_v2.py`): dijalankan 12/07/2026 01:32–01:35, 10 run, seluruhnya tanpa crash.

**Iterasi desain penting**: versi 1 ditulis sebagai penyederhanaan dari notebook eksplorasi untuk mempercepat replikasi 5-seed, namun proses penyederhanaan ini secara tidak sengaja menghilangkan tahap preprocessing linguistik. Solusi: versi 2 menambahkan kembali fungsi `preprocess()` yang identik dengan notebook, dilengkapi mekanisme caching hasil preprocessing (`gojek_labeled_clean.csv`) agar replikasi berikutnya tidak perlu menjalankan ulang stemming yang memakan waktu 5–15 menit.

Detail: [Jadwal_Log_Pelaksanaan_Penelitian.md](Jadwal_Log_Pelaksanaan_Penelitian.md), kode: `multi_run_experiment.py`, `multi_run_experiment_v2.py`.

### 3.3 WS-11 — Data Validation & Integrity

**Status: Selesai — anomali ditemukan dan diperbaiki.** Validasi data dilakukan pada 4 pilar: accuracy (nilai dalam range [0,100]), consistency (format seragam antar-log), completeness (10/10 run tercatat), dan validity (kesesuaian dengan desain eksperimen).

Pada pilar validity, ditemukan anomali: perbandingan silang antara hasil eksplorasi notebook (single-run, dengan preprocessing lengkap, seed=42) dan hasil multi-run versi 1 pada seed yang sama menunjukkan selisih accuracy ~1 poin dan selisih precision ~4,6 poin yang tidak semestinya terjadi jika kedua pipeline identik. Investigasi kode mengonfirmasi `multi_run_experiment.py` versi 1 tidak menjalankan tahap preprocessing linguistik. Ditemukan pula outlier statistik pada NB run seed=789 (accuracy 88,08%, di luar batas IQR bawah pada data versi 1).

Detail: worksheet WS-11 (Data Validation & Integrity).

### 3.4 WS-12 — Result Presentation & Visualization

**Status: Selesai.** Hasil disajikan dalam tabel mean±std (n=5 per algoritma) dan rencana visualisasi (bar chart dengan error bar, dot plot sebaran 5-run, scatter waktu latih skala log). Bias check dilakukan untuk memastikan tidak ada truncated-axis bias — krusial karena gap performa versi final (0,45 poin) jauh lebih kecil dari versi awal (1,71 poin), sehingga lebih rentan disalahartikan tanpa error bar yang jelas.

Detail: worksheet WS-12 (Result Presentation & Visualization).

### 3.5 WS-13 — Data Preprocessing

**Status: Selesai — RESOLVED.** Mendokumentasikan pipeline preprocessing secara lengkap: case folding, cleansing (hapus simbol/angka/URL), stopword removal (NLTK, Bahasa Indonesia, 757 kata), dan stemming (Sastrawi). Setelah anomali pada WS-11 dikonfirmasi, `multi_run_experiment_v2.py` ditulis ulang agar pipeline-nya identik dengan notebook eksplorasi awal dan sesuai proposal bagian E.2.

Detail: [arsitektur-dan-skema.md](arsitektur-dan-skema.md), worksheet WS-13 (Data Preprocessing).

### 3.6 WS-14 — Analysis, Interpretation & Failure Analysis

**Status: Selesai — dengan pelaporan ganda uji statistik.** Data final (versi 2) dianalisis: uji normalitas Shapiro-Wilk (NB normal, W=0,875, p=0,286; RF tidak normal, W=0,686, p=0,0069, akibat satu run dengan accuracy relatif tinggi pada seed 2024), diikuti pelaporan ganda paired t-test (t(4)=5,70, p=0,0047, Cohen's d=2,55 — signifikan) dan Wilcoxon signed-rank test (p=0,0625 — marginal, tidak signifikan pada α=0,05 konvensional, meski merupakan p-value minimum yang bisa dicapai pada n=5).

Detail: worksheet WS-14 (Analysis, Interpretation & Failure Analysis).

### 3.7 WS-15 — Scientific Writing

**Status: Selesai.** Menyusun outline naskah IMRAD, consistency matrix (memverifikasi RQ, variabel, dan klaim konsisten di seluruh bagian Introduction–Conclusion — termasuk memastikan Conclusion tidak sepihak mengutip hanya salah satu hasil uji statistik), dan writing quality check (memperbaiki klaim "signifikan" tanpa p-value menjadi presisi dengan nama uji dan nilai p eksplisit).

Detail: [naskah-jurnal.md](naskah-jurnal.md).

---

## 4. Hasil Penelitian

Ringkasan hasil (detail lengkap & interpretasi: [naskah-jurnal.md](naskah-jurnal.md) §4 Hasil dan Analisis).

### 4.1 Statistik Deskriptif (Data Final, Versi 2)

| Skenario | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Waktu Latih (s) |
|---|---|---|---|---|---|
| Random Forest | 89,59 ± 0,18 | 89,64 ± 0,18 | 89,59 ± 0,18 | 89,58 ± 0,18 | 28,52 ± 0,60 |
| Naïve Bayes | 89,14 ± 0,19 | 89,54 ± 0,16 | 89,14 ± 0,19 | 89,11 ± 0,20 | 0,32 ± 0,03 |

### 4.2 Uji Hipotesis

| Uji | Statistik | p-value | Kesimpulan |
|---|---|---|---|
| Shapiro-Wilk (NB accuracy) | W=0,875 | 0,286 | Normal |
| Shapiro-Wilk (RF accuracy) | W=0,686 | 0,0069 | Tidak normal (outlier seed 2024) |
| Paired t-test (accuracy) | t(4)=5,70 | 0,0047 | Signifikan (d=2,55) |
| Wilcoxon signed-rank (accuracy) | W=0,0 | 0,0625 | Marginal, tidak signifikan pada α=0,05 |
| Paired t-test (F1-score) | t(4)=6,00 | 0,0039 | Signifikan (d=2,68) |

### 4.3 Perbandingan Gap Performa: Sebelum vs Sesudah Preprocessing Diperbaiki

| Versi | Preprocessing | Accuracy RF | Accuracy NB | Gap | Signifikansi |
|---|---|---|---|---|---|
| v1 (superseded) | Tidak ada | 90,13% | 88,42% | 1,71 poin | p=0,0002 (t-test), sangat signifikan |
| v2 (final) | Lengkap | 89,59% | 89,14% | 0,45 poin | p=0,0047 (t-test) / p=0,0625 (Wilcoxon) |

### 4.4 Interpretasi Singkat

1. Random Forest unggul konsisten arahnya di seluruh 5 seed tanpa kecuali — bukan kebetulan satu run.
2. Signifikansi statistik bergantung pada uji: t-test menyatakan signifikan, Wilcoxon (lebih tepat karena RF non-normal) menyatakan marginal — kedua hasil dilaporkan secara transparan, bukan memilih salah satu yang "menguntungkan".
3. Besaran praktis gap (0,45 poin) berada **di bawah ambang bermakna praktis (≥5%)** yang ditetapkan pada proposal — keunggulan RF nyata tapi kecil.
4. **Temuan tambahan penting**: preprocessing linguistik mengecilkan gap performa NB-RF secara substansial (1,71→0,45 poin) — Naïve Bayes lebih diuntungkan oleh representasi teks bersih dibanding Random Forest yang sudah relatif robust terhadap noise pada representasi mentah.

---

## 5. Kendala dan Catatan Lingkungan

- **Kelalaian preprocessing pada implementasi awal**: skrip eksperimen multi-run versi 1 (`multi_run_experiment.py`) tidak menyertakan tahap preprocessing linguistik saat ditulis ulang dari notebook menjadi script otomatis, terdeteksi melalui validasi silang (WS-11) — bukan pemeriksaan kode manual, menegaskan pentingnya validasi data sebagai langkah wajib.
- **Waktu komputasi**: tahap stemming Sastrawi pada seluruh korpus memerlukan estimasi 5–15 menit per eksekusi pertama; dimitigasi dengan mekanisme caching hasil preprocessing (`gojek_labeled_clean.csv`) sehingga replikasi berikutnya jauh lebih cepat.
- **Disparitas waktu latih**: Random Forest (~28,5 detik/run) jauh lebih lambat dibanding Naïve Bayes (~0,3 detik/run), mencerminkan kompleksitas komputasi ensemble tree.
- **Lingkungan eksekusi**: Python 3.x, scikit-learn (TF-IDF, MultinomialNB, RandomForestClassifier), NLTK (stopword Bahasa Indonesia), PySastrawi (stemming); dijalankan lokal (VS Code, Windows) untuk skrip multi-run, dan Google Colab untuk eksplorasi notebook awal.
- **Anomali statistik pada data final**: satu run Random Forest (seed 2024) menghasilkan accuracy relatif tinggi (89,91%) dibanding 4 run RF lain yang sangat rapat (89,48–89,56%), menyebabkan pelanggaran asumsi normalitas Shapiro-Wilk pada grup RF. Investigasi confusion matrix tidak menemukan indikasi bug; run tersebut tetap disertakan dalam analisis sebagai variabilitas alami, bukan dihapus sebagai outlier yang dianggap error.

---

## 6. Kesimpulan dan Saran

Ringkasan kesimpulan & saran penelitian lanjutan: lihat [naskah-jurnal.md](naskah-jurnal.md) §5 Kesimpulan.

Inti kesimpulan: Random Forest menghasilkan performa klasifikasi sentimen yang secara arah konsisten lebih baik dibandingkan Naïve Bayes pada ulasan aplikasi Gojek berbahasa Indonesia — unggul di seluruh 5 replikasi tanpa kecuali — dengan selisih accuracy rata-rata 0,45 poin. H₁ diterima dengan kualifikasi: signifikansi statistik bergantung pada uji yang dipilih (signifikan menurut t-test, marginal menurut Wilcoxon yang lebih tepat), dan besaran praktisnya kecil. Satu temuan tambahan penting teridentifikasi: gap performa NB-RF sensitif terhadap keputusan preprocessing linguistik, sehingga klaim keunggulan algoritma pada klasifikasi teks Bahasa Indonesia perlu selalu dikontekstualisasikan terhadap pipeline yang digunakan.

**Saran penelitian lanjutan**: penambahan jumlah replikasi (10–20 run) untuk meningkatkan power statistik terutama pada uji non-parametrik, ekspansi ke algoritma lain (SVM, XGBoost) dan metode embedding kontekstual (Word2Vec, IndoBERT), serta replikasi lintas aplikasi (Grab, Shopee) untuk menguji generalisasi temuan sensitivitas preprocessing pada domain super-app lainnya.

---

## 7. Lampiran — Peta Artefak Penelitian

| Dokumen/Folder | Isi | Status |
|---|---|---|
| `proposal-penelitian.md` | Proposal penelitian lengkap (A–H) | Selesai |
| `matriks-literatur.md`, `daftar-pustaka.bib` | Matriks literatur (6 studi pembanding + 3 pendukung) dan bibliografi BibTeX (9 entri) | Selesai |
| `arsitektur-dan-skema.md` | Landasan teori (NB, RF, TF-IDF), diagram arsitektur pipeline, skema data | Selesai |
| WS-09 s.d. WS-15 (7 worksheet) | Desain eksperimen, execution plan, validasi data, presentasi hasil, preprocessing, analisis statistik, scientific writing | Selesai |
| `sentimen_gojek.ipynb` | Notebook eksplorasi single-run (seed=42, pipeline lengkap) | Selesai |
| `multi_run_experiment.py` (v1) | Skrip multi-run awal — superseded, disimpan sebagai catatan sejarah & robustness check | Selesai (superseded) |
| `multi_run_experiment_v2.py` (v2) | Skrip multi-run final — dengan preprocessing lengkap | Selesai (final) |
| Data v1: `semua_hasil.csv`, `rekap_statistik.csv`, 10 log JSON | Hasil eksperimen versi awal (tanpa preprocessing) | Tersedia |
| Data v2: `semua_hasil_v2.csv`, `rekap_statistik_v2.csv`, 10 log JSON | Hasil eksperimen versi final (dengan preprocessing) | Tersedia |
| `naskah-jurnal.md` | Naskah jurnal konsolidasi (Judul–Daftar Pustaka) | Selesai |
| `Jadwal_Log_Pelaksanaan_Penelitian.md` | Log kronologis pelaksanaan WS-09 s.d. WS-15 | Selesai |
| `laporan-penelitian.md` | Laporan penelitian (dokumen ini) | Selesai |

**Cara reproduksi penuh:**

```bash
# Eksplorasi awal (opsional, referensi pipeline)
# jalankan sentimen_gojek.ipynb di Google Colab

# Eksperimen multi-run final (v2, dengan preprocessing lengkap)
cd RTI
python multi_run_experiment_v2.py

# Bandingkan dengan versi awal (v1, tanpa preprocessing) — opsional, untuk analisis sensitivitas
python multi_run_experiment.py
```