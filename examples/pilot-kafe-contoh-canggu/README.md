# Pilot — Kafe Contoh Canggu (FIKTIF)

> **Outlet fiktif, SIMULASI.** Vertical fokus restoran/cafe (AI-CONSTITUTION v3.0.0 §2). Tidak ada data client nyata ([AI-BOUNDARY.md](../../core/AI-BOUNDARY.md)).

## Tujuan

Menguji alur [CONTENT-WORKFLOW.md](../../CONTENT-WORKFLOW.md) untuk vertical F&B dengan [fact sheet F&B](../../templates/fnb-fact-sheet.md) baru: promo dengan harga, klaim dietary, dan risiko kata "halal".

## Isi

| File | Langkah |
|---|---|
| [brief.json](./brief.json) | Brief schema v1.4 (dicek validator) |
| [fact-sheet.md](./fact-sheet.md) | Fakta outlet (template F&B) |
| [drafts.md](./drafts.md) | 2 caption IG (ID/EN) + update GBP |
| [qa.md](./qa.md) | Claim check per kalimat, content review, approval **SIMULASI** |

## Hasil Ringkas

| Langkah | Hasil |
|---|---|
| Brief | ✅ Valid schema |
| Klaim | ✅ 7 klaim berlabel; 3 ditahan (jarak, pajak %, halal) |
| Draft | ✅ 2 caption + 1 GBP |
| QA mekanis | ✅ PASS (`check_caption`) |
| Review independen | ✅ 2026-10-09 oleh Dea Karisna (owner): v1 **belum lulus** (klaim lokasi tersirat, "arabika" tanpa sumber) → **v2 lulus** (cek ulang 2026-10-09) |
| Approval | SIMULASI |

Dijalankan 2026-10-09 oleh AI agent (Claude Code). Review owner tetap diperlukan untuk menerima temuan.
