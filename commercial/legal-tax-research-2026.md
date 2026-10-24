# Riset Legal & Pajak untuk Jual Jasa CLAU AI (bahan untuk pengacara/konsultan pajak)

> **Status: Draft riset (2026-10-23), disusun AI agent. BUKAN nasihat hukum atau pajak.** Dikumpulkan dari beberapa sumber publik lewat mesin pencari (halaman resmi seperti JDIH/peraturan.go.id tidak bisa dibuka langsung dari environment AI karena network policy). Setiap baris punya label dan sumber; yang **ASSUMPTION** atau sumbernya hanya satu **wajib** dicek konsultan. Owner akan meminta pengacara mengecek (owner, 2026-10-23). Dipakai bersama [service-agreement-template.md](./service-agreement-template.md) dan [data-processing-addendum.md](./data-processing-addendum.md).

## Ringkasan untuk Owner (5 poin)

1. **Aturan pelaksana UU PDP sudah terbit: PP 33/2026**, berlaku **16 Januari 2027**. Mulai saat itu kewajiban teknis (notifikasi kebocoran, penilaian dampak/DPIA, petugas pelindungan data, transfer ke luar negeri) bisa ditegakkan. Klien pertama CLAU kemungkinan berjalan melewati tanggal itu, jadi kontrak & DPA harus sudah mengikutinya.
2. **Mengirim data ke penyedia AI di luar negeri diatur Pasal 56 UU PDP**: boleh bila negara tujuan setara/lebih tinggi perlindungannya, atau ada perlindungan memadai dan mengikat, atau (jalan terakhir) persetujuan subjek data. MK menolak uji materi pasal ini (Januari 2026). Desain CLAU (data tamu disamarkan sebelum ke AI) mengurangi risiko, tapi tetap perlu pendapat pengacara.
3. **Bentuk usaha paling hemat pajak saat ini: orang pribadi (NIB) atau PT Perorangan.** PP 20/2026 membuat PPh Final 0,5% berlaku **tanpa batas waktu** bagi orang pribadi dan PT Perorangan selama omzet ≤ Rp4,8 miliar/tahun; CV, firma, dan PT biasa yang baru terdaftar **tidak** bisa memakainya.
4. **PPN:** wajib jadi PKP baru bila omzet > Rp4,8 miliar/tahun; di bawahnya boleh sukarela.
5. **Kontrak bisa ditandatangani elektronik** (UU ITE Pasal 11). Tanda tangan elektronik **tersertifikasi** (lewat penyelenggara sertifikasi resmi) lebih kuat sebagai bukti.

## A. Pelindungan Data Pribadi (UU 27/2022 & PP 33/2026)

