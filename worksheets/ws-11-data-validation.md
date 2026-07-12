# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [X] Semua skenario tercakup (NB, RF)
  [X] Jumlah run sesuai rencana (5 per skenario, total 10)
  [X] Tidak ada file output hilang (10 file JSON + semua_hasil.csv + rekap_statistik.csv lengkap)
  Missing: 0 dari 10 data points

Format Consistency:
  [X] Semua file format sama (JSON per run, CSV rekap)
  [X] Header/field konsisten (run_id, timestamp, skenario, seed, ... di semua 10 file)
  [X] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [X] Nilai dalam range masuk akal (88–91%, tidak ada di luar [0,100])
  [X] Tidak ada waktu negatif (0.165s–28.05s, semua positif)
  [~] Metrik 0–100%, tidak di luar range — TAPI ditemukan inkonsistensi metode perhitungan precision (lihat di bawah)
  Anomali ditemukan: (1) NB run-04 seed 789 = outlier ringan pada accuracy; (2) precision pada notebook tunggal (93.83%) tidak konsisten dengan classification_report-nya sendiri (weighted avg 90%) maupun dengan run multi-run seed 42 yang sama (89.23%).

Cross-Validation:
  [X] Run identik (seed sama antar-algoritma) → hasil mendekati pola yang sama antar seed (accuracy NB & RF konsisten naik-turun bersamaan mengikuti "kesulitan" sampel per seed)
  [X] Trend konsisten dengan ekspektasi teori (RF > NB di SEMUA 5 seed, sejalan dengan literatur WS-03)

Keputusan:
  [X] Data 10-run siap analisis statistik (WS-14)
  [~] Perlu cleaning/klarifikasi: definisi metrik precision perlu diseragamkan sebelum dilaporkan di skripsi
  [ ] Perlu re-run
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| NB (Kondisi A) | 5 | 5 | 0 | — |
| RF (Kondisi B) | 5 | 5 | 0 | — |

**Total expected:** 10 | **Total actual:** 10 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data missing — seluruh 10 run selesai tanpa crash (anomali = "NONE" di semua log). Tidak diperlukan re-run untuk kelengkapan.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Bagian A — Anomali yang SUDAH DIKONFIRMASI dan DISELESAIKAN: preprocessing terlewat**

| Sumber | Seed | Accuracy NB | Precision NB | Preprocessing? |
|--------|------|-------------|--------------|----------------|
| Notebook sentimen_gojek.ipynb (single run) | 42 | 89.53% | 93.83%* | Ya (lengkap) |
| multi_run_experiment.py v1, log_NB_run01 | 42 | 88.59% | 89.23% | Tidak |
| multi_run_experiment_v2.py, log_NB_run01_v2 | 42 | 89.20% | 89.61% | Ya (lengkap) |

*\*Precision notebook (93.83%) dihitung dengan average='binary', pos_label='positif' — beda definisi dari v1/v2 yang pakai average='weighted'; bukan dibandingkan apple-to-apple, dicatat sebagai catatan metodologi terpisah.*

Setelah script diperbaiki (v2) dengan menambahkan case folding → cleansing → stopword removal → stemming Sastrawi (identik dengan notebook) sebelum sampling & split, accuracy NB run seed=42 naik dari 88.59% → 89.20%, mendekati notebook (89.53%; sisa selisih kecil wajar karena notebook memakai seluruh dataset yang sudah diproses sekali secara global, sedangkan v2 melakukan sampling stratified per-seed sebelum split).

Dampak pada kesimpulan penelitian: 
Gap accuracy RF-NB mengecil dari 1.71 poin (v1, tanpa preprocessing) menjadi 0.45 poin (v2, dengan preprocessing) — perbedaan yang cukup besar untuk memengaruhi kekuatan klaim di skripsi. Versi v2 dipakai sebagai hasil final (lihat WS-14); v1 didokumentasikan sebagai temuan tambahan/robustness check.

**Bagian B — Anomali baru yang muncul pada data v2 (final): outlier pada grup RF**

| Run | Seed | NB Accuracy (%) | RF Accuracy (%) |
|-----|------|-----------------|-----------------|
| 1 | 42 | 89.20 | 89.49 |
| 2 | 123 | 89.30 | 89.56 |
| 3 | 456 | 88.84 | 89.48 |
| 4 | 789 | 89.06 | 89.50 |
| 5 | 2024 | 89.30 | 89.91 |

