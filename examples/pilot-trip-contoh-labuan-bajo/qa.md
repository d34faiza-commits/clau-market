# QA & Approval — Trip Contoh Labuan Bajo (SIMULASI)

> **Self-review oleh AI agent** — pre-check, **bukan** review independen. Approval = **SIMULASI**.

## Claim verification (per kalimat, carousel IG)

| # | Kalimat | Klaim | Label | Sumber | Hasil |
|---|---|---|---|---|---|
| 1 | 3 hari di kapal, ini rencananya hari per hari | Durasi | DATA FINAL | Itinerary v2 | OK |
| 2 | …berangkat setiap Jumat di bulan November, 6–14 peserta | Jadwal, kuota | DATA FINAL | Fact sheet §2 | OK |
| 3 | Hari 1: snorkeling, lalu trekking bukit ± 30 menit naik tangga (sunset bila cuaca mendukung) | Itinerary, level fisik, kondisi cuaca | DATA FINAL | Itinerary v2 | OK |
| 4 | Hari 2: dua spot snorkeling dan pantai berpasir merah muda | Itinerary | DATA FINAL | Itinerary v2 | OK |
| 5 | Hari 3: snorkeling pagi, kembali ke pelabuhan siang | Itinerary | DATA FINAL | Itinerary v2 | OK |
| 6 | Rp3.250.000 per orang (net): kapal & kabin sharing, makan 7 kali, alat snorkel, pemandu | Harga, isi paket | DATA FINAL | Fact sheet §2 | OK |
| 7 | Belum termasuk tiket pesawat, retribusi kawasan, dan tip kru | Tidak termasuk | DATA FINAL | Fact sheet §2 | OK |
| 8 | Sebelum berangkat ada briefing keselamatan dari kapten, dan setiap peserta dapat life jacket | Keselamatan | DATA FINAL | SOP TCL-SOP-01 | OK |
| 9 | Tanya kuota lewat WhatsApp di bio | CTA | — | — | OK |

## Content review

| Cek | Hasil |
|---|---|
| Voice `informatif-praktis`, "kamu" | ✅ |
| `check_caption --markdown … --brief …` (termasuk daftar GUARANTEE_TERMS) | PASS (mekanis) |
| Izin usaha belum diterima | ⚠️ **Conditional** — konten boleh disiapkan, **tidak boleh tayang** sebelum izin usaha & sertifikat kapten dikonfirmasi (keselamatan peserta) |

## Approval (SIMULASI)

| Field | Isi |
|---|---|
| Mode | **SIMULASI** |
| Level | L2 (harga) |
| Review independen | ⬜ Belum |
| Keputusan | Tertahan sampai izin usaha & sertifikat kapten = DATA FINAL |

## Temuan pilot

| ID | Temuan | Tindak lanjut |
|---|---|---|
| T-01 | Checker tidak menangkap janji "pasti lihat manta"/"100% aman" | **Selesai** — `GUARANTEE_TERMS` di `scripts/check_caption.py` + test |
| T-02 | Schema v1.3 tidak punya kategori klaim itinerary/safety/license | **Selesai** — schema v1.4 |
| T-03 | Legalitas operator harus jadi syarat tayang untuk aktivitas berisiko | Catat di QA travel: izin & sertifikat = gate sebelum publish |
