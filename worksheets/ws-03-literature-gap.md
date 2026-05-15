# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Klasifikasi Machine Learning untuk Soal Ujian Bahasa Indonesia SD
Database   : Google Scholar, Jurnal SISFOKOM, JIP Polinema, JCOSIS, Jurnal Algoritme, CONTEN, Jurnal Algoritma ITG
Query      : "klasifikasi machine learning soal ujian bahasa indonesia" OR "naive bayes random forest text classification Indonesian" OR "WEKA StringToWordVector klasifikasi teks"
Tahun      : 2022–2026
Hasil awal : 20 paper → Screening → 6 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|   Baharuddin & Tjahyanto    |    2022   |    Naïve Bayes, Random Forest, REPTree + StringToWordVector (WEKA)    |   183–418 soal ujian B. Indonesia SD (format CSV → ARFF)   |   REPTree terbaik: 91,15% (418 soal); peningkatan 15% dari awal     |      Hanya 1 mata pelajaran, pelabelan oleh 1 guru, dataset kecil, tidak menggunakan DL      |
|   Putra, Negara & Sastypratiwi (JIP Polinema, 2026)    |    2026   |    Naïve Bayes (Gaussian) & Random Forest + SMOTE / Undersampling (Python)    |  Bank Marketing UCI — 41.188 baris, imbalanced (tabular, non-teks)  |   RF + SMOTE: 93,08% (terbaik); NB Default: 91,78%     |      Dataset tabular bukan teks; domain non-pendidikan; tidak ada uji       |
|   Utami (JCOSIS, 2025)    |    2025   |    Naïve Bayes, SVM, Random Forest + TF-IDF + K-Fold CV (Python)    |   5.000 berita hoaks/valid Bahasa Indonesia (Kaggle + TurnBackHoax)   |   RF: 93,2%; SVM: 91%; NB: 88,5%     |      Domain berita bukan soal ujian; hanya 2 kelas; tidak di domain pendidikan      |
|  Meinita & Anshori (Jurnal Algoritme, 2025)    |    2025   |    Naïve Bayes (Multinomial) & Random Forest + TF-IDF + 5-Fold CV (Python/Google Colab)    |   26.873 percakapan chatbot customer service B. Indonesia (Kaggle)   |   RF: 96%; NB: 95%; perbedaan signifikan statistik (p = 4,78×10⁻⁷)     |      Domain layanan pelanggan bukan soal ujian; tidak ada eksperimen variasi ukuran dataset      |
|  Wati, Suleman & Widodo (CONTEN, 2025)    |    2025   |    Random Forest & Naïve Bayes + TF-IDF + Cross Validation (RapidMiner)    |   200 ulasan aplikasi Deepseek Google Play Store (label manual)   |   RF: 96,38%; NB: 72,96%     |     Dataset sangat kecil (200 data); domain ulasan aplikasi; gap NB sangat besar      |
|  Nugroho, Hayati & Jabir (Jurnal Algoritma ITG, 2025)    |    2025   |    Naïve Bayes & Random Forest + TF-IDF + SMOTE + berbagai rasio split (Python)    |   34.078 ulasan aplikasi IKD Google Play Store (lexicon InSet, B. Indonesia)   |   RF: 93% (terbaik); NB: 89–90% (dengan SMOTE)     |     Label otomatis berbasis lexicon; hanya 2 kelas sentimen; sumber data tunggal (Play Store)      |


Pola yang ditemukan:
  Metode dominan     : Random Forest secara konsisten mengungguli Naive Bayes di semua studi komparasi teks B. Indonesia (akurasi RF: 91–96% vs NB: 65–95%); REPTree hanya diuji pada dataset soal ujian spesifik.
  Dataset umum       : Dataset teks Bahasa Indonesia didominasi domain non-pendidikan seperti berita, chatbot, dan ulasan aplikasi. Dataset soal ujian pendidikan masih sangat terbatas
  Limitasi berulang  : Dataset kecil, domain sempit, pelabelan manual/subjektif, belum ada eksperimen variasi ukuran data, dan belum menggunakan pendekatan deep learning.

GAP IDENTIFICATION

Gap 1: [Performance Gap]
  Deskripsi    : Performa Naïve Bayes masih jauh di bawah Random Forest dan REPTree pada klasifikasi teks soal Bahasa Indonesia SD.
  Bukti        : Pada penelitian Baharuddin & Tjahyanto (2022), NB hanya memperoleh akurasi 64,83% sedangkan REPTree mencapai 91,15%.
  Signifikansi : Menunjukkan masih ada peluang peningkatan performa klasifikasi teks pendidikan Indonesia menggunakan metode dan preprocessing yang lebih modern.

