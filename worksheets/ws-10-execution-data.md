# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu Mulai | Output File |
|-------|----------|------|-----------|--------|-------------|-------------|
| 1     | NB (Kondisi A) | 42   | alpha=1.0, max_features=5000, +preprocessing | Selesai | 01:32:04 | log_NB_run01_v2.json |
| 2     | RF (Kondisi B) | 42   | n_estimators=100, +preprocessing             | Selesai | 01:32:37 | log_RF_run01_v2.json |
| 3     | NB (Kondisi A) | 123  | alpha=1.0, max_features=5000, +preprocessing | Selesai | 01:32:41 | log_NB_run02_v2.json |
| 4     | RF (Kondisi B) | 123  | n_estimators=100, +preprocessing             | Selesai | 01:33:14 | log_RF_run02_v2.json |
| 5     | NB (Kondisi A) | 456  | alpha=1.0, max_features=5000, +preprocessing | Selesai | 01:33:18 | log_NB_run03_v2.json |
| 6     | RF (Kondisi B) | 456  | n_estimators=100, +preprocessing             | Selesai | 01:33:50 | log_RF_run03_v2.json |
| 7     | NB (Kondisi A) | 789  | alpha=1.0, max_features=5000, +preprocessing | Selesai | 01:33:54 | log_NB_run04_v2.json |
| 8     | RF (Kondisi B) | 789  | n_estimators=100, +preprocessing             | Selesai | 01:34:26 | log_RF_run04_v2.json |
| 9     | NB (Kondisi A) | 2024 | alpha=1.0, max_features=5000, +preprocessing | Selesai | 01:34:30 | log_NB_run05_v2.json |
| 10    | RF (Kondisi B) | 2024 | n_estimators=100, +preprocessing             | Selesai | 01:35:03 | log_RF_run05_v2.json |

Jumlah runs per skenario : 5
Total runs               : 10 (5 seed × 2 algoritma)
Catatan                  : Semua run selesai 12/07/2026 pukul 01:32–01:35 tanpa crash/error (anomali = NONE di seluruh 10 log v2).

DATA LOG :
  Run ID    : run-NB-01-v2
  Timestamp : 2026-07-12T01:32:04.558394
  Skenario  : NB (seed=42)
  Input     : n_sample=100.000, test_size=0.2, tfidf_max_features=5000, alpha=1.0, preprocessing=case_folding+cleansing+stopword_removal+sastrawi_stemming
  Output    : accuracy=89.20%, precision=89.61%, recall=89.20%, f1=89.18%, waktu_latih=0.3694s, confusion_matrix={TN:9423, FP:577, FN:1582, TP:8418}
  Anomali   : NONE
  Catatan   : —

