# Perbandingan Algoritma Naïve Bayes dan Random Forest untuk Analisis Sentimen Ulasan Aplikasi Gojek Berbahasa Indonesia Menggunakan TF-IDF

**Mohamad Gilang Rizki Riomdona**
Program Studi Ilmu Komputer, Fakultas Sains dan Teknologi, Universitas Putra Bangsa, Kebumen, Indonesia
240202903

---

## Abstrak

Gojek merupakan platform super-app dengan jutaan pengguna aktif yang menghasilkan ribuan ulasan setiap hari di Google Play Store, sehingga analisis sentimen manual tidak lagi efisien pada skala tersebut. Studi-studi terdahulu melaporkan performa Naïve Bayes (NB) dan Random Forest (RF) yang tidak konsisten pada klasifikasi teks Bahasa Indonesia — gap akurasi RF terhadap NB berkisar 1–24 poin tergantung domain — namun belum ada studi yang membandingkan keduanya secara terkontrol khusus pada ulasan aplikasi Gojek. Penelitian ini membandingkan performa NB dan RF menggunakan TF-IDF sebagai ekstraksi fitur, pada 100.000 ulasan Gojek berbahasa Indonesia (dataset publik Kaggle), melalui pipeline preprocessing seragam (case folding, cleansing, stopword removal, stemming Sastrawi) dan 5 kali replikasi (seed berbeda) per algoritma untuk menjamin keandalan statistik. Hasil menunjukkan Random Forest mencapai rata-rata accuracy 89,59% (±0,18) dibandingkan Naïve Bayes 89,14% (±0,19), selisih 0,45 poin yang signifikan menurut paired t-test (p=0,0047) namun marginal menurut uji Wilcoxon non-parametrik (p=0,0625) yang lebih sesuai karena distribusi accuracy Random Forest melanggar asumsi normalitas (Shapiro-Wilk, p=0,0069). Analisis lanjutan menemukan bahwa preprocessing linguistik mengecilkan gap performa secara substansial dibandingkan representasi TF-IDF pada teks mentah (gap 1,71 poin tanpa preprocessing). Kontribusi penelitian ini adalah perbandingan empiris pertama NB vs RF pada domain ulasan Gojek dengan pipeline seragam, serta bukti kuantitatif bahwa keputusan preprocessing dapat mengubah besaran kesimpulan komparasi algoritma secara signifikan.

**Kata Kunci**: Analisis Sentimen; Naïve Bayes; Random Forest; TF-IDF; Ulasan Aplikasi Gojek; Klasifikasi Teks Bahasa Indonesia

## Abstract

Gojek is a super-app platform with millions of active users generating thousands of daily reviews on the Google Play Store, making manual sentiment analysis impractical at scale. Prior studies report inconsistent performance between Naïve Bayes (NB) and Random Forest (RF) for Indonesian text classification — with accuracy gaps ranging from 1–24 points depending on domain — yet no study has directly compared both algorithms under controlled conditions specifically on Gojek app reviews. This study compares NB and RF performance using TF-IDF feature extraction on 100,000 Indonesian-language Gojek reviews (public Kaggle dataset), applying a uniform preprocessing pipeline (case folding, cleansing, stopword removal, Sastrawi stemming) and 5 replications (distinct seeds) per algorithm to ensure statistical reliability. Results show Random Forest achieving a mean accuracy of 89.59% (±0.18) compared to Naïve Bayes at 89.14% (±0.19), a 0.45-point difference that is statistically significant under a paired t-test (p=0.0047) but marginal under the non-parametric Wilcoxon signed-rank test (p=0.0625), which is more appropriate given that Random Forest's accuracy distribution violates normality (Shapiro-Wilk, p=0.0069). Further analysis found that linguistic preprocessing substantially narrows the performance gap compared to raw-text TF-IDF representations (1.71-point gap without preprocessing). This study contributes the first empirical NB vs RF comparison on the Gojek review domain under a uniform pipeline, along with quantitative evidence that preprocessing decisions can meaningfully alter the magnitude of algorithm comparison conclusions.

