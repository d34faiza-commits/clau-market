# Automations

Tingkat otomasi workflow konten clau-content. Naik level hanya kalau level sebelumnya sudah stabil dan kontrol di [AI-CONSTITUTION.md](../core/AI-CONSTITUTION.md) tetap terpenuhi.

| Level | Nama | Siapa yang menjalankan | Status |
|---|---|---|---|
| **1** | [Manual / semi-manual](./level-1-manual/README.md) | Manusia, dibantu AI chat (copy-paste skill & prompt) | **Aktif** |
| 2 | Semi-otomatis | Script/agent menyiapkan draft & checklist; manusia approve dan menekan tombol publish | Planned — butuh kriteria naik level terpenuhi |
| 3 | Terintegrasi | Integrasi API platform/scheduler | Belum direncanakan — butuh revisi Constitution |

## Prinsip yang Berlaku di Semua Level

1. AI **tidak** publish, schedule, boost, atau approve sendiri (Constitution §4, [rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md)).
2. Credential akun platform **tidak pernah** diberikan ke AI tool atau disimpan di repo.
3. Data tamu dan data client tetap di workspace client ([AI-BOUNDARY.md](../core/AI-BOUNDARY.md)).
4. Setiap output tetap melewati [CONTENT-WORKFLOW.md](../CONTENT-WORKFLOW.md) 9 langkah dan QA gate di [qa/](../qa/content-review.md).