| # | Ketentuan | Isi (ringkas) | Label | Sumber |
|---|---|---|---|---|
| A1 | UU 27/2022 berlaku penuh | Kewajiban penuh sejak 17 Okt 2024 (masa transisi 2 tahun) | **DATA FINAL** | peraturan.bpk.go.id (sudah dirujuk di [regulasi](../knowledge/regulasi/hospitality-content-2026.md) § 1) |
| A2 | **PP 33/2026** (pelaksana UU PDP) | Ditetapkan/diundangkan 15–16 Juli 2026; berlaku 6 bulan kemudian, **16 Januari 2027** (satu sumber menulis 15 Jan). ±224–225 pasal. Mengatur antara lain notifikasi kebocoran, DPIA, Pejabat/Petugas Pelindungan Data Pribadi (PPDP), transfer lintas negara, kewajiban pengendali & prosesor, hak subjek data | Tanggal berlaku **DATA FINAL** (≥ 3 sumber); isi pasal **ASSUMPTION** sampai teks resmi dibaca | Hukumonline Pro; Kompas.id; veritask.ai; ddslaw.id; kres.id; datahukum.com |
| A3 | Lembaga pengawas PDP | Belum beroperasi per laporan Sep 2026; menunggu Perpres | **ASSUMPTION** (cek status terbaru) | Kompas (4 Sep 2026); Kompas.id |
| A4 | **Pasal 56 UU PDP**: transfer ke luar negeri | (1) boleh ke pengendali/prosesor di luar negeri; (2) pengendali wajib memastikan negara tujuan perlindungannya **setara atau lebih tinggi**; (3) bila tidak, wajib ada **perlindungan memadai dan mengikat**; (4) bila (2) dan (3) tidak terpenuhi, wajib **persetujuan subjek data**; (5) rinci di PP | **DATA FINAL** (bunyi pasal dikutip ≥ 2 sumber) | pasal.id; Hukumonline Klinik; Kompas (2022) |
| A5 | Uji materi Pasal 56 | Perkara 137/PUU-XXIII/2025; MK menolak (19 Jan 2026), pasal tetap berlaku | **DATA FINAL** (sumber berita hukum) | Hukumonline (2026); mkri.id |
| A6 | **Pasal 46**: kegagalan pelindungan | Pengendali wajib memberi tahu **tertulis paling lambat 3×24 jam** ke subjek data & lembaga; isi minimal: data yang terungkap, kapan & bagaimana, upaya penanganan & pemulihan; dalam hal tertentu wajib mengumumkan ke masyarakat | **DATA FINAL** (≥ 2 sumber) | NU Online; Hukumonline |
| A7 | Prosesor wajib melapor ke pengendali | PP 33/2026 disebut mengatur kewajiban prosesor melaporkan kegagalan ke pengendali | **ASSUMPTION** (satu sumber ulasan) | veritask.ai |
| A8 | **DPIA** (penilaian dampak) | Wajib bila pemrosesan berpotensi **risiko tinggi** (PP 33/2026 Pasal 120 menurut salinan teks): antara lain keputusan otomatis berdampak hukum/signifikan, data spesifik, skala besar, evaluasi/penskoran/pemantauan sistematis; beberapa ulasan menyebut AI/machine learning eksplisit | **ASSUMPTION** (nomor pasal & daftar kriteria perlu dicek ke teks resmi) | datahukum.com (salinan); kres.id; ddslaw.id |
| A9 | Sanksi administratif (Pasal 57 UU PDP) | Peringatan tertulis, penghentian sementara pemrosesan, penghapusan data, denda administratif **paling tinggi 2% pendapatan/penerimaan tahunan** terhadap variabel pelanggaran; berlaku untuk pengendali **dan** prosesor (Pasal 57 menyebut antara lain Pasal 51 ayat (1) dan (5)) | **DATA FINAL** untuk jenis sanksi & batas 2%; nomor ayat **ASSUMPTION** | Hukumonline; Bisnis.com |
| A10 | Pidana (contoh) | Pasal 67: perolehan/pengumpulan data melawan hukum, penjara maks 5 tahun dan/atau denda maks Rp5 miliar | **DATA FINAL** | sudah di [regulasi](../knowledge/regulasi/hospitality-content-2026.md) § 1 |

### Apa artinya untuk CLAU (analisis AI, perlu konfirmasi pengacara)

| Topik | Posisi CLAU sekarang | Pertanyaan untuk pengacara |
|---|---|---|
| Peran | Klien = pengendali data tamu; CLAU = prosesor ([DPA](./data-processing-addendum.md) § 1) | Apakah pembagian peran ini tepat untuk foto tamu, review publik, dan pesan tamu? |
| Transfer ke penyedia AI (luar negeri) | Hanya fakta usaha + teks yang **disamarkan**; tanpa nama/kontak/nomor booking | (a) Apakah teks yang sudah disamarkan masih "data pribadi"? (b) Bila ya, jalur mana dari Pasal 56 yang dipakai: setara, perlindungan mengikat (mis. syarat kontrak penyedia AI), atau persetujuan subjek? (c) Apa yang perlu ditulis di DPA? |
| DPIA | CLAU memakai AI untuk menulis draft, **bukan** keputusan otomatis yang berdampak hukum ke tamu; tidak ada penskoran orang | Apakah pemrosesan seperti ini masuk "risiko tinggi" PP 33/2026? Bila ya, siapa yang membuat DPIA (klien sebagai pengendali, dibantu CLAU)? |
| Notifikasi kebocoran | DPA: CLAU memberi tahu klien ≤ 24 jam, supaya klien bisa memenuhi 3×24 jam | Apakah 24 jam cukup, dan apa isi minimal laporan prosesor menurut PP 33/2026? |
| PPDP (petugas pelindungan data) | Belum ada | Apakah CLAU (atau klien kecil) wajib menunjuk PPDP menurut PP 33/2026? |
| Mulai 16 Jan 2027 | Kontrak klien pertama kemungkinan melewati tanggal ini | Klausul apa yang perlu ditambah supaya kontrak tetap patuh setelah PP berlaku? |

