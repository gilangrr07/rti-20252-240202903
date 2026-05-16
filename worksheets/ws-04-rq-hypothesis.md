# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Belum ada studi yang membandingkan pendekatan WEKA-based (REPTree + StringToWordVector) dengan pendekatan Python modern (RF + TF-IDF, NB + TF-IDF) pada dataset soal ujian teks Bahasa Indonesia SD, sekaligus menguji pengaruh variasi ukuran dataset secara terkontrol.

Research Question:
  Tipe         : [X] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah algoritma Random Forest dengan TF-IDF menghasilkan correct classification rate (%) lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan jumlah data dari 183 ke 273 ke 418 soal berpengaruh signifikan terhadap akurasi ketiga algoritma tersebut?
  Variabel IV  : -Jenis algoritma klasifikasi: Naive Bayes, Random Forest, REPTree
                 -Ukuran dataset: 183, 273, dan 418 soal
  Variabel DV  : Correct Classification Rate (%)
  Metrik       : Correct Classification Rate (%), Incorrect Classification Count, serta perbandingan akurasi antar algoritma pada setiap ukuran dataset
  Dataset      : Dataset soal ujian Bahasa Indonesia SD (183–418 soal pilihan ganda dengan 3 kategori tingkat kesulitan: mudah, sedang, sulit).
  Baseline     : 1. REPTree + StringToWordVector (WEKA) — Baharuddin & Tjahyanto (2022)
                 2. Random Forest + TF-IDF (Python/sklearn) — state-of-the-art klasifikasi teks Bahasa Indonesia 2025

Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Perbandingan empiris pertama antara REPTree+StringToWordVector (WEKA) dan RF/NB+TF-IDF (Python) pada dataset soal ujian teks Bahasa Indonesia SD, sekaligus bukti kuantitatif pengaruh ukuran dataset terhadap akurasi klasifikasi tingkat kesulitan soal.
  Jenis kontribusi        : [ ] Improvement  [X] Comparison  [ ] Novel approach
  Gap yang diisi          : Method Gap + Context Gap belum ada komparasi sistematis algoritma machine learning modern pada konteks klasifikasi soal ujian teks Bahasa Indonesia SD.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan pada correct classification rate (%) antara algoritma Naive Bayes, Random Forest, dan REPTree pada dataset soal ujian Bahasa Indonesia SD di setiap ukuran dataset (183, 273, dan 418 soal).
  H₁ : Terdapat perbedaan signifikan pada correct classification rate (%) antara minimal satu pasang algoritma pada dataset soal ujian Bahasa Indonesia SD, dan peningkatan ukuran dataset berpengaruh positif terhadap akurasi klasifikasi.
  Threshold              : REPTree ≥ 91,15% (baseline Baharuddin & Tjahyanto, 2022) pada dataset 418 soal; RF+TF-IDF ≥ 85%.
  Justifikasi threshold  : Threshold 91,15% berasal dari hasil terbaik studi identik sebelumnya, sedangkan threshold 85% berasal dari konsensus studi klasifikasi teks Bahasa Indonesia terbaru yang menunjukkan RF umumnya berada pada rentang akurasi tinggi.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Belum ada studi yang membandingkan pendekatan WEKA-based (REPTree + StringToWordVector) dengan pendekatan Python modern (RF + TF-IDF, NB + TF-IDF) pada dataset soal ujian teks Bahasa Indonesia SD, sekaligus menguji pengaruh variasi ukuran dataset secara terkontrol.

**RQ versi pertama (tulis bebas):**
> Algoritma mana yang paling akurat untuk mengklasifikasikan tingkat kesulitan soal ujian Bahasa Indonesia SD, dan apakah penambahan jumlah data meningkatkan akurasinya?

**Evaluasi RQ:**

| Komponen        | Ada?   | Isi                                          |
| --------------- | ------ | -------------------------------------------- |
| Metode spesifik | Ya | Naive Bayes, Random Forest, REPTree              |
| Metrik terukur  | Ya | Correct Classification Rate (%)                  |
| Baseline        | Ya | REPTree+WEKA dan RF+TF-IDF                       |
| Dataset/konteks | Ya | Soal ujian Bahasa Indonesia SD, 183–418 soal     |


**Tipe RQ:** [X] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah algoritma Random Forest dengan TF-IDF menghasilkan correct classification rate (%) lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan jumlah data dari 183 ke 273 ke 418 soal berpengaruh signifikan terhadap akurasi ketiga algoritma tersebut?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen              | Isi                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------|
| H₀                    | *Tidak ada perbedaan signifikan correct classification rate (%) antara NB, RF, dan REPTree*          |
| H₁                    | *Ada perbedaan signifikan minimal satu pasangan algoritma dan ukuran dataset meningkatkan akurasi*   |
| Metrik                | *Correct Classification Rate (%)*                                                                    |
| Threshold             | *REPTree ≥ 91,15%; RF+TF-IDF ≥ 85%*                                                                  |
| Justifikasi threshold | *Berdasarkan hasil studi identik dan konsensus studi terbaru*                                        |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Bagaimana cara membuktikannya salah?
Jika seluruh algoritma menghasilkan akurasi yang tidak berbeda signifikan pada semua ukuran dataset, maka H₀ tidak dapat ditolak. Jika peningkatan jumlah data tidak meningkatkan akurasi, maka klaim pada H₁ terbantah.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap           | Isi                                                                     |
|-----------------|-------------------------------------------------------------------------|
| RQ              | *Apakah RF+TF-IDF menghasilkan correct classification rate lebih tinggi dibandingkan NB dan REPTree pada dataset soal ujian B. Indonesia SD?*                       |
| Variable (IV)   | *Jenis algoritma dan ukuran dataset*                                    |
| Variable (DV)   | *Correct Classification Rate (%)*                                       |
| Metric          | *Correct Classification Rate (%), Incorrect Classification Count*       |
| Data source     | *Dataset soal ujian Bahasa Indonesia SD*                                |
| Analysis method | *Eksperimen klasifikasi menggunakan WEKA dan Python/sklearn*            |

**Apakah rantai lengkap?** [X] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** “Peningkatan Performa Klasifikasi Machine Learning Melalui Perbandingan Metode Machine Learning dan Peningkatan Dataset” — Baharuddin & Tjahyanto (2022)
**RQ yang diekstrak:** Algoritma mana yang menghasilkan performa terbaik untuk klasifikasi soal ujian Bahasa Indonesia SD, dan bagaimana pengaruh peningkatan jumlah dataset terhadap performa klasifikasi?
**Komponen yang hilang:** Baseline eksternal belum disebutkan secara eksplisit sehingga posisi kontribusi penelitian terhadap studi sebelumnya masih kurang jelas.
