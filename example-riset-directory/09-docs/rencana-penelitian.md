# Rencana Penelitian: Perbandingan Naïve Bayes dan Random Forest untuk Analisis Sentimen Ulasan Aplikasi Gojek

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Judul | Perbandingan Algoritma Naïve Bayes dan Random Forest untuk Analisis Sentimen Ulasan Aplikasi Gojek Berbahasa Indonesia Menggunakan TF-IDF |
| Target Publikasi | Jurnal terindeks SINTA 3 atau lebih tinggi, bidang informatika/ilmu komputer Bahasa Indonesia |
| Stack | Python 3.x, scikit-learn, NLTK, PySastrawi, Google Colab / lokal (VS Code) |
| Masalah | Belum ada studi yang membandingkan Naïve Bayes dan Random Forest secara terkontrol khusus pada ulasan aplikasi Gojek berbahasa Indonesia dengan pipeline preprocessing seragam |
| Solusi | Controlled comparison experiment: TF-IDF + pipeline preprocessing seragam (case folding, cleansing, stopword removal, stemming Sastrawi), 5 replikasi (seed berbeda) per algoritma |

## 2. Alur Kerja (Roadmap)

Setiap tahap memiliki file rencana detail tersendiri agar lebih rapi:

- [x] **Tahap 1** — [Perancangan Desain Eksperimen & Arsitektur Pipeline](tahap-1-arsitektur-dan-skema-database.md) — *Selesai* (WS-09)
- [x] **Tahap 2** — [Implementasi Pipeline Eksperimen (Python)](tahap-2-implementasi-gateway.md) — *Selesai* (WS-10)
- [x] **Tahap 3** — [Eksekusi Multi-Run Eksperimen (v1 & v2)](tahap-3-pengujian-k6.md) — *Selesai* (WS-10/WS-11/WS-13)
- [x] **Tahap 4** — [Analisis Statistik & Visualisasi](tahap-4-analisis-data.md) — *Selesai* (WS-12/WS-14)
- [x] **Tahap 5** — [Draf Naskah Jurnal](tahap-5-draf-paper.md) — *Selesai* (WS-15)

---

## 3. Catatan

Dokumen ini adalah indeks utama. Detail teknis, skema, dan keputusan masing-masing tahap dicatat pada file `tahap-N-*.md` terkait dan diperbarui seiring progres pengerjaan. Penamaan file tahap mengikuti konvensi struktur folder riset (`tahap-1-...`, `tahap-2-...`, dst.); nama file **tidak diubah** dari konvensi awal meski substansi kontennya adalah pipeline machine learning, bukan sistem gateway/keamanan.