# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | RF - Accuracy (%) | 89,588 | 0,183 | 89,500 | 89,480 | 89,910 | 5 |
   | NB - Accuracy (%) | 89,140 | 0,194 | 89,200 | 88,840 | 89,300 | 5 |
   | RF - F1-Score (%) | 89,584 | 0,180 | 89,490 | 89,480 | 89,900 | 5 |
   | NB - F1-Score (%) | 89,112 | 0,195 | 89,180 | 88,810 | 89,270 | 5 |
   | RF - Waktu Latih (s)| 28,518 | 0,597 | 28,517 | 27,804 | 29,403 | 5 |
   | NB - Waktu Latih (s)| 0,322 | 0,028 | 0,311 | 0,299 | 0,369 | 5 |

2. Uji Hipotesis:
   (a) Paired t-test (asumsi normalitas dilanggar untuk grup RF, dilaporkan untuk perbandingan):
   Accuracy: t(4) = 5,70, p = 0,00468, Cohen's d (paired) = 2,55, selisih mean (RF-NB) = 0,448 poin, 95% CI = [0,230 ; 0,666]
   F1-Score: t(4) = 6,00, p = 0,00388, Cohen's d = 2,68
   Waktu latih: t(4) = 106,71, p < 0,00001 - RF signifikan lebih lambat (28,52s vs 0,32s, ~89x lipat)
   (b) Wilcoxon signed-rank test (non-parametrik, tepat untuk grup RF yang non-normal):
   Accuracy: W = 0,0, p = 0,0625
   Catatan: p = 0,0625 adalah p-value minimum yang bisa dicapai Wilcoxon pada n=5 (keterbatasan resolusi uji non-parametrik pada sampel sangat kecil) - hasil ini secara teknis tidak signifikan pada alpha=0,05, meski sangat dekat ke ambang, dan searah dengan hasil t-test (RF > NB di semua 5 pasangan).

3. Keputusan:
   [X] Berdasarkan paired t-test: H0 ditolak -> H1 diterima (p=0,0047 < 0,05)
   [~] Berdasarkan Wilcoxon (uji yang lebih tepat karena RF non-normal): H0 TIDAK ditolak pada alpha=0,05 (p=0,0625), meski RF unggul di SEMUA 5 pasangan seed tanpa kecuali
   Kesimpulan gabungan yang jujur: RF secara konsisten mengungguli NB di seluruh 5 seed (bukan kebetulan satu run), dan efeknya besar secara relatif terhadap variabilitasnya sendiri. Namun signifikansi statistik bergantung pada uji yang dipilih - paired t-test mengatakan signifikan, sedangkan Wilcoxon (lebih sesuai karena RF non-normal) berada tepat di ambang batas tanpa mencapai signifikansi konvensional karena keterbatasan resolusi pada n=5. Rekomendasi: laporkan kedua uji di skripsi secara transparan, dan sebutkan keterbatasan power statistik pada n=5 sebagai limitation (lihat bagian 5).