**Keywords**: Sentiment Analysis; Naïve Bayes; Random Forest; TF-IDF; Gojek App Reviews; Indonesian Text Classification

---

## 1. Pendahuluan

Gojek merupakan platform super-app yang berkembang menjadi salah satu ekosistem layanan digital terbesar di Asia Tenggara, mencakup transportasi, pengantaran makanan, pembayaran digital, hingga logistik. Sebagai aplikasi dengan puluhan juta pengguna aktif di Indonesia, Gojek mengumpulkan ribuan ulasan pengguna setiap harinya di Google Play Store. Ulasan-ulasan ini mengandung opini, keluhan, dan apresiasi yang berpotensi besar sebagai sumber intelijen bisnis, namun membacanya satu per satu secara manual tidak memungkinkan pada skala tersebut.

Analisis sentimen otomatis berbasis machine learning menjadi solusi yang relevan. Dua algoritma yang paling umum digunakan untuk klasifikasi teks Bahasa Indonesia adalah Naïve Bayes dan Random Forest. Studi-studi terdahulu melaporkan hasil yang tidak konsisten: Nugroho dkk. [1] melaporkan RF mencapai 93% versus NB 89–90% pada ulasan aplikasi IKD; Meinita dan Anshori [2] mendapatkan RF 96% berbanding NB 95% pada dataset chatbot layanan pelanggan; Wati dkk. [3] mencatat selisih jauh lebih besar, RF 96,38% versus NB 72,96%, pada ulasan aplikasi Deepseek; sementara Pranata dkk. [4] hanya menguji NB dengan TF-IDF pada data Twitter dan memperoleh 74,46%. Variasi hasil yang besar ini menunjukkan bahwa performa kedua algoritma sangat bergantung pada domain dan konteks dataset.

Belum ada studi yang secara khusus membandingkan Naïve Bayes dan Random Forest pada ulasan aplikasi Gojek berbahasa Indonesia dalam satu eksperimen terkontrol, dengan pipeline preprocessing seragam dan metrik evaluasi lengkap. Studi yang ada umumnya menguji satu algoritma tunggal saja [3][4] atau menggunakan domain yang berbeda karakteristik bahasanya (berita, chatbot, e-commerce) dari ulasan Gojek yang cenderung informal. Kesenjangan ini menghasilkan gap Method sekaligus Context yang menjadi celah penelitian.

Rumusan masalah penelitian ini: **apakah Random Forest menghasilkan performa klasifikasi sentimen yang lebih baik dibandingkan Naïve Bayes menggunakan TF-IDF pada dataset ulasan aplikasi Gojek berbahasa Indonesia, berdasarkan accuracy, precision, recall, dan F1-score?** Hipotesis yang diajukan: H₀ menyatakan tidak ada perbedaan signifikan performa antara kedua algoritma, sedangkan H₁ menyatakan Random Forest menghasilkan performa yang lebih baik.

Kontribusi penelitian ini mencakup tiga hal: (1) perbandingan empiris pertama NB versus RF pada domain ulasan Gojek berbahasa Indonesia dengan pipeline seragam dan lima kali replikasi per algoritma; (2) penggunaan dataset publik Kaggle yang mendukung reproducibility eksperimen; dan (3) bukti kuantitatif bahwa gap performa NB-RF sensitif terhadap keputusan preprocessing — sebuah temuan metodologis yang belum eksplisit dilaporkan pada studi-studi pembanding.

## 2. Tinjauan Pustaka

Kajian literatur dilakukan pada Google Scholar dan sejumlah jurnal nasional (SISFOKOM, Algoritme, Algoritma ITG, CONTEN, Informatika Terpadu, Jurnal Ilmu Komputer Universitas Pamulang) dengan rentang tahun 2022–2026. Baharuddin dan Tjahyanto [5] membandingkan metode machine learning secara umum dan menjadi baseline metodologis (REPTree/WEKA) untuk pendekatan peningkatan performa klasifikasi. Firdaus dkk. [6] menguji Random Forest dengan fitur Bag-of-Word pada ulasan Shopee, namun tidak menyertakan Naïve Bayes sebagai pembanding. Pranata dkk. [4] menguji Naïve Bayes dengan TF-IDF pada data Twitter, memperoleh akurasi 74,46%, tanpa pembanding Random Forest.

