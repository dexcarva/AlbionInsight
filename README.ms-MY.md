# Albion Insight (ms-MY)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** ialah alat analisis statistik rentas platform (Linux, Windows, macOS) untuk permainan Albion Online, yang dilaksanakan semula dalam **Python** menggunakan rangka kerja **Flet**. Ia direka untuk menjejaki statistik dalam permainan masa nyata, termasuk perak, kemasyhuran, dan data pertempuran (Meter Kerosakan), dengan menganalisis trafik rangkaian.

Projek ini adalah alternatif moden, sumber terbuka kepada alat `AlbionOnline-StatisticsAnalysis` berasaskan C#/WPF yang asal, memfokuskan pada keserasian berbilang platform dan kemudahan penggunaan.

## Ciri-ciri

*   **Keserasian Rentas Platform:** Berjalan secara asli pada Linux, Windows, dan macOS.
*   **Penjejakan Masa Nyata:** Menggunakan pustaka `Scapy` untuk menghidu paket UDP pada port Albion Online (5055, 5056, 5058).
*   **Struktur Meter Kerosakan:** Termasuk struktur data dan UI yang diperlukan untuk memaparkan statistik pertempuran secara langsung (Kerosakan Dilakukan, Penyembuhan Dilakukan, DPS).
*   **UI Moden:** Dibina dengan Flet, menyediakan aplikasi desktop yang pantas dan kelihatan asli.
*   **Pengurusan Sesi:** Membenarkan memulakan, menghentikan, menetapkan semula, dan menyimpan statistik sesi.

## Prasyarat

*   Python 3.8+
*   Pustaka **Flet** dan **Scapy**.
*   **Keistimewaan Root/Pentadbir:** Diperlukan untuk penangkapan paket rangkaian.

## Pemasangan dan Persediaan

### Pilihan 1: Pemasangan Pantas (Linux - Disyorkan)

Untuk pengguna Linux, kami menyediakan skrip pemasangan automatik:

\`\`\`bash
# 1. Klon repositori
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Jalankan skrip pemasangan
./install.sh

# 3. Jalankan aplikasi
./run.sh
\`\`\`

Skrip `install.sh` akan:
- Memasang kebergantungan sistem (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Mencipta persekitaran maya Python
- Memasang semua pakej Python yang diperlukan (Flet, Scapy)

Skrip `run.sh` akan secara automatik meminta keistimewaan root dan menjalankan aplikasi.

### Pilihan 2: Pemasangan Manual (Semua Platform)

1.  **Klon repositori:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`

2.  **Sediakan persekitaran Python:**
    \`\`\`bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate.bat  # Windows
    \`\`\`

3.  **Pasang kebergantungan:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4.  **Jalankan aplikasi:**
    \`\`\`bash
    # Pada Linux/macOS, anda mungkin perlu menggunakan sudo untuk keistimewaan rangkaian
    sudo python3 -m albion_insight
    
    # Pada Windows, jalankan sebagai Pentadbir
    python3 -m albion_insight
    \`\`\`

## Sumbangan

Kami mengalu-alukan sumbangan! Sila lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan terperinci.

## Lesen

Projek ini dilesenkan di bawah Lesen MIT. Lihat fail [LICENSE](LICENSE) untuk butiran.
