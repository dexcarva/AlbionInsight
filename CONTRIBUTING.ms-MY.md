# Menyumbang kepada Albion Insight

**[Baca dalam Bahasa Inggeris](CONTRIBUTING.md)** | **[Baca dalam Bahasa Portugis (Brazil)](CONTRIBUTING.pt-BR.md)** | **[Baca dalam Bahasa Portugis (Portugal)](CONTRIBUTING.pt-PT.md)**
<!-- Di sini akan ditambah lebih banyak pautan terjemahan -->

Pertama sekali, terima kasih kerana mempertimbangkan untuk menyumbang kepada Albion Insight! Orang seperti anda yang menjadikan Albion Insight alat yang hebat untuk komuniti Albion Online.

## Isi Kandungan
	
- [Kod Etika](#kod-etika)
- [Bagaimana Saya Boleh Menyumbang?](#bagaimana-saya-boleh-menyumbang)
  - [Melaporkan Pepijat](#melaporkan-pepijat)
  - [Mencadangkan Ciri](#mencadangkan-ciri)
  - [Sumbangan Kod](#sumbangan-kod)
  - [Dokumentasi](#dokumentasi)
- [Persediaan Pembangunan](#persediaan-pembangunan)
- [Piawaian Pengekodan](#piawaian-pengekodan)
- [Mesej Komit](#mesej-komit)
- [Proses Permintaan Tarik (Pull Request)](#proses-permintaan-tarik-pull-request)

## Kod Etika

Projek ini dan semua yang mengambil bahagian di dalamnya dikawal oleh Kod Etika kami. Dengan mengambil bahagian, anda dijangka mematuhi kod ini. Sila laporkan tingkah laku yang tidak boleh diterima kepada penyelenggara projek.

## Bagaimana Saya Boleh Menyumbang?

### Melaporkan Pepijat

Sebelum membuat laporan pepijat, sila semak isu sedia ada untuk mengelakkan penduaan. Apabila anda membuat laporan pepijat, sertakan seberapa banyak butiran yang mungkin menggunakan templat laporan pepijat.

**Laporan pepijat yang baik termasuk:**
- Tajuk yang jelas dan deskriptif
- Langkah-langkah yang tepat untuk menghasilkan semula masalah
- Tingkah laku yang dijangka berbanding tingkah laku sebenar
- Tangkapan skrin jika berkenaan
- Butiran persekitaran anda (OS, versi Python, dsb.)
- Log atau mesej ralat yang berkaitan

### Mencadangkan Ciri

Cadangan ciri dialu-alukan! Sila gunakan templat permintaan ciri dan berikan:
- Penerangan yang jelas tentang ciri tersebut
- Masalah yang diselesaikannya
- Pendekatan pelaksanaan yang mungkin
- Sebarang alternatif yang telah anda pertimbangkan

### Sumbangan Kod

Kami suka sumbangan kod! Berikut ialah cara untuk bermula:

1. **Fork repositori** dan buat cawangan anda daripada `master`
2. **Sediakan persekitaran pembangunan anda** (lihat Persediaan Pembangunan di bawah)
3. **Buat perubahan anda** mengikut piawaian pengekodan kami
4. **Uji perubahan anda** dengan teliti
5. **Kemas kini dokumentasi** jika perlu
6. **Hantar permintaan tarik** menggunakan templat PR kami

### Dokumentasi

Penambahbaikan pada dokumentasi sentiasa dihargai! Ini termasuk:
- Fail README
- Halaman Wiki
- Komen kod
- Tutorial dan panduan
- Terjemahan ke bahasa lain

## Persediaan Pembangunan

### Prasyarat

- Python 3.8 atau lebih tinggi
- Git
- Hak Akses Root/Pentadbir (untuk penangkapan paket)

### Menyediakan Persekitaran Anda

```bash
# Klon fork anda
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Cipta persekitaran maya
python3 -m venv venv

# Aktifkan persekitaran maya
# Di Linux/macOS:
source venv/bin/activate
# Di Windows:
venv\Scripts\activate

# Pasang kebergantungan
pip install -r requirements.txt

# Pasang kebergantungan pembangunan
pip install pylint flake8 black pytest
```

### Menjalankan Aplikasi

```bash
# Di Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Di Windows (sebagai Pentadbir):
python albion_insight.py
```

## Piawaian Pengekodan

Kami mengikut garis panduan gaya PEP 8 untuk kod Python. Sila pastikan kod anda mematuhi piawaian ini:

- Gunakan 4 ruang untuk inden (bukan tab)
- Panjang baris maksimum 100 aksara
- Gunakan nama pembolehubah dan fungsi yang bermakna
- Tambah docstrings pada semua fungsi dan kelas
- Sertakan petunjuk jenis (type hints) jika sesuai
- Pastikan fungsi fokus dan ringkas

**Alat untuk membantu:**
```bash
# Format kod anda dengan black
black albion_insight.py

# Semak isu gaya
flake8 albion_insight.py

# Jalankan linter
pylint albion_insight.py
```

## Mesej Komit

Tulis mesej komit yang jelas dan bermakna:

- Gunakan kala kini ("Tambah ciri" bukan "Menambah ciri")
- Gunakan mood imperatif ("Alihkan kursor ke..." bukan "Mengalihkan kursor ke...")
- Hadkan baris pertama kepada 72 aksara
- Rujuk isu dan permintaan tarik apabila berkaitan

**Contoh:**
```
Tambah kefungsian eksport meter kerosakan
	
Betulkan penghuraian paket rangkaian untuk sambungan IPv6
	
Kemas kini README dengan arahan pemasangan macOS
	
Menutup #123
```

## Proses Permintaan Tarik (Pull Request)

1. **Kemas kini dokumentasi** untuk sebarang perubahan pada kefungsian
2. **Tambah ujian** untuk ciri baharu atau pembetulan pepijat
3. **Pastikan semua ujian lulus** sebelum menghantar
4. **Kemas kini README.md** jika perlu
5. **Isi templat PR** sepenuhnya
6. **Pautkan isu berkaitan** dalam penerangan PR anda
7. **Minta semakan** daripada penyelenggara
8. **Tangani maklum balas** dengan segera dan profesional

### Senarai Semak PR

Sebelum menghantar PR anda, pastikan:
- [ ] Kod mematuhi garis panduan gaya projek
- [ ] Semakan kendiri selesai
- [ ] Komen ditambah pada bahagian kod yang kompleks
- [ ] Dokumentasi dikemas kini
- [ ] Tiada amaran baharu dijana
- [ ] Ujian ditambah dan lulus
- [ ] Perubahan yang bergantung digabungkan

## Soalan?

Jangan teragak-agak untuk bertanya! Anda boleh:
- Buka isu dengan label "question"
- Sertai perbincangan komuniti kami
- Hubungi penyelenggara

Terima kasih kerana menyumbang kepada Albion Insight! Usaha anda membantu menjadikan alat ini lebih baik untuk seluruh komuniti Albion Online.
