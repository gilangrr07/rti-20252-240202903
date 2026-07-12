# Tahap 5 — Penulisan Draf Paper Jurnal

**Status:** Konten naskah selesai — naskah konsolidasi tersedia di [../07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md), tinjauan pustaka lengkap dengan 9 referensi (BibTeX di [../02-literatur/daftar-pustaka.bib](../02-literatur/daftar-pustaka.bib)). Sisa pekerjaan: pemindahan ke template jurnal tujuan (lihat "Yang Masih Perlu Dilengkapi").
**Bergantung pada:** [tahap-4-analisis-data.md](tahap-4-analisis-data.md) — *Selesai*

---

## Tujuan

Menyusun draf naskah ilmiah dengan gaya bahasa akademis formal, objektif, dan pasif, sesuai target publikasi jurnal terindeks SINTA 3 atau lebih tinggi.

## Rencana Deliverable (Struktur Naskah)

| Bagian | Sumber | Status |
|---|---|---|
| Naskah konsolidasi (template jurnal) | [../07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md) | Selesai — gabungan Judul, Abstrak, §1–§5 + Daftar Pustaka |
| Abstrak (ID & EN) | Bagian awal `naskah-jurnal.md` | Selesai |
| Pendahuluan (latar belakang, rumusan masalah, tujuan, kontribusi) | `naskah-jurnal.md` §1 | Selesai — mengacu proposal bagian D |
| Tinjauan Pustaka (perbandingan NB/RF pada klasifikasi teks Indonesia, *related work*) | `naskah-jurnal.md` §2 | Selesai — 9 sitasi, lihat [../02-literatur/matriks-literatur.md](../02-literatur/matriks-literatur.md) |
| Metodologi (desain eksperimen, variabel, preprocessing, prosedur) | `naskah-jurnal.md` §3 | Selesai — termasuk catatan metodologis revisi v1→v2 |
| Hasil & Analisis (statistik deskriptif, uji hipotesis, analisis sensitivitas) | `naskah-jurnal.md` §4 | Selesai, mengacu ke worksheet WS-12/WS-14 |
| Kesimpulan & Saran Penelitian Lanjutan | `naskah-jurnal.md` §5 | Selesai |
| Daftar Pustaka | `naskah-jurnal.md` (akhir) | Selesai — 9 referensi format IEEE; BibTeX: [../02-literatur/daftar-pustaka.bib](../02-literatur/daftar-pustaka.bib) |

Outline & consistency matrix: WS-15 (Scientific Writing).

## Yang Masih Perlu Dilengkapi Sebelum Submit

1. **Pemindahan ke template jurnal tujuan** — dilakukan oleh peneliti (di luar scope AI assistant), menggunakan [../07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md) sebagai sumber.
2. **Konversi ke `.docx`** sesuai gaya jurnal (margin, font, penomoran) — belum dibuat, hanya tersedia versi `.md`.
3. **Penempatan figure/tabel final** sesuai gaya jurnal (caption, penomoran) — sumber tabel: worksheet WS-12/WS-14; figure (bar chart, dot plot, dsb.) masih berupa rencana, belum digenerate sebagai file PNG (lihat [../06-output/README.md](../06-output/README.md)).
4. **Lengkapi metadata penulis & afiliasi lengkap** (NIM, program studi, fakultas — sudah ada di proposal, perlu dipindah ke format jurnal).
5. **Review konsistensi angka lintas dokumen** — pastikan naskah-jurnal.md, laporan-penelitian.md, dan seluruh worksheet WS-10 s.d. WS-14 melaporkan angka yang identik (mean±std, p-value, gap v1/v2).

## Catatan

Bagian Hasil & Analisis mengacu langsung pada output Tahap 4. Ringkasan naratif tambahan (versi lebih panjang, gaya laporan institusional) tersedia di `laporan-penelitian.md`. Bibliografi (9 referensi) dapat diimpor ke Mendeley/Zotero dari [../02-literatur/daftar-pustaka.bib](../02-literatur/daftar-pustaka.bib).