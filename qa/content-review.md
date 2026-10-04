# QA — Content Review

## Purpose

Gate baseline untuk setiap konten sebelum approval: objective, voice, bahasa, budaya, format, dan kelengkapan.

## Hasil

| Status | Arti |
|---|---|
| **Pass** | Semua item wajib terpenuhi |
| **Conditional** | Ada exception terkontrol dengan owner, due date, dan approval tertulis |
| **Fail** | Ada blocker; kembali ke draft |
| **N/A** | Item tidak relevan (alasan dicatat) |

## Required Inputs

- Brief, draft final, Voice Card, tabel klaim, spec platform terverifikasi.

## Checklist

### Objective & Struktur

- [ ] Konten menjawab objective di brief.
- [ ] Satu ide utama, satu CTA.
- [ ] Hook kuat di awal (caption baris 1 / video 3 detik pertama).
- [ ] Info praktis lengkap bila relevan (lokasi, jam, cara booking).

### Brand Voice ([rule 03](../rules/03-CLIENT-BRAND-VOICE-STANDARD.md))

- [ ] Sesuai Voice Card (arketipe, sapaan, emoji).
- [ ] Tidak ada kata terlarang client.
- [ ] Tidak ada klise AI (lihat [hospitality-voice](../knowledge/voice-guides/hospitality-voice.md)).
- [ ] Nama brand/outlet ditulis benar.

### Bahasa & Budaya ([rule 06](../rules/06-LOCALIZATION-BAHASA-STANDARD.md))

- [ ] Ejaan & tata bahasa benar (ID/EN).
- [ ] Bilingual: klaim identik di kedua bahasa.
- [ ] Istilah lokal benar & dijelaskan untuk audiens asing.
- [ ] Tidak ada penggunaan simbol/upacara/agama yang tidak hormat.
- [ ] Tidak ada stereotip atau eksotisasi.

### Platform ([rule 05](../rules/05-PLATFORM-STANDARD.md))

- [ ] Panjang & format sesuai spec terverifikasi.
- [ ] Hashtag relevan, tidak spam.
- [ ] Alt text / subtitle tersedia.
- [ ] Disclosure untuk konten berbayar/kolaborasi.

### Kecocokan dengan Brief (cek ke field brief, bukan ingatan)

- [ ] CTA tiap konten = `channels[].cta.type` untuk channel/format itu, dan hanya **satu** CTA per konten ([rule 05](../rules/05-PLATFORM-STANDARD.md)). Jalankan `python scripts/check_caption.py <caption> --expect-cta <type>` per caption.
- [ ] CTA link/nomor memakai `channels[].cta.target_ref` dari brief.
- [ ] Sapaan (`voice.address`) cocok dengan arketipe (`voice.archetype`) menurut tabel Sapaan di [hospitality-voice](../knowledge/voice-guides/hospitality-voice.md). Bila tidak cocok, kembalikan ke brief (**CLIENT CONFIRMATION**), jangan diputuskan di draft.
- [ ] Segmen yang masih **CLIENT CONFIRMATION** tidak dikunci di konten publish: tidak lewat kalimat ("cocok untuk honeymoon") dan tidak lewat hashtag (#honeymoonbali).
- [ ] `objective.success_metric` bisa diukur dari format yang dipakai (mis. "replies" butuh konten yang mengundang reply; link sticker → link taps).

### Kelengkapan

- [ ] Tabel klaim terlampir.
- [ ] Open items (**CLIENT CONFIRMATION** / **FIELD VERIFICATION**) tercatat.
- [ ] Level approval ditentukan.

## Re-check Penuh per Versi

Setiap versi baru me-review **semua konten**, termasuk yang tidak berubah. "Tidak berubah dari v1 (lolos semua gate)" bukan hasil review.

## Blockers (otomatis Fail)

- Konten tidak sesuai objective atau channel di brief.
- Konten menyinggung agama/adat/SARA.
- Disclosure berbayar tidak ada.
- Lebih dari satu CTA, atau CTA berbeda dari `channels[].cta` di brief tanpa revisi brief.

## Record

| Reviewer | Tanggal | Versi | Hasil | Catatan |
|---|---|---|---|---|
| | | | | |
