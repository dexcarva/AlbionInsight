# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Basahin ito sa ibang wika</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)**

</details>

Ang **Albion Insight** ay isang cross-platform (Linux, Windows, macOS) na tool sa pagsusuri ng istatistika para sa larong Albion Online, na muling ipinatupad sa **Python** gamit ang **Flet** framework. Ito ay dinisenyo upang subaybayan ang real-time na istatistika sa laro, kabilang ang silver, fame, at combat data (Damage Meter), sa pamamagitan ng pagsusuri ng network traffic.

Ang proyektong ito ay isang moderno, open-source na alternatibo sa orihinal na C#/WPF-based na `AlbionOnline-StatisticsAnalysis` tool, na nakatuon sa multi-platform compatibility at kadalian ng paggamit.

## Mga Tampok (Features)

*   **Cross-Platform Compatibility:** Tumatakbo nang natural sa Linux, Windows, at macOS.
*   **Real-Time Tracking:** Gumagamit ng `Scapy` library upang suminghot ng UDP packets sa mga port ng Albion Online (5055, 5056, 5058).
*   **Damage Meter Structure:** Kasama ang kinakailangang data structures at UI upang ipakita ang live combat statistics (Damage Done, Healing Done, DPS).
*   **Modern UI:** Binuo gamit ang Flet, nagbibigay ng mabilis, parang native na desktop application.
*   **Session Management:** Nagpapahintulot sa pagsisimula, paghinto, pag-reset, at pag-save ng istatistika ng session.

## Mga Kinakailangan (Prerequisites)

*   Python 3.8+
*   **Flet** at **Scapy** libraries.
*   **Root/Administrator Privileges:** Kinakailangan para sa network packet capture.

## Pag-install at Pag-set up (Installation and Setup)

### Opsyon 1: Mabilis na Pag-install (Linux - Inirerekomenda)

Para sa mga gumagamit ng Linux, nagbibigay kami ng mga automated installation script:

```bash
# 1. I-clone ang repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Patakbuhin ang installation script
./install.sh

# 3. Patakbuhin ang application
./run.sh
```

Ang `install.sh` script ay:
- Mag-i-install ng system dependencies (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Gagawa ng Python virtual environment
- Mag-i-install ng lahat ng kinakailangang Python packages (Flet, Scapy)

Ang `run.sh` script ay awtomatikong hihingi ng root privileges at patatakbuhin ang application.

### Opsyon 2: Manwal na Pag-install (Manual Installation)

#### 1. I-install ang System Dependencies

**Sa Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Sa Windows:**

I-install ang Python 3.8+ mula sa [python.org](https://www.python.org/downloads/)

#### 2. I-install ang Python Dependencies

**Sa Linux (gamit ang virtual environment - inirerekomenda):**

```bash
# Gumawa ng virtual environment
python3 -m venv venv

# I-activate ang virtual environment
source venv/bin/activate

# I-install ang dependencies
pip install flet scapy
```

**Sa Linux (system-wide installation):**

```bash
pip3 install flet scapy --break-system-packages
```

**Sa Windows:**

```bash
pip install flet scapy
```

#### 3. Pagpapatakbo ng Application (Running the Application)

Dahil ang network sniffing ay nangangailangan ng mataas na pribilehiyo, kailangan mong patakbuhin ang application bilang root o administrator.

**Sa Linux (may virtual environment):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Sa Linux (system-wide installation):**

```bash
sudo python3 albion_insight/main.py
```

**Sa Windows (Patakbuhin ang Command Prompt/PowerShell bilang Administrator):**

```bash
python albion_insight/main.py
```

Ang application ay magbubukas sa isang native desktop window.

## Paano Gumawa ng Executable (How to Build an Executable)

Ang application ay maaaring i-package sa isang standalone executable gamit ang **PyInstaller**. Nagbibigay-daan ito sa mga gumagamit na patakbuhin ang application nang hindi nag-i-install ng Python o ang mga dependencies nito.

Para sa detalyadong instruksyon sa paggawa ng executables para sa Linux, Windows, at macOS, tingnan ang **[PACKAGING.md](PACKAGING.md)** guide.

### Mabilis na Pagbuo (Quick Build - Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Ang executable ay matatagpuan sa `dist/` folder.

## Estruktura ng Proyekto (Project Structure)

Ang application ay naka-estruktura sa modular components para sa mas mahusay na maintainability at scalability:

| File | Deskripsyon |
| :--- | :--- |
| `albion_insight/core/` | Core logic, network tracking, data models, at protocol decoding. |
| `albion_insight/ui/` | User interface components na binuo gamit ang Flet. |
| `albion_insight/utils/` | Utility functions, configuration, at logging. |
| `albion_insight/__main__.py` | Entry point para sa application. |
| `README.md` | Ang dokumentasyong ito. |
| `README.fil-PH.md` | Ang dokumentasyong ito sa Filipino (Tagalog). |
| `CONTRIBUTING.md` | Mga gabay para sa pag-ambag sa proyekto. |
| `CODE_OF_CONDUCT.md` | Ang Code of Conduct ng proyekto. |
| `SECURITY.md` | Patakaran para sa pag-uulat ng mga kahinaan sa seguridad. |

## Kasalukuyang Katayuan (Real-Time Data)

Kasama na ngayon sa application ang **Photon Protocol Decoding** logic, na isinalin mula sa orihinal na C# project. Nagbibigay-daan ito sa application na iproseso ang real-time na mga kaganapan tulad ng `UpdateMoney`, `UpdateFame`, `KilledPlayer`, at `Died` nang direkta mula sa network traffic.

**Tandaan:** Ang kumpletong pagsasalin ng bawat combat event (tulad ng `CastHit`, `Attack`) ay isang patuloy na pagsisikap. Ang kasalukuyang implementasyon ay nakatuon sa core statistics at ang estruktura para sa Damage Meter. Ang DPS calculation ng Damage Meter ay batay sa mga na-decode na kaganapan.

## Pag-ambag (Contributing)

Tinatanggap namin ang mga kontribusyon mula sa komunidad! Kung ikaw ay isang developer, designer, o isang tagahanga lamang ng Albion Online, maraming paraan upang makatulong na mapabuti ang Albion Insight.

Mangyaring basahin ang aming [Contributing Guidelines](CONTRIBUTING.md) para sa detalyadong impormasyon kung paano mag-ambag sa proyektong ito.

### Mabilis na Simula para sa mga Nag-aambag:

1.  I-fork ang repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  I-clone ang iyong fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Gumawa ng bagong branch: `git checkout -b feature/your-feature-name`
4.  Gawin ang iyong mga pagbabago at i-commit: `git commit -m "Idagdag ang iyong tampok"`
5.  I-push sa iyong fork: `git push origin feature/your-feature-name`
6.  Magbukas ng Pull Request sa pangunahing repository

## Lisensya (License)

Ang proyektong ito ay lisensyado sa ilalim ng MIT License - tingnan ang [LICENSE](LICENSE) file para sa mga detalye.

## Pagkilala (Acknowledgments)

- Orihinal na proyekto: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) ni Triky313
- Binuo gamit ang [Flet](https://flet.dev/) framework
- Network analysis na pinapagana ng [Scapy](https://scapy.net/)

---
*Isang cross-platform na solusyon para sa komunidad ng Albion Online.*
