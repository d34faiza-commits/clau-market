# Platform: Google Business Profile (GBP)

## Scope

Profil bisnis di Google Search & Maps: info bisnis, foto, posts/updates, Q&A, dan balasan review. Sangat penting untuk restaurant/cafe/spa (pencarian lokal) dan juga hotel/villa.

> **Spec platform berubah.** Nilai teknis berstatus **ASSUMPTION** sampai diverifikasi ke Google Business Profile Help dengan tanggal akses.

## Spec Teknis

| Item | Nilai kerja | Sumber | Status | Diverifikasi |
|---|---|---|---|---|
| Panjang teks post/update maksimum | 1.500 karakter (konsisten di alat pihak ketiga; tidak ditemukan di Help resmi). Yang terlihat sebelum "Read more" jauh lebih pendek: taruh info inti di ±100 karakter pertama | Pihak ketiga | **ASSUMPTION** | Dicek 2026-10-22 |
| Jenis post | Update, Offer, Event. Offer wajib judul + tanggal/jam berlaku dan otomatis punya tombol "View offer"; Event wajib judul + tanggal & jam mulai/selesai (tanpa jam = dianggap 24 jam) | Google Business Profile Help: Create & manage posts (answer 7342169) | **DATA FINAL** | 2026-10-22 (lewat pencarian; halaman belum dibuka langsung karena network policy) |
| Tombol CTA post | Book, Order, Learn more, Call, dll. | Google Business Profile Help | **ASSUMPTION** | — |
| Kebijakan konten post (mis. nomor telepon di teks) | — | Google Business Profile Help | **CLIENT CONFIRMATION** | — |

## Data Inti (NAP+) — Wajib Konsisten

| Field | Aturan |
|---|---|
| Nama bisnis | Sesuai nama resmi/brand; tanpa keyword stuffing ("Villa X Best Bali Cheap") |
| Alamat & pin | Akurat; cek pin di peta |
| Nomor telepon/WhatsApp | Sama dengan website, IG, OTA |
| Jam buka | Update untuk Ramadan, libur nasional, Nyepi (Bali), renovasi |
| Kategori | Kategori utama yang tepat (Hotel, Restaurant, Day spa, dll.) |
| Atribut | Hanya yang benar (Wi-Fi, outdoor seating, wheelchair accessible) |

Data inti berstatus **DATA FINAL** dari client; perubahan wajib approval L2.

## Posts / Updates

- Fungsi: promo, event, menu baru, info operasional.
- Teks ringkas: apa, kapan, harga (lengkap), cara reservasi.
- Offer post wajib periode & syarat.
- Foto post: foto asli (rule 07 kategori A/B).

## Foto

- Prioritas: eksterior (agar mudah ditemukan), interior, menu/kamar, tim (dengan consent).
- Pantau foto unggahan pengguna; laporkan yang melanggar kebijakan, jangan dihapus sepihak bila tidak bisa.

## Q&A

- Jawab pertanyaan umum dengan fakta **DATA FINAL** (parkir, mushola, kids friendly, reservasi).
- Jangan menjawab dengan klaim yang belum dikonfirmasi.

## Review

- Balas dengan skill [reply-guest-review](../../skills/reply-guest-review/SKILL.md).
- Dilarang meminta review dengan insentif yang melanggar kebijakan Google; dilarang review palsu.

## Kesalahan Umum

- Jam buka tidak diupdate saat libur → tamu datang saat tutup → review negatif.
- Nama bisnis diisi keyword (berisiko suspend).
- Offer post kedaluwarsa masih tampil.
- Nomor telepon beda dengan IG/website.

## References

- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [knowledge/segments/restaurant.md](../segments/restaurant.md)
- Google Business Profile Help (sumber verifikasi)