Tiga studi memberikan perbandingan langsung NB vs RF: Nugroho dkk. [1] pada ulasan aplikasi pemerintahan (IKD) dengan gap ~3–4 poin; Meinita dan Anshori [2] pada chatbot layanan pelanggan dengan gap ~1 poin (gap terkecil di antara studi pembanding); dan Wati dkk. [3] pada ulasan Deepseek dengan gap ~23,4 poin (gap terbesar). Random Forest secara konsisten mengungguli Naïve Bayes di ketiga studi ini, namun besaran gap sangat bervariasi (1–24 poin), mengindikasikan sensitivitas tinggi terhadap domain dan konfigurasi eksperimen.

Gap yang teridentifikasi bersifat Method Gap sekaligus Context Gap: belum ada studi yang membandingkan NB dan RF secara bersamaan pada ulasan Gojek dengan pipeline seragam, dan karakteristik bahasa informal ulasan Gojek berbeda dari domain pemerintahan, chatbot, e-commerce, maupun politik yang sudah diteliti. Referensi tambahan dari domain klasifikasi teks Bahasa Indonesia yang lebih luas — klasifikasi berita [7], deteksi hoaks [8], dan klasifikasi dokumen berbasis ontologi [9] — memperkuat gambaran bahwa performa algoritma klasifikasi teks Bahasa Indonesia bersifat sangat domain-dependent, mendukung urgensi studi khusus pada domain Gojek.

## 3. Metodologi

### 3.1 Desain Penelitian

Penelitian ini menggunakan desain kuantitatif eksperimental bertipe controlled comparison experiment. Variabel independen (IV) adalah jenis algoritma klasifikasi (Multinomial Naïve Bayes vs Random Forest); variabel dependen (DV) adalah performa klasifikasi yang dioperasionalisasikan menjadi accuracy, precision, recall, dan F1-score (average='weighted'); variabel kontrol (CV) meliputi dataset, pipeline preprocessing, parameter TF-IDF, rasio split, dan lingkungan eksekusi — seluruhnya dikunci identik antar kondisi.

Kondisi A (baseline) menggunakan Multinomial Naïve Bayes (alpha=1,0); Kondisi B (intervensi) menggunakan Random Forest (n_estimators=100, max_depth=None). Kedua kondisi memakai TF-IDF Vectorizer identik (max_features=5.000, di-fit hanya pada data latih untuk mencegah data leakage).

### 3.2 Data dan Preprocessing

Dataset berasal dari platform publik Kaggle berupa ulasan aplikasi Gojek berbahasa Indonesia. Setiap replikasi mengambil sampel stratified 100.000 ulasan (50.000 positif, 50.000 negatif) dengan seed berbeda (42, 123, 456, 789, 2024), lalu dibagi 80:20 (train:test) dengan random_state sama dengan seed replikasi tersebut.

Pipeline preprocessing diterapkan secara seragam pada kedua kondisi: (1) case folding, (2) cleansing (penghapusan simbol, angka, URL), (3) stopword removal menggunakan daftar stopword Bahasa Indonesia dari NLTK, dan (4) stemming menggunakan Sastrawi. Seluruh tahap ini dijalankan sekali pada korpus penuh sebelum sampling per-seed, dengan hasil di-cache untuk efisiensi replikasi.

**Catatan metodologis penting**: implementasi awal skrip eksperimen multi-run (v1) sempat tidak menyertakan tahap preprocessing linguistik ini akibat kelalaian implementasi, menghasilkan representasi TF-IDF pada teks mentah. Anomali ini terdeteksi melalui proses validasi silang antara hasil eksplorasi single-run (yang memakai pipeline lengkap) dan hasil multi-run awal pada seed yang sama, yang menunjukkan selisih akurasi ~1 poin yang tidak seharusnya terjadi jika kedua pipeline identik. Setelah dikonfirmasi dan diperbaiki (v2), seluruh hasil pada bagian 4 menggunakan pipeline preprocessing lengkap sebagai hasil akhir; hasil versi v1 dilaporkan pada bagian 4.4 sebagai analisis sensitivitas.

