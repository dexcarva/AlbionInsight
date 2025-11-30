# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Baca ini dalam bahasa lain</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)** | **[Finnish](README.fi-FI.md)** | **[Polish](README.pl-PL.md)** | **[Danish](README.da-DK.md)** | **[Ukrainian](README.uk-UA.md)** | **[Malay](README.ms-MY.md)**

</details>

**Albion Insight** adalah alat analisis statistik rentas platform (Linux, Windows, macOS) untuk permainan Albion Online, yang diimplementasikan semula dalam **Python** menggunakan rangka kerja **Flet**. Ia direka untuk menjejaki statistik dalam permainan masa nyata, termasuk perak, kemasyhuran, dan data pertempuran (Meter Kerosakan), dengan menganalisis trafik rangkaian.

Projek ini adalah alternatif moden, sumber terbuka kepada alat `AlbionOnline-StatisticsAnalysis` asal berasaskan C#/WPF, yang memfokuskan pada keserasian berbilang platform dan kemudahan penggunaan.

## Ciri-ciri

*   **Keserasian Rentas Platform:** Berjalan secara asli di Linux, Windows, dan macOS.
*   **Penjejakan Masa Nyata:** Menggunakan pustaka `Scapy` untuk menghidu paket UDP pada port Albion Online (5055, 5056, 5058).
*   **Struktur Meter Kerosakan:** Termasuk struktur data dan UI yang diperlukan untuk memaparkan statistik pertempuran secara langsung (Kerosakan Dilakukan, Penyembuhan Dilakukan, DPS).
*   **UI Moden:** Dibina dengan Flet, menyediakan aplikasi desktop yang pantas dan kelihatan asli.
*   **Pengurusan Sesi:** Membenarkan memulakan, menghentikan, menetapkan semula, dan menyimpan statistik sesi.

## Prasyarat

*   Python 3.8+
*   Pustaka **Flet** dan **Scapy**.
*   **Hak Akses Root/Pentadbir:** Diperlukan untuk penangkapan paket rangkaian.

## Pemasangan dan Persediaan

### Pilihan 1: Pemasangan Pantas (Linux - Disyorkan)

Untuk pengguna Linux, kami menyediakan skrip pemasangan automatik:

```bash
# 1. Klon repositori
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Jalankan skrip pemasangan
./install.sh

# 3. Jalankan aplikasi
./run.sh
```

