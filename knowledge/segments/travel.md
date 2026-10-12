# Segment: Travel & Tour Operator

> **Status: Fokus — aktivasi enterprise (2026-10-09).** Vertical fokus menurut AI-CONSTITUTION §2. Knowledge di bawah masih **ASSUMPTION** (pengetahuan umum, belum diverifikasi sumber resmi); sebelum dipakai untuk client, selesaikan [Status Verifikasi](#status-verifikasi). Fact sheet: [templates/travel-fact-sheet.md](../../templates/travel-fact-sheet.md) · Pilot SIMULASI: [examples/pilot-trip-contoh-labuan-bajo](../../examples/pilot-trip-contoh-labuan-bajo/README.md).

## Scope

Tour operator, agen perjalanan, open trip, private tour, aktivitas (surf, dive, snorkeling, trekking, cruise/liveaboard), transportasi wisata, dan paket honeymoon.

> Knowledge ini **Reusable** dan generik. Itinerary, harga, kuota, dan izin dari dokumen client (**DATA FINAL**).

## Karakter Segment

- Pembeli membandingkan itinerary, harga, dan ulasan di banyak kanal (IG, TikTok, OTA aktivitas, Google).
- Kepercayaan & keselamatan menentukan; ulasan dan bukti legalitas sangat dicari.
- Sangat musiman: libur sekolah, Lebaran, Natal-Tahun Baru, musim kering, musim satwa tertentu.

## Audience Umum

| Segmen | Kebutuhan | Angle konten |
|---|---|---|
| Keluarga | Aman, nyaman, ramah anak | Itinerary santai, fasilitas |
| Backpacker / open trip | Harga, teman jalan, jadwal pasti | Jadwal keberangkatan, apa yang termasuk |
| Honeymoon / couple | Privat, romantis | Private tour, sunset, dokumentasi |
| Adventure (dive/surf/trek) | Sertifikasi pemandu, alat, level kesulitan | Level fisik, keselamatan, syarat |
| Wisatawan asing | Bahasa, penjemputan, pembayaran | Info praktis, bahasa pemandu |

## Content Pillars (contoh)

1. **Destinasi & Itinerary** — rute hari per hari.
2. **Real Trips** — dokumentasi trip nyata (dengan consent peserta).
3. **Safety & Crew** — briefing, alat, pemandu bersertifikat (bila **DATA FINAL**).
4. **Tips Perjalanan** — musim, apa yang dibawa, etika lokal.
5. **Jadwal & Paket** — tanggal keberangkatan, kuota, syarat.
6. **Ulasan** — dengan izin.

## Claim Hotspots

| Klaim | Masalah umum | Perlakuan |
|---|---|---|
| "Pasti lihat manta/lumba-lumba/hiu paus" | Satwa liar tidak bisa dijamin | Hard block kata "pasti/dijamin"; tulis "peluang tinggi di musim X" hanya bila bersumber |
| "100% aman" | Tidak ada aktivitas tanpa risiko | Ganti dengan langkah keselamatan nyata (briefing, alat, asuransi bila **DATA FINAL**) |
| Izin usaha / lisensi pemandu | Belum dicek | **CLIENT CONFIRMATION** dokumen izin & sertifikat |
| Harga paket | Tanpa tiket masuk, retribusi taman nasional, pajak, tip | Rinci termasuk/tidak termasuk |
| Cuaca & sunrise/sunset | Tidak pasti | "Bila cuaca mendukung" + kebijakan reschedule |
| Kuota "tinggal 2 seat" | Urgensi palsu | Hanya bila angka nyata dan terbaru |
| Interaksi satwa (naik gajah, memegang satwa) | Isu kesejahteraan satwa & aturan konservasi | **RISK**; ikuti aturan pengelola kawasan |

## Foto & Video

- Foto destinasi dari trip sendiri atau berlisensi; sebut lokasi dengan benar.
- Drone: izin penerbangan & aturan kawasan (taman nasional, tempat suci) → **CLIENT CONFIRMATION**.
- Visual AI tidak boleh menggambarkan destinasi seolah nyata (rule 07).

## Practical Info Wajib Konsisten

| Item | Sumber |
|---|---|
| Itinerary & jam penjemputan | Itinerary resmi versi terbaru |
| Termasuk / tidak termasuk | Price list resmi |
| Kebijakan pembatalan & cuaca | Syarat & ketentuan client |
| Syarat fisik / umur / sertifikasi | Kebijakan operator |

## Kesalahan Umum

- Menjanjikan penampakan satwa atau cuaca.
- Harga "mulai dari" tanpa menyebut minimum peserta.
- Memakai foto destinasi milik orang lain tanpa izin.

## Temuan Riset (2026-10-09, sumber sekunder)

> Dari pencarian web 2026-10-09. Kecuali baris kuota (pernyataan Balai TN Komodo yang dikutip ANTARA), sumbernya berita/operator/riset, **bukan** halaman resmi pengelola. Halaman primer (Balai TN Komodo, aplikasi SiOra) belum bisa dibuka dari environment AI. Label tetap **ASSUMPTION** sampai dicek ke sumber primer; per client = **CLIENT CONFIRMATION**.

| Topik | Temuan | Sumber (akses 2026-10-09) | Dampak ke konten |
|---|---|---|---|
| Kuota TN Komodo | **Terkonfirmasi:** 1.000 wisatawan/hari, berlaku sejak 1 April 2026 (pernyataan Koordinator Kehumasan, Kerjasama & Pelayanan Perijinan Balai TN Komodo, Maria Rosdalima Panggur). Alasan: kunjungan 2025 = 429.509 (68% mancanegara), melampaui daya dukung kawasan 366.108/tahun (kajian 2022: 378.870). Kuota dievaluasi berkala | [ANTARA, 14 Apr 2026](https://www.antaranews.com/berita/5525623/btnk-tetapkan-kuota-1000-wisatawan-per-hari-di-tn-komodo) (teks artikel dikonfirmasi owner 2026-10-09); evaluasi kuota: [Republika](https://news.republika.co.id/berita/te1ozv484/kemenhut-kaji-penambahan-kuota-wisatawan-di-taman-nasional-komodo) | Jangan menjanjikan "pasti masuk Padar/Komodo"; tulis "tergantung kuota harian taman nasional". Cek ulang sebelum musim ramai karena kuota bisa berubah |
| Pembelian tiket TN Komodo | Lewat aplikasi SiOra — **belum terkonfirmasi** (tidak disebut di artikel ANTARA 14 Apr 2026) | Pemberitaan lain (sekunder) | Operator wajib menyebut siapa yang membeli tiket (termasuk/tidak termasuk) |
| Tarif masuk WNI | Rp50.000 hari kerja / Rp75.000 hari libur (PP 36/2024, berlaku sejak 30 Okt 2024 menurut berita) | [ANTARA Kupang](https://kupang.antaranews.com/berita/140801/btn-komodo-sosialisasi-penyesuaian-tarif-baru-masuk-kawasan) | Angka retribusi **jangan** ditulis di konten sebelum dicek ke SiOra/Balai; aman: "belum termasuk tiket masuk kawasan" |
| Tarif masuk WNA | **Belum terkonfirmasi** untuk 2026 (angka yang beredar dari pemberitaan 2022, kemungkinan sudah tidak berlaku) | — | Hard rule: tidak menulis angka tarif WNA |
| Manta di TN Komodo | Riset menyebut manta ada sepanjang tahun; puncak per lokasi/musim **saling bertentangan** antar operator | [Murdoch University](https://www.murdoch.edu.au/news/articles/ray-of-hope-for-indonesian-manta-populations), [Mongabay](https://mongabay.co.id/2022/06/03/perairan-tn-komodo-rumah-bagi-pari-manta-karang-yang-rentan-punah/) | Tetap "mungkin terlihat"; jangan sebut bulan puncak tanpa data operator client |

## Status Verifikasi

| Item | Status | Untuk jadi DATA FINAL / dipakai client |
|---|---|---|
| Karakter, audience, content pillars | ASSUMPTION | Validasi lewat 3–5 wawancara operator |
| Aturan kawasan (taman nasional, retribusi, drone) | ASSUMPTION — sebagian bersumber sekunder untuk TN Komodo (lihat Temuan Riset) | Konfirmasi ke sumber primer (Balai TN Komodo / SiOra); aturan drone belum ditemukan; per client = **CLIENT CONFIRMATION** |
| Izin usaha & sertifikat pemandu | CLIENT CONFIRMATION per client | Dokumen client di workspace |
| Fact sheet & pilot | ✅ Template + pilot SIMULASI tersedia | Review independen manusia atas pilot (rule 08) |
| Eval agent | ✅ Kasus travel di `clau-ai-agents/agents/evals/` | Penilaian rubrik oleh manusia |

## References

- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md)
- [07 AI Visual Disclosure](../../rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md)
- [destinations/indonesia-overview.md](../destinations/indonesia-overview.md)
