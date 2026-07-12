# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Apakah Random Forest menghasilkan performa klasifikasi sentimen yang lebih baik dibandingkan Naïve Bayes menggunakan TF-IDF pada dataset ulasan aplikasi Gojek berbahasa Indonesia?
Metrik Utama      : Accuracy (primer); Precision, Recall, F1-score (pendukung)

Tabel Hasil (mean ± std, N=5 per algoritma):
| Skenario | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Waktu Latih (s) | n |
|----------|--------------|---------------|------------|--------------|-----------------|---|
| Random Forest | 89.59 ± 0.18 | 89.68 ± 0.18 | 89.59 ± 0.18 | 89.58 ± 0.18 | 28.69 ± 0.70 | 5 |
| Naïve Bayes | 89.14 ± 0.18 | 89.52 ± 0.23 | 89.14 ± 0.18 | 89.10 ± 0.19 | 0.37 ± 0.01 | 5 |

*(Data eksperimen v2 — pipeline lengkap: case folding → cleansing → stopword removal → stemming Sastrawi → TF-IDF. 12/07/2026.)*

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar chart + error bar | Perbandingan accuracy rata-rata RF vs NB dengan std sebagai error bar — selisih 0.45 poin nyata walau kecil | Mean accuracy ± std, 2 kategori |
| 2 | Box plot / dot plot | Sebaran accuracy 5 run per algoritma — RF unggul di 4 dari 5 seed; hanya seed 789 di mana NB (89.06%) hampir menyamai RF (89.50%) | Semua 5 nilai accuracy per algoritma |
| 3 | Grouped bar chart (log scale waktu) | Trade-off accuracy vs waktu latih (RF ~77× lebih lambat dari NB setelah preprocessing; gap accuracy hanya 0.45 poin) | Mean accuracy & mean waktu latih |

Bias Check:
  [X] Y-axis mulai dari 0 (atau dengan catatan eksplisit jika di-zoom ke 88–91% untuk kejelasan selisih kecil 0.45 poin)
  [X] Error bar/std ditampilkan pada grafik accuracy
  [X] Semua 10 data run disertakan (tidak cherry-picked; termasuk RF run-05 seed 2024 yang lebih tinggi — outlier IQR)
  [X] Tidak menggunakan efek 3D
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Waktu Latih (s) | n |
|----------|--------------|---------------|------------|--------------|-----------------|---|
| Random Forest | 89.59 ± 0.18 | 89.68 ± 0.18 | 89.59 ± 0.18 | 89.58 ± 0.18 | 28.69 ± 0.70 | 5 |
| Naïve Bayes | 89.14 ± 0.18 | 89.52 ± 0.23 | 89.14 ± 0.18 | 89.10 ± 0.19 | 0.37 ± 0.01 | 5 |

*(Data v2 dengan preprocessing Sastrawi. Mean ± std. N=5 per algoritma. Diurutkan berdasarkan Accuracy.)*

**Detail per-run:**
| Run | Seed | NB Accuracy (%) | RF Accuracy (%) | NB Waktu (s) | RF Waktu (s) |
|-----|------|-----------------|-----------------|--------------|-------------|
| 1 | 42 | 89.20 | 89.49 | 0.37 | 28.10 |
| 2 | 123 | 89.30 | 89.56 | 0.38 | 28.49 |
| 3 | 456 | 88.84 | 89.48 | 0.36 | 29.05 |
| 4 | 789 | 89.06 | 89.50 | 0.37 | 29.36 |
| 5 | 2024 | 89.30 | 89.91* | 0.37 | 28.02 |

*\*Outlier IQR, terdokumentasi di WS-11.*