Gap 2: [Method Gap]
  Deskripsi    : Belum ada penelitian yang menerapkan TF-IDF, K-Fold Cross Validation, maupun SMOTE pada dataset soal ujian Bahasa Indonesia SD.
  Bukti        : Studi yang ada hanya menggunakan StringToWordVector berbasis WEKA tanpa eksplorasi pipeline Python modern.
  Signifikansi : Metode tersebut telah terbukti efektif pada domain teks lain dan berpotensi meningkatkan akurasi klasifikasi soal ujian.

Gap 3: [Data Gap]
  Deskripsi    : Dataset soal ujian Bahasa Indonesia SD masih sangat kecil dan belum representatif..
  Bukti        : Seluruh studi pada domain ini hanya menggunakan 183–418 soal.
  Signifikansi : Dataset kecil menyebabkan model kurang generalizable dan sulit mengevaluasi performa pada kondisi nyata.

Gap 4: [Context Gap]
  Deskripsi    : Penelitian terbaru NB vs RF lebih banyak dilakukan pada domain non-pendidikan.
  Bukti        :Studi tahun 2025–2026 fokus pada berita, chatbot, marketing, dan ulasan aplikasi.
  Signifikansi : Belum ada validasi apakah performa metode tersebut tetap konsisten pada konteks soal ujian Bahasa Indonesia SD.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
|     REPTree + StringToWordVecto     |    Menyelesaikan task yang sama persis       |       Menjadi acuan performa terbaik pada dataset soal ujian        |    Baharuddin & Tjahyanto (2022)    |
|     Random Forest + TF-IDF     |    Digunakan luas pada klasifikasi teks Bahasa Indonesia      |       Common practice pada banyak studi terbaru        |    Utami (2025), Meinita & Anshori (2025), Nugroho et al. (2025)    |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** ________________________________________
**Query pencarian:** ____________________________________
**Database:** ___________________________________________

| # | Study                  | Tahun | Method           | Dataset         | Result         | Limitasi               |
| - | ---------------------- | ----- | ---------------- | --------------- | -------------- | ---------------------- |
| 1 | Baharuddin & Tjahyanto | 2022  | NB, RF, REPTree  | 418 soal ujian  | REPTree 91,15% | Dataset kecil          |
| 2 | Putra et al.           | 2026  | NB, RF + SMOTE   | Bank Marketing  | RF 93,08%      | Non-teks               |
| 3 | Utami                  | 2025  | NB, RF, SVM      | Berita hoaks    | RF 93,2%       | Domain berbeda         |
| 4 | Meinita & Anshori      | 2025  | NB & RF + TF-IDF | Chatbot CS      | RF 96%         | Tidak uji variasi data |
| 5 | Nugroho et al.         | 2025  | NB & RF + TF-IDF | Ulasan aplikasi | RF 93%         | Sumber data tunggal    |


**Pola yang terlihat — Metode dominan:** Random Forest + TF-IDF
**Limitasi yang berulang:** Dataset kecil, domain non-pendidikan, dan kurang variasi eksperimen.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap       | Ditemukan? | Gap Statement                                                       |
| --------------- | ---------- | ------------------------------------------------------------------- |
| Performance Gap | [X] Ya     | Akurasi NB masih rendah pada teks pendidikan Indonesia              |
| Method Gap      | [X] Ya     | Belum ada TF-IDF dan pipeline Python modern pada dataset soal ujian |
| Data Gap        | [X] Ya     | Dataset soal ujian masih kecil                                      |
| Context Gap     | [X] Ya     | Belum ada evaluasi pada domain pendidikan SD                        |


**Gap utama yang dipilih:** Method Gap + Context Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena penelitian sebelumnya belum membandingkan pendekatan modern klasifikasi teks pada konteks soal ujian Bahasa Indonesia SD, sehingga belum ada referensi yang kuat untuk pengembangan sistem bank soal digital pendidikan Indonesia.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | *REPTree + StringToWordVector* | *Task sama* | *Acuan performa terbaik* | *Ya* | *Baharuddin & Tjahyanto (2022)* |
| 2 | *RF + TF-IDF* | *Banyak dipakai pada klasifikasi teks Indonesia* | *Common practice terbaru* | *Ya* | *Baharuddin & Utami (2025), Meinita (2025)* |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [X] Tidak
> Justifikasi: Baseline yang dipilih merupakan metode terbaik pada konteks serupa dan metode yang paling sering digunakan pada penelitian klasifikasi teks Bahasa Indonesia terbaru.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim “belum ada yang meneliti ini” tanpa bukti bukan research gap yang valid karena tidak didukung proses penelusuran literatur. Research gap yang valid harus diperoleh melalui pencarian paper secara sistematis, kemudian dianalisis untuk menemukan pola, keterbatasan, dan area yang belum dieksplorasi.
Gap dapat dibuktikan dengan:
1.Mendokumentasikan query pencarian
2.Membuat literature matrix
3.Membandingkan metode, dataset, dan konteks penelitian
4.Menunjukkan kombinasi metode–data–konteks yang belum pernah diuji sebelumnya.
