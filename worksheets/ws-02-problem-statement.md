# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Machine Learning & Pendidikan (Natural Language Processing / Text Classification)
  Konteks  : Klasifikasi otomatis soal ujian Bahasa Indonesia tingkat SD berdasarkan tingkat kesulitan menggunakan WEKA Tools

System Context
  Input       : Dataset soal ujian Bahasa Indonesia (teks pilihan ganda), label kategori (mudah/sedang/sulit)
  Process     : Pra proses (pelabelan manual), filtering StringToWordVector, klasifikasi ML (Naive Bayes, Random Forest, REPTree)
  Output      : Label prediksi tingkat kesulitan soal + performa akurasi klasifikasi (%)
  Outcome     : Klasifikasi soal ujian yang efisien dan akurat tanpa pelabelan manual

  Constraints : Dataset terbatas (hanya 183 soal awal), pelabelan ground truth dilakukan manual oleh 1 guru, hanya satu mata pelajaran (B. Indonesia SD)

  Stakeholders: Guru SD, pengembang sistem ujian, institusi pendidikan, peneliti NLP


Fenomena → Problem
  Fenomena yang diamati             : Guru kesulitan mengkategorikan soal ujian secara manual berdasarkan tingkat kesulitan secara konsisten

  Gejala (symptom) yang terukur     : Proses pelabelan soal tidak konsisten, bergantung pada subjektivitas guru, dan memakan waktu

  Masalah yang didiagnosis          : Belum ada metode otomatis yang andal untuk klasifikasi tingkat kesulitan soal teks Bahasa Indonesia

  Masalah riset (researchable)      : Algoritma ML mana yang menghasilkan performa terbaik, dan seberapa besar pengaruh ukuran dataset terhadap akurasi klasifikasi?

  Variabel yang terukur             : Correct Classification Rate (%), jumlah data (183→273→418), algoritma (NB, RF, REPTree)


Problem Quality Check
  [Y] Clarity — Apakah satu orang membaca akan paham?
  [Y] Measurability — Apakah ada metrik kuantitatif?
  [Y] Relevance — Apakah penting untuk domain?
  [Y] Testability — Apakah bisa gagal?
  [Y] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Proses kategorisasi soal ujian Bahasa Indonesia tingkat sekolah dasar berdasarkan tingkat kesulitan masih dilakukan secara manual dan subjektif, sehingga tidak konsisten dan tidak skalabel. Belum ada studi yang secara sistematis membandingkan performa algoritma machine learning (Naive Bayes, Random Forest, REPTree) terhadap dataset soal teks Bahasa Indonesia, sekaligus mengukur pengaruh peningkatan kuantitas dataset terhadap akurasi klasifikasi. Penelitian ini bertujuan mengisi gap tersebut dengan mengeksperimentasi kombinasi metode klasifikasi dan ukuran dataset menggunakan WEKA Tools, dengan metrik keberhasilan berupa correct classification rate (%).
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Klasifikasi machine learning untuk soal ujian Bahasa Indonesia

