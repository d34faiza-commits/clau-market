# Trip & Operator Fact Sheet — Travel & Tour

> Sumber fakta resmi tour operator/agen untuk semua konten (caption, reel, itinerary publik, listing OTA aktivitas, jawaban inquiry). Satu fact sheet per **operator** + satu bagian per **trip/paket**. Diisi bersama owner saat onboarding dan setiap ada perubahan itinerary, harga, atau syarat. Simpan versi terisi di **workspace client**, jangan di repo ([AI-BOUNDARY.md](../core/AI-BOUNDARY.md)). Contoh fiktif terisi: [pilot Trip Contoh Labuan Bajo](../examples/pilot-trip-contoh-labuan-bajo/fact-sheet.md). Knowledge segment: [travel.md](../knowledge/segments/travel.md).

## Cara Pakai

1. Isi setiap baris dengan nilai **dan** label evidence ([rule 09](../rules/09-DATA-CLASSIFICATION.md)).
2. Hanya baris **DATA FINAL** yang boleh dipakai di konten publish. Satwa, cuaca, dan sunrise/sunset **tidak pernah** dijamin ([rule 02 § Experience](../rules/02-HOSPITALITY-CLAIM-STANDARD.md#experience--aktivitas)).
3. Kolom **Sumber** = itinerary resmi/price list/izin/sertifikat + tanggal; referensi opaque.
4. Baris tidak relevan = `N/A`, jangan dihapus.
5. Setiap perubahan itinerary/harga menaikkan versi; konten dengan nilai lama dicek ulang.

## 0. Dokumen

| Field | Isi |
|---|---|
| Kode client | |
| Versi fact sheet | v1 |
| Tanggal | YYYY-MM-DD |
| Disetujui oleh (peran) | |
| Tipe | tour operator / travel agent / open trip / private tour / aktivitas (surf, dive, trekking, cruise) |

## 1. Operator & Legalitas

| Field | Nilai | Label | Sumber |
|---|---|---|---|
| Nama resmi (penulisan persis) | | | |
| Izin usaha / NIB (referensi, bukan foto dokumen) | | **CLIENT CONFIRMATION** | |
| Lisensi/sertifikat pemandu, kapten, instruktur (jenis + masa berlaku) | | | |
| Asuransi peserta (cakupan ringkas; polis di workspace) | | | |
| Kanal booking resmi — referensi opaque | | | |

## 2. Trip / Paket

Satu blok per trip.

| Field | Nilai | Label | Sumber |
|---|---|---|---|
| Nama trip & kode | | | |
| Durasi (hari/malam) | | | |
| Titik & jam penjemputan | | | |
| Jadwal keberangkatan / tanggal open trip | | | |
| Kuota minimum & maksimum peserta | | | |
| Kebijakan bila kuota minimum tidak terpenuhi (batal/reschedule/refund) | | | |
| Harga (unit: per-pax / per-trip; net / ++) | | | |
| Periode harga berlaku | | | |
| Level fisik (ringan/sedang/berat) & syarat (umur, bisa berenang, sertifikat diving) | | | |
| Bahasa pemandu | | | |

### Itinerary

| Hari | Kegiatan (urut) | Estimasi waktu | Catatan cuaca/alternatif | Label |
|---|---|---|---|---|
| 1 | | | | |

### Termasuk / Tidak Termasuk

| Item | Termasuk? | Catatan | Label |
|---|---|---|---|
| Transportasi (jenis kendaraan/kapal) | | | |
| Akomodasi (tipe, sharing?) | | | |
| Makan (berapa kali, halal?) | | | |
| Tiket masuk / retribusi kawasan / taman nasional | | | |
| Alat (snorkel, wetsuit, life jacket) | | | |
| Dokumentasi | | | |
| Tip pemandu/kru | | | |
| Asuransi | | | |

## 3. Keselamatan

| Item | Nilai | Label | Sumber |
|---|---|---|---|
| Briefing keselamatan (kapan, oleh siapa) | | | |
| Alat keselamatan di kendaraan/kapal (life jacket per peserta, P3K, radio) | | | |
| Prosedur cuaca buruk (batal/reschedule/refund — ringkas) | | | |
| Kontak darurat & fasilitas kesehatan terdekat (untuk SOP internal, bukan konten) | | Internal | |

## 4. Satwa, Alam & Aturan Kawasan

| Item | Nilai | Label | Sumber |
|---|---|---|---|
| Satwa yang **mungkin** terlihat + musim (sumber; tidak dijamin) | | | |
| Aturan kawasan (jarak satwa, larangan menyentuh/memberi makan, drone) | | | |
| Tempat suci/adat di rute (etika berpakaian, area terlarang) | | | |

## 5. Good to Know (jujur)

| Hal | Label | Sumber |
|---|---|---|
| Laut berombak musim tertentu / mabuk laut | | |
| Sinyal & listrik terbatas di lokasi | | |
| Lainnya | | |

## 6. Open Items

| Item | Label | Owner | Target |
|---|---|---|---|
| | **CLIENT CONFIRMATION** / **FIELD VERIFICATION** | | |
