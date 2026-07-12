# Tahap 2 — Implementasi Pipeline Eksperimen (Python)

**Status:** Selesai
**Acuan arsitektur:** [tahap-1-arsitektur-dan-skema-database.md](tahap-1-arsitektur-dan-skema-database.md)
**Lokasi kode:** [../05-kode/](../05-kode/)

---

## Tujuan

Mengimplementasikan pipeline klasifikasi sentimen (Python + scikit-learn) yang mendukung dua mode operasi:

- **Eksplorasi (notebook)** — single-run per algoritma (seed=42), pipeline preprocessing lengkap, dipakai sebagai referensi metode.
- **Multi-run (script)** — 5 replikasi (seed berbeda) per algoritma, otomatis via `multi_run_experiment.py` / `multi_run_experiment_v2.py`, menghasilkan log JSON terstruktur per run.

## Deliverable

- [x] Notebook eksplorasi (`sentimen_gojek.ipynb`) — preprocessing lengkap, evaluasi single-run, confusion matrix
- [x] Script multi-run versi awal (`multi_run_experiment.py`) — 5 seed × 2 algoritma, execution plan pre-determined
- [x] Script multi-run versi final (`multi_run_experiment_v2.py`) — preprocessing lengkap ditambahkan, dengan caching hasil preprocessing
- [x] Fungsi `preprocess()` (case folding, cleansing, stopword removal NLTK, stemming Sastrawi) — identik antara notebook dan v2
- [x] Konfigurasi via dict `CONFIG` (path dataset, n_sample, test_size, tfidf_max_features, seed list) — bukan hardcode di badan skrip
- [x] Data logging JSON per run (identitas, konfigurasi, hasil metrik, confusion matrix, status anomali)
- [x] Validasi range metrik otomatis (flag `anomali` jika nilai di luar [0,100])
- [x] Rekap statistik otomatis (`rekap_statistik.csv`, `rekap_statistik_v2.csv`) — mean±std per algoritma

## Hasil Verifikasi

Diverifikasi melalui pemeriksaan log JSON dan validasi silang (lihat WS-11 Data Validation & Integrity):

- **Notebook (single-run, seed=42)**: NB accuracy=89,53%, RF accuracy=89,92% — dipakai sebagai baseline referensi pipeline preprocessing.
- **Script v1 (tanpa preprocessing)**: seluruh 10 run selesai tanpa crash (`anomali=NONE`), namun ditemukan selisih ~1 poin accuracy vs notebook pada seed yang sama (42) — mengindikasikan pipeline tidak identik (lihat Tahap 3).
- **Script v2 (dengan preprocessing, final)**: seluruh 10 run selesai tanpa crash; accuracy NB seed=42 naik dari 88,59% (v1) menjadi 89,20% (v2), mendekati notebook (89,53%) — mengonfirmasi pipeline v2 sudah konsisten dengan referensi.
- **Leakage check**: dikonfirmasi TF-IDF Vectorizer di-fit hanya pada `X_train` di seluruh versi skrip (notebook, v1, v2) — tidak ada data leakage pada tahap ekstraksi fitur.

## Catatan Lingkungan

- **Google Colab** dipakai untuk eksplorasi notebook awal (stemming Sastrawi dan NLTK stopword tersedia via `pip install`/`nltk.download` langsung di runtime Colab).
- **Eksekusi lokal (VS Code, Windows)** dipakai untuk script multi-run (`multi_run_experiment.py`/`_v2.py`) — memerlukan `pip install --break-system-packages` atau virtual environment untuk PySastrawi dan NLTK di beberapa konfigurasi Windows.
- **Waktu eksekusi stemming**: tahap stemming Sastrawi pada seluruh korpus (v2) memerlukan estimasi 5–15 menit pada eksekusi pertama; dimitigasi dengan mekanisme caching (`gojek_labeled_clean.csv`) sehingga replikasi berikutnya tidak perlu mengulang stemming.
- **Paralelisasi Random Forest**: `n_jobs=-1` dipakai pada `RandomForestClassifier` untuk memakai seluruh core CPU — menyebabkan variasi kecil waktu latih run-to-run (bergantung beban CPU saat itu), namun tidak memengaruhi hasil metrik (deterministik via `random_state`).