4. Interpretasi:
   Hubungan ke RQ       : RQ menanyakan apakah RF > NB. Arah efek konsisten mendukung RF di semua metrik dan semua seed, tapi kekuatan bukti statistik lebih moderat dari yang terlihat pada uji parametrik saja
   Practical significance: Selisih 0,45 poin jauh di bawah ambang "bermakna praktis >=5%" di proposal (E.5) - dari sudut pandang praktis, keunggulan RF pada domain ulasan Gojek tergolong kecil, meski konsisten
   Perbandingan literatur: Gap 0,45% berada di ujung paling bawah rentang literatur (1-24 poin, WS-03) - lebih kecil dari studi manapun yang direview di proposal. Ini kemungkinan karena preprocessing yang matang (stemming, stopword removal) membantu Naive Bayes secara proporsional lebih besar dibanding Random Forest, mengurangi kesenjangan performa yang biasa dilaporkan pada representasi teks yang lebih kasar

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Statistical limitation | n=5 sangat kecil untuk uji apapun; Wilcoxon pada n=5 punya batas resolusi p-minimum=0,0625, tidak bisa mencapai signifikansi konvensional walau pola sempurna (RF>NB di semua pasangan) | Ketidakpastian apakah hasil "marginal non-signifikan" ini benar-benar H0 atau sekadar keterbatasan power | Nyatakan eksplisit sebagai limitasi; sarankan replikasi dengan lebih banyak seed (mis. 10-20) sebagai future work |
   | Distributional/normality | Grup RF melanggar asumsi normalitas (Shapiro-Wilk p=0,0069) karena satu outlier (seed 2024) | Paired t-test yang dilaporkan sebagai pendukung mungkin sedikit overstate signifikansi | Laporkan kedua uji (t-test & Wilcoxon) secara transparan, seperti dilakukan di sini |
   | External validity | Dataset hanya ulasan Gojek - tidak digeneralisasi ke aplikasi lain | Kesimpulan gap kecil RF-NB terbatas pada domain ulasan Gojek Bahasa Indonesia dengan preprocessing spesifik ini | Nyatakan eksplisit sebagai batasan; sarankan replikasi ke Grab/Shopee (future work di proposal D.4) |
   | Construct validity - sensitivitas preprocessing | Gap RF-NB berubah drastis (1,71 -> 0,45 poin) hanya karena penambahan preprocessing linguistik - menunjukkan kesimpulan sangat sensitif terhadap pilihan pipeline | Klaim keunggulan RF perlu selalu disertai konteks pipeline yang dipakai, tidak bisa digeneralisasi sebagai "RF selalu unggul X poin" | Laporkan kedua versi (v1 & v2) di Discussion sebagai bukti sensitivitas metodologis |

6. Failure Analysis (Kondisi Wilcoxon p=0,0625 & Perbandingan v1 vs v2):
   Penyebab potensial  : Wilcoxon pada n=5 punya batas resolusi p-minimum=0,0625, sehingga tidak bisa mencapai p<0,05 meski pola RF > NB sempurna di 5 seed. Ini masalah power uji non-parametrik pada sampel super kecil.
   Boundary condition   : Preprocessing yang matang (v2) menyamakan performa NB & RF (gap 0,45 poin), sementara representasi kasar (v1) memberi gap lebih besar untuk RF (1,71 poin).
   Insight              : Preprocessing linguistik menaikkan accuracy NB (88,42% -> 89,14%) sementara RF justru sedikit turun (90,13% -> 89,59%), menyempitkan gap secara signifikan. Preprocessing bukan sekadar "pembersih", tapi bisa mengubah konklusi perbandingan model.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 (Naive Bayes, Random Forest) |
| Apakah data berpasangan (paired)? | Ya - setiap pasangan NB/RF dijalankan pada seed identik (42, 123, 456, 789, 2024) |
| Apakah distribusi normal? (uji normalitas) | Campuran: NB normal (Shapiro-Wilk p=0,286), RF TIDAK normal (p=0,0069, karena outlier seed 2024) |
| **Uji yang dipilih:** | Dilaporkan keduanya: Paired t-test (untuk perbandingan dengan asumsi standar) DAN Wilcoxon signed-rank (uji yang secara ketat lebih tepat karena salah satu grup non-normal) |
| **Justifikasi:** | Ketika satu dari dua grup berpasangan melanggar normalitas, praktik yang jujur adalah melaporkan uji non-parametrik sebagai rujukan utama, sambil tetap menampilkan t-test sebagai pembanding |

**Effect size yang dilaporkan:** [X] Cohen's d (paired, untuk t-test) [ ] Eta-squared [X] Arah & konsistensi tanda (untuk Wilcoxon, n=5 terlalu kecil untuk effect size non-parametrik yang stabil)

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data riil final (v2, dengan preprocessing):**
| Model | Accuracy (mean +/- std) | n |
|-------|----------------------|---|
| Random Forest | 89,59 +/- 0,18 | 5 |
| Naive Bayes | 89,14 +/- 0,19 | 5 |

