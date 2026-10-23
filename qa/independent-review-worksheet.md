# QA — Lembar Kerja Review Independen (manusia)

## Purpose

Memandu reviewer **manusia** (owner atau content lead yang tidak menulis draft) menghitung ulang skor sebuah pilot atau konten dengan [rubrik](./scoring-rubric.md), dalam ±60–90 menit. Hasilnya mengangkat batas "Kesiapan client nyata" dari 60 (self-score) ke skor yang sebenarnya. Dipakai pertama kali untuk TASK-028 (pilot 2 v3).

**Aturan keras:** lembar ini disiapkan AI, tapi **semua kolom diisi manusia**. AI tidak boleh mengisi skor, centang, atau "Setuju" di sini; bila AI mengisi, hasilnya self-review ([rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md)). Jangan membuka § 7 (self-score) file pilot sebelum langkah 5 supaya tidak terpengaruh.

## Required Inputs

- File pilot, mis. [examples/pilot-2/v3.md](../examples/pilot-2/v3.md) § 1–6 (drafts, tabel ekstraksi, content review, output `check_caption`, publication checklist).
- Brief & fact sheet pilot (folder pilot yang sama).
- [claim-verification.md](./claim-verification.md), [content-review.md](./content-review.md), [publication-checklist.md](./publication-checklist.md), [scoring-rubric.md](./scoring-rubric.md).

## Langkah

| # | Langkah | Waktu | Catatan |
|---|---|---|---|
| 1 | Baca brief + fact sheet. Tandai 5 fakta yang paling sering muncul di draft | 10 mnt | |
| 2 | **Dimensi A:** baca draft yang dipilih untuk publish kalimat per kalimat. Untuk setiap kalimat, tanya: "Kalau tamu membaca ini lalu datang, apakah ada yang bisa tidak sesuai?" Cocokkan dengan tabel ekstraksi di file pilot; tulis kalimat yang **terlewat** atau yang statusnya menurut Anda salah | 25 mnt | Klaim tersirat (suasana, jarak, view, "cocok untuk…") dihitung |
| 3 | **Dimensi B:** catat pelanggaran rule yang Anda temukan sendiri + severity (High 15 / Medium 8 / Low 3) | 10 mnt | Termasuk hashtag > 5 di IG, CTA ganda, kata terlarang |
| 4 | **Dimensi C & D:** cek ulang item "Kecocokan dengan Brief" dan publication checklist; N/A hanya untuk item yang memang tidak berlaku di Mode SIMULASI | 15 mnt | |
| 5 | Hitung skor dengan rumus rubrik, **lalu** buka self-score file pilot dan bandingkan | 10 mnt | Selisih > 5 poin = temuan |
| 6 | Tulis 3 hal yang akan Anda ubah sebelum konten seperti ini dikirim ke klien nyata | 5–10 mnt | Ini yang paling berharga untuk perbaikan skill |

## Tabel 1 — Kalimat yang terlewat / salah status (Dimensi A)

| # | Kalimat (kutip) | Masalah | Status yang benar | Severity |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Baris ekstraksi file pilot: total ___ · menurut Anda OK tanpa perubahan ___ → A = 100 × ___ ÷ ___ = ___

## Tabel 2 — Pelanggaran rule (Dimensi B)

| # | Rule | Lokasi | Severity | Penalti |
|---|---|---|---|---|
| 1 | | | | |

B = max(0, 100 − Σ penalti) = ___

## Tabel 3 — Brief & publication (Dimensi C, D)

| Dimensi | Item Pass | Item berlaku | Skor |
|---|---|---|---|
| C. Kecocokan brief | | | |
| D. Kelengkapan deliverable | | | |

## Hasil

| Field | Isi |
|---|---|
| Reviewer (nama, peran) | |
| Tanggal | |
| Independen? | Ya — bukan pembuat draft / Tidak |
| A / B / C / D | ___ / ___ / ___ / ___ |
| **Independent score** (rata-rata, dibulatkan) | |
| Self-score di file pilot | |
| Selisih (> 5 = temuan) | |
| Kesiapan client nyata (nilai terendah tabel rubrik) | |
| 3 perubahan sebelum klien nyata | 1. 2. 3. |
| Waktu yang benar-benar dipakai | ___ menit (untuk mengoreksi kapasitas di [delivery-sop](../commercial/delivery-sop.md#5-kapasitas)) |

## Setelah Selesai

1. Simpan lembar terisi; isinya boleh di-commit ke folder pilot karena data SIMULASI, tanpa data klien nyata.
2. Temuan yang menunjukkan skill/prompt kurang → kartu ClickUp baru atau PR perbaikan skill.
3. Kartu TASK-028 **Closed** bila tabel Hasil terisi oleh manusia dan selisih sudah dicatat.
