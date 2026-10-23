---
name: draft-caption
description: Draft on-brand social media captions (Instagram feed/carousel/Reels, TikTok, Facebook) for Indonesian hospitality businesses — villas, hotels, restaurants, cafes, beach clubs, spas — with verified claims, one clear CTA, and a claim table. Use when the user asks for a caption, post copy, or Reels/TikTok text for a hospitality client.
---

# Draft Caption

## Load Required Context

Baca sebelum bekerja:

- `../../core/AI-CONSTITUTION.md`
- `../../rules/01-CONTENT-INTEGRITY-STANDARD.md`
- `../../rules/02-HOSPITALITY-CLAIM-STANDARD.md`
- `../../rules/03-CLIENT-BRAND-VOICE-STANDARD.md`
- `../../rules/05-PLATFORM-STANDARD.md`
- `../../knowledge/voice-guides/hospitality-voice.md`
- `../../knowledge/voice-guides/humanize-copy.md` (copy jelas dulu baru indah, singkat, elegan; psikologi persuasi yang jujur)
- `../../knowledge/platforms/instagram.md`, `../../knowledge/platforms/tiktok.md`, atau `../../knowledge/platforms/facebook.md` sesuai channel
- `../../prompts/caption/draft-instagram-caption.md`

## Workflow

1. Pastikan input minimum: brand, vertical, lokasi umum, Voice Card, topik/visual, objective, CTA, bahasa. Voice Card diambil dari field `voice` di brief (arketipe, kata sifat, "bukan", sapaan, emoji) plus `restrictions` (kata wajib/terlarang). Bila `voice.evidence_label` = **CLIENT CONFIRMATION**, pakai arketipe di brief dan catat di output bahwa voice belum disetujui client. Input lain yang kurang → tanya, atau tandai **CLIENT CONFIRMATION**.
2. Daftar fakta yang boleh dipakai; hanya **DATA FINAL**.
3. Cek segment knowledge vertical (`../../knowledge/segments`) untuk angle konten yang relevan.
4. Tulis hook sensory dan spesifik di baris pertama.
5. Buat 3 varian (storytelling, informatif, conversational) sesuai Voice Card.
6. Tambahkan 1 CTA dan 3–5 hashtag relevan (Instagram menerima maks 5 hashtag per post/Reels sejak 18 Des 2025; lihat [instagram.md](../../knowledge/platforms/instagram.md)). Untuk **Facebook**: info praktis di 125 karakter pertama, link langsung boleh, hashtag 0–3 ([facebook.md](../../knowledge/platforms/facebook.md)); jangan menyalin caption IG apa adanya.
7. Tulis alt text **per gambar/slide** (carousel 5 slide = 5 alt text), deskriptif, tanpa hashtag.
8. Isi tabel klaim, termasuk **klaim tersirat**: baca ulang setiap varian kalimat per kalimat dan catat semua gambaran pengalaman (view, jarak, suasana, kapasitas) sebagai klaim. Lalu jalankan self-check.

## Output

- 3 varian caption, masing-masing dalam code block terpisah.
- Alt text per gambar/slide.
- Hasil `python scripts/check_caption.py --markdown <file> --brief <brief.json>` (bila dijalankan).
- Tabel klaim: Klaim | Label | Sumber.
- Data gap (**CLIENT CONFIRMATION** / **FIELD VERIFICATION**) + **NEXT ACTION**.
- Level approval yang dibutuhkan (L1/L2/L3).

## Self-Check

1. Setiap klaim di caption ada di tabel klaim dengan label **DATA FINAL**.
2. Tidak ada superlatif tanpa bukti, klise AI, klaim halal/bintang/medis tanpa bukti.
3. Harga (bila ada) lengkap: Rp, unit, periode, syarat, net/++.
4. Hanya 1 CTA.
5. Tidak ada nama/foto tamu tanpa consent.
6. Konten berbayar → disclosure tercantum.
7. Klaim tersirat ikut dicek: setiap kalimat yang menggambarkan apa yang *akan dialami* tamu (view, jarak/waktu tempuh, suasana sepi/ramai, kapasitas, kecepatan, kebersihan, "bisa lihat X dan Y sekaligus") dicatat sebagai klaim di tabel klaim dan harus **DATA FINAL**; kalau tidak, kalimatnya dihapus atau diubah. Contoh pilot: "view sawah dan kolam dua-duanya kelihatan" adalah klaim view yang butuh foto bukti. Kalimat pembuka suasana juga dihitung: "ombak pagi sudah menunggu" atau CTA "buat pagi sebelum surf" menyiratkan lokasi dekat pantai, dan "pagi yang tenang" menyiratkan suasana sepi — keduanya klaim (review independen pilot Kafe Contoh Canggu, 2026-10-09). Klaim view atau layout ("laut di belakang Anda", "satu meja panjang") butuh baris fact sheet; kapasitas pembanding selalu dengan jenis layout (pilot Wedding). Syarat keselamatan di fact sheet (bisa berenang, level fisik) dan kondisi itinerary (spot bisa diganti, berangkat bila kuota minimum terpenuhi) wajib ikut ditulis, bukan dihilangkan (pilot Trip Labuan Bajo). Revisi atas temuan diterapkan ke **semua kanal & bahasa** di draft (IG, GBP, TikTok, Varian EN), dan terjemahan nama area/fasilitas tidak boleh menambah klaim ("Cliff Lawn" = rumput, "Hall" = ruang tertutup) — pakai nama asli + deskripsi dari fact sheet (cek ulang v2, 2026-10-09).
8. Hook (baris pertama) ≤125 karakter; alt text ada untuk setiap gambar/slide.
9. Tidak ada kata positioning tanpa dasar (mewah/luxury/premium/eksklusif/5-star) dan tidak ada kalimat yang memperkuat klaim tersirat dari nama brand (rule 02).
10. Lulus 5 tes di [humanize-copy.md § 5](../../knowledge/voice-guides/humanize-copy.md#5-rumus-singkat-dan-tes): paham sekali baca, baca keras, tukar nama, kata besar, jujur. Jelas dulu, baru indah: tidak ada kalimat puitis yang membuat tamu menebak. Detail yang terdengar seperti cerita harus ada di fact sheet/foto/catatan staf.

## Safety Boundary

- Tidak publish, schedule, atau boost.
- Tidak mengarang fasilitas, harga, rating, testimoni.
- Tidak menyebut kompetitor.
- Tidak memproses credential atau data pribadi tamu.

## Exit Criteria

**Pass** bila self-check lulus semua, `scripts/check_caption.py` lulus mekanis (hook ≤125 karakter, hashtag 3–5, tanpa kata positioning/terlarang, satu CTA sesuai `--expect-cta` dari brief), dan open items tercatat. **Fail** bila ada klaim non-**DATA FINAL** di teks caption, termasuk klaim tersirat. Klaim tersirat yang belum **DATA FINAL** tidak boleh hanya diberi tanda ⚠️: **ubah atau hapus kalimatnya sebelum diserahkan**. Kalau masih ada saat diserahkan = **Fail**.
