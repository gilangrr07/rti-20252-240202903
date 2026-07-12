# Tahap 4 — Analisis Statistik & Visualisasi

**Status:** Selesai — analisis dijalankan atas data final v2 (10 run, dengan preprocessing), dengan perbandingan terhadap data v1 sebagai analisis sensitivitas
**Bergantung pada:** [tahap-3-pengujian-k6.md](tahap-3-pengujian-k6.md)
**Lokasi kode/hasil:** [../06-output/](../06-output/)

---

## Tujuan

Mengolah data mentah hasil eksekusi multi-run (`results/semua_hasil_v2.csv`, log JSON per run) menjadi statistik deskriptif, uji hipotesis yang sesuai dengan karakteristik data, dan visualisasi untuk penulisan naskah (Tahap 5).

## Deliverable

- [x] Statistik deskriptif (mean/std/median/min/max) per algoritma untuk accuracy, precision, recall, F1-score, waktu latih
- [x] Uji normalitas (Shapiro-Wilk) per grup sebelum memilih uji hipotesis
- [x] Uji hipotesis ganda: paired t-test (asumsi normal) dan Wilcoxon signed-rank test (non-parametrik), dilaporkan keduanya karena satu grup melanggar normalitas
- [x] Deteksi outlier (IQR) pada distribusi accuracy tiap grup
- [x] Perhitungan gap performa v1 (tanpa preprocessing) vs v2 (dengan preprocessing) sebagai analisis sensitivitas
- [x] Rencana visualisasi (bar chart error bar, dot plot sebaran run, scatter waktu latih) dengan bias check

## Desain yang Diimplementasikan

### Alur analisis

| Langkah | Fungsi | Output |
|---|---|---|
| Load data | Baca `semua_hasil_v2.csv` / `rekap_statistik_v2.csv` | DataFrame per algoritma |
| Statistik deskriptif | Hitung mean, std, median, min, max per metrik | Tabel 1 (lihat Hasil) |
| Uji normalitas | Shapiro-Wilk per grup (NB, RF) pada accuracy | W-statistic, p-value |
| Uji hipotesis | Paired t-test (`scipy.stats.ttest_rel`) dan Wilcoxon (`scipy.stats.wilcoxon`) pada pasangan seed yang sama | t/W, p-value, Cohen's d, CI 95% |
| Deteksi outlier | IQR (Q1-1.5×IQR, Q3+1.5×IQR) pada accuracy tiap grup | Daftar outlier + investigasi |
| Analisis sensitivitas | Bandingkan gap accuracy RF-NB pada data v1 vs v2 | Tabel 2 (lihat Hasil) |

### Definisi Uji Hipotesis

```
Paired t-test:  t = mean(diff) / (std(diff) / sqrt(n))   -- asumsi diff berdistribusi normal
Wilcoxon:       uji rank non-parametrik untuk data berpasangan -- tidak mengasumsikan normalitas
```

Uji dipilih berdasarkan hasil Shapiro-Wilk: jika kedua grup normal, paired t-test dipakai sebagai rujukan utama; jika salah satu grup tidak normal (seperti pada data ini), kedua uji dilaporkan secara transparan.

## Hasil

### Statistik Deskriptif (data v2, final)

| Skenario | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Waktu Latih (s) |
|---|---|---|---|---|---|
| Random Forest | 89,59 ± 0,18 | 89,64 ± 0,18 | 89,59 ± 0,18 | 89,58 ± 0,18 | 28,52 ± 0,60 |
| Naïve Bayes | 89,14 ± 0,19 | 89,54 ± 0,16 | 89,14 ± 0,19 | 89,11 ± 0,20 | 0,32 ± 0,03 |

### Uji Normalitas & Hipotesis

| Uji | Statistik | p-value | Kesimpulan |
|---|---|---|---|
| Shapiro-Wilk (NB accuracy) | W=0,875 | 0,286 | Normal |
| Shapiro-Wilk (RF accuracy) | W=0,686 | 0,0069 | **Tidak normal** (outlier seed 2024) |
| Paired t-test (accuracy) | t(4)=5,70 | 0,0047 | Signifikan, d=2,55 |
| Wilcoxon signed-rank (accuracy) | W=0,0 | 0,0625 | Marginal, tidak signifikan pada α=0,05 |

Random Forest **tidak menambah kompleksitas tanpa manfaat** — unggul konsisten di seluruh 5 pasangan seed — namun signifikansi statistiknya bergantung pada uji yang dipilih karena distribusinya tidak normal (satu outlier pada seed 2024, accuracy 89,91% dibanding 4 run lain yang sangat rapat 89,48–89,56%).

### Analisis Sensitivitas: Gap v1 vs v2

| Versi | Preprocessing | Accuracy RF | Accuracy NB | Gap | Signifikansi |
|---|---|---|---|---|---|
| v1 | Tidak ada | 90,13% | 88,42% | **1,71 poin** | p=0,0002 (t-test) |
| v2 | Lengkap | 89,59% | 89,14% | **0,45 poin** | p=0,0047 (t-test) / p=0,0625 (Wilcoxon) |

Preprocessing linguistik **menaikkan accuracy NB** (88,42%→89,14%) sementara **RF sedikit menurun** (90,13%→89,59%), sehingga gap menyempit signifikan (~74% penyusutan). Ini adalah temuan penting untuk narasi Tahap 5: kesimpulan komparasi algoritma sensitif terhadap keputusan preprocessing, sehingga tidak bisa digeneralisasi sebagai "RF selalu unggul X poin" tanpa menyebut pipeline yang dipakai.

### Rencana Visualisasi

| # | Jenis Grafik | Pesan |
|---|---|---|
| 1 | Bar chart + error bar | Perbandingan mean accuracy RF vs NB (v2, final) |
| 2 | Dot plot 5 titik per algoritma | Tidak ada overlap sebaran accuracy meski gap sempit |
| 3 | Scatter/bar skala log | Trade-off accuracy vs waktu latih (RF ~89× lebih lambat) |
| 4 | Bar chart perbandingan | Gap accuracy v1 vs v2 — ilustrasi sensitivitas preprocessing |

## Catatan untuk Tahap 5

- Trade-off signifikansi statistik (t-test vs Wilcoxon) di atas adalah temuan penting: kedua uji harus dilaporkan bersamaan di naskah, bukan memilih salah satu yang "menguntungkan" kesimpulan (prinsip anti p-hacking).
- Gap v1 vs v2 (1,71→0,45 poin) adalah kontribusi tambahan penelitian ini, relevan untuk bagian "Diskusi"/"Analisis Sensitivitas" pada naskah jurnal.
- Seluruh angka di atas adalah mean dari 5 replikasi; deteksi outlier IQR dan investigasi konfusi matrix mendukung keputusan untuk tetap menyertakan run seed=2024 (RF) sebagai variabilitas alami, bukan dihapus sebagai error.