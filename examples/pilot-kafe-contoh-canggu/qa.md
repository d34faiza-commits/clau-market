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
| Review independen | ⬜ Belum (wajib manusia, bukan pembuat draft) |
| Keputusan | Varian A + GBP siap diajukan setelah review independen |

## Temuan pilot

| ID | Temuan | Tindak lanjut |
|---|---|---|
| K-01 | Sebelum fact sheet F&B ada, jam last order, alergen, dan status halal tidak punya tempat baku | **Selesai** — [templates/fnb-fact-sheet.md](../../templates/fnb-fact-sheet.md) |
| K-02 | Brief tidak bisa menandai "halal" sebagai klaim berisiko selain lewat forbidden_terms | Cukup: label RISK di `claims` + `forbidden_terms` |