| Tahap | Hasil |
|-------|-------|
| Reality |Guru SD harus menyusun bank soal ujian dengan tingkat kesulitan yang terukur dan merata, namun prosesnya dilakukan manual|
| Observed Issue (Symptom) |Pelabelan tingkat kesulitan soal tidak konsisten antar guru dan memakan waktu signifikan|
| Diagnosed Problem (Root Cause) |Belum ada sistem otomatis yang dapat mengklasifikasikan soal teks Bahasa Indonesia berdasarkan tingkat kesulitan secara akurat|
| Researchable Problem |Algoritma ML mana (NB, RF, REPTree) yang paling akurat, dan seberapa besar pengaruh ukuran dataset terhadap performa klasifikasi?|
| Measurable Variable |Correct Classification Rate (%), jumlah soal (183 / 273 / 418), algoritma yang digunakan |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data soal pilihan ganda Bahasa Indonesia SD (teks uraian, pertanyaan, 4 opsi jawaban, kunci jawaban) yang dikumpulkan dari bank soal online dan buku pembahasan; format awal CSV kemudian dikonversi ke ARFF |
| Process | Proses penelitian dimulai dengan pelabelan manual kategori tingkat kesulitan soal (mudah, sedang, sulit) yang dilakukan oleh guru berpengalaman. Selanjutnya, dataset yang semula dalam format CSV dikonversi ke format ARFF agar dapat diproses menggunakan WEKA. Setelah itu, dilakukan tahap filtering berupa tokenisasi menggunakan metode StringToWordVector yang mengubah data teks menjadi atribut fitur. Dataset yang telah diproses kemudian diklasifikasikan menggunakan tiga algoritma, yaitu Naive Bayes, Random Forest, dan REPTree. Hasil klasifikasi selanjutnya dievaluasi, dan apabila performanya belum optimal, maka dilakukan peningkatan dataset dan seluruh proses diulang hingga diperoleh hasil yang lebih baik. |
| Output | Label prediksi kategori soal (mudah/sedang/sulit) untuk setiap soal dalam dataset, beserta correct classification rate (%) dari masing-masing algoritma pada setiap iterasi dataset |
| Outcome | 	Rekomendasi algoritma terbaik (REPTree) dan bukti empiris bahwa penambahan data meningkatkan akurasi klasifikasi secara signifikan hingga 15% |
| Constraints | Penelitian ini punya beberapa keterbatasan. Dataset yang dipakai cuma dari satu mata pelajaran, yaitu Bahasa Indonesia, dan hanya untuk tingkat SD. Penentuan label tingkat kesulitan juga bergantung pada satu guru, jadi ada kemungkinan subjektif. Selain itu, tools yang digunakan hanya WEKA, tanpa mencoba metode yang lebih lanjut seperti deep learning. Ditambah lagi, jumlah datanya masih relatif sedikit, maksimal cuma 418 soal, jadi bisa berpengaruh ke kemampuan model untuk generalisasi. |
| Stakeholders | 	Guru SD (pengguna akhir sistem), pengembang bank soal digital, Kemendikbud/institusi pendidikan, peneliti NLP Bahasa Indonesia |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan input

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 4 | Masalah jelas dibaca: membandingkan algoritma ML untuk klasifikasi soal. Kekurangan: "tingkat kesulitan" tidak didefinisikan secara operasional hanya bergantung penilaian 1 guru tanpa rubrik eksplisit. |
| Measurability | 5 | 
5/5
Sangat baik
Metrik sangat eksplisit: correct classification rate (%). Setiap percobaan menghasilkan angka yang presisi (mis. 75.96%, 91.15%). Jumlah data juga terdokumentasi dengan baik. |
| Relevance | 4 | Relevan untuk NLP Bahasa Indonesia dan teknologi pendidikan yang masih berkembang. Sedikit berkurang karena scope sangat sempit (hanya SD, hanya B. Indonesia).|
| Testability | 5 | Bisa gagal dan bisa direplikasi. Jika penambahan data tidak meningkatkan akurasi, hipotesis terbantah. Prosedur eksperimen dengan WEKA cukup detail untuk direplikasi peneliti lain. |
| Impact | 4 | Kontribusi nyata: panduan pemilihan algoritma dan ukuran dataset untuk kasus sejenis. Dampaknya bisa lebih besar jika dataset dipublikasikan dan metodologi diperluas ke mata pelajaran lain. |

**Skor total:** 22 / 25

**Problem statement versi final (1 paragraf):**
> Saat ini, pengelompokan soal ujian Bahasa Indonesia tingkat SD berdasarkan tingkat kesulitan masih dilakukan secara manual oleh guru, sehingga hasilnya bisa tidak konsisten dan sulit diterapkan dalam skala besar. Masalahnya, belum banyak studi yang membandingkan performa algoritma machine learning seperti Naive Bayes, Random Forest, dan REPTree pada dataset soal berbahasa Indonesia. Selain itu, juga belum jelas seberapa besar pengaruh penambahan jumlah data terhadap akurasi klasifikasi. Penelitian ini mencoba menjawab hal tersebut dengan melakukan eksperimen klasifikasi secara bertahap menggunakan WEKA dan metode StringToWordVector, di mana performa diukur menggunakan tingkat akurasi pada tiga ukuran dataset berbeda, yaitu 183, 273, dan 418 soal.


---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
<Masalah Coding: Masalah dalam coding biasanya      didefinisikan sebagai sesuatu yang tidak berjalan, seperti bug, error, atau fitur yang belum ada. Tujuannya sederhana: cukup sampai sistem bisa bekerja sesuai harapan. Misalnya kalau diibaratkan dari jurnal ini dalam konteks engineering, cukup “buat program yang bisa mengklasifikasi soal.” Begitu akurasinya sudah dianggap cukup dan sistem berjalan, masalahnya dianggap selesai tanpa perlu pembuktian lebih lanjut.>

<Masalah Riset: Masalah dalam riset didefinisikan sebagai adanya gap dalam pengetahuan, yaitu sesuatu yang belum terbukti atau belum dibandingkan secara sistematis. Masalah seperti ini harus bisa diuji, bisa gagal, dan bisa direplikasi oleh peneliti lain. Kalau dikaitkan dengan jurnal ini, pertanyaannya bukan sekadar “bisa bikin sistem klasifikasi atau tidak”, tapi lebih ke “algoritma mana yang paling baik dan kenapa?” serta “berapa jumlah data yang cukup untuk mendapatkan performa optimal?”. Pertanyaan seperti ini hanya bisa dijawab lewat eksperimen yang terkontrol, bukan sekadar membuat sistem berjalan.>

> <Perbedaan utamanya, engineering biasanya berhenti saat sistem sudah berjalan dengan baik, sedangkan research berhenti ketika klaimnya sudah terbukti atau justru terbantah. Dalam jurnal Baharuddin & Tjahyanto, mereka tidak hanya membuat sistem klasifikasi, tapi juga membuktikan bahwa kombinasi REPTree dengan dataset 418 soal bisa mencapai akurasi 91,15%. Artinya, mereka menghasilkan klaim yang bisa diuji, diverifikasi, bahkan dibantah oleh peneliti lain.>
