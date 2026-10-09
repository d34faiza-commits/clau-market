# QA & Approval — Villa Contoh Uluwatu Wedding (SIMULASI)

> **Self-review oleh AI agent** — pre-check, **bukan** review independen. Approval = **SIMULASI**.

## Claim verification (per kalimat, Varian A)

| # | Kalimat | Klaim | Label | Sumber | Hasil |
|---|---|---|---|---|---|
| 1 | Empat puluh kursi, satu meja panjang, dan laut di belakang Anda | Kapasitas 40 seated; view laut dari Area Tebing | DATA FINAL | Fact sheet §2 + foto VCW-MEDIA-022 | OK |
| 2 | …untuk 20–40 tamu seated: sewa Area Tebing 6 jam, katering 3 hidangan, dekor dasar, sound & lighting, serta koordinator hari H | Min/max pax, isi paket | DATA FINAL | Fact sheet §3 | OK |
| 3 | Bila hujan, acara pindah ke Ruang Joglo dengan kapasitas yang sama | Rencana hujan, kapasitas | DATA FINAL | Fact sheet §2 | OK |
| 4 | Rp185.000.000++ per acara, berlaku untuk tanggal sepanjang 2027 | Harga, unit, periode | DATA FINAL | Price list fiktif 2027 | OK |
| 5 | Musik hingga 22.00 | Aturan venue | DATA FINAL | Fact sheet §4 | OK |
| 6 | Foto: acara nyata di venue ini, dibagikan dengan izin pasangan. Foto: Studio Contoh | Keaslian aset + consent + kredit | DATA FINAL | VCW-CONSENT-03 | OK |
| 7 | Hubungi kami lewat WhatsApp di bio… | CTA | — | — | OK |

## Content review

| Cek | Hasil |
|---|---|
| Voice `elegan-tertata`, sapaan "Anda", tanpa emoji | ✅ |
| `check_caption --markdown … --brief …` | PASS (mekanis) |
| Satu CTA (WhatsApp) | ✅ |

## Privacy & rights

| Cek | Hasil |
|---|---|
| VCW-MEDIA-021: orang dapat dikenali, consent VCW-CONSENT-03 | ✅ |
| Nama pasangan tidak disebut | ✅ |

## Approval (SIMULASI)

| Field | Isi |
|---|---|
| Mode | **SIMULASI** |
| Level | L2 (harga/paket) |
| Review independen | ✅ 2026-10-09 — lihat [Review Independen](#review-independen-2026-10-09) (v1 belum lulus) |
| Keputusan | Siap diajukan setelah review independen; halal katering tetap ditahan |

## Review Independen (2026-10-09)

| Field | Isi |
|---|---|
| Reviewer | **Dea Karisna (d34faiza)**, owner — bukan pembuat draft (draft dibuat AI agent) |
| Metode | AI agent menyusun **pre-review kritis** atas draft-nya sendiri (bukan review independen); reviewer membaca dan menyatakan **"setuju"** di sesi Claude Code 2026-10-09. Penilaian akhir = reviewer |
| Objek | Varian A v1 (IG). Temuan 1a, 1b, 3 juga berlaku untuk Varian B (EN: "one long table", "the ocean behind you", "seats the same number") — revisi dengan pola yang sama sebelum dipakai |
| Keputusan | v1 belum lulus → **v2 lulus** (cek ulang 2026-10-09, reviewer: "lulus semua"; dapat di-upgrade kapan saja). v2 di [drafts.md](./drafts.md) |

| # | Kalimat (v1) | Hasil | Catatan |
|---|---|---|---|
| 1a | …satu meja panjang… | ❌ | Klaim layout tersirat; fact sheet hanya "40 seated" |
| 1b | …laut di belakang Anda | ❌ | Klaim view tanpa baris fact sheet (QA v1 merujuk foto, bukan fakta tercatat) |
| 2 | Isi paket, 20–40 seated | ✅ | |
| 3 | Ruang Joglo "dengan kapasitas yang sama" | ⚠️ (diubah) | Benar hanya untuk seated (40); standing & upacara berbeda |
| 4 | Harga, unit, periode | ✅ | Catatan: tambahkan "(belum termasuk pajak & service)" |
| 5 | Musik hingga 22.00 | ✅ | |
| 6 | Kredit foto + izin pasangan | ✅ | "Foto:" dobel — dirapikan |
| 7 | CTA WhatsApp | ✅ (CTA, bukan klaim) | |

| Pertanyaan | Jawaban reviewer |
|---|---|
| B1 Pelanggaran rule | Ya: view laut tanpa fakta (Medium), meja panjang tersirat (Low), "kapasitas yang sama" setengah benar (Low) |
| B2 Sesuai brief | Ya |
| B3 Kalimat izin pasangan di caption? | Pertahankan, singkat (transparan, membangun kepercayaan; tidak wajib) |
| B4 Daftar "tidak termasuk" di IG? | Tidak wajib bila ada di website/WA dan IG menyebut "belum termasuk pajak & service" |

### Record (qa/scoring-rubric)

| Versi | Penghitung | Status | A | B | C | D | Total | Kesiapan | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| v1 | Dea Karisna (owner) atas pre-review AI | Independent score | 67 | 86 | 100 | — | 84 | **0** (blocker: klaim view non-DATA FINAL) | A = 4 dari 6 baris klaim OK tanpa perubahan (#2, #4, #5, #6; #1 dihitung 1 kalimat dengan 2 klaim gagal, #3 diubah); B = 100 − 8 − 3 − 3; D tidak dihitung; total = rata-rata A–C |
| v2 | Dea Karisna (owner) atas cek ulang AI | Independent score — **Lulus** (2026-10-09) | 100 | 100 | 100 | — | 100 | 100 | IG ID/EN v2 + website; tanpa klaim view/layout. Catatan opsional: EN "cliff-top area" boleh diganti "Area Tebing" saja. Kesiapan berlaku dalam SIMULASI saja; tidak pernah publish |

## Temuan pilot

| ID | Temuan | Tindak lanjut |
|---|---|---|
| W-01 | Schema v1.3 tidak punya vertical wedding, unit per-event, dan kategori klaim kapasitas/izin | **Selesai** — schema v1.4 |
| W-02 | Caption IG terlalu pendek untuk daftar "tidak termasuk" lengkap | Daftar lengkap di website/WA; IG merujuk ke sana (pola standar untuk paket wedding) |
| W-03 | Pertanyaan legal pernikahan WNA berpotensi datang lewat DM | Masuk Level C (eskalasi) saat AI Sales aktif — catat di blueprint Sales |
| W-04 | Review independen: klaim view & layout tersirat di kalimat pembuka lolos self-check; QA v1 merujuk foto padahal fakta view tidak ada di fact sheet | Template wedding fact sheet ditambah baris **View dari area** (§ 2); self-check klaim tersirat sudah mencakup view |
| W-05 | "Kapasitas yang sama" untuk area cadangan menyamakan layout berbeda | Aturan: kapasitas selalu ditulis dengan jenis layout (sudah di segment wedding) — dicek ulang di QA |
| W-06 | Cek ulang v2: terjemahan nama area ("Cliff Lawn", "Joglo Hall") menambah klaim tersirat (rumput, ruang tertutup) | Varian B v2 memakai nama area asli + deskripsi dari fact sheet ("cliff-top", "semi-indoor") |