## B. Kontrak

| # | Ketentuan | Isi | Label | Sumber |
|---|---|---|---|---|
| B1 | Syarat sah perjanjian | Pasal 1320 KUHPerdata: sepakat, cakap, hal tertentu, sebab yang halal | **DATA FINAL** | KUHPerdata; jurnal hukum |
| B2 | Kebebasan berkontrak | Pasal 1338 KUHPerdata: perjanjian sah berlaku sebagai undang-undang bagi para pihak, dilaksanakan dengan itikad baik; dibatasi undang-undang, kepentingan umum, kesusilaan | **DATA FINAL** | KUHPerdata; Hukumonline Klinik |
| B3 | Klausula pembatasan tanggung jawab (eksonerasi) | Untuk **konsumen**, Pasal 18 UU Perlindungan Konsumen melarang klausula baku yang mengalihkan tanggung jawab (batal demi hukum). Untuk kontrak **antarpelaku usaha (B2B)** sumber tidak tegas: dinilai dengan itikad baik dan keseimbangan posisi tawar | Konsumen **DATA FINAL**; B2B **ASSUMPTION** | Hukumonline Klinik (klausula eksonerasi); jurnal Unpas, USM, Warmadewa; Putusan MA 2078K/PDT/2009 (disebut sumber) |
| B4 | Tanda tangan elektronik | UU ITE (UU 1/2024) Pasal 11: TTE sah bila memenuhi syarat (identifikasi penanda tangan, menunjukkan persetujuan, dll.). PP 71/2019: TTE **tersertifikasi** (penyelenggara sertifikasi elektronik Indonesia) lebih kuat pembuktiannya daripada tidak tersertifikasi | **DATA FINAL** (≥ 2 sumber) | Hukumonline Klinik; siplawfirm.id; tilaka.id |

Pertanyaan untuk pengacara: (1) Apakah klien CLAU (villa, kafe yang membeli jasa untuk usahanya) dihitung "konsumen" menurut UU Perlindungan Konsumen atau murni B2B? (2) Apakah batas tanggung jawab "biaya 1 bulan" di Pasal 8.4 template wajar dan sah? (3) Forum sengketa: Pengadilan Negeri domisili atau BANI? (4) Cukupkah TTE tidak tersertifikasi untuk kontrak bernilai kecil, atau sebaiknya pakai penyelenggara bersertifikat?

## C. Bentuk Usaha

| # | Pilihan | Fakta | Label | Sumber |
|---|---|---|---|---|
| C1 | **Orang pribadi + NIB** | Daftar di OSS (oss.go.id); NIB tanpa biaya | NIB gratis **DATA FINAL** (≥ 2 sumber) | izin.co.id; industry.co.id |
| C2 | **PT Perorangan** | Dasar: UU Cipta Kerja, PP 8/2021 (+ Permenkum 49/2025 menurut sumber). Pendiri 1 orang WNI ≥ 17 tahun, cakap hukum; untuk usaha **mikro/kecil**; tanpa akta notaris (Pernyataan Pendirian online di portal AHU); biaya resmi PNBP mulai ±Rp50.000; satu orang hanya satu PT Perorangan per tahun; tanggung jawab terbatas (harta pribadi lebih terpisah) | Garis besar **DATA FINAL** (≥ 3 sumber); portal & rincian modal **ASSUMPTION** (sumber berbeda) | izin.co.id; voffice.co.id; smartlegal.id; industry.co.id |
| C3 | CV / PT biasa | Butuh akta notaris; lebih formal; **tidak** lagi bisa memakai PPh Final 0,5% bila baru terdaftar (lihat D2) | **DATA FINAL** (D2) | lihat D2 |
| C4 | **KBLI** | Paling dekat: **73100 Periklanan** (kampanye iklan, identitas merek, materi kreatif media digital; praktisi menyebut termasuk media sosial). Alternatif/sekunder: 74130 (desain) bila fokus desain. OSS disebut memakai KBLI 2025 untuk pendaftaran baru sejak 16 Juni 2026 | 73100 sebagai pilihan utama **ASSUMPTION** (cek deskripsi di BPS/OSS saat daftar) | dpb.unpad.ac.id (KBLI 2025); kbli.co.id; smartlegal.id |

