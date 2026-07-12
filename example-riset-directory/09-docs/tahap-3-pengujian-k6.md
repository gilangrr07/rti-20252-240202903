# Tahap 3 — Eksekusi Multi-Run Eksperimen (v1 & v2)

**Status:** Selesai — matrix v2 (10 run, dengan preprocessing lengkap) sudah dijalankan dan menjadi hasil final; matrix v1 (10 run, tanpa preprocessing) diarsipkan sebagai temuan pembanding/robustness check
**Bergantung pada:** [tahap-2-implementasi-gateway.md](tahap-2-implementasi-gateway.md)
**Lokasi kode:** [../05-kode/](../05-kode/)

---

## Tujuan

Menjalankan eksperimen multi-run untuk membandingkan Naïve Bayes (NB) vs Random Forest (RF) pada kondisi yang benar-benar identik, dengan 5 replikasi (seed berbeda) per algoritma agar kesimpulan tidak bergantung pada satu angka (single run).

## Deliverable

- [x] Script `multi_run_experiment.py` (v1) — 5 seed × 2 algoritma
- [x] Script `multi_run_experiment_v2.py` (v2, revisi) — 5 seed × 2 algoritma, dengan preprocessing lengkap
- [x] Konfigurasi seed pre-determined (`[42, 123, 456, 789, 2024]`) untuk kedua versi
- [x] Output log JSON per run + rekap CSV untuk Tahap 4
- [x] Verifikasi awal (single-run notebook) sebagai kalibrasi pipeline sebelum multi-run
- [x] Matrix penuh v1 (10 run) dan v2 (10 run)

## Desain yang Diimplementasikan

### Struktur kode

```
05-kode/
├── eksplorasi/
│   └── sentimen_gojek.ipynb        # eksplorasi single-run, preprocessing lengkap
├── multi-run/
│   ├── multi_run_experiment.py     # v1 — tanpa preprocessing (superseded)
│   └── multi_run_experiment_v2.py  # v2 — dengan preprocessing (final)
├── Dataset/
│   ├── gojek_labeled.csv
│   └── gojek_labeled_clean.csv     # cache preprocessing, dihasilkan v2
└── results/
    ├── log_NB_run{01-05}.json, log_RF_run{01-05}.json       # v1
    ├── semua_hasil.csv, rekap_statistik.csv                  # v1
    ├── log_NB_run{01-05}_v2.json, log_RF_run{01-05}_v2.json # v2
    └── semua_hasil_v2.csv, rekap_statistik_v2.csv            # v2
```

### Skrip & skenario

| Skrip | Seed | Algoritma | Preprocessing |
|---|---|---|---|
| `multi_run_experiment.py` (v1) | 42, 123, 456, 789, 2024 | NB, RF | Tidak ada — TF-IDF pada teks mentah |
| `multi_run_experiment_v2.py` (v2) | 42, 123, 456, 789, 2024 | NB, RF | Lengkap — case folding, cleansing, stopword removal, stemming Sastrawi |

Matrix eksperimen: **5 seed × 2 algoritma = 10 run**, dijalankan dua kali (v1 dan v2) — total 20 run tercatat.

### Runner

Untuk setiap seed, script menjalankan `run_experiment()`: stratified sampling → train-test split → TF-IDF fit (train saja) → training classifier → prediksi → hitung metrik → validasi range → tulis log JSON. Loop utama mengulang untuk NB lalu RF pada tiap seed, mencetak ringkasan ke terminal (accuracy/precision/recall/F1/waktu latih/anomali) sekaligus menulis file log.

### Output per run

```
results/log_<algoritma>_run<NN>[_v2].json
{
  "run_id", "timestamp", "skenario", "seed",
  "n_sample", "test_size", "tfidf_max_features",
  "preprocessing" (v2 saja), "metric_average" (v2 saja),
  "accuracy", "precision", "recall", "f1_score",
  "waktu_latih_detik", "confusion_matrix", "anomali", "catatan"
}
```

## Hasil Verifikasi Awal (Notebook, Sebelum Multi-Run)

Eksplorasi notebook (`sentimen_gojek.ipynb`, seed=42, 23/06/2026) dijalankan sebagai kalibrasi pipeline sebelum multi-run: NB accuracy=89,53%, precision=93,83%; RF accuracy=89,92%. Preprocessing pada notebook menghasilkan pengurangan data dari 100.000 menjadi 97.223 baris (2.777 ulasan terlalu pendek pasca-stemming dibuang).

## Hasil Matrix v1 (10 run — superseded)

Matrix v1 dijalankan 07/07/2026 20:53–20:57 (~4 menit), seluruhnya `anomali=NONE`. Hasil: NB accuracy mean=88,42% (±0,20), RF accuracy mean=90,13% (±0,19) — **gap 1,71 poin**.

**Anomali ditemukan (lihat WS-11)**: perbandingan seed=42 antara notebook (89,53%) dan v1 run-NB-01 (88,59%) menunjukkan selisih ~1 poin yang tidak semestinya terjadi jika kedua pipeline identik. Investigasi kode mengonfirmasi `multi_run_experiment.py` (v1) tidak menjalankan tahap preprocessing linguistik — fungsi `get_sample()` mengambil teks mentah langsung ke TF-IDF tanpa case folding/cleansing/stopword/stemming.

Dataset v1 ini kemudian **diarsipkan** sebagai temuan pembanding (bukan dihapus), dipakai untuk analisis sensitivitas pada Tahap 4.

## Hasil Matrix v2 (10 run — final)

Untuk memperbaiki anomali di atas, `multi_run_experiment_v2.py` ditulis ulang dengan menambahkan fungsi `preprocess()` yang identik dengan notebook (case folding → cleansing → stopword removal NLTK → stemming Sastrawi), diterapkan sekali ke seluruh korpus sebelum sampling per-seed, dengan hasil di-cache ke `gojek_labeled_clean.csv` agar replikasi berikutnya tidak perlu mengulang stemming.

Matrix v2 dijalankan 12/07/2026 01:32–01:35 (~3 menit), seluruhnya `anomali=NONE`. Hasil: NB accuracy mean=89,14% (±0,19), RF accuracy mean=89,59% (±0,18) — **gap menyusut menjadi 0,45 poin**. Accuracy NB seed=42 (89,20%) kini mendekati notebook referensi (89,53%), mengonfirmasi pipeline v2 sudah konsisten.

Data v2 inilah yang menjadi input Tahap 4 (analisis statistik) sebagai hasil resmi, menggantikan v1 sebagai kesimpulan utama.

## Catatan Lingkungan

- Eksekusi lokal di Windows (VS Code terminal), bukan Google Colab, untuk kedua versi script multi-run — memungkinkan iterasi cepat re-run setelah revisi kode (v1→v2) tanpa perlu upload ulang dataset ke Colab.
- Waktu eksekusi v2 run pertama lebih lama dari v1 karena tahap stemming Sastrawi ke seluruh korpus (~5-15 menit sekali di awal, dimitigasi caching); run-run berikutnya sebanding waktunya dengan v1.
- Tidak ditemukan kendala crash/error pada kedua matrix — seluruh 20 run (v1+v2) selesai dengan status `anomali=NONE` di level validasi range; anomali yang ditemukan bersifat **logic/metodologis** (preprocessing terlewat), bukan error teknis runtime.