Paired t-test: p=0,0047, d=2,55, CI 95% selisih=[0,23 ; 0,67] | Wilcoxon: p=0,0625

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | Bergantung uji: t-test p<0,01 (signifikan), Wilcoxon p=0,0625 (marginal, tidak signifikan pada alpha=0,05 konvensional) |
| Effect size | d=2,55 -> "large" menurut ambang Cohen's, tapi effect size besar ini banyak didorong oleh std yang sangat kecil (+/-0,18-0,19), bukan selisih mean yang besar |
| Practical significance | Selisih 0,45 poin jauh di bawah ambang bermakna praktis 5% di proposal - dari sisi keputusan praktis, gap ini kecil |
| Hubungan ke RQ | RQ terjawab dengan nuansa: RF unggul konsisten arahnya, tapi besaran keunggulannya kecil dan signifikansi statistiknya bergantung pada uji yang dipakai |
| Perbandingan literatur | Gap 0,45% jauh di bawah semua studi pembanding di WS-03 (gap 1-24 poin) - memunculkan pertanyaan menarik untuk Discussion: apakah preprocessing yang matang justru menyamakan performa NB dan RF pada domain ini? |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

(Skenario template asli menggunakan data hipotetis F1 83,2% vs 84,7%, p=0,12 - dikerjakan sesuai template sebagai latihan konseptual. Kolom kanan menambahkan catatan paralel ke kondisi riil Wilcoxon p=0,0625 di atas.)

| Pertanyaan | Jawaban (skenario template) | Paralel dengan temuan riil (Wilcoxon p=0,0625) |
|-----------|-----------------------------|-----------------------------------------------|
| Apakah ini "gagal"? | Bukan gagal total - hipotesis tidak terdukung adalah temuan valid | Sama - arah efek tetap konsisten (RF>NB di semua seed), "marginal" bukan "tidak ada efek sama sekali" |
| Kemungkinan penyebab? | Metode baru menambah kompleksitas tanpa cukup peningkatan F1 | Di kasus riil: n=5 terlalu kecil untuk power Wilcoxon mencapai p<0,05 meski pola sempurna |
| Boundary condition? | Metode efektif hanya di data besar | Di kasus riil: preprocessing yang matang tampaknya menyamakan performa NB & RF pada domain Gojek - RF unggul lebih besar pada representasi kasar (v1) daripada representasi bersih (v2) |
| Insight yang bisa diambil? | Ada trade-off yang perlu hybrid approach | Kesimpulan "RF lebih baik" perlu selalu disertai kondisi: seberapa matang preprocessing yang dipakai |
| Apakah layak dilaporkan? Mengapa? | Ya - negative result + boundary condition adalah kontribusi | Ya - melaporkan hasil marginal dengan jujur (bukan memilih uji yang menguntungkan) adalah praktik ilmiah yang baik |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Penelitian ini melewati tiga babak kesimpulan yang berbeda: (1) notebook single-run awal mengarah ke H0 dipertahankan karena hanya 1 angka; (2) 5-run tanpa preprocessing (v1) menunjukkan H1 diterima sangat kuat (p=0,0002, d=5,78); (3) 5-run dengan preprocessing yang benar (v2, final) menunjukkan hasil yang lebih bernuansa - signifikan menurut t-test tapi marginal menurut Wilcoxon yang lebih tepat untuk data non-normal. 
> Bukan salah satu dari ketiganya yang benar secara mutlak dan yang lain gagal - masing-masing mengajarkan sesuatu: single-run mengajarkan bahaya kesimpulan tergesa-gesa; v1 mengajarkan bahaya melewatkan langkah metodologis; v2 mengajarkan bahwa bahkan hasil final yang tampak rapi tetap perlu diuji asumsi statistiknya (normalitas) sebelum diklaim signifikan secara membabi-buta. Kejujuran melaporkan p=0,0625 sebagai marginal, bukan signifikan - alih-alih diam-diam hanya melaporkan t-test yang p=0,0047 - adalah bentuk konkret dari sikap ilmiah yang baik: tidak p-hacking dengan memilih uji yang memberi hasil paling menguntungkan.
