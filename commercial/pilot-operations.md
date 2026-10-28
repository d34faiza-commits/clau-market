# Pilot jasa hospitality — operasi yang dapat diukur

Status: template operasional, perintah Pak Indra 2026-10-28. **Belum ada klien atau
hasil pilot nyata yang dicatat di sini.** Salin ke Client Workspace privat. Tidak ada
harga, identitas, kontrak terisi, atau data tamu di repo public.

## 1. Gate sebelum kontrak pertama

Prospek/discovery/proposal boleh berjalan sesuai K6 TASK-067. Tanda tangan menunggu
seluruh bukti berikut; AI menyiapkan dokumen dan mencatat keputusan, bukan menggantikan
reviewer, konsultan atau pemilik usaha.

| Gate | Penanggung jawab | Bukti minimum di workspace | Status awal |
|---|---|---|---|
| TASK-028, pilot 2 v3 | Reviewer manusia yang independen | Lembar rubrik terisi sendiri, temuan, tanggal, versi yang dinilai | Belum diverifikasi |
| Knowledge vertical | Owner/content lead | File/versi dibaca, fakta meragukan diselesaikan atau dikeluarkan dari scope | Belum diverifikasi |
| TASK-053 | Owner + konsultan hukum | Kontrak, DPA, jawaban L1–L6 dan perubahan final; alasan tertulis bila tidak berlaku | Belum diverifikasi |
| Identitas usaha/pajak | Owner + penasihat terkait | Identitas penagih, invoice, perlakuan pajak terkonfirmasi | Belum diverifikasi |
| Harga dan margin | Owner | Price sheet final, jam dan tarif internal per peran, biaya tools/provider, batas diskon | Belum diverifikasi |
| Kapasitas & pengganti | Content lead | Operator dan reviewer berbeda; alokasi jam masing-masing ≤85%; PIC cadangan | Belum diverifikasi |

Paket untuk konsultan: [kontrak](./service-agreement-template.md),
[DPA](./data-processing-addendum.md), [pertanyaan legal](./legal-tax-research-2026.md),
scope satu vertical, daftar provider/subprosesor yang benar-benar akan dipakai,
aliran data, retensi, akses, dan draft invoice. Catat siapa menjawab, kapan, versi,
open issues dan syarat penandatanganan. Jangan mengirim dokumen otomatis.

## 2. Scope dan peran

- Satu klien, satu vertical, satu–dua kanal. Pilih dari discovery, tidak mengarang calon klien.
- Gunakan kuota paket yang disepakati di [katalog](./service-catalog.md). Pilot lebih kecil
  hanya melalui scope/proposal tertulis; tidak diam-diam mengurangi kuota atau SLA.
- Konten feed adalah caption, tabel klaim, dan brief visual; video berupa naskah/shot list.
  Foto, rekaman, desain final dan publishing harus jelas siapa mengerjakan sebelum penawaran.
- Operator meminta/menyusun draft. Reviewer independen memeriksa seluruh kalimat, termasuk
  implikasi; approver klien memberi keputusan versi tertentu. Satu orang tidak merangkap
  pembuat dan reviewer independen. Jika reviewer cuti/sakit dan tidak ada pengganti, hold.
- Jadwal awal: minggu 1–2 setup, minggu 3–4 batch pertama; review tiap minggu,
  evaluasi biaya dan kapasitas pada akhir bulan kedua. Tanggal nyata ditetapkan bersama klien.
- Manual boleh memakai tools AI yang memang diizinkan untuk data tersebut. Jangan
  memasukkan data tamu mentah. Runtime palsu/simulasi tidak menghasilkan konten klien nyata.

## 3. Log minimum per deliverable