## D. Pajak

| # | Ketentuan | Isi | Label | Sumber |
|---|---|---|---|---|
| D1 | **PP 20/2026** (ubah PP 55/2022) | Ditandatangani 22 April 2026 | **DATA FINAL** (≥ 3 sumber) | DDTC News; Ortax; online-pajak.com; pajak.go.id |
| D2 | PPh Final UMKM 0,5% | Omzet ≤ **Rp4,8 miliar/tahun**. **Orang pribadi dan PT Perorangan: tanpa batas waktu** (Pasal 59 PP 55/2022 dihapus). Koperasi maks 4 tahun. **CV, firma, PT biasa, BUMDes yang baru terdaftar tidak bisa lagi** memakai skema ini. Peralihan: WP OP yang masa pakainya habis 2024/2025 tetap bisa 0,5% untuk tahun pajak 2025 dan 2026 | **DATA FINAL** (≥ 3 sumber) untuk tarif, batas omzet, dan cakupan OP/PT Perorangan; rincian peralihan **ASSUMPTION** | DDTC News; Ortax; online-pajak.com; ubico.id; pajakku.com |
| D3 | Omzet sampai Rp500 juta tidak kena PPh Final (OP) | Ketentuan PP 55/2022; belum dipastikan tidak berubah di PP 20/2026 | **ASSUMPTION** | online-pajak.com (menyebut PP 55/2022) |
| D4 | **Batas PKP (PPN)** | Wajib dikukuhkan PKP bila peredaran bruto dalam satu tahun buku **melebihi Rp4,8 miliar**; permohonan paling lambat akhir tahun buku (PMK 164/2023 Pasal 17 ayat (3)); memungut PPN mulai masa pajak pertama tahun buku berikutnya. Di bawah batas: boleh PKP sukarela | **DATA FINAL** (≥ 2 sumber) | DDTC News (beberapa artikel 2026); izin.co.id |
| D5 | Wacana turunkan batas PKP | Bank Dunia (Juli 2026) mengusulkan Rp500 juta; DJP hanya akan mengevaluasi, tidak dalam waktu dekat | **ASSUMPTION** (usulan, bukan aturan) | Bisnis.com (Mar 2026); IKPI |
| D6 | Tarif PPN untuk jasa 2026 | Tidak terkonfirmasi dalam pencarian ini | **NEXT ACTION** (tanya konsultan pajak; relevan hanya bila PKP) | — |

Pertanyaan untuk konsultan pajak: (1) Orang pribadi atau PT Perorangan untuk CLAU, dengan rencana omzet tahun pertama Rp[...]? (2) Apakah pembebasan omzet Rp500 juta untuk OP masih berlaku setelah PP 20/2026? (3) Apakah perlu PKP sukarela supaya bisa menagih klien hotel/resort besar yang meminta faktur pajak? (4) Bagaimana perlakuan pajak atas biaya langganan AI dari luar negeri (PPN PMSE)?

## E. Rekomendasi Urutan (analisis AI)

1. **Minggu ini:** konsultasi singkat ke konsultan pajak (C, D) → pilih **orang pribadi + NIB** untuk mulai cepat, atau **PT Perorangan** bila ingin harta pribadi terpisah. Keduanya tetap bisa PPh Final 0,5%.
2. **Paralel:** kirim [template kontrak](./service-agreement-template.md), [DPA](./data-processing-addendum.md), dokumen ini, dan daftar L1–L6 ke pengacara. Minta jawaban tertulis atas pertanyaan di § A, § B, dan bagian "Catatan untuk Konsultan Hukum" di template.
3. **Sebelum 16 Januari 2027:** DPA dan kebijakan internal CLAU sudah mengikuti PP 33/2026 (hasil dari langkah 2).

## F. Skala 100 Klien: Perlu CV/PT dan Pajak Apa? (ditambahkan 2026-10-24)

### F1. Perkiraan omzet (ilustrasi, harga = rekomendasi di kartu ClickUp TASK-067, **ASSUMPTION**)

| Campuran 100 klien | Omzet per tahun |
|---|---|
| 100 × Esensial (Rp3,5 jt) | ±Rp4,2 miliar |
| 60 Esensial + 30 Growth (Rp7,5 jt) + 10 Signature (Rp12,5 jt) | ±Rp6,7 miliar |
| 40 Esensial + 40 Growth + 20 Signature | ±Rp8,3 miliar |

