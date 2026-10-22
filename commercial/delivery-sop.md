# SOP Delivery Bulanan — Paket Konten Pilar 1

> **Status: Draft (2026-10-22).** Menjalankan paket di [katalog](./service-catalog.md) dengan alur yang sudah berlaku: [CONTENT-WORKFLOW](../CONTENT-WORKFLOW.md) 9 langkah + [automation level 1](../automations/level-1-manual/README.md) (manual, AI lewat chat/agent). Berlaku sampai platform CLAU AI dipakai klien (server hidup, provider AI nyata, domain; TASK-065, TASK-052, TASK-047).

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
