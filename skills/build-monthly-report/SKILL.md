---
name: build-monthly-report
description: Build an honest monthly content report for an Indonesian hospitality client from platform insights (Instagram, Facebook, TikTok, Google Business Profile, OTA reviews) and the delivery log, covering package quota used, SLA, performance as-is, reviews, incidents, and next-month plan, without inflating or estimating numbers. Use when the user asks for a monthly report, performance recap, or client report.
---

# Build Monthly Report

## Load Required Context

- `../../core/AI-CONSTITUTION.md`
- `../../rules/01-CONTENT-INTEGRITY-STANDARD.md`
- `../../rules/09-DATA-CLASSIFICATION.md`
- `../../templates/monthly-report.md`
- `../../commercial/service-catalog.md` (kuota paket & SLA)
- `../../commercial/delivery-sop.md` (ukuran mutu)
- `../../agents/agents/personas/report-builder.md` (kartu persona: gaya bahasa, batas & eskalasi)

## Workflow

1. Konfirmasi: client, bulan, paket, kanal aktif, dan siapa yang mengekspor angka (manusia dengan akses insight; AI tidak login ke akun client).
2. Kumpulkan angka **apa adanya** dari export/screenshot insight tiap platform, catat sumber + tanggal pengambilan per baris. Angka yang tidak tersedia ditulis "tidak tersedia", bukan diperkirakan.
3. Isi kuota paket & SLA dari log delivery (konten direncanakan vs tayang, balasan review, tanggal kirim kalender/batch). Keterlambatan karena approval klien ditulis apa adanya, tanpa menyalahkan.
4. Bandingkan dengan bulan lalu hanya bila definisi metrik sama; perubahan definisi oleh platform dicatat.
5. Top & bottom konten: analisis "kenapa" diberi label **ASSUMPTION**.
6. Konversi/booking hanya diklaim bila ada tracking (UTM, booking engine, catatan client) → selain itu tulis sebagai korelasi dan **CLIENT CONFIRMATION**.
7. Tulis ringkasan eksekutif 3 poin + yang tidak berjalan + 3 rekomendasi bulan depan yang bisa dikerjakan dalam paket.
8. Jalankan self-check.

## Output

- Laporan mengikuti [monthly-report.md](../../templates/monthly-report.md), termasuk § 2a Kuota Paket & SLA.
- Daftar data yang tidak tersedia + **NEXT ACTION** untuk mendapatkannya bulan depan.
- Level approval: L1 (dikirim content lead; tanpa klaim baru ke publik).

## Self-Check

1. Setiap angka punya sumber + tanggal pengambilan; tidak ada pembulatan ke atas.
2. Tidak ada klaim sebab-akibat (konten → booking) tanpa tracking.
3. Tidak ada data pribadi tamu (nama reviewer disamarkan bila dikutip).
4. Kuota & SLA jujur, termasuk yang meleset.
5. Rekomendasi tidak menjanjikan hasil dan tidak di luar katalog paket.
6. Nada sesuai kartu persona `report-builder`: lugas, tidak menyebut diri AI.

## Safety Boundary

- Tidak login ke akun platform client dan tidak meminta password.
- Tidak mengarang, mengestimasi, atau "menghaluskan" angka.
- Tidak mengirim laporan ke client; content lead manusia yang mengirim.

## Exit Criteria

**Pass** bila semua angka bersumber, kuota & SLA terisi, dan data yang hilang tercatat. **Fail** bila ada angka tanpa sumber atau klaim konversi tanpa tracking.
