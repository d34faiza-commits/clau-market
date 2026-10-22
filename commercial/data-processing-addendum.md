# Lampiran C — Pemrosesan Data Pribadi (template)

> **Status: Draft (2026-10-22), disusun AI agent. BUKAN nasihat hukum.** Disusun mengikuti UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP) dan aturan internal (`core/AI-BOUNDARY.md` § Data ke Provider AI, [rule 04](../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md), [rule 09](../rules/09-DATA-CLASSIFICATION.md)). Rujukan pasal di bawah wajib dicek konsultan hukum (TASK-053) sebelum dipakai.

Lampiran ini bagian dari Perjanjian Layanan Konten Nomor [ ] antara **Penyedia** dan **Klien**.

## 1. Peran

| Pihak | Peran menurut UU PDP | Artinya |
|---|---|---|
| Klien | **Pengendali Data Pribadi** | Menentukan tujuan pemrosesan data tamu/staf, memegang dasar pemrosesan (antara lain persetujuan orang yang tampil di foto) |
| Penyedia | **Prosesor Data Pribadi** | Memproses data hanya atas perintah Klien untuk melaksanakan layanan konten |

## 2. Data yang Diproses

| Kategori | Contoh | Perlakuan |
|---|---|---|
| Foto/video orang yang dapat dikenali | Tamu, staf, pengantin, peserta trip | Hanya bila Klien menyatakan ada persetujuan tercatat; tanpa itu, wajah tidak dipakai |
| Teks review publik | Review Google/OTA | Nama, nomor kamar, tanggal inap, dan kode booking disamarkan (`<NAMA_TAMU>`, `<NO_BOOKING>`) sebelum diproses AI |
| Kontak PIC & approver Klien | Nama, email, nomor kerja | Untuk koordinasi saja |
| **Tidak diproses** | Data pembayaran, identitas resmi (KTP/paspor), data kesehatan, data anak di luar konten yang disetujui wali, kata sandi akun | Ditolak bila dikirim; Klien diminta menghapus dari kanal kerja |

## 3. Kewajiban Penyedia

1. Memproses data hanya untuk layanan dalam Perjanjian dan atas instruksi tertulis Klien.
2. Menyamarkan data tamu sebelum dimasukkan ke perangkat AI; hanya fakta usaha yang dikonfirmasi Klien dan teks yang sudah disamarkan yang dikirim ke penyedia model AI.
3. Membatasi akses ke personel yang membutuhkan, terikat kerahasiaan, dan memakai akses berbasis peran (tanpa berbagi kata sandi).
4. Menyimpan data Klien di workspace Klien yang terpisah dari klien lain, tidak di repositori kode.
5. Membantu Klien menanggapi permintaan subjek data (akses, koreksi, penarikan persetujuan, penurunan konten) paling lambat **[2] hari kerja** setelah diminta, supaya Klien dapat memenuhi tenggat UU PDP.
6. Memberi tahu Klien tertulis paling lambat **24 jam** setelah mengetahui kegagalan pelindungan data yang menyangkut data Klien, berisi data yang terdampak, waktu, penyebab yang diketahui, dan langkah penanganan, supaya Klien dapat memenuhi kewajiban pemberitahuan **3×24 jam** (rujukan: UU PDP Pasal 46, **ASSUMPTION** sampai dicek konsultan hukum).
7. Tidak menjual, menyewakan, atau memakai data Klien untuk melatih model AI.

## 4. Subprosesor & Transfer ke Luar Negeri

| Subprosesor | Fungsi | Lokasi pemrosesan | Data yang diterima |
|---|---|---|---|
| [Penyedia model AI, mis. Anthropic (Claude)] | Menulis draft | [Di luar Indonesia; dicatat di `core/shared/integrations.md`] | Fakta usaha yang dikonfirmasi + teks yang sudah disamarkan |
| [Penyedia workspace/penyimpanan dokumen] | Menyimpan fact sheet, draft, approval | [ ] | Data Klien |

1. Penyedia memberi tahu Klien paling lambat [14] hari sebelum menambah atau mengganti subprosesor; Klien boleh keberatan dengan alasan wajar.
2. Pemrosesan oleh subprosesor di luar wilayah Indonesia dilakukan dengan pelindungan yang setara dan data minimal (disamarkan). **RISK:** syarat transfer data pribadi ke luar wilayah hukum Indonesia (UU PDP Pasal 56) wajib dicek konsultan hukum sebelum klien pertama.

## 5. Keamanan

- Autentikasi dua faktor untuk akun kerja Penyedia.
- Tidak ada kata sandi, OTP, atau token akun Klien yang disimpan Penyedia.
- Panggilan ke model AI dicatat tanpa menyimpan isi prompt/jawaban di log (bila memakai platform CLAU AI).
- Perangkat kerja terkunci dan terenkripsi.

## 6. Retensi & Pengakhiran

1. Data dipakai selama Perjanjian berlaku.
2. Paling lambat **30 hari** setelah Perjanjian berakhir, Penyedia mengembalikan (atas permintaan) lalu menghapus data Klien, kecuali yang wajib disimpan menurut hukum (mis. dokumen penagihan) atau catatan persetujuan konten yang diperlukan sebagai bukti.
3. Penyedia memberi konfirmasi penghapusan tertulis.

## 7. Audit

Klien dapat meminta penjelasan tertulis tentang penerapan lampiran ini paling banyak [1] kali per tahun, atau sewaktu-waktu setelah kegagalan pelindungan data.

| Penyedia | Klien |
|---|---|
| [nama, jabatan, tanda tangan, tanggal] | [nama, jabatan, tanda tangan, tanggal] |

## Catatan untuk Konsultan Hukum

| # | Hal yang perlu dicek | Label |
|---|---|---|
| 1 | Pembagian peran pengendali/prosesor untuk foto yang diambil Penyedia sendiri (bila nanti ada produksi) | **RISK** |
| 2 | Pasal 46 (pemberitahuan kegagalan) dan Pasal 56 (transfer luar negeri) beserta peraturan pelaksananya | **ASSUMPTION** |
| 3 | Perlu tidaknya DPIA dan pejabat pelindungan data untuk skala Penyedia | **NEXT ACTION** |
| 4 | Bentuk bukti persetujuan foto tamu yang cukup (consent register Klien) | **CLIENT CONFIRMATION** |
