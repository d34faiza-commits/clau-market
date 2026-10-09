# Segment: Travel & Tour Operator

> **Status: Planned — belum dipakai untuk client.** Disiapkan 2026-10-09 sebagai knowledge awal (**ASSUMPTION**) untuk vertical gelombang 1 (`clau-ai-core/docs/verticals.md`). Aktif setelah checklist aktivasi vertical selesai (TASK-041).

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

## References

- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md)
- [07 AI Visual Disclosure](../../rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md)
- [destinations/indonesia-overview.md](../destinations/indonesia-overview.md)