```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | NB, Gojek review (preprocessed) | 42 | alpha=1.0, max_features=5000 | Selesai |
| 2 | RF, Gojek review (preprocessed) | 42 | n_estimators=100, max_depth=None | Selesai |
| 3 | NB, Gojek review (preprocessed) | 123 | alpha=1.0, max_features=5000 | Selesai |
| 4 | RF, Gojek review (preprocessed) | 123 | n_estimators=100, max_depth=None | Selesai |
| 5 | NB, Gojek review (preprocessed) | 456 | alpha=1.0, max_features=5000 | Selesai |
| 6 | RF, Gojek review (preprocessed) | 456 | n_estimators=100, max_depth=None | Selesai |
| 7 | NB, Gojek review (preprocessed) | 789 | alpha=1.0, max_features=5000 | Selesai |
| 8 | RF, Gojek review (preprocessed) | 789 | n_estimators=100, max_depth=None | Selesai |
| 9 | NB, Gojek review (preprocessed) | 2024 | alpha=1.0, max_features=5000 | Selesai |
| 10 | RF, Gojek review (preprocessed) | 2024 | n_estimators=100, max_depth=None | Selesai |

**Total skenario:** 2 (Naïve Bayes, Random Forest)
**Run per skenario:** 5
**Total run keseluruhan:** 10

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh (run-NB-01) |
|-------|--------|
| Run ID | run-NB-01 |
| Timestamp | 2026-07-07T20:54:28.567715 (ISO 8601, dicatat otomatis oleh datetime.now()) |
| Skenario | NB (Kondisi A) |

**Konfigurasi:**
| Field | Contoh (run-NB-01) |
|-------|--------|
| Seed | 42 |
| Code version | multi_run_experiment.py (versi terakhir dimodifikasi 07/07/2026) |
| n_sample | 100.000 (50.000 positif + 50.000 negatif) |
| test_size | 0.2 (80:20 split) |
| tfidf_max_features | 5.000 |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Accuracy | float | 0.0 – 100.0 (%) |
| Precision | float | 0.0 – 100.0 (%), average='weighted' |
| Recall | float | 0.0 – 100.0 (%), average='weighted' |
| F1-score | float | 0.0 – 100.0 (%), average='weighted' |
| waktu_latih_detik | float | > 0 detik |
| confusion_matrix | dict (TN,FP,FN,TP) | jumlah = ukuran data uji (19.445–20.000-an, tergantung sampling) |

**Format output:** [X] CSV / [X] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh dari Data Riil | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Tidak terjadi — seluruh 10 run v2 bertanda anomali "NONE" | Tidak perlu tindakan; checklist crash tetap disiapkan untuk run mendatang |
| Hasil ekstrem | RF run-05 (seed 2024): accuracy 89.91% — di luar batas IQR atas kelompok RF (89.385–89.665), sedikit lebih tinggi dari 4 run RF lain yang sangat rapat (89.48–89.56) | Diinvestigasi (WS-11/WS-14): tidak ada indikasi bug; ini melanggar asumsi normalitas Shapiro-Wilk untuk grup RF (p=0,0069) — memengaruhi pemilihan uji statistik di WS-14 |
| Waktu eksekusi anomali | Waktu latih RF v2 lebih stabil (27.8–29.4s, ±5%) dibanding versi awal tanpa preprocessing (21.9–28.1s, ±28%) — preprocessing menghasilkan vocabulary lebih ringkas sehingga variasi run-to-run mengecil | Tidak ada tindakan; dicatat sebagai perbaikan konsistensi setelah preprocessing ditambahkan |
| Inkonsistensi dengan run lain | RESOLVED: setelah preprocessing ditambahkan di v2, gap accuracy RF-NB mengecil dari 1.71 poin (v1, tanpa preprocessing) menjadi 0.45 poin (v2, dengan preprocessing) — mengonfirmasi dugaan WS-11 bahwa versi v1 melewatkan tahap preprocessing | Versi v2 dipakai sebagai hasil final; versi v1 didokumentasikan sebagai temuan robustness check tambahan (WS-14) |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya. Notebook eksplorasi awal (sentimen_gojek.ipynb) hanya menjalankan satu run per algoritma dengan seed=42, dan menyimpulkan H₀ dipertahankan karena selisih accuracy hanya +0.38% (di bawah ambang 5% yang ditetapkan di proposal). Kesimpulan itu murni bertumpu pada satu angka per algoritma.

**Yang berubah setelah multiple run (dan setelah preprocessing diperbaiki):**
> Setelah menjalankan 5 run per algoritma dengan seed berbeda DAN preprocessing lengkap (v2), selisih rata-rata accuracy RF vs NB adalah +0.45 poin (RF mean 89.59% ± 0.18, NB mean 89.14% ± 0.19). Ini jauh lebih kecil dibanding versi awal tanpa preprocessing (+1.71 poin) — menunjukkan bahwa preprocessing bahasa Indonesia (stemming, stopword removal) membantu KEDUA algoritma, tapi membantu Naïve Bayes relatif lebih banyak, sehingga gap keunggulan RF menyempit. Proses ini mengajarkan dua pelajaran sekaligus: (1) satu run saja bisa menyesatkan (seperti sudah dibahas), dan (2) bahkan setelah 5 run, kalau ada bug/kelalaian implementasi (di sini: preprocessing terlewat), angka yang "terlihat robust karena konsisten di 5 seed" tetap bisa salah — robust terhadap variasi seed tidak sama dengan benar secara metodologis.
