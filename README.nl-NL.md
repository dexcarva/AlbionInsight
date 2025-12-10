# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** is een platformonafhankelijke (Linux, Windows, macOS) statistiekanalyse-tool voor het spel Albion Online, opnieuw geïmplementeerd in **Python** met behulp van het **Flet** framework. Het is ontworpen om real-time in-game statistieken, waaronder zilver, roem en gevechtsgegevens (Damage Meter), bij te houden door netwerkverkeer te analyseren.

Dit project is een modern, open-source alternatief voor de originele C#/WPF-gebaseerde `AlbionOnline-StatisticsAnalysis` tool, met de nadruk op multi-platform compatibiliteit en gebruiksgemak.

## Functies

*   **Platformonafhankelijke Compatibiliteit:** Draait native op Linux, Windows en macOS.
*   **Real-Time Tracking:** Gebruikt de `Scapy` bibliotheek om UDP-pakketten op Albion Online poorten (5055, 5056, 5058) te sniffen.
*   **Damage Meter Structuur:** Bevat de nodige datastructuren en UI om live gevechtsstatistieken weer te geven (Toegebrachte Schade, Toegebrachte Genezing, DPS).
*   **Moderne UI:** Gebouwd met Flet, wat een snelle, native-uitziende desktopapplicatie biedt.
*   **Sessiebeheer:** Maakt het mogelijk om sessiestatistieken te starten, stoppen, resetten en op te slaan.

## Vereisten

*   Python 3.8+
*   **Flet** en **Scapy** bibliotheken.
*   **Root/Administrator Rechten:** Noodzakelijk voor het vastleggen van netwerkpakketten.

## Installatie en Setup

### Optie 1: Snelle Installatie (Linux - Aanbevolen)

Voor Linux-gebruikers bieden we geautomatiseerde installatiescripts:

\`\`\`bash
# 1. Kloon de repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Voer het installatiescript uit
./install.sh

# 3. Voer de applicatie uit
./run.sh
\`\`\`

Het `install.sh` script zal:
- Systeemafhankelijkheden installeren (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Een Python virtuele omgeving creëren
- Alle vereiste Python-pakketten installeren (Flet, Scapy)

Het `run.sh` script zal automatisch root-rechten aanvragen en de applicatie uitvoeren.

### Optie 2: Handmatige Installatie

#### 1. Installeer Systeemafhankelijkheden

**Op Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Op Windows:**

Installeer Python 3.8+ van [python.org](https://www.python.org/downloads/)

#### 2. Installeer Python Afhankelijkheden

**Op Linux (met virtuele omgeving - aanbevolen):**

\`\`\`bash
# Creëer virtuele omgeving
python3 -m venv venv

# Activeer virtuele omgeving
source venv/bin/activate

# Installeer afhankelijkheden
pip install flet scapy
\`\`\`

**Op Linux (systeemwijde installatie):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Op Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. De Applicatie Uitvoeren

Aangezien netwerk sniffing verhoogde rechten vereist, moet u de applicatie als root of beheerder uitvoeren.

**Op Linux (met virtuele omgeving):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Op Linux (systeemwijde installatie):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Op Windows (Voer Command Prompt/PowerShell uit als Beheerder):**

\`\`\`bash
python -m albion_insight
\`\`\`

De applicatie zal openen in een native desktopvenster.

## Hoe een Executable te Bouwen

De applicatie kan worden verpakt in een op zichzelf staande executable met behulp van **PyInstaller**. Dit stelt gebruikers in staat de applicatie uit te voeren zonder Python of de afhankelijkheden te installeren.

Voor gedetailleerde instructies over het bouwen van executables voor Linux, Windows en macOS, zie de **[PACKAGING.md](PACKAGING.md)** gids.

### Snelle Build (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

De executable zal zich in de map `dist/` bevinden.

## Projectstructuur

De applicatie is gestructureerd in modulaire componenten voor betere onderhoudbaarheid en schaalbaarheid:

| Bestand | Beschrijving |
| :--- | :--- |
| `albion_insight/core/` | Kernlogica, netwerk tracking, datamodellen en protocol decodering. |
| `albion_insight/ui/` | Gebruikersinterface componenten gebouwd met Flet. |
| `albion_insight/utils/` | Utility functies, configuratie en logging. |
| `albion_insight/__main__.py` | Toegangspunt voor de applicatie. |
| `README.md` | Dit documentatiebestand. |
| `CONTRIBUTING.md` | Richtlijnen voor het bijdragen aan het project. |
| `CODE_OF_CONDUCT.md` | De gedragscode van het project. |
| `SECURITY.md` | Beleid voor het melden van beveiligingslekken. |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档 (Simplified Chinese documentation). |
| `README.ko-KR.md` | 한국어 문서 (Korean documentation). |
| `README.es-ES.md` | Documentación en español (Spanish documentation). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (German documentation). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |
| `README.sv-SE.md` | Dokumentation på svenska (Swedish documentation). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnamese documentation). |
| `README.ar-SA.md` | توثيق باللغة العربية (Arabic documentation). |
| `README.pt-PT.md` | Documentação em português europeu. |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Hindi documentation). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Hungarian documentation). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Thai documentation). |
| `README.ja-JP.md` | 日本語のドキュメント (Japanese documentation). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Turkish documentation). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia. |
| `README.cs-CZ.md` | Dokumentace v češtině (Czech documentation). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Dutch documentation). |

## Huidige Status (Real-Time Data)

De applicatie bevat nu de **Photon Protocol Decoding** logica, vertaald vanuit het originele C# project. Dit stelt de applicatie in staat om real-time gebeurtenissen zoals `UpdateMoney`, `UpdateFame`, `KilledPlayer` en `Died` direct vanuit het netwerkverkeer te verwerken.

**Opmerking:** De volledige vertaling van elk gevechtsevenement (zoals `CastHit`, `Attack`) is een doorlopende inspanning. De huidige implementatie richt zich op de kernstatistieken en de structuur voor de Damage Meter. De DPS-berekening van de Damage Meter is gebaseerd op de gedecodeerde gebeurtenissen.

## Bijdragen

We verwelkomen bijdragen van de gemeenschap! Of u nu een ontwikkelaar, ontwerper of gewoon een Albion Online-enthousiasteling bent, er zijn veel manieren om Albion Insight te helpen verbeteren.

Lees onze [Richtlijnen voor Bijdragen](CONTRIBUTING.md) voor gedetailleerde informatie over hoe u kunt bijdragen aan dit project.

### Snelle Start voor Bijdragers:

1.  Fork de repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Kloon uw fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Creëer een nieuwe branch: `git checkout -b feature/uw-functie-naam`
4.  Voer uw wijzigingen door en commit: `git commit -m "Voeg uw functie toe"`
5.  Push naar uw fork: `git push origin feature/uw-functie-naam`
6.  Open een Pull Request op de hoofdrepository

## Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het [LICENSE](LICENSE) bestand voor details.

## Erkenningen

- Origineel project: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) door Triky313
- Gebouwd met [Flet](https://flet.dev/) framework
- Netwerkanalyse aangedreven door [Scapy](https://scapy.net/)

---
*Een platformonafhankelijke oplossing voor de Albion Online-gemeenschap.*
