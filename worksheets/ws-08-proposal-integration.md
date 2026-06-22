# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [X] Problem → Gap:Masalah terdokumentasi dari analisis literatur
  hasil penelitian sebelumnya tentang Naive Bayes vs Random Forest pada klasifikasi teks Bahasa Indonesia     masih berbeda-beda tergantung dataset, preprocessing, dan domain sehingga menunjukkan adanya gap            penelitian yang nyata.
  [X] Gap → RQ: pertanyaan menjawab gap spesifik
  penelitian secara spesifik menanyakan apakah Random Forest menghasilkan performa lebih baik dibanding       Naive Bayes menggunakan TF-IDF pada dataset ulasan aplikasi Bahasa Indonesia dengan kondisi eksperimen      yang terkontrol.
  [X] RQ → Hypothesis: hipotesis memprediksi jawaban
  H₀ dan H₁ memprediksi jawaban RQ secara falsifiable menggunakan metrik accuracy, precision, recall, dan     F1-score.
  [X] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  Metrik accuracy, precision, recall, dan F1-score secara langsung mengoperasionalisasikan konsep “performa   klasifikasi sentimen” dalam hipotesis.
  [X] Metric → System: komponen sistem menghasilkan/mengukur metrik
  Setiap metrik dihasilkan otomatis oleh modul evaluasi classification_report dari scikit-learn sehingga      seluruh DV memiliki komponen sistem pengukurnya.
  [X] System → Experiment: desain eksperimen menggunakan sistem
  Desain eksperimen menggunakan sistem sebagai instrumen: modul classifier dapat di-swap antara Naive Bayes   dan Random Forest sementara dataset, preprocessing, TF-IDF, dan train-test split dijaga tetap identik.

Koneksi Horizontal (Konsistensi):
  [X] Istilah sama di semua bagian
      Istilah “Naive Bayes”, “Random Forest”, “TF-IDF”, “ulasan aplikasi Bahasa Indonesia”, “accuracy”,           “precision”, “recall”, dan “F1-score” digunakan secara konsisten dari WS-02 sampai WS-07.
  [X] Variabel di RQ = variabel di hipotesis = metrik di desain
      IV = jenis algoritma (NB vs RF); DV = performa klasifikasi; CV = dataset, preprocessing, TF-IDF, dan        train-test split konsisten di seluruh bagian proposal.
  [X] Scope tidak berubah dari masalah ke eksperimen
      Scope penelitian tetap fokus pada klasifikasi sentimen ulasan aplikasi Bahasa Indonesia menggunakan         Naive Bayes dan Random Forest berbasis TF-IDF tanpa melebar ke deep learning atau domain lain.

Cognitive Trap Checklist:
  [ ] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [ ] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [ ] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [ ] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [ ] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi | Banyak koneksi putus | Sebagian terhubung |Semua koneksi terdokumentasi| 3 |
