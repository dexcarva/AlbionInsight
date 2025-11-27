# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Lees dit in andere talen</summary>

**[Arabisch](README.ar-SA.md)** | **[Duits](README.de-DE.md)** | **[Grieks](README.el-GR.md)** | **[Spaans](README.es-ES.md)** | **[Frans](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hongaars](README.hu-HU.md)** | **[Indonesisch](README.id-ID.md)** | **[Italiaans](README.it-IT.md)** | **[Japans](README.ja-JP.md)** | **[Koreaans](README.ko-KR.md)** | **[Nederlands](README.nl-NL.md)** | **[Pools](README.pl-PL.md)** | **[Portugees (Brazilië)](README.pt-BR.md)** | **[Roemeens](README.ro-RO.md)** | **[Russisch](README.ru-RU.md)** | **[Zweeds](README.sv-SE.md)** | **[Thais](README.th-TH.md)** | **[Turks](README.tr-TR.md)** | **[Vietnamees](README.vi-VN.md)** | **[Chinees (Vereenvoudigd)](README.zh-CN.md)** | **[Chinees (Traditioneel)](README.zh-TW.md)** | **[Chinees (Traditioneel - Hong Kong)](README.zh-HK.md)** | **[Tsjechisch](README.cs-CZ.md)** | **[Perzisch (Farsi)](README.fa-IR.md)** | **[Filipijns (Tagalog)](README.fil-PH.md)** | **[Portugees (Portugal)](README.pt-PT.md)** | **[Hebreeuws](README.he-IL.md)** | **[Noors](README.no-NO.md)** | **[Fins](README.fi-FI.md)** | **[Pools](README.pl-PL.md)**

</details>

**Albion Insight** is een platformonafhankelijke (Linux, Windows, macOS) statistische analysetool voor het spel Albion Online, opnieuw geïmplementeerd in **Python** met behulp van het **Flet** framework. Het is ontworpen om real-time in-game statistieken, waaronder zilver, roem en gevechtsgegevens (Damage Meter), bij te houden door netwerkverkeer te analyseren.

Dit project is een modern, open-source alternatief voor de originele C#/WPF-gebaseerde `AlbionOnline-StatisticsAnalysis` tool, met de nadruk op multi-platform compatibiliteit en gebruiksgemak.

## Functies

*   **Platformonafhankelijke Compatibiliteit:** Draait native op Linux, Windows en macOS.
*   **Real-Time Tracking:** Gebruikt de `Scapy` bibliotheek om UDP-pakketten te sniffen op Albion Online poorten (5055, 5056, 5058).
*   **Damage Meter Structuur:** Bevat de nodige datastructuren en UI om live gevechtsstatistieken (Toegebrachte Schade, Genezing, DPS) weer te geven.
*   **Moderne UI:** Gebouwd met Flet, wat zorgt voor een snelle, native-uitziende desktopapplicatie.
*   **Sessiebeheer:** Maakt het starten, stoppen, resetten en opslaan van sessiestatistieken mogelijk.

## Vereisten

*   Python 3.8+
*   **Flet** en **Scapy** bibliotheken.
*   **Root/Administrator Rechten:** Noodzakelijk voor het vastleggen van netwerkpakketten.

## Installatie en Setup

### Optie 1: Snelle Installatie (Linux - Aanbevolen)

Voor Linux-gebruikers bieden we geautomatiseerde installatiescripts:

```bash
# 1. Kloon de repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Voer het installatiescript uit
./install.sh

# 3. Voer de applicatie uit
./run.sh
```