### 3.3 Prosedur Eksperimen dan Fairness

Setiap replikasi (seed) menjalankan kedua algoritma pada data latih dan uji yang identik. Fairness eksperimen dijaga melalui: dataset identik, preprocessing seragam, TF-IDF vectorizer tunggal yang di-fit pada data latih dan dipakai untuk mentransformasi data uji pada kedua kondisi, train-test split identik per seed, dan parameter default tanpa tuning manual untuk menghindari bias yang menguntungkan salah satu algoritma. Total 10 run (5 seed × 2 algoritma) dieksekusi dan dicatat sebagai log terstruktur (JSON) berisi identitas run, konfigurasi, hasil metrik, confusion matrix, dan status anomali.

### 3.4 Teknik Analisis

Data dianalisis secara deskriptif (mean, std) per algoritma atas 5 replikasi. Uji normalitas Shapiro-Wilk diterapkan pada distribusi accuracy tiap grup sebelum memilih uji hipotesis. Karena satu grup (Random Forest) melanggar asumsi normalitas, penelitian ini melaporkan baik paired t-test (asumsi normal) maupun Wilcoxon signed-rank test (non-parametrik) untuk transparansi penuh. Effect size dilaporkan menggunakan Cohen's d untuk t-test. Perbedaan accuracy ≥5% ditetapkan sebagai ambang bermakna secara praktis, mengacu pada konsensus studi klasifikasi teks Bahasa Indonesia terkini.

## 4. Hasil dan Analisis

### 4.1 Statistik Deskriptif

Tabel 1 menyajikan hasil deskriptif atas 5 replikasi per algoritma, menggunakan pipeline preprocessing lengkap (hasil final).

**Tabel 1.** Statistik deskriptif performa NB dan RF (n=5 per algoritma)

| Skenario | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Waktu Latih (s) |
|---|---|---|---|---|---|
| Random Forest | 89,59 ± 0,18 | 89,64 ± 0,18 | 89,59 ± 0,18 | 89,58 ± 0,18 | 28,52 ± 0,60 |
| Naïve Bayes | 89,14 ± 0,19 | 89,54 ± 0,16 | 89,14 ± 0,19 | 89,11 ± 0,20 | 0,32 ± 0,03 |

Random Forest mengungguli Naïve Bayes pada seluruh 5 seed tanpa kecuali, dengan selisih accuracy rata-rata 0,45 poin. Waktu latih Random Forest ~89 kali lebih lama dibanding Naïve Bayes, mencerminkan kompleksitas komputasi ensemble tree dibanding model probabilistik linear.

### 4.2 Uji Hipotesis

Uji normalitas Shapiro-Wilk menunjukkan distribusi accuracy Naïve Bayes normal (W=0,875, p=0,286) namun distribusi Random Forest tidak normal (W=0,686, p=0,0069), disebabkan satu nilai accuracy yang relatif tinggi pada seed 2024 (89,91%) dibanding empat run RF lainnya yang sangat rapat (89,48–89,56%).

Paired t-test pada accuracy menghasilkan t(4)=5,70, p=0,0047, Cohen's d=2,55, dengan selisih mean 0,448 poin (95% CI [0,230; 0,666]) — signifikan pada α=0,05. Namun, karena asumsi normalitas Random Forest dilanggar, uji Wilcoxon signed-rank yang lebih sesuai menghasilkan p=0,0625 — marginal, tidak signifikan pada α=0,05 konvensional, meskipun p-value ini merupakan nilai minimum yang dapat dicapai Wilcoxon pada n=5 (keterbatasan resolusi uji non-parametrik pada sampel kecil). Kedua uji tetap sejalan dalam hal arah efek: Random Forest unggul pada seluruh 5 pasangan seed tanpa kecuali.