| Specificity | Variabel abstrak | Sebagian terdefinisi | Semua variabel dan metrik teroperasionalisasi | 3 |
| Feasibility | Tidak realistis | Sebagian dapat dilakukan | Realistis dan terjadwal | 2 |
| Rigor     | Tidak ada kontrol | Beberapa dikontrol | Eksperimen terkontrol dan tervalidasi | 2 |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | *Belum jelas algoritma mana yang paling efektif untuk analisis sentimen teks Bahasa Indonesia pada konteks ulasan aplikasi karena hasil penelitian sebelumnya berbeda-beda tergantung dataset, preprocessing, dan ukuran data. Perbedaan hasil tersebut menunjukkan perlunya eksperimen yang lebih terkontrol dan terstandarisasi.* |
| Gap | WS-03 | *Belum ada perbandingan sistematis antara Naive Bayes dan Random Forest menggunakan TF-IDF pada dataset ulasan aplikasi Bahasa Indonesia dengan evaluasi accuracy, precision, recall, dan F1-score dalam kondisi eksperimen yang fair dan terkontrol.* |
| RQ | WS-04 | *Contoh: Apakah penambahan context-aware signals pada collaborative filtering meningkatkan satisfaction score tanpa menurunkan RMSE?* |
| RQ | WS-04 | *Apakah Random Forest menghasilkan performa klasifikasi sentimen yang lebih baik dibanding Naive Bayes menggunakan TF-IDF pada dataset ulasan aplikasi Bahasa Indonesia berdasarkan accuracy, precision, recall, dan F1-score?.* |
| Hipotesis | WS-04 | *H₀: Tidak ada perbedaan signifikan performa antara Naive Bayes dan Random Forest. H₁: Random Forest menghasilkan performa lebih baik dibanding Naive Bayes berdasarkan accuracy, precision, recall, dan F1-score.* |
| Variabel & Metrik | WS-05 | *IV = jenis algoritma (NB vs RF); DV = accuracy, precision, recall, F1-score; CV = dataset, preprocessing, TF-IDF, dan train-test split 80:20.* |
| Sistem | WS-06 | *Pipeline sistem terdiri dari preprocessing teks → TF-IDF Vectorizer → modul classifier (NB/RF) → modul evaluasi classification_report sklearn. Setiap komponen dipetakan langsung ke variabel penelitian.* |
| Desain Eksperimen | WS-07 | *Comparison study: Naive Bayes dan Random Forest diuji menggunakan dataset, preprocessing, TF-IDF, split data, dan environment yang identik sehingga hanya algoritma yang berubah.* |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | *✅* | *Gap berasal dari literature review WS-03 yang menunjukkan hasil NB vs RF masih inkonsisten di berbagai domain teks Bahasa Indonesia.* |
| Gap → RQ | *✅* | *RQ secara langsung menanyakan apakah RF lebih baik dibanding NB pada konteks yang sama dengan gap.* |
| RQ → Hypothesis | *✅* | *H₀ dan H₁ memprediksi jawaban RQ secara eksplisit dan dapat diuji secara empiris.* |
| Hypothesis → Metric |*✅* | *Variabel performa dioperasionalisasikan menjadi accuracy, precision, recall, dan F1-score.* |
| Metric → System | *✅*| *Semua metrik dihasilkan langsung oleh modul evaluasi sklearn.* |
| System → Experiment |*✅* | *Eksperimen menggunakan pipeline identik dengan hanya mengganti algoritma classifier.* |

**Koneksi mana yang paling lemah?** Hypothesis → Metric
**Bagaimana cara memperkuatnya?**
> Menambahkan threshold numerik eksplisit pada hipotesis, misalnya “Random Forest menghasilkan F1-score minimal 5% lebih tinggi dibanding Naive Bayes”, sehingga hipotesis tidak hanya menyatakan arah perbedaan tetapi juga magnitude yang dianggap bermakna.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [X] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | *3* | *Seluruh koneksi Problem → Gap → RQ → Hipotesis → Metrik → Sistem → Eksperimen saling terhubung dan tidak ada lompatan logis.* |
| Specificity | *3* | *Variabel, dataset, metrik, tools, dan konfigurasi eksperimen sudah dijelaskan secara konkret dan numerik.* |
| Feasibility | *2* | *Pipeline implementasi realistis, tetapi kualitas dan ukuran dataset masih perlu dipastikan agar representatif.* |
| Rigor | *2* | *Desain eksperimen sudah fair dan terkontrol, namun belum menggunakan uji statistik inferensial formal.* |

**Skor total:** 10 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** WS-06 (System-Experiment Mapping) Karena seluruh variabel dan pipeline penelitian sudah jelas sehingga pemetaan komponen sistem ke variabel dapat dilakukan secara langsung.
**Bagian tersulit:** WS-03 (Literature Mapping & Gap)  Karena harus membaca dan membandingkan banyak paper secara konseptual untuk menemukan gap yang benar-benar valid dan didukung bukti literatur.
**Yang akan dilakukan berbeda:**
> Pertama, menentukan dataset sejak awal sebelum menyusun RQ agar feasibility penelitian lebih terjamin.
> Kedua, sejak awal menetapkan threshold numerik pada hipotesis sehingga hubungan antara RQ, hipotesis, metrik, dan eksperimen menjadi lebih kuat dan spesifik.