**IQR check — RF accuracy:**
- Q1 = 89.490 | Q3 = 89.560 | IQR = 0.070
- Batas atas (Q3 + 1.5×IQR) = 89.665
- Outlier terdeteksi: RF Run 5 (seed 2024, accuracy 89.91%) — di atas batas atas 89.665

**IQR check — NB accuracy:**
- Q1 = 89.060 | Q3 = 89.300 | IQR = 0.240 → batas [88.700, 89.660] → tidak ada outlier pada NB

**Investigasi outlier RF run-05:**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| RF Run 5 (seed 2024) | 89.91% | Bukan bug — confusion matrix menunjukkan FN 1.188 (terendah di antara 5 run RF), menandakan subset sampling seed 2024 kebetulan lebih mudah dipisahkan oleh RF dibanding 4 seed lain, bukan kesalahan eksekusi | Bukan bug (anomali=NONE di log, tidak ada error format). Tetap disertakan dalam mean±std sebagai variabilitas alami; TAPI dicatat karena memengaruhi hasil uji normalitas Shapiro-Wilk (WS-14) |

**Catatan penting untuk WS-14:**
Outlier RF run-05 menyebabkan grup RF (n=5) GAGAL uji normalitas Shapiro-Wilk (W=0.686, p=0.0069 < 0.05), berbeda dari grup NB yang tetap normal (p=0.286). Ini berarti paired t-test (yang mengasumsikan normalitas) perlu dipertimbangkan ulang — uji non-parametrik (Wilcoxon signed-rank) menjadi alternatif yang lebih tepat secara statistik meski powernya terbatas pada n=5. Kedua hasil dilaporkan di WS-14 untuk transparansi.

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

1. Completeness: 100% data terkumpul (10/10 run v2)
2. Format: [X] Konsisten (semua JSON v2 + CSV memiliki skema sama, termasuk field preprocessing & metric_average yang eksplisit)
3. Range check (anomali): RF run-05 (seed 2024, acc 89.91%) — outlier ringan by IQR pada grup RF, terdokumentasi, tidak dihapus, tapi memengaruhi hasil uji normalitas (dibawa ke WS-14)
4. Logic check: [X] Sudah sesuai — preprocessing (case folding, cleansing, stopword removal, stemming Sastrawi) kini identik dengan yang dijanjikan proposal E.2 dan dijalankan di notebook. Anomali v1 (preprocessing terlewat) sudah RESOLVED melalui re-run v2.

**Kesimpulan:** 
[X] Data 10-run v2 siap dipakai sebagai hasil final untuk analisis statistik (WS-14). Versi v1 (tanpa preprocessing, gap 1.71 poin) tetap disimpan dan dilaporkan sebagai temuan tambahan/robustness check di Discussion, bukan dibuang, karena tetap informatif untuk menunjukkan sensitivitas hasil terhadap keputusan preprocessing.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Kesepuluh log JSON v1 "benar" dalam artian tidak ada crash, tidak ada nilai di luar range, dan format konsisten — logger tidak berbohong soal apa yang terjadi. Tapi itu belum berarti data v1 "bisa dipercaya" untuk menjawab RQ skripsi: proses validasi logic-check pada Latihan 2 mengungkap bahwa script otomatis (multi_run_experiment.py v1) diam-diam menjalankan pipeline yang berbeda dari yang didesain di proposal. 
> Setelah diperbaiki dan di-re-run (v2), dugaan itu terkonfirmasi: gap RF-NB yang tadinya terlihat besar dan sangat signifikan (1.71 poin, d=5.78) menyusut jadi jauh lebih kecil (0.45 poin) begitu preprocessing yang benar dijalankan. Ini bukti nyata bahwa "logging otomatis ≠ data benar" — 10 run yang tampak rapi dan konsisten (semua anomali=NONE) tetap bisa membawa kesimpulan yang keliru kalau logic/desain eksperimennya sendiri menyimpang dari yang dimaksud, dan hanya validasi formal (cross-check logika, bukan sekadar cek angka) yang bisa menangkapnya.
