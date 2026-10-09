# Outlet Fact Sheet — Restaurant, Cafe & Beach Club

> Sumber fakta resmi outlet F&B untuk semua konten (caption, GBP, website, balasan review, jawaban FAQ). Diisi bersama owner/manager saat onboarding dan setiap ada perubahan menu, jam, atau kebijakan. Simpan versi terisi di **workspace client**, jangan di repo ([AI-BOUNDARY.md](../core/AI-BOUNDARY.md)). Contoh fiktif terisi: [pilot Kafe Contoh Canggu](../examples/pilot-kafe-contoh-canggu/fact-sheet.md). Knowledge segment: [restaurant.md](../knowledge/segments/restaurant.md).

## Cara Pakai

1. Isi setiap baris dengan nilai **dan** label evidence ([rule 09](../rules/09-DATA-CLASSIFICATION.md)).
2. Hanya baris **DATA FINAL** yang boleh dipakai di konten publish ([rule 01](../rules/01-CONTENT-INTEGRITY-STANDARD.md), [rule 02](../rules/02-HOSPITALITY-CLAIM-STANDARD.md)).
3. Kolom **Sumber** berisi dokumen/foto/konfirmasi owner beserta tanggal. Jangan tulis URL privat; gunakan referensi opaque.
4. Baris yang tidak relevan diisi `N/A`, jangan dihapus.
5. Setiap perubahan menaikkan versi; konten yang memakai nilai lama wajib dicek ulang. Menu musiman/Ramadan = versi terpisah dengan periode berlaku.

## 0. Dokumen

| Field | Isi |
|---|---|
| Kode client | |
| Versi fact sheet | v1 |
| Tanggal | YYYY-MM-DD |
| Disetujui oleh (peran) | |
| Tipe | restaurant / cafe / beach club / bar / bakery |

## 1. Identitas & Lokasi

| Field | Nilai | Label | Sumber |
|---|---|---|---|
| Nama resmi (penulisan persis) | | | |
| Alamat & pin GBP (sama dengan GBP) | | | |
| Area (kabupaten/kota, provinsi) | | | |
| Parkir (mobil/motor, berbayar?) | | | |
| Akses (tangga, ramah kursi roda, ramah stroller) | | | |

## 2. Jam & Reservasi

| Field | Nilai | Label | Sumber |
|---|---|---|---|
| Jam buka normal per hari (sama di GBP, bio IG, website) | | | |
| Jam dapur terakhir (last order) | | | |
| Perubahan jam Ramadan / libur nasional / Nyepi | | | |
| Kanal reservasi resmi (WA/booking tool) — referensi opaque | | | |
| Kebijakan reservasi (deposit, batas waktu tunggu, grup besar) | | | |
| Minimum spend / dress code / batas umur (beach club, bar) | | | |

## 3. Kapasitas & Area

| Area | Kursi | Indoor/outdoor | Smoking? | Catatan (view, musik, AC) | Label | Sumber |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Menu & Harga

| Item | Nilai | Label | Sumber |
|---|---|---|---|
| Versi menu & periode berlaku | | | |
| Menu andalan (maks 5; nama persis seperti di menu) | | | |
| Status harga di menu | net / ++ | | |
| Pajak restoran / PB1 daerah (%) | | | |
| Service charge (%) | | | |
| Paket/bundling aktif (nama, isi, harga, periode, syarat) | | | |

## 5. Halal & Dietary

| Klaim | Status | Nomor sertifikat / penerbit | Berlaku sampai | Label | Sumber |
|---|---|---|---|---|---|
| Halal (outlet) | bersertifikat / tidak | | | | |
| Menyajikan babi / alkohol | ya / tidak | — | — | | |
| "No pork no lard" (bila dipakai: dapur + supplier) | | — | — | | |
| Opsi vegetarian / vegan (per menu) | | — | — | | |
| Gluten-free / alergen (catatan cross-contamination) | | — | — | | |

> Tanpa sertifikat aktif, kata "halal" **hard block** (rule 02). "No pork no lard" tetap **CLIENT CONFIRMATION** + legal review.

## 6. Sertifikasi & Klaim Khusus

| Klaim | Nomor / penerbit | Berlaku sampai | Label | Sumber |
|---|---|---|---|---|
| Sertifikat laik higiene / keamanan pangan | | | | |
| Kopi/bahan dengan origin disebut (invoice/label roaster) | | | | |
| Award (nama, penyelenggara, tahun) | | | | |

## 7. Event & Program Rutin

| Event | Jadwal | Biaya masuk / minimum spend | Batas umur | Label | Sumber |
|---|---|---|---|---|---|
| | | | | | |

## 8. Good to Know (jujur, mengurangi review negatif)

| Hal yang perlu diketahui tamu | Label | Sumber |
|---|---|---|
| Waktu tunggu saat ramai | | |
| Musik keras / jam tenang lingkungan | | |
| Lainnya | | |

## 9. Open Items

| Item | Label | Owner | Target |
|---|---|---|---|
| | **CLIENT CONFIRMATION** / **FIELD VERIFICATION** | | |
