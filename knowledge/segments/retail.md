# Segment: Toko, Retail & UMKM Produk

> **Status: Planned — belum dipakai untuk client.** Disiapkan 2026-10-09 sebagai knowledge awal (**ASSUMPTION**) untuk vertical gelombang 2 (`clau-core/docs/verticals.md`). Di luar hospitality: butuh amandemen scope AI-CONSTITUTION §2 (TASK-040) + rule klaim produk sebelum aktif (TASK-041).

## Scope

Toko offline & online (IG shop, marketplace, website), UMKM produk (makanan kemasan, fashion, kerajinan, kosmetik lokal), dan toko oleh-oleh.

> Knowledge ini **Reusable** dan generik. Produk, harga, stok, dan izin dari dokumen client (**DATA FINAL**).

## Karakter Segment

- Pembelian cepat dan sensitif harga; promo marketplace (tanggal kembar, Harbolnas, Ramadan) sangat berpengaruh.
- Foto produk & ulasan menentukan konversi.
- Banyak transaksi kecil → nilai tinggi untuk AI Admin (data entry, stok) dan BI.

## Audience Umum

| Segmen | Kebutuhan | Angle konten |
|---|---|---|
| Pembeli online | Harga, ongkir, ulasan, keaslian | Detail produk, bukti kirim, ulasan |
| Pembeli lokal | Lokasi, stok, jam buka | Produk baru, promo toko |
| Wisatawan (oleh-oleh) | Khas daerah, kemasan, tahan lama | Cerita produk, daya tahan |
| Reseller | Harga grosir, minimum order | Syarat reseller |

## Content Pillars (contoh)

1. **Produk** — detail, bahan, ukuran, cara pakai.
2. **Cerita Pembuat** — proses produksi (dengan consent).
3. **Ulasan & Unboxing** — dengan izin.
4. **Promo** — periode & syarat.
5. **Info Praktis** — ongkir, cara order, garansi/retur.

## Claim Hotspots

| Klaim | Masalah umum | Perlakuan |
|---|---|---|
| "Original", "100% asli" | Barang pihak ketiga tanpa bukti | Hanya bila client distributor resmi (**DATA FINAL**) |
| Diskon "up to 70%" | Harga coret tidak pernah berlaku | Harga coret = harga normal yang benar-benar pernah berlaku; sebut periode |
| "Halal", "BPOM", "SNI", "PIRT" | Tanpa nomor izin | Sebut hanya dengan nomor izin aktif (**DATA FINAL**) |
| Klaim kesehatan pada makanan/minuman/kosmetik | Klaim khasiat medis | Hard block; ikuti label produk terdaftar |
| "Stok terbatas" | Urgensi palsu | Hanya bila stok nyata rendah |
| "Garansi" | Syarat tidak jelas | Rinci syarat, durasi, cara klaim |

## Foto & Video

- Foto produk asli; warna sesuai (catat bila ada perbedaan layar).
- Mockup AI hanya untuk produk yang belum ada, berlabel "ilustrasi".
- Ulasan pelanggan di-screenshot hanya dengan izin; sembunyikan nama/nomor.

## Practical Info Wajib Konsisten

| Item | Sumber |
|---|---|
| Harga & varian | Price list / marketplace terbaru |
| Stok | Sistem stok client (bukan ingatan AI) |
| Ongkir, retur, garansi | Kebijakan toko |

## Kesalahan Umum

- Harga coret palsu.
- Klaim "menyembuhkan"/"menurunkan berat badan" pada produk.
- Stok di konten tidak sama dengan stok nyata.

## References

- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md) (akan diperluas untuk klaim produk)
- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
