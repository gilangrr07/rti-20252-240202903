# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Perbandingan Algoritma Naive Bayes dan Random Forest untuk Analisis Sentimen Ulasan Aplikasi Gojek Berbahasa Indonesia Menggunakan TF-IDF
Target  : [X] Jurnal terindeks SINTA 3+ (sesuai proposal F)  [ ] Konferensi  [X] Laporan skripsi

Section Check:
  [X] Abstract — masalah, metode, hasil utama, kontribusi (target <=250 kata)
  [X] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [X] Related Work — concept-centric, gap positioning (sudah ada di WS-03)
  [X] Method — reproducible: desain, variabel, metrik, setup, prosedur (termasuk pipeline preprocessing v2 final)
  [X] Results — tabel + grafik + observasi (tanpa interpretasi) (data dari WS-12)
  [X] Discussion — interpretasi, perbandingan, implikasi, limitation (termasuk temuan sensitivitas preprocessing v1 vs v2)
  [X] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [X] RQ di Introduction = RQ di Method = RQ di Conclusion ("Apakah RF > NB pada accuracy/precision/recall/F1?")
  [X] Variabel di Method (IV=algoritma, DV=4 metrik) = variabel di Results
  [~] Klaim di Discussion perlu didukung DUA angka (t-test p=0,0047 DAN Wilcoxon p=0,0625), bukan hanya salah satu
  [X] Limitasi di Discussion (n=5 kecil, RF non-normal) di-address di Conclusion/Future Work (usul: tambah seed)

Writing Quality:
  [X] Clarity — mudah dipahami tanpa re-read
  [X] Precision — tidak ada istilah ambigu ("signifikan" selalu disertai p-value dan nama uji)
  [X] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Ulasan Gojek berjumlah besar sulit dianalisis manual. Studi ini membandingkan Naive Bayes dan Random Forest dengan TF-IDF pada 100.000 ulasan berbahasa Indonesia, 5 run per algoritma dengan seed berbeda dan pipeline preprocessing seragam (case folding, cleansing, stopword removal, stemming Sastrawi). Random Forest unggul tipis (89,59% vs 89,14% accuracy; selisih 0,45 poin), signifikan menurut paired t-test (p=0,0047) namun marginal menurut Wilcoxon (p=0,0625) karena satu outlier melanggar asumsi normalitas. Preprocessing linguistik terbukti mengecilkan gap performa dibanding representasi TF-IDF mentah (1,71 poin tanpa preprocessing). | 200-250 |
| Introduction | Konteks: Gojek punya jutaan ulasan yang perlu dianalisis otomatis. Gap: belum ada studi yang membandingkan NB vs RF secara terkontrol khusus pada domain ulasan Gojek dengan pipeline seragam (WS-03). RQ: apakah RF menghasilkan performa lebih baik dari NB pada accuracy/precision/recall/F1? Kontribusi: perbandingan empiris pertama pada domain ini, dataset publik Kaggle untuk reproducibility, dan bukti kuantitatif bahwa gap performa NB-RF sensitif terhadap keputusan preprocessing. | 500-700 |
| Related Work | Sudah dikerjakan di WS-03: literature matrix 6 studi (Baharuddin & Tjahyanto 2022; Firdaus et al. 2024; Meinita & Anshori 2025; Nugroho et al. 2025; Pranata et al. 2024; Wati et al. 2025), gap Method+Context, baseline REPTree/WEKA dan RF+TF-IDF. | 700-1000 |
| Method | Controlled comparison experiment; IV=algoritma (NB vs RF), DV=accuracy/precision/recall/F1 (weighted); CV=dataset Kaggle, preprocessing (case folding->cleansing->stopword removal NLTK->stemming Sastrawi), TF-IDF max_features=5000, split 80:20, 5 seed pre-determined (42,123,456,789,2024). Prosedur eksekusi mengikuti WS-10 (execution plan, data logging JSON per run) dan validasi WS-11 (4 pilar: accuracy, consistency, completeness, validity). | 800-1200 |
| Results | Tabel mean+/-std WS-12: RF 89,59+/-0,18% vs NB 89,14+/-0,19% accuracy (n=5). Dot plot menunjukkan tidak ada overlap sebaran 5-run kedua algoritma meski jaraknya sempit. Waktu latih RF ~89x lebih lambat (28,52s vs 0,32s). | 500-800 |
| Discussion | RF unggul konsisten arahnya di semua 5 seed, tapi signifikansi bergantung pada uji (t-test signifikan, Wilcoxon marginal p=0,0625 karena RF non-normal, WS-14). Practical significance kecil (0,45 poin, di bawah ambang 5% yang ditetapkan proposal). Perbandingan dengan versi tanpa preprocessing (gap 1,71 poin) menunjukkan preprocessing linguistik menyamakan performa NB-RF pada domain ini -- temuan yang belum pernah dilaporkan eksplisit di studi pembanding WS-03. Limitation: n=5 kecil, satu outlier RF melanggar normalitas, generalisasi terbatas pada domain Gojek. | 600-900 |
| Conclusion | RF menghasilkan performa klasifikasi sentimen yang secara arah konsisten lebih baik dari NB pada ulasan Gojek berbahasa Indonesia, meski signifikansi statistik marginal dan besaran praktisnya kecil. Kontribusi: bukti empiris pertama pada domain ini + evidensi kuantitatif sensitivitas preprocessing. Future work: tambah jumlah seed/run, replikasi ke Grab/Shopee, uji algoritma lain (SVM, XGBoost, IndoBERT). | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ (RF vs NB) | v | v | v | v | v |
| Metrik utama (accuracy/prec/rec/F1) | v | v | v | v | v |
| Variabel IV (jenis algoritma) | v | v | v | v | v |
| Variabel DV (4 metrik, weighted avg) | ~ (disebut umum) | v | v | v | ~ (disebut umum) |
| Preprocessing (case folding-cleansing-stopword-stemming) | ~ (disinggung ringkas) | v | x | v | x |
| Uji statistik (paired t-test & Wilcoxon) | x | v (disebutkan rencana) | x (hasil mentah saja) | v | ~ (disebut ringkas) |
| Klaim/kontribusi (perbandingan empiris pertama pada domain Gojek) | v | x | x | v | v |