Het `install.sh` script zal:
- Systeemafhankelijkheden installeren (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Een Python virtuele omgeving creëren
- Alle vereiste Python-pakketten installeren (Flet, Scapy)

Het `run.sh` script zal automatisch root-rechten aanvragen en de applicatie uitvoeren.

### Optie 2: Handmatige Installatie

#### 1. Installeer Systeemafhankelijkheden

**Op Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Op Windows:**

Installeer Python 3.8+ van [python.org](https://www.python.org/downloads/)

#### 2. Installeer Python Afhankelijkheden

**Op Linux (met virtuele omgeving - aanbevolen):**

```bash
# Creëer virtuele omgeving
python3 -m venv venv

# Activeer virtuele omgeving
source venv/bin/activate

# Installeer afhankelijkheden
pip install flet scapy
```

**Op Linux (systeemwijde installatie):**

```bash
pip3 install flet scapy --break-system-packages
```

**Op Windows:**

```bash
pip install flet scapy
```

#### 3. De Applicatie Uitvoeren

Aangezien netwerk sniffing verhoogde rechten vereist, moet u de applicatie als root of beheerder uitvoeren.

**Op Linux (met virtuele omgeving):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Op Linux (systeemwijde installatie):**

```bash
sudo python3 -m albion_insight
```

**Op Windows (Voer Opdrachtprompt/PowerShell uit als Beheerder):**

```bash
python -m albion_insight
```

De applicatie zal openen in een native desktopvenster.

## Hoe een Uitvoerbaar Bestand te Bouwen

De applicatie kan worden verpakt in een standalone uitvoerbaar bestand met behulp van **PyInstaller**. Dit stelt gebruikers in staat om de applicatie uit te voeren zonder Python of de afhankelijkheden te installeren.

Voor gedetailleerde instructies over het bouwen van uitvoerbare bestanden voor Linux, Windows en macOS, zie de **[PACKAGING.md](PACKAGING.md)** gids.

### Snelle Build (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Het uitvoerbare bestand zal zich in de map `dist/` bevinden.

## Projectstructuur

De applicatie is gestructureerd in modulaire componenten voor betere onderhoudbaarheid en schaalbaarheid:

| Bestand | Beschrijving |
| :--- | :--- |
| `albion_insight/core/` | Kernlogica, netwerk tracking, datamodellen en protocol decodering. |
| `albion_insight/ui/` | Gebruikersinterface componenten gebouwd met Flet. |
| `albion_insight/utils/` | Hulpprogrammafuncties, configuratie en logging. |
| `albion_insight/__main__.py` | Startpunt voor de applicatie. |
| `README.md` | Dit documentatiebestand. |
| `README.pt-BR.md` | Dit documentatiebestand in Braziliaans Portugees. |
| `README.fil-PH.md` | Dit documentatiebestand in Filipijns (Tagalog). |
| `README.pt-PT.md` | Dit documentatiebestand in Portugees (Portugal). |
| `README.sv-SE.md` | Dit documentatiebestand in Zweeds. |
| `CONTRIBUTING.sv-SE.md` | Richtlijnen voor het bijdragen aan het project in Zweeds. |
| `CONTRIBUTING.md` | Richtlijnen voor het bijdragen aan het project. |
| `CODE_OF_CONDUCT.md` | De gedragscode van het project. |
| `SECURITY.md` | Beleid voor het melden van beveiligingslekken. |

## Huidige Status (Real-Time Gegevens)

De applicatie bevat nu de **Photon Protocol Decoding** logica, vertaald vanuit het originele C#-project. Dit stelt de applicatie in staat om real-time gebeurtenissen zoals `UpdateMoney`, `UpdateFame`, `KilledPlayer` en `Died` direct vanuit het netwerkverkeer te verwerken.

**Opmerking:** De volledige vertaling van elke afzonderlijke gevechtsgebeurtenis (zoals `CastHit`, `Attack`) is een doorlopende inspanning. De huidige implementatie richt zich op de kernstatistieken en de structuur voor de Damage Meter. De DPS-berekening van de Damage Meter is gebaseerd op de gedecodeerde gebeurtenissen.

## Bijdragen

We verwelkomen bijdragen van de gemeenschap! Of u nu een ontwikkelaar, ontwerper of gewoon een Albion Online-enthousiasteling bent, er zijn veel manieren om Albion Insight te helpen verbeteren.

Lees onze [Bijdrage Richtlijnen](CONTRIBUTING.md) voor gedetailleerde informatie over hoe u kunt bijdragen aan dit project.

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

*   Origineel project: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) door Triky313
*   Gebouwd met [Flet](https://flet.dev/) framework
*   Netwerkanalyse mogelijk gemaakt door [Scapy](https://scapy.net/)

---
*Een platformonafhankelijke oplossing voor de Albion Online-gemeenschap.*
