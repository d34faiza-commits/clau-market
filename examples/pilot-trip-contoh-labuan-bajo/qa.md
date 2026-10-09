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
| Review independen | ✅ 2026-10-09 — lihat [Review Independen](#review-independen-2026-10-09) (v1 belum lulus) |
| Keputusan | Tertahan sampai izin usaha & sertifikat kapten = DATA FINAL |

## Review Independen (2026-10-09)

| Field | Isi |
|---|---|
| Reviewer | **Dea Karisna (d34faiza)**, owner — bukan pembuat draft (draft dibuat AI agent) |
| Metode | AI agent menyusun **pre-review kritis** atas draft-nya sendiri (bukan review independen); reviewer membaca dan menyatakan **"setuju"** di sesi Claude Code 2026-10-09. Penilaian akhir = reviewer |
| Objek | Carousel IG v1 (dinilai). Caption TikTok v1 diperiksa di luar skor |
| Keputusan | **Belum lulus — revisi kecil.** v2 di [drafts.md](./drafts.md). Tetap **tertahan** sampai izin usaha & sertifikat kapten DATA FINAL (T-03) |

| # | Kalimat (v1) | Hasil | Catatan |
|---|---|---|---|
| 1 | 3 hari di kapal… | ✅ | |
| 2 | …**berangkat** setiap Jumat di bulan November, 6–14 peserta | ⚠️ (diubah) | Terbaca pasti berangkat, padahal minimal 6 peserta; kebijakan bila < 6 belum ada di fact sheet |
| 3 | Hari 1: snorkeling, lalu trekking… | ⚠️ (diubah) | Syarat **bisa berenang dasar** (fact sheet §2) tidak ditulis — keselamatan; lolos self-check agent |
| 4 | Hari 2: dua spot snorkeling… | ⚠️ (diubah) | Ditulis pasti; fact sheet: spot bisa diganti bila arus kuat |
| 5 | Hari 3… | ✅ | |
| 6 | Harga net + isi paket | ✅ | Catatan: tulis "kabin sharing berkipas" (tanpa AC) |
| 7 | Belum termasuk… | ✅ | |
| 8 | Briefing keselamatan + life jacket | ✅ | |
| 9 | CTA WhatsApp | ✅ (CTA, bukan klaim) | |
| TikTok | "tanpa drama harga tersembunyi" | ❌ (di luar skor) | Klaim mutlak (Medium) sementara besaran retribusi masih CLIENT CONFIRMATION |

| Pertanyaan | Jawaban reviewer |
|---|---|
| B1 Pelanggaran rule | Ya: syarat berenang tidak ditulis (Medium, keselamatan), kesan pasti berangkat (Low), spot ditulis pasti (Low) |
| B2 Sesuai brief | Ya; revisi memperkuat key message "keselamatan nyata" |
| B3 Kabin tanpa AC disebut? | Ya, cukup "berkipas" |
| B4 Makan "tanpa babi" ditulis di IG? | Tidak; kata "halal" tidak dipakai, pertanyaan dijawab di DM sesuai fact sheet |

### Record (qa/scoring-rubric)

| Versi | Penghitung | Status | A | B | C | D | Total | Kesiapan | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| v1 | Dea Karisna (owner) atas pre-review AI | Independent score | 63 | 86 | 100 | — | 83 | **0** (blocker: gate T-03 izin usaha & sertifikat kapten = CLIENT CONFIRMATION) | A = 5 dari 8 baris klaim OK tanpa perubahan (#1, #5–#8); B = 100 − 8 − 3 − 3; D tidak dihitung; total = rata-rata A–C |
| v2 | — | Menunggu cek ulang reviewer | | | | | | | Revisi atas semua temuan v1 (IG + TikTok) |

## Temuan pilot

| ID | Temuan | Tindak lanjut |
|---|---|---|
| T-01 | Checker tidak menangkap janji "pasti lihat manta"/"100% aman" | **Selesai** — `GUARANTEE_TERMS` di `scripts/check_caption.py` + test |
| T-02 | Schema v1.3 tidak punya kategori klaim itinerary/safety/license | **Selesai** — schema v1.4 |
| T-03 | Legalitas operator harus jadi syarat tayang untuk aktivitas berisiko | Catat di QA travel: izin & sertifikat = gate sebelum publish |
| T-04 | Review independen: syarat keselamatan peserta (bisa berenang) ada di fact sheet tetapi tidak ditulis, dan lolos self-check | **Selesai** — self-check `skills/draft-caption` #7: syarat keselamatan & kondisi itinerary wajib ikut ditulis |
| T-05 | "Berangkat setiap Jumat" dengan kuota minimum tanpa kebijakan bila kuota tidak terpenuhi | Template travel fact sheet: baris kebijakan bila kuota minimum tidak terpenuhi; NEXT ACTION: minta ke client (CLIENT CONFIRMATION) |
