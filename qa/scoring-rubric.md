# QA — Scoring Rubric

## Purpose

Skor konten/pilot harus bisa **diaudit**: orang lain yang memegang file yang sama harus mendapat angka yang sama. Karena itu setiap dimensi dihitung dari **hitungan** di record QA, bukan angka bebas. Rubrik ini menggantikan skor tanpa kriteria yang dipakai di pilot 2 v1/v2 (temuan S-04 di [review adversarial pilot 2](../examples/pilot-2/ADVERSARIAL-REVIEW.md)).

## Required Inputs

- [Tabel Ekstraksi Kalimat](./claim-verification.md#tabel-ekstraksi-kalimat) untuk **semua** konten versi ini.
- Checklist [content review](./content-review.md) (termasuk "Kecocokan dengan Brief") per konten.
- [Publication checklist](./publication-checklist.md).
- Daftar pelanggaran rule (dari reviewer mana pun), dengan severity.

## Dimensi

| Kode | Dimensi | Rumus | Sumber hitungan |
|---|---|---|---|
| A | Integritas klaim | 100 × (baris ekstraksi berhasil **OK** tanpa perubahan ÷ total baris) | Tabel Ekstraksi Kalimat |
| B | Kepatuhan rule | max(0, 100 − Σ penalti); penalti per pelanggaran: High 15, Medium 8, Low 3 | Daftar pelanggaran |
| C | Kecocokan brief | 100 × (item "Kecocokan dengan Brief" Pass ÷ item yang berlaku), dirata-rata per konten | Content review |
| D | Kelengkapan deliverable | 100 × (item publication checklist terpenuhi ÷ item yang berlaku). Item yang **sengaja** gagal di Mode SIMULASI (approval nyata, review independen) dihitung N/A | Publication checklist |

**Skor total** = rata-rata A–D, dibulatkan ke bilangan bulat.

Catatan untuk A: baris yang lolos **setelah diubah** pada versi yang sama tidak dihitung OK. Skor A mengukur draft yang diserahkan creator, bukan draft setelah reviewer memperbaikinya.

## Status Review (bukan skor, tapi membatasi skor)

| Status | Syarat | Batas |
|---|---|---|
| **Self-score** | Hanya pembuat draft (AI atau creator) yang menghitung | Ditulis "self-score". Kesiapan client nyata maks **60** |
| **Independent score** | Minimal satu reviewer independen ([rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md)) menghitung ulang dari file yang sama, memakai [lembar kerja](./independent-review-worksheet.md) | Tanpa batas. Selisih > 5 poin dengan self-score dicatat sebagai temuan |

## Kesiapan Client Nyata

Kesiapan **bukan** rata-rata. Ambil nilai **terendah** dari:

| Syarat | Nilai bila belum terpenuhi |
|---|---|
| Review independen sudah ada | 60 |
| Spec platform terverifikasi (bukan **ASSUMPTION**) | 70 |
| Knowledge yang dipakai sudah direview manusia | 70 |
| Semua klaim di konten publish **DATA FINAL** | 0 (blocker) |
| Semua syarat di atas terpenuhi | Skor total |

## Record

| Versi | Penghitung | Status | A | B | C | D | Total | Kesiapan | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| | | Self-score / Independent | | | | | | | |

Simpan semua hitungan (jumlah baris, jumlah pelanggaran, item checklist) di record QA versi itu supaya angka bisa dicek ulang.
