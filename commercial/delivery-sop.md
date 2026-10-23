# SOP Delivery Bulanan — Paket Konten Pilar 1

> **Status:** **Approved v1.0.0 (2026-10-23)**: owner Dea Karisna (d34faiza) menjawab paket keputusan TASK-067 K1–K8 "setuju semua". Menjalankan paket di [katalog](./service-catalog.md) dengan alur yang sudah berlaku: [CONTENT-WORKFLOW](../CONTENT-WORKFLOW.md) 9 langkah + [automation level 1](../automations/level-1-manual/README.md) (manual, AI lewat chat/agent). Berlaku sampai platform CLAU AI dipakai klien (server hidup, provider AI nyata, domain; TASK-065, TASK-052, TASK-047).

## 1. Peran

| Peran | Siapa | Tugas | Tidak boleh |
|---|---|---|---|
| Content lead (CLAU) | Manusia | Brief, menjalankan skill, QA klaim & privasi, kirim paket approval, laporan | Menyetujui atas nama klien; me-review draft buatannya sendiri sebagai review independen L2/L3 |
| Reviewer independen (CLAU) | Manusia lain atau owner | Claim verification L2/L3 ([rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md)) | — |
| AI | Agent/chat dengan skill repo | Draft, tabel klaim, self-check | Publish, approve, menerima password atau data tamu mentah |
| Approver klien | Sesuai approval matrix | Setuju/revisi tertulis | — |
| Publisher | Klien, atau CLAU (add-on) lewat akses partner | Menjadwalkan konten yang sudah disetujui | Mengubah konten setelah approval tanpa approval ulang |

Draft dari AI yang diperiksa content lead manusia dihitung **independen** (rule 08). Untuk L2/L3, bila content lead ikut menulis ulang drafnya, review klaim dilakukan orang lain.

## 2. Siklus Bulanan

| Kapan | Kegiatan | Rujukan | Keluaran |
|---|---|---|---|
| Tgl 10–15 | Cek ulang fact sheet & promo bulan depan dengan PIC klien | [fact sheet](../templates/property-fact-sheet.md) | Fakta baru dikonfirmasi |
| Tgl 15–20 | Kalender bulan depan (`build-content-calendar`), tanggal dari [kalender 2027](../knowledge/calendar-id/national-holidays-2027.md) | [skill](../skills/build-content-calendar/SKILL.md) | Kalender dikirim ≤ tgl 20 |
| Tgl 20–25 | Approval kalender oleh klien | [approval record](../templates/approval-record.md) | Kalender disetujui |
| Bila ada momen besar | Rencana kampanye (`plan-seasonal-campaign`) sesuai tabel lead time kalender | [skill](../skills/plan-seasonal-campaign/SKILL.md) | Rencana kampanye L2/L3 |
| Hari kerja ke-5 bulan berikutnya | Laporan bulanan, angka dari insight platform apa adanya | [monthly-report](../templates/monthly-report.md) | Laporan terkirim |

## 3. Siklus Mingguan

| Hari | Kegiatan | Keluaran |
|---|---|---|
| Kamis–Jumat | Draft batch minggu depan: caption, naskah Reels, stories, GBP (skill sesuai intent), versi EN bila paket bilingual (`localize-content`) | Draft + tabel klaim |
| Jumat | `python scripts/check_caption.py --markdown <draft> --brief <brief.json>` lalu QA gate: [claim verification](../qa/claim-verification.md), [content review](../qa/content-review.md), [privacy](../qa/privacy-rights-review.md), [visual AI](../qa/visual-ai-review.md) bila ada | Pass / Conditional / Fail |
| Senin | Kirim paket approval (draft final, visual, kanal, jadwal, tabel klaim, open items) | Approval record dibuka |
| Senin–Rabu | Revisi (maks 2 putaran) → approval tertulis | Approval record ditutup |
| Sesuai jadwal | Publikasi oleh manusia + [publication checklist](../qa/publication-checklist.md) | URL + log publikasi |

## 4. Harian: Review Tamu

1. Kumpulkan review baru (Google + OTA dalam paket); samarkan nama/kamar/tanggal/booking sebelum ditempel ke AI.
2. Draft balasan dengan [`reply-guest-review`](../skills/reply-guest-review/SKILL.md).
3. Rating ≥ 4 rutin: L1 (template yang disetujui klien boleh dipakai). Rating ≤ 3, keluhan keselamatan/kesehatan/hukum: **L3**, kirim ke owner/GM klien dengan ringkasan, jangan dibalas sebelum disetujui.
4. Catat jumlah per bulan untuk kuota paket.

## 5. Kapasitas

Batas jumlah klien = jam reviewer manusia. Perkiraan awal (**ASSUMPTION**, diukur ulang setelah 2 bulan klien pilot):

| Paket | Jam kerja manusia per bulan (setup tidak termasuk) |
|---|---|
| Esensial | ±10 jam |
| Growth | ±18 jam |
| Signature | ±30 jam |
| Setup (sekali) | ±8 jam |

Satu content lead penuh waktu (±120 jam produktif/bulan) ≈ contoh campuran: 4 Esensial + 2 Growth + 1 Signature. Klien baru tidak diterima bila jam terjadwal > 85% kapasitas (TASK-059 SOP tim).

## 6. Mutu

