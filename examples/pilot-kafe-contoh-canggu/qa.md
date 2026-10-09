# QA & Approval — Kafe Contoh Canggu (SIMULASI)

> **Self-review oleh AI agent** (AI-CONSTITUTION §11) — pre-check, **bukan** review independen. Approval di bawah = **SIMULASI**.

## Claim verification (per kalimat, Varian A)

| # | Kalimat | Klaim | Label | Sumber | Hasil |
|---|---|---|---|---|---|
| 1 | Ombak pagi sudah menunggu, kopinya juga | Suasana, bukan klaim fakta spesifik | — | — | OK |
| 2 | Kafe Contoh Canggu buka 06.30 setiap hari | Jam buka | DATA FINAL | Fact sheet v1 §2 | OK |
| 3 | Paket Pagi Rp65.000++ per orang: kopi arabika Kintamani + pilihan sarapan | Harga, isi paket, origin kopi | DATA FINAL | Fact sheet v1 §4, §6 | OK |
| 4 | termasuk 2 menu tanpa daging | Dietary | DATA FINAL | Menu v3 | OK |
| 5 | Berlaku 06.30–09.00, 1–30 November, dine-in | Syarat & periode | DATA FINAL | Fact sheet v1 §4 | OK |
| 6 | Simpan post ini buat pagi sebelum surf | CTA | — | — | OK |

## Content review

| Cek | Hasil |
|---|---|
| Voice `santai-playful`, sapaan "kamu" | ✅ (sapaan tersirat) |
| Emoji ≤ 2 | ✅ 1 |
| `python scripts/check_caption.py --markdown examples/pilot-kafe-contoh-canggu/drafts.md --brief examples/pilot-kafe-contoh-canggu/brief.json` | PASS (mekanis) |
| Pajak: "++" disebut tanpa persentase | ⚠️ Conditional — persentase PB1/service masih CLIENT CONFIRMATION; boleh tayang dengan "++" sesuai rule 02 harga |

## Privacy & rights

| Cek | Hasil |
|---|---|
| Aset KCC-MEDIA-011 kategori A, tanpa orang | ✅ |

## Approval (SIMULASI)

| Field | Isi |
|---|---|
| Mode | **SIMULASI** |
| Level | L2 (ada harga/promo) |
| Review independen | ✅ 2026-10-09 — lihat [Review Independen](#review-independen-2026-10-09) (v1 belum lulus) |
| Keputusan | Varian A + GBP siap diajukan setelah review independen |

## Review Independen (2026-10-09)

| Field | Isi |
|---|---|
| Reviewer | **Dea Karisna (d34faiza)**, owner — bukan pembuat draft (draft dibuat AI agent) |
| Metode | AI agent menyusun **pre-review kritis** atas draft-nya sendiri (bukan review independen); reviewer membaca dan menyatakan **"setuju"** di sesi Claude Code 2026-10-09. Penilaian akhir = reviewer |
| Objek | Varian A v1 (IG). Temuan #1 dan #3 juga berlaku untuk Varian B (EN: "dawn patrol", "early surf", "Kintamani arabica") — Varian B harus direvisi dengan pola yang sama sebelum dipakai |
| Keputusan | **Belum lulus — revisi kecil.** v2 di [drafts.md](./drafts.md) |

| # | Kalimat (v1) | Hasil | Catatan |
|---|---|---|---|
| 1 | Ombak pagi sudah menunggu, kopinya juga | ❌ | Klaim lokasi **tersirat** (dekat ombak); jarak ke pantai masih FIELD VERIFICATION. Lolos self-check agent |
| 2 | …buka 06.30 setiap hari | ✅ | |
| 3 | …kopi arabika Kintamani… | ❌ | "arabika" tidak ada di fact sheet (hanya di brief) |
| 4 | …termasuk 2 menu tanpa daging | ✅ | Catatan: "tanpa daging" ambigu (telur/seafood?) — perjelas di menu |
| 5 | Berlaku 06.30–09.00, 1–30 November, dine-in | ✅ | |
| 6 | Simpan post ini buat pagi sebelum surf | ⚠️ (CTA, bukan klaim) | Memperkuat klaim tersirat #1 |

| Pertanyaan | Jawaban reviewer |
|---|---|
| B1 Pelanggaran rule | Ya: klaim lokasi tersirat (Medium), "arabika" tanpa sumber (Low) |
| B2 Sesuai brief | Ya |
| B3 "tanpa daging" terbaca halal? | Tidak |
| B4 "++" tanpa persentase | Boleh; lebih baik dijelaskan "(belum termasuk pajak & service)" |

### Record (qa/scoring-rubric)

| Versi | Penghitung | Status | A | B | C | D | Total | Kesiapan | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| v1 | Dea Karisna (owner) atas pre-review AI | Independent score | 60 | 89 | 100 | — | 83 | **0** (blocker: klaim tersirat non-DATA FINAL) | A = 3 dari 5 kalimat klaim OK tanpa perubahan (#2, #4, #5); B = 100 − 8 − 3; D tidak dihitung (publication checklist belum dijalankan di pilot ini); total = rata-rata A–C. Self-check agent sebelumnya "lulus" → selisih dengan self-score = temuan K-03 |
| v2 | — | Menunggu cek ulang reviewer | | | | | | | Revisi atas semua temuan v1 |

## Temuan pilot

| ID | Temuan | Tindak lanjut |
|---|---|---|
| K-01 | Sebelum fact sheet F&B ada, jam last order, alergen, dan status halal tidak punya tempat baku | **Selesai** — [templates/fnb-fact-sheet.md](../../templates/fnb-fact-sheet.md) |
| K-02 | Brief tidak bisa menandai "halal" sebagai klaim berisiko selain lewat forbidden_terms | Cukup: label RISK di `claims` + `forbidden_terms` |
| K-03 | Review independen: kalimat pembuka suasana ("ombak pagi") dan CTA ("sebelum surf") menyiratkan lokasi yang belum DATA FINAL, tetapi lolos self-check agent | **Selesai** — contoh ditambahkan di self-check `skills/draft-caption` (#7) |
| K-04 | Kata di brief ("arabika") tidak ada di fact sheet | Brief diperbaiki; aturan: klaim brief harus sama persis dengan fact sheet |
