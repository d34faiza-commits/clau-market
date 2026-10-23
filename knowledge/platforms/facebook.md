# Platform: Facebook

## Scope

Facebook Page, feed post, Reels, Stories, Event, Group komunitas, dan rekomendasi (review) Page untuk bisnis hospitality. Ditambahkan 2026-10-23 atas permintaan owner.

> **Spec platform berubah.** Nilai teknis berstatus **ASSUMPTION** sampai diverifikasi ke Facebook Help Center / Meta Business Help Center dengan tanggal akses. Diverifikasi 2026-10-22/23 lewat pencarian (halaman tidak bisa dibuka langsung dari environment AI karena network policy).

## Spec Teknis

| Item | Nilai kerja | Sumber | Status | Diverifikasi |
|---|---|---|---|---|
| Panjang teks post maksimum | ±63.206 karakter (angka yang beredar; Meta tidak mempublikasikan angka resmi). Teks terpotong "See more" setelah ±125 karakter di HP | Pihak ketiga | **ASSUMPTION** | 2026-10-23 |
| Hashtag | Tidak ada batas resmi yang ditemukan; dampaknya kecil di Facebook. Pakai **0–3**, bukan daftar panjang | Pihak ketiga | **ASSUMPTION** | 2026-10-23 |
| Durasi Reels | Batas 90 detik dihapus Meta (pengumuman Juni 2025); peluncuran bertahap, beberapa akun mungkin masih melihat batas lama | Pengumuman Meta via pihak ketiga | **ASSUMPTION** | 2026-10-23 |
| Label AI | "AI info": Meta memasang label bila sistem mendeteksi penanda AI standar industri atau pembuat mengungkapkannya. Wajib memakai alat pengungkapan AI untuk video fotorealistis atau audio realistis yang dibuat/diubah secara digital; konten yang hanya diedit dengan AI → label di menu post | About Meta (Apr 2024, update Sep 2024; Feb 2026) | **DATA FINAL** | 2026-10-23 |
| Label konten berbayar | Branded content / paid partnership tersedia untuk Page tertentu | Meta Business Help Center | **ASSUMPTION** | — |
| Aturan promosi/giveaway di Page | Lazim dipahami: peserta tidak boleh diwajibkan membagikan ke timeline pribadi atau menandai teman sebagai syarat ikut | Kebijakan Pages, Groups & Events | **ASSUMPTION** sampai dibuka kebijakan resminya | — |
| Jumlah pengguna di Indonesia | 122 juta (awal 2025; jangkauan iklan, bukan pengguna aktif; metodologi Meta berubah) | DataReportal Digital 2025 | **ASSUMPTION** untuk 2026 | 2026-10-23 |

## Kenapa Facebook Masih Penting untuk Hospitality Indonesia

| Pola | Dampak ke konten | Label |
|---|---|---|
| Audiens domestik usia 30+ dan keluarga banyak memakai Facebook untuk mencari tempat makan, penginapan, paket wisata, dan vendor wedding | Info praktis (harga + syarat, jam buka, lokasi, cara pesan) lebih penting dari estetika | **ASSUMPTION** (pola pasar; cek insight Page client) |
| Group komunitas lokal (info kuliner kota, open trip, komunitas pengantin, traveler) jadi tempat orang bertanya rekomendasi | Hadir sebagai brand yang membantu, bukan iklan berulang | **ASSUMPTION** |
| Meta Business Suite bisa menjadwalkan post ke Instagram dan Facebook sekaligus, jadi banyak bisnis memposting silang | Silang boleh, tapi caption **diadaptasi** (lihat Struktur) | Fitur **DATA FINAL**; pola pemakaian **ASSUMPTION** |
| Pertanyaan masuk lewat Messenger & komentar | Membalas DM/Messenger = Pilar 2 (belum dijual): klien yang membalas; CLAU hanya menyiapkan jawaban FAQ statis bila diminta | Keputusan owner 2026-10-22 |

## Format

| Format | Cocok untuk | Catatan |
|---|---|---|
| Post foto/album | Paket, menu, kamar, galeri wedding | Teks inti di 125 karakter pertama; album untuk room tour |
| Reels | Suasana, walkthrough, proses | Bisa sama dengan Reels IG; subtitle wajib |
| Stories | Info harian | Sama dengan IG Stories bila diposting silang |
| Event | Promo bertanggal: NYE dinner, open trip, wedding open house, live music | Tanggal, jam, harga, kuota dari fact sheet (**DATA FINAL**) |
| Post di Group | Menjawab pertanyaan rekomendasi, info event | **Hanya** bila aturan group mengizinkan promosi bisnis; ikuti aturan admin; jangan posting teks identik ke banyak group |
| Rekomendasi (review) Page | Balasan tamu | Pakai [`reply-guest-review`](../../skills/reply-guest-review/SKILL.md); negatif = L3 |

## Struktur Caption yang Disarankan

1. **Baris pertama** (≤ 125 karakter): apa + untuk siapa + kapan. Contoh fiktif: "Paket sarapan keluarga Kafe Contoh Canggu, Sabtu–Minggu 07.00–10.00."
2. **Info praktis**: harga + periode + syarat (net/++), lokasi singkat, cara pesan.
3. **Satu CTA**: link langsung boleh di Facebook (berbeda dengan IG yang lewat bio), atau tombol Page (Kirim Pesan, Pesan Sekarang).
4. **Hashtag 0–3** di akhir: brand + lokasi.

Adaptasi dari caption IG: buang daftar hashtag, pindahkan info praktis ke atas, ganti "link di bio" dengan link langsung atau tombol. Pengecekan mekanis: `python scripts/check_caption.py <file> --platform facebook` (hashtag 1–3, atau tanpa hashtag sama sekali).

## Disclosure & Kolaborasi

- Konten AI → alat pengungkapan AI Meta + rule 07.
- Kolaborasi berbayar/gifting → label paid partnership bila tersedia + teks jelas; approval L3.
- Giveaway → syarat tertulis jelas; jangan mewajibkan share ke timeline atau tag teman (**ASSUMPTION** kebijakan, cek sebelum kampanye).

## Kesalahan Umum

- "Engagement bait" ("ketik AMIN", "like kalau setuju", "tag 5 teman") → jangkauan diturunkan platform dan terkesan murahan.
- Posting silang IG apa adanya: "link di bio" dan 5 hashtag di Facebook.
- Promo di Group tanpa izin admin → dihapus atau akun diblokir dari group.
- Info Page (jam buka, alamat, nomor) beda dengan GBP/OTA (NAP tidak konsisten).
- Membuat akun pribadi palsu untuk mempromosikan Page (AI-CONSTITUTION § 13).

## References

- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [instagram.md](./instagram.md) (posting silang)
- About Meta, "Our Approach to Labeling AI-Generated Content and Manipulated Media" (about.fb.com, Apr 2024, update Sep 2024)
- About Meta, "How Meta Is Preparing for the 2026 US Midterm Elections" (about.fb.com, Feb 2026), bagian pengungkapan AI
- Facebook Help Center / Meta Business Help Center (sumber verifikasi)
