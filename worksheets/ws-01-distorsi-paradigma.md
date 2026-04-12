# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Mohamad Gilang rizki Riomdona
Tanggal          : 12 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Apakah akurasi tersebut diperoleh dari dataset yang representatif dan menggunakan metode evaluasi yang valid (misalnya cross-validation), serta apakah dibandingkan dengan baseline yang relevan?
   - Data yang dibutuhkan untuk verifikasi: Dataset yang digunakan, metode pembagian data (train-test atau cross-validation), confusion matrix, metrik evaluasi (precision, recall, F1-score), serta hasil perbandingan dengan metode lain.

2. Posisi paradigma:
   - Pendekatan: [x] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Karena penelitian berfokus pada pengukuran performa metode secara objektif menggunakan data kuantitatif dan eksperimen terkontrol, sehingga kebenaran dinilai berdasarkan hasil empiris yang dapat diuji ulang.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Dataset dianggap merepresentasikan kondisi dunia nyata secara keseluruhan, padahal soal hanya dikumpulkan dari bank soal online dan buku tertentu — bukan dari seluruh populasi soal ujian Bahasa Indonesia SD.
   - Sumber bias potensial: Sampling bias (data hanya dari sumber tertentu), overfitting pada dataset (tidak ada evaluasi pada data uji independen yang jelas), serta subjektivitas dalam proses pelabelan data (kategori kesulitan ditentukan oleh satu guru tanpa verifikasi silang).
   - Langkah mitigasi: Menggunakan dataset yang lebih beragam dari berbagai sumber, menerapkan cross-validation untuk evaluasi yang lebih robust, melakukan evaluasi pada data uji independen, serta menjaga transparansi dalam proses pelabelan dengan melibatkan lebih dari satu rater.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Hasil eksperimen, termasuk data yang tidak sesuai dengan hipotesis atau hasil yang tidak signifikan.
   - Batasan yang diakui sejak awal: Keterbatasan jumlah dan kualitas dataset (418 soal dari sumber online), potensi bias dalam data akibat pelabelan oleh satu guru, serta keterbatasan generalisasi hasil penelitian ke mata pelajaran lain, jenjang berbeda, atau konteks dataset yang tidak serupa.

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Peningkatan Performa Klasifikasi Machine Learning Melalui Perbandingan Metode Machine Learning dan Peningkatan Dataset
> Penulis (Tahun): Fikri Baharuddin & Aris Tjahyanto (2022)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | *Mengumpulkan soal ujian Bahasa Indonesia dari bank soal online dan buku pembahasan ujian SD.* | *Data tidak representatif hanya berasal dari sumber tertentu, bukan seluruh populasi soal.* |
| Data → Processing |Pelabelan tingkat kesulitan (Mudah/Sedang/Sulit) secara manual oleh satu guru berpengalaman 7 tahun.|Label kesulitan bersifat subjektif; tidak ada inter-rater reliability check. |
| Processing → Analysis |Preprocessing dengan filter StringToWordVector; klasifikasi menggunakan WEKA Tools.|Informasi semantik dan konteks teks bisa hilang saat tokenisasi tanpa stopword removal.|
| Analysis → Inference |Membandingkan performa Naïve Bayes, Random Forest, dan REPTree di tiga ukuran dataset.|Tidak ada penjelasan eksplisit tentang cross-validation; hanya overall accuracy yang dilaporkan tanpa F1-score per kelas.|
| Inference → Knowledge |Menyimpulkan REPTree sebagai algoritma terbaik dan penambahan dataset meningkatkan performa klasifikasi.| Kesimpulan digeneralisasi ke semua kasus klasifikasi, padahal hanya diuji pada satu domain dan satu jenis tokenisasi.|

**Distorsi paling besar di tahap:** Data → Processing — pelabelan oleh satu guru tanpa verifikasi silang menjadi titik lemah utama karena seluruh akurasi dibangun di atas ground truth yang subjektivitasnya tidak diukur.
**Dua distorsi spesifik yang teridentifikasi:**
1. Subjektivitas pelabelan data : Kategori soal (Mudah/Sedang/Sulit) ditentukan berdasarkan opini satu guru tanpa cross-check rater kedua atau pengukuran inter-rater reliability.
2. Bias dataset (tidak representatif) : Data hanya berasal dari bank soal online tertentu, bukan dari seluruh populasi soal ujian Bahasa Indonesia SD, sehingga generalisasi hasil menjadi lemah.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah |Peneliti harus melaporkan hasil dengan dan tanpa outlier secara transparan, tanpa memilih versi yang lebih menguntungkan hipotesis.|
| Transparansi |Harus menjelaskan alasan penghapusan outlier secara eksplisit di bagian metodologi apakah merupakan kesalahan data (error) atau data valid yang kebetulan menyimpang.|
| Peer review |Reviewer akan mempertanyakan manipulasi jika outlier dihapus tanpa alasan yang kuat dan terdokumentasi; penghapusan diam-diam tidak akan lolos scrutiny ilmiah.|

**Keputusan akhir dan justifikasi:**
> Outlier tidak boleh dihapus semata-mata untuk membuat hasil signifikan. Jika outlier merupakan kesalahan data, penghapusan boleh dilakukan dengan justifikasi yang jelas. Namun jika data valid, kedua hasil dengan dan tanpa outlier harus dilaporkan untuk menjaga integritas penelitian. Hasil negatif pun merupakan kontribusi ilmiah yang sah.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Peningkatan performa klasifikasi machine learning pada dataset teks

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | *5* | *1* | *4* |
| Jenis data yang dikumpulkan |Data numerik dan kuantitatif: akurasi klasifikasi, jumlah data, hasil perbandingan algoritma.|Persepsi manusia terhadap kesulitan soal tidak digunakan dalam penelitian ini.|Artefak berupa model ML dan dataset berlabel yang dibangun dan dievaluasi sebagai sistem.|
| Limitasi paradigma |Kurang menangkap konteks semantik dan subjektivitas label; mengasumsikan ground truth bersifat objektif.|Tidak menghasilkan model yang dapat digeneralisasi; terlalu kontekstual untuk otomatisasi klasifikasi.|Artefak yang dihasilkan masih terlalu kecil dan spesifik; lebih fokus ke sistem daripada kontribusi teori.|

**Paradigma yang dipilih:** Positivis
**Alasan:** Karena penelitian menggunakan eksperimen terkontrol dan mengukur performa model secara kuantitatif (akurasi klasifikasi) dengan variabel yang terukur dan dapat diuji ulang. Pendekatan ini paling sesuai dengan tujuan penelitian yang bersifat komparatif dan empiris.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum memahami materi ini, saya cenderung langsung menerima klaim seperti "peningkatan performa" tanpa mempertanyakan proses di baliknya. Setelah memahami Research Trust Model, saya akan mempertanyakan bagaimana data dikumpulkan, bagaimana proses pelabelan dilakukan, apakah terdapat bias dalam dataset, serta metode evaluasi yang digunakan. Saya juga akan lebih kritis terhadap kemungkinan distorsi baik yang disengaja maupun tidak dalam setiap tahap penelitian.
> 