Kesimpulan: dengan 100 klien, omzet **hampir pasti melewati Rp4,8 miliar/tahun**, tetapi masih **di bawah Rp15 miliar**.

### F2. Akibat hukum & pajak bila omzet > Rp4,8 miliar

| # | Akibat | Isi | Label | Sumber |
|---|---|---|---|---|
| F2a | PPh Final 0,5% berhenti | Batas PP 55/2022 & PP 20/2026 Rp4,8 miliar; setelah terlampaui, PPh final dipakai sampai akhir tahun pajak itu, lalu tahun berikutnya tarif umum + **wajib pembukuan** | Batas **DATA FINAL**; aturan "sampai akhir tahun" **ASSUMPTION** (satu sumber sekunder) | pajak.go.id "Cermati 3 Hal Ini Saat Omzet Lebihi Rp4,8 Miliar"; DDTC News; pajak.com |
| F2b | Wajib PKP (PPN) | Peredaran bruto > Rp4,8 miliar dalam satu tahun buku → wajib dikukuhkan PKP, memungut PPN mulai tahun buku berikutnya | **DATA FINAL** | DDTC News (PMK 164/2023 Pasal 17) |
| F2c | Tarif PPN jasa | 12% × DPP nilai lain 11/12 = **efektif 11%** untuk jasa non-mewah (PMK 131/2024); tidak ada perubahan untuk 2026 menurut pernyataan pemerintah Agustus 2025. PPN ditagihkan ke klien di atas harga jasa | **DATA FINAL** (≥ 2 sumber) | DDTC News (beberapa artikel) |
| F2d | Orang pribadi (tarif umum) | Tarif progresif Pasal 17 UU PPh (UU HPP): 5% s.d. Rp60 jt; 15% >Rp60–250 jt; 25% >Rp250–500 jt; 30% >Rp500 jt–Rp5 M; 35% >Rp5 M (atas penghasilan kena pajak/laba, bukan omzet) | **DATA FINAL** (UU 7/2021 HPP) | UU HPP; pajak.go.id |
| F2e | PT (badan) | Tarif 22%; **Pasal 31E**: badan dengan peredaran bruto ≤ Rp50 miliar mendapat pengurangan 50% tarif (jadi 11%) atas bagian penghasilan kena pajak dari peredaran bruto s.d. Rp4,8 miliar; berlaku otomatis lewat SPT | **DATA FINAL** (≥ 3 sumber) | DDTC News; IKPI; pajakku.com; pajak.go.id |
| F2f | PT Perorangan masih boleh? | Ya selama usaha **kecil**: hasil penjualan > Rp2 M s.d. **Rp15 M**/tahun (PP 7/2021). Wajib berubah jadi PT biasa bila > Rp15 M (atau modal > Rp5 M) **atau** pemegang saham lebih dari satu (PP 8/2021 Pasal 9; Permenkum 49/2025) | Batas omzet **DATA FINAL**; pasal turunan **ASSUMPTION** | Hukumonline Klinik (kriteria UMKM); DDTC News; izin.co.id; smartlegal.id; lexmundus.com |

### F3. Ilustrasi beban PPh (laba 30% dari omzet Rp6,7 M = laba ±Rp2 M; **ASSUMPTION**, bukan nasihat pajak)

| Bentuk | Perhitungan kasar | PPh ±/tahun |
|---|---|---|
| Orang pribadi, tarif progresif | 5%·60 jt + 15%·190 jt + 25%·250 jt + 30%·1,5 M | ±Rp544 jt (±27% laba) |
| PT (Perorangan atau biasa), Pasal 31E | Bagian fasilitas: 2 M × 4,8/6,7 ≈ 1,43 M × 11% ≈ Rp157 jt; sisa 0,57 M × 22% ≈ Rp126 jt | ±Rp283 jt (±14% laba), **belum termasuk** pajak dividen bila laba dibagikan ke pemilik |

Selisih ini yang membuat **PT** umumnya lebih hemat pada skala 100 klien. Angka nyata bergantung pada biaya (gaji tim, AI, sewa), PTKP, dan pembagian dividen: hitung ulang dengan konsultan pajak.