| Field | Cara mencatat |
|---|---|
| client_code, item_id, channel, format | Kode privat; satu unit konten lintas IG/FB dihitung sesuai katalog |
| version, operator, reviewer, approver | Orang dan versi yang benar-benar mengerjakan; timestamp approval terpisah |
| source_versions | Brief, fact sheet, Voice Card, aset/consent yang dipakai |
| scope_received_at, input_complete_at, original_due_at | Deadline pertama tidak ditimpa |
| pause_started_at, pause_ended_at, reason, agreed_due_at | Waktu menunggu klien dipisahkan, dengan bukti kesepakatan |
| first_sent_at, approved_at, published_at | Kosong bila belum terjadi; publish hanya diisi manusia dengan URL |
| work_minutes, role, activity | Timer aktual: setup, draft, QA, revisi, komunikasi, laporan, add-on |
| revision_rounds, major_revision, reason | Major = perubahan fakta/angle/voice/struktur yang memerlukan pengerjaan ulang; minor = typo/format |
| provider_cost, allocated_tool_cost, external_cost | Biaya aktual dan metode alokasi; unknown tetap kosong, bukan nol |
| incident, correction_minutes | Klaim, privacy, wrong version, keterlambatan, penyebab dan tindakan |

Approval terlambat: ingatkan H+1 sesuai SOP, jadwal mundur dengan bukti. Jangan
menghapus backlog atau menganggap diam sebagai setuju. Fakta baru membuat versi baru;
catat waktu revisi meskipun tidak mengurangi jatah revisi klien. Permintaan mendadak
harus masuk kapasitas; jangan menjanjikan respons di luar jam layanan.

## 4. Scorecard mingguan/bulanan

| Metrik | Rumus / interpretasi |
|---|---|
| Jam aktual | Jumlah menit /60, per orang dan aktivitas; setup dipisahkan dari recurring |
| Kapasitas orang | (komitmen berjalan + setup + backlog + add-on) / jam tersedia; ≤85% |
| Major revision rate | Item dengan ≥1 revisi major / item yang sudah mendapat keputusan review |
| Approval tanpa major | Item approved tanpa major / item yang sudah mendapat keputusan; pending ditampilkan terpisah |
| SLA original | Deliverable dikirim tepat original_due_at / seluruh deliverable jatuh tempo, termasuk overdue belum dikirim |
| SLA adjusted | Rumus sama dengan agreed_due_at; selalu tampilkan original, jumlah pause dan alasannya |
| Labor cost | Σ jam aktual per orang × tarif internal per jam; owner tidak dianggap gratis |
| Contribution | Pendapatan bersih untuk periode − labor − provider − tools teralokasi − biaya eksternal langsung |
| Contribution margin | Contribution / pendapatan bersih ×100%; bukan laba bersih setelah seluruh overhead/pajak |
| Defect kritis | Salah fakta kritis, kebocoran lintas klien, privacy/consent violation: target 0 |

Denominator nol → **N/A**, tidak ditulis 0%/100%. Pendapatan/biaya yang belum lengkap
→ **belum dapat dihitung**, jangan mengisi angka asumsi sebagai aktual. Setup fee dan
biaya setup dilaporkan terpisah agar margin bulan pertama tidak menyamarkan recurring.
Target awal SLA ≥90% sesuai SOP; approval tanpa major ≥80% adalah target blueprint,
bukan hasil yang telah dicapai. Margin minimum ditetapkan owner dari price sheet privat.

## 5. Keputusan nyata

- **Lanjut pilot:** gate kontrak terpenuhi, fakta/aset/consent dan approver siap,
  reviewer tersedia, scope jelas dan kapasitas mencukupi.
- **Hold konten:** fakta berubah/bertentangan, consent hilang, reviewer/approver tidak ada,
  atau klaim belum dapat dibuktikan. Pekerjaan lain yang aman boleh jalan.
- **Hold ekspansi:** defect kritis belum selesai, SLA berulang meleset, backlog meningkat,
  margin belum diketahui/di bawah batas owner, atau salah satu orang >85% kapasitas.
- **Tambah klien:** dua siklus delivery sudah diukur, temuan ditutup, kapasitas per orang
  dan pengganti tersedia, owner menyetujui angka aktual. Tidak otomatis karena CI hijau.

Case study hanya dari hasil nyata dan izin tertulis. Persetujuan pilot lama tidak
otomatis menutup TASK-028 untuk versi baru; status review selalu menyebut versi dan metode.
