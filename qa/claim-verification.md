# QA — Claim Verification

## Purpose

Gate wajib untuk memastikan setiap klaim di konten (teks, visual, voice-over, on-screen text) terbukti dan berstatus **DATA FINAL** sebelum approval.

## Required Inputs

- Draft final (semua varian & bahasa).
- Tabel klaim dari creator.
- Dokumen sumber client (fact sheet, menu, rate card, sertifikat).

## Langkah

1. **Ekstraksi per kalimat (wajib).** Masukkan **setiap kalimat** konten ke [Tabel Ekstraksi Kalimat](#tabel-ekstraksi-kalimat): caption (semua bahasa), on-screen text, teks story/slide, alt text, voice-over, dan hashtag yang menyebut segmen/fasilitas. Untuk visual, satu baris per aset/shot. Jangan memakai "baca ulang" bebas: kalimat yang tidak ada di tabel dianggap belum dicek.
2. Untuk tiap baris, tulis klaim **eksplisit** dan **tersirat**. Pertanyaan pemicu klaim tersirat:
   - Waktu: apakah kalimat menyebut/menyiratkan pagi, sunset, musim, yang tidak cocok dengan aset atau fakta?
   - Jarak & akses: "langsung", "di depan", "open onto", "steps from" menyiratkan jarak/akses yang harus terbukti.
   - Privasi & eksklusivitas: "yours alone", "hanya untuk kamu" bertentangan dengan pemakaian bersama?
   - Segmen: apakah kalimat/hashtag mengunci segmen yang masih **CLIENT CONFIRMATION**?
3. Cocokkan dengan tabel klaim dari creator; tambahkan klaim yang terlewat.
4. Verifikasi setiap klaim ke sumber; catat versi/tanggal sumber.
5. Klaim tanpa sumber → hapus/ubah, atau tandai **CLIENT CONFIRMATION** / **FIELD VERIFICATION** dan blok publish.

## Re-check Penuh per Versi

Setiap versi baru (v2, v3, …) menjalankan **semua langkah di atas untuk semua konten**, termasuk konten yang "tidak berubah" dari versi sebelumnya. Hasil versi lama tidak boleh dibawa ("lolos semua gate di v1"). Alasannya: gate bisa berubah di antara versi, dan pelanggaran yang lolos di v1 akan terbawa diam-diam.

## Tabel Ekstraksi Kalimat

| # | Konten · lokasi | Kalimat / shot (persis) | Klaim eksplisit | Klaim tersirat | Label | Hasil |
|---|---|---|---|---|---|---|
| 1 | C-A · caption baris 1 | | | | DATA FINAL / … / tidak ada klaim | OK / Ubah / Hapus |

Hitungan untuk [rubrik skor](./scoring-rubric.md): jumlah baris total, dan jumlah baris **OK** tanpa perubahan.

## Tabel Verifikasi

| # | Klaim (persis seperti di konten) | Kategori | Label | Sumber + versi/tanggal | Verifier | Hasil |
|---|---|---|---|---|---|---|
| 1 | | fasilitas / lokasi / harga / rating / sertifikasi / F&B / treatment / experience | | | | OK / Ubah / Hapus |

## Checklist per Kategori ([rule 02](../rules/02-HOSPITALITY-CLAIM-STANDARD.md))

### Umum

- [ ] Tidak ada superlatif tanpa bukti ("terbaik", "nomor 1", "best", "termurah").
- [ ] Tidak ada testimoni/review karangan.
- [ ] Klaim musiman/bersyarat menyebut kondisinya.
- [ ] Tidak ada penyebutan kompetitor.

### Rating, sertifikasi, award

- [ ] Bintang = sertifikat klasifikasi berlaku (bukan rating OTA).
- [ ] Rating platform menyebut platform + tanggal.
- [ ] Sertifikasi/award: nama, penyelenggara, tahun benar, masih berlaku.

### Halal & dietary

- [ ] "Halal" hanya dengan sertifikat berlaku untuk outlet/produk.
- [ ] Vegan/gluten-free/allergen dikonfirmasi per menu.

### Harga & promo

- [ ] Mata uang, unit, periode, syarat lengkap.
- [ ] Net/++ jelas.
- [ ] Harga acuan diskon benar-benar pernah berlaku.
- [ ] Tidak ada fake scarcity/countdown.
- [ ] Konsisten dengan harga di OTA/website.

### Lokasi & fasilitas

- [ ] Jarak menyebut moda + estimasi; verifikasi lapangan bila meragukan.
- [ ] Beachfront / ocean view / private pool / private beach sesuai fakta.
- [ ] Fasilitas berbayar disebut berbayar; jam operasional benar.

### Spa & wellness

- [ ] Tidak ada klaim medis (menyembuhkan, detoks racun, melangsingkan, dll.).
- [ ] Kualifikasi terapis hanya bila terbukti.

### Experience

- [ ] Satwa/alam tidak dijamin.
- [ ] Aktivitas berisiko menyebut syarat & keselamatan.

## Blockers (otomatis Fail)

- Klaim non-**DATA FINAL** di konten publish.
- Klaim halal/bintang/sertifikasi tanpa bukti.
- Klaim medis spa.
- Harga tanpa periode/syarat/net-++.
- Tabel ekstraksi kalimat tidak ada, tidak lengkap, atau tidak mencakup semua konten versi ini.

## Record

| Verifier | Independen? (Ya / Tidak — self-review) | Tanggal | Versi konten | Hasil | Catatan |
|---|---|---|---|---|---|
| | | | | | |

Konten L2/L3 butuh minimal satu verifikasi **independen** ([rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md)). Self-review AI/creator hanya pre-check.