Hasil serupa diperoleh pada F1-score (paired t-test: t(4)=6,00, p=0,0039, d=2,68).

### 4.3 Interpretasi

Berdasarkan konsistensi arah efek di seluruh replikasi, penelitian ini menyimpulkan bahwa Random Forest secara konsisten mengungguli Naïve Bayes pada domain ulasan Gojek, namun signifikansi statistiknya bergantung pada uji yang dipilih dan besaran praktisnya (0,45 poin) berada di bawah ambang bermakna praktis (≥5%) yang ditetapkan pada bagian metodologi. Gap ini juga berada di ujung paling bawah rentang yang dilaporkan studi-studi pembanding (1–24 poin) [1][2][3], jauh lebih kecil dari yang diperkirakan berdasarkan pola literatur.

### 4.4 Analisis Sensitivitas: Pengaruh Preprocessing terhadap Gap Performa

Sebagai bagian dari validasi metodologis (lihat bagian 3.2), penelitian ini membandingkan hasil final (dengan preprocessing lengkap) terhadap versi awal eksperimen yang tanpa sengaja menggunakan representasi TF-IDF pada teks mentah (Tabel 2).

**Tabel 2.** Perbandingan gap accuracy RF-NB dengan dan tanpa preprocessing linguistik

| Versi | Preprocessing | Accuracy RF | Accuracy NB | Gap | Uji Signifikansi |
|---|---|---|---|---|---|
| Tanpa preprocessing | Tidak ada (TF-IDF pada teks mentah) | 90,13% | 88,42% | 1,71 poin | Paired t-test: p=0,0002, d=5,78 |
| Dengan preprocessing (final) | Lengkap | 89,59% | 89,14% | 0,45 poin | Paired t-test: p=0,0047; Wilcoxon: p=0,0625 |

Preprocessing linguistik menaikkan accuracy Naïve Bayes (88,42%→89,14%) sementara Random Forest justru sedikit menurun (90,13%→89,59%), sehingga gap menyempit signifikan. Temuan ini mengindikasikan bahwa Naïve Bayes lebih diuntungkan oleh representasi teks yang bersih (kata dasar, tanpa noise imbuhan dan stopword) dibanding Random Forest, yang kemungkinan sudah cukup robust terhadap noise pada representasi TF-IDF mentah karena mekanisme ensemble-nya. Implikasinya, klaim keunggulan Random Forest atas Naïve Bayes pada klasifikasi teks Bahasa Indonesia perlu selalu disertai konteks pipeline preprocessing yang digunakan, bukan digeneralisasi sebagai keunggulan tetap.

### 4.5 Keterbatasan

Penelitian ini memiliki keterbatasan: (1) jumlah replikasi (n=5) tergolong kecil, membatasi power statistik terutama pada uji non-parametrik yang p-value minimumnya terbatas pada 0,0625; (2) distribusi accuracy Random Forest melanggar asumsi normalitas akibat satu outlier, meski investigasi tidak menemukan indikasi bug; (3) hasil terbatas pada domain ulasan Gojek berbahasa Indonesia dan tidak serta-merta berlaku untuk aplikasi lain; dan (4) gap performa terbukti sensitif terhadap keputusan preprocessing, sehingga kesimpulan penelitian ini spesifik untuk pipeline yang digunakan.

## 5. Kesimpulan

Random Forest menghasilkan performa klasifikasi sentimen yang secara arah konsisten lebih baik dibandingkan Naïve Bayes pada seluruh replikasi (5 dari 5 seed) dalam mengklasifikasikan ulasan aplikasi Gojek berbahasa Indonesia menggunakan TF-IDF, dengan selisih accuracy rata-rata 0,45 poin (89,59% vs 89,14%). Signifikansi statistik bergantung pada uji yang digunakan — signifikan menurut paired t-test (p=0,0047) namun marginal menurut Wilcoxon signed-rank test (p=0,0625) yang lebih sesuai karena pelanggaran asumsi normalitas pada grup Random Forest — sehingga H₁ diterima dengan kualifikasi: efek konsisten arahnya namun besaran praktisnya kecil. Kontribusi utama penelitian ini adalah perbandingan empiris pertama NB vs RF pada domain ulasan Gojek dengan pipeline seragam, serta bukti kuantitatif bahwa preprocessing linguistik dapat mengecilkan gap performa NB-RF secara substansial (dari 1,71 menjadi 0,45 poin), menegaskan bahwa kesimpulan komparasi algoritma perlu selalu dikontekstualisasikan terhadap pipeline representasi teks yang digunakan.

