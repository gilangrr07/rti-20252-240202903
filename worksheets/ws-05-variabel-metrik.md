# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: ____________________

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Jenis algoritma klasifikasi | IV   | Pendekatan klasifikasi teks yang digunakan |     Categorical: Naive Bayes / Random Forest / REPTree   |    Nominal   | -|       Ditentukan sebelum eksperimen dan dijalankan pada dataset yang sama        |      Ketiga algoritma mewakili pendekatan berbeda: probabilistik, ensemble, dan decision tree       |
|Ukuran dataset| IV   |Jumlah data soal yang digunakan|183, 273, dan 418 soal|Ratio|Jumlah soal|Dihitung berdasarkan jumlah data pada setiap iterasi eksperimen|Untuk menguji pengaruh penambahan data terhadap akurasi|
|Correct Classification Rate| DV   |Tingkat ketepatan algoritma dalam mengklasifikasikan soal| (Jumlah prediksi benar / total data) × 100 |Ratio|Persen (%) |Dihitung otomatis oleh WEKA/Python setelah proses klasifikasi|Menjadi metrik utama pada jurnal primer sehingga hasil dapat dibandingkan langsung|
|Filter/tokenizer| CV   |Metode preprocessing teks| StringToWordVector atau TF-IDF |Nominal|- |Dikontrol tetap pada setiap pendekatan eksperimen|Perbedaan preprocessing dapat memengaruhi representasi fitur|
|Distribusi kelas soal| CV   |Proporsi kelas mudah/sedang/sulit|Jumlah soal per kategori|Ratio|Jumlah soal |Dicatat pada setiap iterasi dataset|Class imbalance dapat memengaruhi akurasi model|


Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah algoritma Random Forest dengan TF-IDF menghasilkan correct classification rate (%) lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan jumlah data dari 183 ke 273 ke 418 soal berpengaruh signifikan terhadap akurasi ketiga algoritma tersebut?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| *Jenis algoritma klasifikasi* | *IV* | *Pendekatan klasifikasi teks* | *Naive Bayes / Random Forest / REPTree* | *Nominal* | *—* |
| *Ukuran dataset* | *IV* | *Jumlah data eksperimen* | *183 / 273 / 418 soal* | *Ratio* | *Jumlah soal* |
| *Correct Classification Ratei* | *DV* | *Ketepatan klasifikasi model* | *(Prediksi benar / total data) × 100* | *Ratio* | *Persen (%)* |
| *Filter/tokenizer* | *CV* | *Representasi fitur teks* | *StringToWordVector / TF-IDF* | *Nominal* | *—* |
| *Distribusi kelas soal* | *CV* | *Proporsi tingkat kesulitan soal* | *Jumlah soal per kategori* | *Ratio* | *Jumlah soal* |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | *5* |  *Correct Classification Rate langsung merepresentasikan kemampuan model dalam mengklasifikasikan tingkat kesulitan soal* |
| Sensitive |  *4* |  *Mampu menangkap perbedaan performa antar algoritma, namun bisa kurang stabil pada dataset kecil* |
| Feasible |  *5* |  *Mudah diperoleh karena dihitung otomatis oleh WEKA dan Python* |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Incorrect Classification Count digunakan sebagai secondary metric untuk memberikan gambaran jumlah kesalahan klasifikasi secara absolut.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika seluruh algoritma mencapai akurasi di atas 95%, perbedaan antar model menjadi sangat kecil sehingga sulit membedakan performa sebenarnya hanya dengan correct classification rate.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* |*Dataset masih terbatas dan kemungkinan jumlah soal sulit lebih sedikit* | *Penambahan data dilakukan bertahap dan distribusi kelas dicatat*|
| Consistency | *Apakah ada kontradiksi internal?* |*Pelabelan tingkat kesulitan berpotensi subjektif* |*Menggunakan guru yang sama dan kriteria pelabelan konsisten* |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* |*Akurasi model tidak sepenuhnya menjamin validitas konsep “tingkat kesulitan”* |*Limitasi dicatat dan disarankan multi-rater pada penelitian lanjutan*|
| Representativeness | *Apakah sampel mewakili populasi target?* |*Dataset hanya berasal dari soal Bahasa Indonesia SD* |*Mengambil soal dari berbagai sumber untuk meningkatkan variasi* |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena peneliti dapat secara tidak sadar memilih metrik yang membuat hasil terlihat lebih baik atau signifikan. Hal ini mengurangi objektivitas penelitian karena keputusan pengukuran dibuat setelah mengetahui hasil eksperimen.
> Berbeda dengan p-hacking, eksplorasi data yang sah dilakukan secara transparan dan dilaporkan sebagai exploratory finding, bukan sebagai bukti utama hipotesis. Temuan eksploratif boleh digunakan untuk membangun hipotesis baru, tetapi tidak boleh diperlakukan sebagai hasil confirmatory yang sudah direncanakan sejak awal eksperimen.