| Ukuran | Target | Cara cek |
|---|---|---|
| Konten tayang dengan klaim tanpa fact sheet | 0 | Sampling 5 konten/bulan oleh reviewer independen |
| Konten tayang tanpa approval tertulis | 0 | Approval record vs log publikasi |
| Skor rubrik rata-rata | ≥ 85 ([rubrik](../qa/scoring-rubric.md)) | Sampling bulanan |
| Ketepatan SLA (kalender, batch, balasan review) | ≥ 90% | Log tanggal kirim |

## 7. Insiden (konten salah tayang)

1. Klien atau tim melapor → content lead menilai: salah fakta, privasi, atau sensitif.
2. ≤ 4 jam kerja: draft koreksi atau permintaan penurunan ke publisher; privasi (wajah tanpa consent, data tamu) = turunkan dulu, jelaskan kemudian.
3. ≤ 2 hari kerja: catatan insiden (apa, kenapa lolos, perbaikan aturan/skill) di Client Workspace; aturan atau skill yang perlu diubah → PR ke repo ini.
4. Data pribadi bocor → ikuti [Lampiran C § 3](./data-processing-addendum.md#3-kewajiban-penyedia) (beri tahu klien ≤ 24 jam).

## 8. Offboarding

1. Serahkan konten final yang sudah dibayar + kalender yang belum tayang.
2. Klien mencabut akses partner; CLAU konfirmasi akses sudah tidak dipakai.
3. Kembalikan lalu hapus data klien ≤ 30 hari ([Lampiran C § 6](./data-processing-addendum.md#6-retensi--pengakhiran)).
4. Minta izin tertulis bila hasil kerja akan dipakai sebagai case study (TASK-062).

## 9. Realita Lapangan (cara menanganinya)

Klien hospitality Indonesia jarang bekerja seperti di template. Yang paling sering terjadi, dan cara CLAU menanganinya tanpa melanggar rules:

| Situasi nyata | Cara menangani | Dasar |
|---|---|---|
| Approval lewat **WhatsApp** ("ok kak", stiker 👍, voice note) | Sah sebagai approval tertulis **bila** membalas pesan yang memuat versi spesifik (nomor/tanggal batch + teks/visual). Screenshot + ekspor chat disimpan di approval record. Voice note: tulis ulang isinya dan minta "ok" tertulis | [Rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md) (approval tertulis & dapat ditelusuri) |
| Klien lambat membalas approval | Pengingat H+1 (sopan, satu pesan). Lewat 2 hari kerja → jadwal tayang mundur; kuota tidak hangus. Jangan pernah posting "karena sudah lama tidak dijawab" | Katalog § 6, kontrak Pasal 2.4 |
| "Besok posting promo ya kak" (mendadak) | Dikerjakan bila fakta promo lengkap (harga, periode, syarat) dan approver L2 bisa dihubungi hari itu. Kalau tidak, tawarkan versi tanpa harga ("info promo segera") | Rule 02, rule 08 |
| Harga/promo berubah setelah konten disetujui | Konten yang belum tayang ditahan; konten yang sudah tayang diedit atau ditambah koreksi; fact sheet dinaikkan versinya | Rule 02, SOP § 7 |
| Foto dari HP, gelap, atau sedikit | Pilih yang terbaik + brief foto sederhana untuk staf (cahaya pagi, horizontal untuk feed, vertikal untuk Reels). **Tidak** "memperbaiki" dengan AI sampai mengubah fakta (ukuran kamar, view, porsi) | Rule 07 |
| Klien mengirim data tamu mentah di WA (nama, nomor, foto KTP, bukti transfer) | Jangan diteruskan ke AI; minta klien menghapus dari chat kerja; hapus salinan di perangkat CLAU; samarkan bila memang dibutuhkan untuk balasan review | Rule 04, Lampiran C § 2 |
| Owner/GM klien sulit dihubungi untuk L3 (review negatif) | Draft siap ≤ 1 hari kerja; tanpa approval L3, review **tidak dibalas** (lebih baik terlambat daripada salah). Tawarkan approver L3 cadangan di onboarding | Rule 08 |
| Klien minta "pakai foto villa sebelah dulu" / foto stok seolah milik sendiri | Tolak dengan sopan; tawarkan foto detail yang ada atau ilustrasi berlabel | Rule 01, rule 07 |
| Content lead CLAU sakit/cuti | Klien diberi tahu ≥ 3 hari kerja sebelumnya untuk cuti; batch dikerjakan lebih awal; sakit mendadak → owner mengambil alih atau jadwal mundur dengan pemberitahuan hari itu juga. Tidak ada AI yang "jalan sendiri" saat manusia tidak ada | SOP § 1, § 5 |
| Libur panjang (Lebaran, Nyepi, Nataru) = momen paling ramai klien | Batch kampanye dikunci sebelum libur (lihat tabel lead time di [kalender 2027](../knowledge/calendar-id/national-holidays-2027.md) § D); selama libur hanya balasan review yang dijadwalkan dan konten yang sudah disetujui | Kalender 2027 |
| Pembayaran terlambat | Pengingat sopan H+3; lewat 14 hari → pemberitahuan tertulis lalu penangguhan (kontrak Pasal 4.4). Konten yang sudah disetujui tetap diserahkan | Kontrak Pasal 4 |
| Klien membandingkan dengan "AI Rp 1 juta 28 post" | Jelaskan bedanya tanpa menjelekkan kompetitor: cek klaim, privasi tamu, approval, kalender Indonesia, balasan review | [competitor-content-agencies.md](../knowledge/market/competitor-content-agencies.md), AI-CONSTITUTION § 13 |

Catat setiap situasi baru yang tidak ada di tabel ini di Client Workspace; bila terjadi dua kali, tambahkan barisnya lewat PR.