Skrip `install.sh` akan:
- Memasang kebergantungan sistem (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Mencipta persekitaran maya Python
- Memasang semua pakej Python yang diperlukan (Flet, Scapy)

Skrip `run.sh` akan secara automatik meminta hak akses root dan menjalankan aplikasi.

### Pilihan 2: Pemasangan Manual

#### 1. Pasang Kebergantungan Sistem

**Di Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Di Windows:**

Pasang Python 3.8+ dari [python.org](https://www.python.org/downloads/)

#### 2. Pasang Kebergantungan Python

**Di Linux (menggunakan persekitaran maya - disyorkan):**

```bash
# Cipta persekitaran maya
python3 -m venv venv
# Aktifkan persekitaran maya
source venv/bin/activate
# Pasang kebergantungan
pip install flet scapy
```

**Di Linux (pemasangan seluruh sistem):**

```bash
pip3 install flet scapy --break-system-packages
```

**Di Windows:**

```bash
pip install flet scapy
```

#### 3. Menjalankan Aplikasi

Oleh kerana penghiduan rangkaian memerlukan hak akses yang ditingkatkan, anda mesti menjalankan aplikasi sebagai root atau pentadbir.

**Di Linux (dengan persekitaran maya):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Di Linux (pemasangan seluruh sistem):**

```bash
sudo python3 -m albion_insight
```

**Di Windows (Jalankan Command Prompt/PowerShell sebagai Pentadbir):**

```bash
python -m albion_insight
```

Aplikasi akan dibuka dalam tetingkap desktop asli.

## Cara Membina Boleh Laksana (Executable)

Aplikasi boleh dibungkus menjadi boleh laksana kendiri menggunakan **PyInstaller**. Ini membolehkan pengguna menjalankan aplikasi tanpa memasang Python atau kebergantungannya.

Untuk arahan terperinci tentang membina boleh laksana untuk Linux, Windows, dan macOS, lihat panduan **[PACKAGING.md](PACKAGING.md)**.

### Pembinaan Pantas (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Boleh laksana akan terletak di folder `dist/`.

## Struktur Projek

Aplikasi distrukturkan kepada komponen modular untuk penyelenggaraan dan skalabiliti yang lebih baik:

| Fail | Penerangan |
| :--- | :--- |
| `albion_insight/core/` | Logik teras, penjejakan rangkaian, model data, dan penyahkodan protokol. |
| `albion_insight/ui/` | Komponen antara muka pengguna dibina dengan Flet. |
| `albion_insight/utils/` | Fungsi utiliti, konfigurasi, dan pengelogan. |
| `albion_insight/__main__.py` | Titik masuk untuk aplikasi. |
| `README.md` | Fail dokumentasi ini. |
| `README.pt-BR.md` | Fail dokumentasi ini dalam Bahasa Portugis Brazil. |
| `README.fil-PH.md` | Fail dokumentasi ini dalam Bahasa Filipina (Tagalog). |
| `README.pt-PT.md` | Fail dokumentasi ini dalam Bahasa Portugis (Portugal). |
| `README.sv-SE.md` | Fail dokumentasi ini dalam Bahasa Sweden. |
| `README.da-DK.md` | Fail dokumentasi ini dalam Bahasa Denmark. |
| `CONTRIBUTING.sv-SE.md` | Garis Panduan untuk menyumbang kepada projek dalam Bahasa Sweden. |
| `CONTRIBUTING.md` | Garis Panduan untuk menyumbang kepada projek. |
| `CODE_OF_CONDUCT.md` | Kod Etika projek. |
| `SECURITY.md` | Polisi untuk melaporkan kelemahan keselamatan. |

## Status Semasa (Data Masa Nyata)

Aplikasi kini termasuk logik **Penyahkodan Protokol Foton**, diterjemahkan dari projek C# asal. Ini membolehkan aplikasi memproses peristiwa masa nyata seperti `UpdateMoney`, `UpdateFame`, `KilledPlayer`, dan `Died` secara langsung dari trafik rangkaian.

**Nota:** Terjemahan penuh setiap peristiwa pertempuran (seperti `CastHit`, `Attack`) adalah usaha yang berterusan. Pelaksanaan semasa memfokuskan pada statistik teras dan struktur untuk Meter Kerosakan. Pengiraan DPS Meter Kerosakan adalah berdasarkan peristiwa yang dinyahkod.

## Menyumbang

Kami mengalu-alukan sumbangan daripada komuniti! Sama ada anda seorang pembangun, pereka, atau hanya peminat Albion Online, terdapat banyak cara untuk membantu meningkatkan Albion Insight.

Sila baca [Garis Panduan Sumbangan](CONTRIBUTING.md) kami untuk maklumat terperinci tentang cara menyumbang kepada projek ini.

### Permulaan Pantas untuk Penyumbang:

1.  Fork repositori: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klon fork anda: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Cipta cawangan baharu: `git checkout -b feature/your-feature-name`
4.  Buat perubahan anda dan komit: `git commit -m "Add your feature"`
5.  Tolak ke fork anda: `git push origin feature/your-feature-name`
6.  Buka Permintaan Tarik (Pull Request) pada repositori utama

## Lesen

Projek ini dilesenkan di bawah Lesen MIT - lihat fail [LICENSE](LICENSE) untuk butiran.

## Penghargaan

- Projek asal: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) oleh Triky313
- Dibina dengan rangka kerja [Flet](https://flet.dev/)
- Analisis rangkaian dikuasakan oleh [Scapy](https://scapy.net/)
---
*Penyelesaian rentas platform untuk komuniti Albion Online.*
