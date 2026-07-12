# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat update dokumen `worksheets/ws-*.md` dan eksekusi skrip). Tanggal mengikuti log riil eksperimen.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-07-11 | Tahap 1 & 2 | Eksplorasi awal dengan notebook (single-run) dan perancangan eksperimen 5-run menggunakan skrip `multi_run_experiment.py` (v1) tanpa preprocessing linguistik. | [worksheets/ws-10-execution-data.md](../../worksheets/ws-10-execution-data.md) |
| 2026-07-11 | Tahap 3 | Eksekusi matrix 5-run awal (v1) untuk Naive Bayes dan Random Forest; anomali gap performa (1,71 poin) terdeteksi. | [worksheets/ws-11-data-validation.md](../../worksheets/ws-11-data-validation.md) |
| 2026-07-12 | Tahap 4 | Validasi data mengonfirmasi adanya under-processing pada v1 (tahap linguistik terlewat). Skrip direvisi menjadi `multi_run_experiment_v2.py` dengan pipeline preprocessing lengkap (case folding, cleansing, stopword NLTK, stemming Sastrawi). | [worksheets/ws-13-preprocessing.md](../../worksheets/ws-13-preprocessing.md) |
| 2026-07-12 (01:32–01:35) | Tahap 3 | Eksekusi ulang matrix penuh 5-run menggunakan skrip v2. Seluruh 10 run selesai tanpa error dengan data tersimpan di log JSON v2. Gap performa menyusut menjadi 0,45 poin. | [worksheets/ws-10-execution-data.md](../../worksheets/ws-10-execution-data.md) |
| 2026-07-12 | Tahap 4 & 5 | Analisis hasil eksperimen v2, uji hipotesis (paired t-test & Wilcoxon karena outlier di RF), dan evaluasi limitasi (n=5). Laporan visualisasi, interpretasi, dan struktur paper ilmiah diperbarui dengan data v2 final. | [worksheets/ws-14-analysis-interpretation.md](../../worksheets/ws-14-analysis-interpretation.md), [worksheets/ws-15-scientific-writing.md](../../worksheets/ws-15-scientific-writing.md), [worksheets/ws-12-result-presentation.md](../../worksheets/ws-12-result-presentation.md) |

## Status Ringkas

- **Tahap 1–4**: Selesai. Data final menggunakan eksekusi v2 (dengan preprocessing) sebanyak 5-run per algoritma (selesai dieksekusi 2026-07-12). Hasil awal (v1) dipertahankan sebagai analisis sensitivitas metodologis.
- **Tahap 5**: Laporan interpretasi (WS-14) dan checklist paper ilmiah (WS-15) selesai (target: SINTA 3+ / Skripsi) dengan narasi yang menyoroti dampak metodologis preprocessing.

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Selesaikan validasi dan perbaikan script otomatisasi menjadi `multi_run_experiment_v2.py`
- [x] Lakukan re-run eksperimen 5 seed untuk v2 dan perbarui dokumen WS-10 hingga WS-14
- [x] Buat outline dan matriks konsistensi di WS-15 (Scientific Writing) berdasarkan hasil v2
- [ ] Pindahkan draf kerangka paper dari worksheet ke dalam template jurnal SINTA 3+ atau format laporan skripsi
- [ ] Finalisasi penyusunan grafik hasil evaluasi ke naskah skripsi
- [ ] (Opsional) Tambahkan replikasi seed (misal n=10 atau n=20) sebagai rekomendasi future work jika diperlukan untuk menutupi limitasi power uji statistik Wilcoxon (karena p-minimum 0,0625 pada n=5)

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