Penelitian lanjutan yang direkomendasikan mencakup penambahan jumlah replikasi (10–20 run) untuk meningkatkan power statistik, ekspansi ke algoritma lain (SVM, XGBoost) dan metode embedding kontekstual (Word2Vec, IndoBERT), serta replikasi lintas aplikasi (Grab, Shopee) untuk menguji generalisasi temuan preprocessing-sensitivity pada domain super-app lainnya.

## Daftar Pustaka

[1] A. K. Nugroho, L. N. Hayati, and S. R. Jabir, "Analisis Perbandingan Metode Naive Bayes dan Random Forest pada Klasifikasi Sentimen Publik terhadap Aplikasi Identitas Kependudukan Digital (IKD)," *Jurnal Algoritma ITG*, vol. 22, no. 2, pp. 619–631, 2025, doi: 10.33364/algoritma/v.22-2.2729.

[2] R. Meinita and I. F. Anshori, "Perbandingan Algoritma Naïve Bayes dan Random Forest untuk Klasifikasi Intent Chatbot Layanan Pelanggan," *Jurnal Algoritme*, vol. 6, no. 1, pp. 186–198, 2025, doi: 10.35957/algoritme.v5i3.12639.

[3] F. F. Wati, Suleman, and A. E. Widodo, "Analisis Sentimen Ulasan Pengguna Aplikasi Deepseek Menggunakan Algoritma Random Forest dan Naive Bayes," *CONTEN: Computer and Network Technology*, vol. 5, no. 1, pp. 8–15, 2025.

[4] A. Pranata, Rudiman, and N. A. Verdikha, "Klasifikasi Teks Quick Count Pemilihan Presiden 2024 pada Twitter Menggunakan Metode TF-IDF dan Naive Bayes," *Jurnal Informatika Terpadu*, vol. 10, no. 2, pp. 93–100, 2024.

[5] F. Baharuddin and A. Tjahyanto, "Peningkatan Performa Klasifikasi Machine Learning Melalui Perbandingan Metode Machine Learning dan Peningkatan Dataset," *Jurnal SISFOKOM (Sistem Informasi dan Komputer)*, vol. 11, no. 1, pp. 25–31, 2022, doi: 10.32736/sisfokom.v11i1.1337.

[6] A. A. Firdaus, A. I. Hadiana, and A. K. Ningsih, "Klasifikasi Sentimen pada Aplikasi Shopee Menggunakan Fitur Bag of Word dan Algoritma Random Forest," *Ranah Research: Journal of Multidisciplinary Research and Development*, vol. 6, no. 5, pp. 1678–1683, 2024, doi: 10.38035/rrj.v6i5.

[7] K. K. M. Nuryasin, T. Taryo, and Sudarno, "Klasifikasi Berita Bahasa Indonesia Dengan Menggunakan Metode K-Nearest Neighbor Dan Naive Bayes," *Jurnal Ilmu Komputer*, vol. 3, no. 1, pp. 60–71, 2025.

[8] M. D. Desriansyah, I. U. Sari, and Zulfahmi, "Analisis Efektivitas Algoritma Machine Learning dalam Deteksi Hoaks: Pada Berita Digital Berbahasa Indonesia," *JISKA: Jurnal Sistem Informasi Dan Informatika*, vol. 3, no. 2, pp. 63–69, 2025.

[9] A. P. Lestari, Maskur, and N. Hayatin, "Klasifikasi Teks Berbasis Ontologi Untuk Dokumen Tugas Akhir Berbahasa Indonesia," *REPOSITOR*, vol. 1, no. 2, pp. 79–86, 2019.