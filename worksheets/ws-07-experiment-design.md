# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah Random Forest + TF-IDF menghasilkan correct classification rate lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan ukuran dataset (183 → 273 → 418 soal) berpengaruh signifikan terhadap akurasi ketiga algoritma?
Hypothesis        : H₀: Tidak ada perbedaan signifikan pada CCR (%) antara Naive Bayes, Random Forest, dan REPTree di setiap ukuran dataset.
H₁: Terdapat perbedaan signifikan pada CCR (%) antara minimal satu pasangan algoritma, dan penambahan data berpengaruh positif terhadap akurasi.
Tipe Eksperimen   : [X] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
|Control (C1) |Replikasi kondisi awal jurnal primer menggunakan dataset terkecil |NB, RF, REPTree + 183 soal|StringToWordVector; kategori mudah/sedang/sulit; use training set|
| Treatment 1 (T1) |Pengujian efek penambahan data tahap pertama|NB, RF, REPTree + 273 soal|StringToWordVector; kategori mudah/sedang/sulit; use training set|
| Treatment 2 (T2) |Pengujian efek penambahan data tahap kedua dengan dataset terbesar|NB, RF, REPTree + 418 soal|StringToWordVector; kategori mudah/sedang/sulit; use training set|

Fairness Checklist:
  [X] Dataset identik untuk semua kondisi
  [X] Preprocessing setara
  [X] Tuning effort setara
  [X] Environment identik
  [X] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    |Pelabelan tingkat kesulitan dilakukan oleh 1 guru sehingga berpotensi subjektif|Menggunakan guru yang sama dan kriteria penilaian konsisten pada seluruh dataset|
| External    |Dataset hanya berasal dari soal Bahasa Indonesia SD |Limitasi generalisasi dijelaskan dan direkomendasikan perluasan domain pada penelitian lanjutan|
| Construct   |CCR hanya mengukur kecocokan prediksi terhadap label guru, bukan validitas psikometri tingkat kesulitan|Menambahkan Incorrect Classification Count sebagai secondary metric dan mendokumentasikan keterbatasan konstruk |
| Conclusion  |Dataset maksimal hanya 418 soal sehingga estimasi akurasi berpotensi tidak stabil|Replikasi eksperimen beberapa kali dan melaporkan hasil secara deskriptif|

Statistical Plan:
  Uji statistik   : Perbandingan deskriptif correct classification rate (%) antar algoritma pada setiap ukuran dataset.
  Justifikasi      : Ukuran dataset relatif kecil dan penelitian primer juga menggunakan pendekatan deskriptif sehingga belum dilakukan uji inferensial formal.
  Alpha            : Tidak diterapkan; jika penelitian lanjutan menggunakan uji inferensial maka α = 0,05.
  Effect size min  : Perbedaan CCR ≥ 5% dianggap bermakna secara praktis.
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah algoritma Random Forest dengan TF-IDF menghasilkan correct classification rate (%) lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan jumlah data dari 183 ke 273 ke 418 soal berpengaruh signifikan terhadap akurasi ketiga algoritma tersebut?
**Tipe eksperimen:** [X] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | *Replikasi dataset awal jurnal primer* | *NB, RF, REPTree + 183 soal* | *StringToWordVector; use training set; WEKA* |
| Treatment 1 | *Pengujian dataset menengah* | *NB, RF, REPTree + 273 soal* | *StringToWordVector; use training set; WEKA* |
| Treatment 2 | *Pengujian dataset terbesar* | *NB, RF, REPTree + 418 soal* | *StringToWordVector; use training set; WEKA* |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | *✅* | *Semua algoritma menggunakan dataset yang sama pada setiap iterasi* |
| Preprocessing setara | *✅* | *StringToWordVector diterapkan dengan parameter identik* |
| Tuning effort setara | *✅* | *Semua algoritma menggunakan parameter default WEKA* |
| Environment identik | *✅* | *Seluruh eksperimen dijalankan pada perangkat dan versi software yang sama* |
| Metrik evaluasi sama | *✅* | *Semua kondisi menggunakan CCR (%) sebagai metrik utama* |

**Ada yang tidak fair?** [ ] Ya / [X] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | *Risiko subjektivitas label tingkat kesulitan* | *Menggunakan satu guru berpengalaman dengan kriteria konsisten* |
| External | *Dataset hanya mencakup satu domain pelajaran* | *Menyatakan keterbatasan generalisasi secara eksplisit* |
| Construct | *CCR tidak mengukur validitas psikometri tingkat kesulitan* | *Menambahkan secondary metric dan dokumentasi limitasi* |
| Conclusion | *Jumlah data kecil dan tidak ada uji inferensial* | *Hasil dilaporkan deskriptif dan tidak membuat klaim kausalitas kuat* |

**Ancaman mana yang paling sulit dimitigasi?** Construct Validity
**Mengapa?**
> Karena konsep “tingkat kesulitan soal” bersifat subjektif dan belum memiliki standar psikometri yang benar-benar baku pada konteks soal Bahasa Indonesia SD. Walaupun label dibuat konsisten, tetap ada kemungkinan interpretasi tingkat kesulitan berbeda antar guru.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah baseline yang digunakan benar-benar representatif dan relevan dengan state-of-the-art?
2. Apakah semua metode diuji pada kondisi eksperimen yang identik dan fair?
3. Apakah ukuran dataset, metrik, dan analisis statistik cukup kuat untuk mendukung klaim tersebut?
