# Examples

Contoh dan pilot memakai **properti fiktif**, sesuai [AI-BOUNDARY.md](../core/AI-BOUNDARY.md) (konten yang diizinkan, poin 3).

## Aturan

- Nama properti selalu mengandung kata **"Contoh"** (mis. "Villa Contoh Ubud", "Kafe Contoh Canggu").
- Tidak ada data client nyata, foto asli, nama tamu, harga kontrak, atau credential.
- Approval di contoh selalu ditandai **SIMULASI**.
- Setiap `brief.json` di folder ini divalidasi terhadap [schema](../schemas/content-brief.schema.json) oleh `python scripts/validate.py`.

## Index

| Folder | Isi | Task |
|---|---|---|
| [pilot-villa-contoh-ubud/](./pilot-villa-contoh-ubud/README.md) | Pilot WORKFLOW end-to-end: villa, IG carousel + Booking.com | TASK-012 |
| [pilot-2/](./pilot-2/REPORT.md) | Test end-to-end "otak": villa 5 kamar, IG post + reel + story, scoring; [v2](./pilot-2/v2.md) setelah perbaikan; [v3](./pilot-2/v3.md) setelah review adversarial (QA per kalimat, rubrik skor) | TASK-027 |
| [pilot-kafe-contoh-canggu/](./pilot-kafe-contoh-canggu/README.md) | Vertical fokus restoran/cafe: promo Paket Pagi, klaim dietary, kata "halal" ditahan; [fact sheet F&B](../templates/fnb-fact-sheet.md) | TASK-041 |
| [pilot-wedding-contoh-uluwatu/](./pilot-wedding-contoh-uluwatu/README.md) | Vertical fokus wedding: paket intimate, kapasitas per layout, consent pasangan, legal WNA dihindari; schema v1.4 | TASK-041 |
| [pilot-trip-contoh-labuan-bajo/](./pilot-trip-contoh-labuan-bajo/README.md) | Vertical fokus travel: open trip 3H2M, satwa tidak dijamin, keselamatan nyata, izin operator = syarat tayang | TASK-041 |
