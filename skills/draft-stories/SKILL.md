---
name: draft-stories
description: Draft a 3-5 frame Instagram or Facebook Stories sequence for an Indonesian hospitality client (villa, restaurant, cafe, beach club, wedding venue, tour operator) with one hook, at most one interactive sticker per frame, one CTA, and daily info (menu, availability, opening hours, event) verified for the posting date. Use when the user asks for Stories, a story sequence, or daily story content.
---

# Draft Stories

## Load Required Context

- `../../core/AI-CONSTITUTION.md`
- `../../rules/01-CONTENT-INTEGRITY-STANDARD.md`
- `../../rules/02-HOSPITALITY-CLAIM-STANDARD.md`
- `../../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md`
- `../../rules/05-PLATFORM-STANDARD.md`
- `../../prompts/stories/stories-sequence.md`
- `../../knowledge/platforms/instagram.md` dan `../../knowledge/platforms/facebook.md` (bila Stories juga tayang di Facebook)
- `../../knowledge/voice-guides/hospitality-voice.md`
- `../../agents/agents/personas/story-writer.md` (kartu persona: gaya bahasa, batas & eskalasi)

## Workflow

1. Konfirmasi: client, tanggal & jam tayang (zona WIB/WITA/WIT), tujuan (info harian, engagement, teaser, behind-the-scenes), satu CTA, kanal (IG saja atau IG + Facebook).
2. Ambil fakta dari brief/fact sheet berlabel **DATA FINAL**. Info harian (menu, availability, jam buka, event malam ini) hanya dipakai bila **berlaku pada tanggal tayang**; selain itu **CLIENT CONFIRMATION** dan frame-nya ditahan.
3. Cek aset per frame: ada orang yang bisa dikenali? Consent tercatat? Tanpa consent → aset lain ([rule 04](../../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md)).
4. Susun 3–5 frame: frame 1 = hook; teks ≤ 8 kata per frame; maksimal 1 sticker interaktif per frame; pertanyaan poll/quiz tidak memuat klaim baru.
5. Link sticker hanya ke URL resmi client; bila belum ada tulis `<URL_RESMI>` sebagai blocker publish.
6. Bila tayang juga di Facebook: pastikan tidak ada "link di bio" dan teks tetap terbaca tanpa sticker IG yang tidak tersedia di Facebook.
7. Jalankan self-check.

## Output

- Tabel frame: # | visual (aset) | teks | sticker | klaim (label) | catatan.
- Highlight tujuan (bila disimpan).
- Tabel klaim + daftar blocker publish (URL, consent, info harian yang belum dikonfirmasi).
- Level approval: L1 (info rutin tanpa klaim baru) / L2 (harga, promo, orang).

## Self-Check

1. Setiap info harian berlaku pada tanggal tayang dan berlabel **DATA FINAL**.
2. Teks ≤ 8 kata per frame; hook tanpa emoji bila Voice Card melarang.
3. Maksimal 1 sticker per frame; satu CTA untuk seluruh sequence.
4. Tidak ada wajah tamu/staf tanpa consent; tidak ada data tamu.
5. Tidak ada kelangkaan palsu ("tinggal 1 kamar!") kecuali **DATA FINAL** dari sistem booking pada hari itu.
6. Nada sesuai Voice Card dan kartu persona `story-writer`; tidak menyebut diri AI, tidak mengaku manusia.

## Safety Boundary

- Tidak memposting atau menjadwalkan Stories.
- Tidak membuat availability, menu, atau harga yang tidak dikonfirmasi client untuk hari tayang.
- Tidak me-repost Stories/UGC tamu tanpa izin pemilik akun.

## Exit Criteria

**Pass** bila self-check lulus, blocker publish tercatat, dan level approval tertulis. **Fail** bila ada info harian atau klaim yang tidak **DATA FINAL** untuk tanggal tayang.
