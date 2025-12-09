# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** adalah alat analisis statistik lintas platform (Linux, Windows, macOS) untuk game Albion Online, diimplementasikan ulang dalam **Python** menggunakan kerangka kerja **Flet**. Alat ini dirancang untuk melacak statistik *real-time* dalam game, termasuk *silver*, *fame*, dan data pertempuran (*Damage Meter*), dengan menganalisis lalu lintas jaringan.

Proyek ini adalah alternatif modern dan *open-source* untuk alat asli `AlbionOnline-StatisticsAnalysis` berbasis C#/WPF, berfokus pada kompatibilitas multi-platform dan kemudahan penggunaan.

## Fitur

*   **Kompatibilitas Lintas Platform:** Berjalan secara *native* di Linux, Windows, dan macOS.
*   **Pelacakan *Real-Time*:** Menggunakan pustaka `Scapy` untuk mengendus paket UDP pada *port* Albion Online (5055, 5056, 5058).
*   **Struktur *Damage Meter*:** Mencakup struktur data dan UI yang diperlukan untuk menampilkan statistik pertempuran langsung (*Damage Done*, *Healing Done*, DPS).
*   **UI Modern:** Dibangun dengan Flet, menyediakan aplikasi desktop yang cepat dan terlihat *native*.
*   **Manajemen Sesi:** Memungkinkan memulai, menghentikan, mengatur ulang, dan menyimpan statistik sesi.

## Prasyarat

*   Python 3.8+
*   Pustaka **Flet** dan **Scapy**.
*   **Hak Akses *Root*/Administrator:** Diperlukan untuk pengambilan paket jaringan.

## Instalasi dan Pengaturan

### Opsi 1: Instalasi Cepat (Linux - Direkomendasikan)

Untuk pengguna Linux, kami menyediakan skrip instalasi otomatis:

\`\`\`bash
# 1. Kloning repositori
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Jalankan skrip instalasi
./install.sh

# 3. Jalankan aplikasi
./run.sh
\`\`\`

Skrip `install.sh` akan:
- Menginstal dependensi sistem (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Membuat lingkungan virtual Python
- Menginstal semua paket Python yang diperlukan (Flet, Scapy)

Skrip `run.sh` akan secara otomatis meminta hak akses *root* dan menjalankan aplikasi.

### Opsi 2: Instalasi Manual

#### 1. Instal Dependensi Sistem

**Di Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Di Windows:**

Instal Python 3.8+ dari [python.org](https://www.python.org/downloads/)

#### 2. Instal Dependensi Python

**Di Linux (menggunakan lingkungan virtual - direkomendasikan):**

\`\`\`bash
# Buat lingkungan virtual
python3 -m venv venv

# Aktifkan lingkungan virtual
source venv/bin/activate

# Instal dependensi
pip install flet scapy
\`\`\`

**Di Linux (instalasi sistem-luas):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Di Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Menjalankan Aplikasi

Karena pengintaian jaringan memerlukan hak akses yang ditinggikan, Anda harus menjalankan aplikasi sebagai *root* atau administrator.

**Di Linux (dengan lingkungan virtual):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Di Linux (instalasi sistem-luas):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Di Windows (Jalankan *Command Prompt*/PowerShell sebagai Administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

Aplikasi akan terbuka di jendela desktop *native*.

## Cara Membuat *Executable*

Aplikasi dapat dikemas menjadi *executable* mandiri menggunakan **PyInstaller**. Ini memungkinkan pengguna untuk menjalankan aplikasi tanpa menginstal Python atau dependensinya.

Untuk instruksi rinci tentang membuat *executable* untuk Linux, Windows, dan macOS, lihat panduan **[PACKAGING.md](PACKAGING.md)**.

### *Quick Build* (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

*Executable* akan berada di folder `dist/`.

## Struktur Proyek

Aplikasi ini disusun menjadi komponen modular untuk pemeliharaan dan skalabilitas yang lebih baik:

| File | Deskripsi |
| :--- | :--- |
| `albion_insight/core/` | Logika inti, pelacakan jaringan, model data, dan dekode protokol. |
| `albion_insight/ui/` | Komponen antarmuka pengguna yang dibangun dengan Flet. |
| `albion_insight/utils/` | Fungsi utilitas, konfigurasi, dan *logging*. |
| `albion_insight/__main__.py` | Titik masuk untuk aplikasi. |
| `README.md` | File dokumentasi ini. |
| `CONTRIBUTING.md` | Panduan untuk berkontribusi pada proyek. |
| `CODE_OF_CONDUCT.md` | Kode Etik proyek. |
| `SECURITY.md` | Kebijakan untuk melaporkan kerentanan keamanan. |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia. |

## Status Saat Ini (Data *Real-Time*)

Aplikasi sekarang mencakup logika **Dekode Protokol Photon**, yang diterjemahkan dari proyek C# asli. Ini memungkinkan aplikasi untuk memproses peristiwa *real-time* seperti `UpdateMoney`, `UpdateFame`, `KilledPlayer`, dan `Died` langsung dari lalu lintas jaringan.

**Catatan:** Terjemahan lengkap dari setiap peristiwa pertempuran (seperti `CastHit`, `Attack`) adalah upaya yang berkelanjutan. Implementasi saat ini berfokus pada statistik inti dan struktur untuk *Damage Meter*. Perhitungan DPS *Damage Meter* didasarkan pada peristiwa yang didekode.

## Berkontribusi

Kami menyambut kontribusi dari komunitas! Baik Anda seorang pengembang, desainer, atau hanya penggemar Albion Online, ada banyak cara untuk membantu meningkatkan Albion Insight.

Silakan baca [Panduan Berkontribusi](CONTRIBUTING.md) kami untuk informasi rinci tentang cara berkontribusi pada proyek ini.

### Mulai Cepat untuk Kontributor:

1.  *Fork* repositori: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  *Clone* *fork* Anda: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Buat cabang baru: `git checkout -b feature/nama-fitur-anda`
4.  Buat perubahan Anda dan *commit*: `git commit -m "Tambahkan fitur Anda"`
5.  *Push* ke *fork* Anda: `git push origin feature/nama-fitur-anda`
6.  Buka *Pull Request* di repositori utama

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.

## Ucapan Terima Kasih

- Proyek asli: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) oleh Triky313
- Dibangun dengan kerangka kerja [Flet](https://flet.dev/)
- Analisis jaringan didukung oleh [Scapy](https://scapy.net/)

---
*Solusi lintas platform untuk komunitas Albion Online.*
