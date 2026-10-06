# CLAUDE.md — clau-ai-marketing

> Peta repo untuk AI agent. Baca file ini dulu sebelum menjelajah repo. Last updated: 2026-10-06

## 1. Identitas

| Item | Nilai |
|---|---|
| Repo | `d34faiza-commits/clau-ai-marketing` (private) |
| Peran | Pilar 1 — Marketing & Content untuk hospitality Indonesia |
| Submodule | `core/` → clau-ai-core · `agents/` → clau-ai-agents (`agents/core/` ikut pin agents) |
| Default branch | `main` |

## 2. Peta File

| Path | Fungsi |
|---|---|
| `CONTENT-WORKFLOW.md` · `AGENTS.md` | Workflow konten 9 langkah · instruksi agent Pilar 1 (v1.0.0 Approved) |
| `rules/01–09` | Standard konten (integritas, klaim, voice, privacy, platform, bahasa, AI visual, approval, data) |
| `skills/` · `prompts/` | 7 skill agent · prompt library |
| `knowledge/` | Segment, platform, kalender, destinasi, voice guide, market, regulasi |
| `templates/` · `schemas/` | Template brief/fact sheet/approval · `content-brief.schema.json` (v1.3) |
| `qa/` | Claim verification (per kalimat), content review, privacy, visual AI, publication, scoring rubric |
| `examples/` | Pilot **fiktif** (SIMULASI). Nama properti fiktif wajib mengandung "Contoh" |
| `scripts/` | `validate.py`, `check_caption.py`, `sync-submodules.sh`, `check-core-pins.sh` |
| `SUBMODULE.md` | Update, sync, troubleshooting submodule & setup token Actions |

## 3. Command

```bash
git submodule update --init --recursive
python scripts/validate.py --require-submodules
python scripts/check_caption.py --markdown <file> --brief <brief.json>   # hasil: PASS (mekanis), bukan lulus QA
scripts/sync-submodules.sh --dry-run
```

Jangan mengedit file di `core/` atau `agents/`; edit di repo aslinya.

## Aturan Kerja untuk Agent

- Baca `AGENTS.md` (instruksi agent) dan, untuk aturan induk, `core/AI-CONSTITUTION.md` + `core/AI-BOUNDARY.md`.
- **Otoritas perubahan:** dokumen berstatus Approved hanya diubah atas perintah **Pak Indra** atau **Dea Karisna (d34faiza)**.
- AI **tidak** publish, kirim ke pihak luar, atau self-approve. Review independen L2/L3 = manusia.
- **Jangan** commit data client nyata (brief, fact sheet, caption, harga, foto, data tamu), `.env`, atau credential. Data client nyata ada di Client Workspace (Drive), bukan repo.
- Label evidence dipakai persis: `DATA FINAL`, `ASSUMPTION`, `CLIENT CONFIRMATION`, `FIELD VERIFICATION`, `RISK`, `NEXT ACTION`.
- Commit message: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`, `test:`. Jalankan validator sebelum push.