**Checklist tabel:**
- [X] Self-contained (judul jelas: "Perbandingan RF vs NB, 5 run v2, dataset ulasan Gojek", satuan %, dan detik ada, N=5 tercantum)
- [X] Mean ± std (bukan single number)
- [X] Diurutkan berdasarkan metrik utama (Accuracy, RF di atas karena lebih tinggi)
- [X] Format konsisten di semua baris (2 desimal, satuan sama)

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart + error bar | RF unggul 0.45 poin accuracy dibanding NB — lebih kecil dari versi tanpa preprocessing (+1.71 poin), tapi tetap konsisten | Mean accuracy RF (89.59) vs NB (89.14), error bar = std (0.18) |
| 2 | Dot plot 5 titik per algoritma | RF unggul di 4 dari 5 seed; seed 789 paling ketat (NB 89.06% vs RF 89.50%, selisih hanya 0.44 poin); seed 2024 RF outlier tinggi (89.91%) | 5 nilai accuracy NB: 89.20, 89.30, 88.84, 89.06, 89.30; 5 nilai RF: 89.49, 89.56, 89.48, 89.50, 89.91 |
| 3 | Grouped bar log-scale waktu | RF lebih akurat tapi ~77× lebih lambat (28.69s vs 0.37s) — selisih accuracy 0.45 poin perlu ditimbang terhadap biaya komputasi yang jauh lebih besar | Mean waktu latih RF vs NB, beserta mean accuracy untuk konteks trade-off |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario contoh dari template:**
*(Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.)*

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya, jika Y-axis dipotong terlalu agresif (misal mulai dari 90%) — beda 0.4% dalam skenario contoh bisa terlihat seperti perbedaan besar |
| Apakah error bar ditampilkan? | Perlu — tanpa error bar, pembaca tidak tahu apakah 0.4% itu di dalam rentang variabilitas normal atau bukan |
| Apakah semua kondisi ditampilkan? | Harus — semua run/skenario, tidak hanya yang "menang" |
| Apa solusinya? | Y-axis mulai dari 0 atau beri catatan eksplisit "axis di-zoom untuk kejelasan, lihat teks untuk selisih aktual", serta selalu sertakan error bar |

**Evaluasi grafik Anda sendiri (data RF vs NB riil v2):**
Untuk kasus RF vs NB pada penelitian v2 ini, selisih accuracy (0.45 poin, dari 89.14% ke 89.59%) jauh lebih kecil dibanding v1 (1.71 poin). Ini menimbulkan tantangan visualisasi baru: dengan selisih yang hanya 0.45 poin dan std yang sama (0.18), bar chart dengan Y-axis mulai dari 0 akan membuat perbedaan hampir tidak terlihat secara visual. Solusi yang diterapkan:
- Untuk konteks (overview): Y-axis dari 0, tampilkan error bar
- Untuk detail (close-up): Y-axis di-zoom ke 88–91% dengan catatan eksplisit "axis dimulai dari 88%, bukan 0, untuk kejelasan; nilai absolut pada tabel"
- Dot plot per-run justru lebih informatif dari bar chart untuk kasus selisih kecil: memperlihatkan bahwa RF masih di atas NB di 5/5 seed walau selisihnya kecil

- [~] Bias check: Y-axis zoom mungkin diperlukan untuk grafik ke-2 dan harus diberi label eksplisit agar tidak menyesatkan — ini adalah contoh nyata trade-off antara "kejujuran representasi" vs "kejelasan pesan visual"

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel memberi angka presisi yang dibutuhkan untuk menulis laporan (mean ± std, N) dan untuk memverifikasi tidak ada kesalahan input; grafik dot plot pada Latihan 2 justru yang paling penting untuk kasus v2 ini: berbeda dengan v1 di mana RF selalu di atas NB tanpa overlap sama sekali, pada v2 pola ini masih ada (RF di atas di 5/5 seed) tapi jauh lebih ketat — perbedaan yang hanya terlihat sebagai "sedikit lebih tinggi" di bar chart akan terlihat jauh lebih jelas di dot plot karena setiap pasangan seed bisa dibandingkan langsung.
> Pengalaman merevisi WS-12 setelah re-run v2 juga mengajarkan bahwa grafik yang "terlihat dramatis" (bar chart v1 dengan gap besar) tidak selalu mencerminkan realita yang lebih kaya — gap yang menyusut dari 1.71 ke 0.45 poin setelah preprocessing diperbaiki justru menjadi narasi saintifik yang lebih menarik dan lebih jujur. Memperbarui visualisasi setelah menemukan kesalahan metodologi adalah bagian dari integritas riset, bukan tanda kelemahan.
