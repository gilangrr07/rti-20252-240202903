# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah Random Forest + TF-IDF menghasilkan correct classification rate lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan ukuran dataset (183 → 273 → 418 soal) berpengaruh signifikan terhadap akurasi ketiga algoritma?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
|Jenis algoritma klasifikasi | IV   |Modul Classifier — swap Naive Bayes / Random Forest / REPTree| Ganti pilihan algoritma di menu Classify WEKA Explorer atau parameter clf Python; komponen lain tidak berubah |
|Ukuran dataset| IV |Modul Dataset Loader — memuat file ARFF/CSV sesuai iterasi|Ganti file input (dataset_183, dataset_273, dataset_418); struktur atribut tetap identik|
|Correct Classification Rate (%)| DV   |Modul Output Logger — membaca hasil evaluasi dari WEKA atau sklearn |Dicatat dari output “Correctly Classified Instances” WEKA atau accuracy_score Python |
|Filter / tokenizer| CV   |Modul Preprocessing — StringToWordVector (WEKA) atau TF-IDF (Python) |Dikonfigurasi sekali sebelum eksperimen dan dikunci konstan |
|Distribusi kelas soal| CV   |Modul Dataset — komposisi mudah/sedang/sulit dimonitor |Dilaporkan tiap iterasi; imbalance ekstrem dicatat sebagai limitasi |



4 Prinsip Desain:
  [X] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [X] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [X] Measurement Integration — Pengukuran DV built-in
  [X] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : File ARFF (WEKA) atau CSV (Python): dataset_183.arff, dataset_273.arff, dataset_418.arff
  Parameter      : Naive Bayes, Random Forest, REPTree
  Output format  : Tabel correct classification rate (%) dan incorrect classification count untuk setiap kombinasi algoritma × ukuran dataset.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah algoritma Random Forest dengan TF-IDF menghasilkan correct classification rate (%) lebih tinggi dibandingkan Naive Bayes dan REPTree pada dataset soal ujian Bahasa Indonesia SD, dan apakah peningkatan jumlah data dari 183 ke 273 ke 418 soal berpengaruh signifikan terhadap akurasi ketiga algoritma tersebut?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| *Jenis algoritma klasifikasi* | *IV* | *Modul Classifier — swap Naive Bayes ↔ Random Forest ↔ REPTree* | *Ganti classifier pada WEKA Explorer atau parameter model di Python* |
| *Ukuran dataset* | *IV* | *Modul Dataset Loader* | *Mengganti file input sesuai iterasi eksperimen* |
| *Correct Classification Rate (%)* | *DV* | *Modul Output Logger* | *Dicatat dari output evaluasi WEKA atau sklearn* |
| *Filter / tokenizer* | *CV* | *Modul Preprocessingr* | *Dikunci tetap menggunakan StringToWordVector atau TF-IDF* |
| *Distribusi kelas soal* | *CV* | *Modul Dataset* | *Dipantau pada setiap iterasi dataset* |


**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? Semua variabel berhasil dipetakan ke komponen sistem konkret sehingga eksperimen dapat dilakukan secara terstruktur dan terukur.

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | *✅* |*Setiap modul memiliki hubungan langsung dengan IV, DV, atau CV* |
| Modularity | *✅* |*Algoritma dapat diganti tanpa memengaruhi preprocessing dan dataset*|
| Controllability | *✅* |*Parameter preprocessing dan dataset dikunci tetap selama eksperimen*|
| Measurability | *✅* |*WEKA dan Python menghasilkan output akurasi otomatis*|

**Prinsip mana yang paling sulit dipenuhi?** Controllability
**Strategi untuk mengatasinya:**
> Seluruh parameter preprocessing dan algoritma didokumentasikan sebelum eksperimen. Pada Python, parameter diletakkan di bagian konfigurasi awal skrip agar mudah direproduksi. Pada WEKA, konfigurasi disimpan menggunakan fitur save setup.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

Tiga komponen utama:
A = Filter/tokenizer (StringToWordVector / TF-IDF)
B = Dataset penuh (418 soal)
C = Algoritma terbaik (REPTree atau Random Forest)
| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | *✅ Filter aktif* | *✅ 418 soal* | *✅ REPTree/RF* | *Akurasi tertinggi sebagai baseline* |
| – A | ❌ (Tanpa filter | ✅ | ✅ |*Akurasi turun drastis karena teks mentah tidak direpresentasikan menjadi fitur*|
| – B | ✅ | ❌ (Dataset kecil) | ✅ | *Akurasi lebih rendah karena data pelatihan terbatas* |
| – C | ✅ | ✅ | ❌ (Ganti NB) | *Akurasi turun karena NB lebih lemah pada teks Indonesia* |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A — Filter/tokenizer
**Mengapa?**
> Karena filter/tokenizer merupakan fondasi pipeline klasifikasi teks. Tanpa StringToWordVector atau TF-IDF, teks tidak dapat diubah menjadi fitur numerik sehingga algoritma tidak dapat melakukan proses klasifikasi secara optimal.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Jika sistem dibangun seperti produk monolitik lalu eksperimen dilakukan belakangan, maka variabel penelitian akan sulit diisolasi. Perubahan pada satu komponen dapat memengaruhi komponen lain sehingga hasil eksperimen menjadi bias dan sulit dianalisis.
> Arsitektur modular penting dalam riset karena memungkinkan setiap variabel dipisahkan secara jelas. Dengan modularitas, peneliti dapat mengganti algoritma, preprocessing, atau dataset tanpa memengaruhi komponen lain. Hal ini meningkatkan traceability, reproducibility, dan validitas eksperimen sehingga hasil penelitian lebih dapat dipercaya.