**Isi setiap sel:** v (ada & konsisten), x (missing), ~ (ada tapi ringkas/tidak lengkap)

**Inkonsistensi yang ditemukan:**
> (1) Preprocessing disebutkan di Introduction hanya sekilas padahal ini adalah keputusan metodologis penting yang mengubah kesimpulan (WS-13/WS-14) -- perlu porsi lebih di Introduction sebagai bagian dari kontribusi. 
> (2) Uji statistik (t-test vs Wilcoxon) tidak muncul di Results (Results seharusnya hanya melaporkan angka mentah tanpa interpretasi, ini sudah benar), tapi perlu dipastikan Conclusion tidak menyebutkan salah satu uji secara sepihak (misal hanya menyebut p=0,0047 tanpa p=0,0625) karena itu akan tidak konsisten dengan Discussion yang melaporkan keduanya.

**Tindakan perbaikan:**
> Tambahkan 1-2 kalimat di akhir Introduction yang menyinggung bahwa preprocessing linguistik adalah bagian dari kontribusi (bukan cuma detail teknis), dan pastikan Conclusion memakai bahasa yang sama hati-hatinya dengan Discussion ("konsisten arahnya, signifikansi bergantung pada uji") -- tidak menyederhanakan jadi klaim tegas "RF terbukti lebih baik" tanpa kualifikasi.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> "Hasil penelitian menunjukkan bahwa performa Random Forest lebih baik dibandingkan Naive Bayes secara signifikan. Hal ini konsisten dengan penelitian-penelitian sebelumnya yang juga menunjukkan hasil yang sama. Oleh karena itu dapat disimpulkan bahwa Random Forest adalah algoritma yang lebih unggul untuk analisis sentimen ulasan aplikasi Gojek."

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | "Performa lebih baik" ambigu -- lebih baik di metrik mana, seberapa besar? | Ubah jadi: "Random Forest mencapai accuracy 89,59% dibanding Naive Bayes 89,14% (selisih 0,45 poin)" |
| Precision | "Secara signifikan" tanpa p-value atau nama uji -- klaim kosong yang tidak bisa diverifikasi pembaca. Juga menyembunyikan bahwa Wilcoxon menunjukkan hasil marginal (p=0,0625) untuk data RF yang non-normal | Ubah jadi: "...secara statistik signifikan menurut paired t-test (p=0,0047), meski uji Wilcoxon non-parametrik yang lebih sesuai menunjukkan hasil marginal (p=0,0625)" |
| Conciseness | Kalimat kedua ("konsisten dengan penelitian sebelumnya") tidak menyebut studi mana, tidak menambah informasi konkret; kalimat ketiga terlalu general ("lebih unggul" tanpa syarat) | Gabungkan jadi satu kalimat spesifik yang menyebut rentang gap di literatur (WS-03: 1-24 poin) dan posisi temuan ini (0,45 poin, di ujung bawah rentang tersebut) |

**Paragraf setelah perbaikan:**
> "Random Forest mencapai rata-rata accuracy 89,59% (+/-0,18) dibandingkan Naive Bayes 89,14% (+/-0,19) pada 5 run dengan seed berbeda, selisih 0,45 poin yang secara statistik signifikan menurut paired t-test (p=0,0047) meski marginal menurut uji Wilcoxon non-parametrik (p=0,0625) yang lebih sesuai karena distribusi accuracy Random Forest tidak normal (Shapiro-Wilk p=0,0069). Gap ini berada di ujung bawah rentang yang dilaporkan studi-studi pembanding berbahasa Indonesia (1-24 poin), mengindikasikan bahwa preprocessing linguistik yang diterapkan pada penelitian ini turut mengecilkan kesenjangan performa antara kedua algoritma."

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset berarti melaporkan apa yang dilakukan secara kronologis -- notebook dulu, lalu script v1, lalu ditemukan anomali, lalu v2 -- seolah itu jurnal harian. Menulis sebagai "argumen" berarti menyusun ulang urutan itu supaya pembaca melihat satu alur logis: gap -> RQ -> method yang sudah final (v2) -> hasil -> interpretasi yang jujur soal ketidakpastian statistik. Perjalanan menemukan bahwa preprocessing terlewat (WS-11) dan bahwa RF ternyata non-normal (WS-14) bukan bagian dari argumen utama, tapi jadi bahan Discussion dan Limitation yang memperkuat kredibilitas -- menunjukkan penelitian ini diuji dengan teliti, bukan disembunyikan seolah semuanya berjalan mulus sejak awal. Menulis Method dan Results lebih dulu (memakai data final v2) memaksa kejelasan angka sebelum menulis narasi Introduction yang framing-nya bisa disesuaikan dengan temuan aktual -- termasuk framing bahwa "sensitivitas terhadap preprocessing" adalah salah satu kontribusi, bukan sekadar catatan kaki.