### F4. Kewajiban lain karena tim bertambah

100 klien butuh ±14 content lead/reviewer (kapasitas SOP § 5: ±7 klien campuran per orang) + admin. Konsekuensinya: kontrak kerja, **PPh 21** atas gaji, dan **BPJS Kesehatan & Ketenagakerjaan** untuk pekerja (kewajiban pemberi kerja; **NEXT ACTION**: konfirmasi rincian ke konsultan). Bentuk badan usaha (PT) memudahkan semua ini serta kontrak dengan hotel/resort besar yang meminta faktur pajak.

### F5. Rekomendasi bertahap (analisis AI)

| Tahap | Bentuk | Pajak |
|---|---|---|
| 1–±10 klien (omzet < Rp4,8 M) | Orang pribadi + NIB **atau** langsung PT Perorangan | PPh Final 0,5%; belum wajib PKP |
| Menuju 100 klien (omzet > Rp4,8 M, < Rp15 M) | **PT Perorangan** (atau PT biasa bila ada mitra/investor) | Pembukuan, PPh badan 22% dengan Pasal 31E, **PKP** (PPN efektif 11% ditagihkan ke klien), PPh 21 + BPJS tim |
| > Rp15 M atau ada pemegang saham kedua | **PT biasa** (akta notaris) | Sama, dengan kewajiban pelaporan PT |

CV tidak disarankan: sejak PP 20/2026 CV baru tidak bisa memakai PPh Final 0,5%, dan sekutu aktif CV bertanggung jawab sampai harta pribadi.

## Sumber (dibaca lewat hasil mesin pencari, 2026-10-23)

- Kompas, "UU PDP dan Transfer Data Pribadi ke Luar Negeri" (2022); Kompas, "Segera Bentuk Badan Pelindungan Data Pribadi" (4 Sep 2026); Kompas.id, "Peraturan pelaksana UU PDP akhirnya terbit, lembaga pengawas masih dinanti"
- Hukumonline: "Pasal 56 UU PDP Dinilai Belum Memadai…", "Aturan dan Risiko Transfer Data Pribadi Antarnegara" (Klinik), "Transfer Data Lintas Negara… Pasca Putusan MK", "Ancaman Sanksi Administratif hingga Pidana dalam UU PDP", "Klausula Eksonerasi" (Klinik), "Begini Pembuktian Tanda Tangan Elektronik di Pengadilan" (Klinik); Hukumonline Pro, PP 33/2026
- pasal.id, Pasal 56 UU 27/2022; mkri.id (berita sidang Perkara 137/PUU-XXIII/2025)
- NU Online, "Data Nasional Bocor, Bagaimana Tanggung Jawab Pemerintah Sesuai UU PDP?"
- veritask.ai, ddslaw.id, kres.id, robere.co.id, datahukum.com (salinan PP 33/2026), meridianhukum.com
- Bisnis.com, "Langgar UU PDP Bisa Kena Sanksi…" (2022) dan "Bank Dunia: Ambang Batas Pajak Pengusaha Terlalu Tinggi…" (Mar 2026)
- DDTC News: "Khusus Orang Pribadi, PPh Final UMKM Diperpanjang hingga 2029", "Omzet Tembus Rp4,8 Miliar Tengah Tahun, Kapan WP Wajib Jadi PKP", "Omzet Belum Tembus Rp4,8 Miliar, Bolehkah Pengusaha Kecil Pungut PPN"; Ortax; online-pajak.com ("PPh Final UMKM 2026 Diperpanjang? Aturan PP 20/2026"); pajakku.com; ubico.id; pajak.go.id
- izin.co.id, voffice.co.id, smartlegal.id, industry.co.id (PT Perorangan); dpb.unpad.ac.id dan kbli.co.id (KBLI 73100)
- siplawfirm.id, tilaka.id (tanda tangan elektronik)
- § F: pajak.go.id "Cermati 3 Hal Ini Saat Omzet Lebihi Rp4,8 Miliar"; DDTC News (Pasal 31E, PPN DPP 11/12, kriteria UMKM PP 7/2021); IKPI; pajakku.com; Hukumonline Klinik "Kriteria UMKM Terbaru"; izin.co.id, smartlegal.id, lexmundus.com, kontrakhukum.com (PT Perorangan → PT biasa)
