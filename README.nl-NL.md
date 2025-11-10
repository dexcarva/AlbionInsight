# Albion Insight

[![Licentie: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versie](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Bijdragen Welkom](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Lees dit in het Duits (Lesen Sie dies auf Deutsch)](README.de-DE.md)**
**[Lees dit in het Portugees (Leia em Português)](README.pt-BR.md)**
**[Lees dit in het Spaans (Leer en Español)](README.es-ES.md)**
**[Lees dit in het Frans (Lire en Français)](README.fr-FR.md)**
**[Lees dit in het Italiaans (Leggi in Italiano)](README.it-IT.md)**
**[Lees dit in het Vereenvoudigd Chinees (阅读简体中文)](README.zh-CN.md)**
**[Lees dit in het Russisch (Прочитать на русском)](README.ru-RU.md)**
**[Lees dit in het Japans (日本語で読む)](README.ja-JP.md)**
**[Lees dit in het Arabisch (اقرأ هذا بالعربية)](README.ar-SA.md)**
**[Lees dit in het Turks (Türkçe Oku)](README.tr-TR.md)**
**[Lees dit in het Koreaans (한국어로 읽기)](README.ko-KR.md)**
**[Lees dit in het Nederlands](README.nl-NL.md)**

**Albion Insight** is een cross-platform (Linux, Windows, macOS) statistieken-analysetool voor het spel Albion Online, opnieuw geïmplementeerd in **Python** met behulp van het **Flet** framework. Het is ontworpen om real-time in-game statistieken bij te houden, inclusief zilver, roem en gevechtsgegevens (Damage Meter), door netwerkverkeer te analyseren.

Dit project is een modern, open-source alternatief voor de originele C#/WPF-gebaseerde `AlbionOnline-StatisticsAnalysis` tool, met een focus op multi-platform compatibiliteit en gebruiksgemak.

## Functies

*   **Cross-Platform Compatibiliteit:** Draait native op Linux, Windows en macOS.
*   **Real-Time Tracking:** Gebruikt de `Scapy` bibliotheek om UDP-pakketten te sniffen op Albion Online-poorten (5055, 5056, 5058).
*   **Damage Meter Structuur:** Bevat de benodigde datastructuren en UI om live gevechtsstatistieken weer te geven (Veroorzaakte Schade, Genezing, DPS).
*   **Moderne UI:** Gebouwd met Flet, wat zorgt voor een snelle, native-ogende desktopapplicatie.
*   **Sessiebeheer:** Maakt het mogelijk om sessiestatistieken te starten, stoppen, resetten en op te slaan.

## Vereisten

*   Python 3.8+
*   **Flet** en **Scapy** bibliotheken.
*   **Root/Administrator Rechten:** Noodzakelijk voor het vastleggen van netwerkpakketten.

## Installatie en Configuratie

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

Het `run.sh` script zal automatisch rootrechten aanvragen en de applicatie uitvoeren.

### Optie 2: Handmatige Installatie

#### 1. Installeer Systeemafhankelijkheden

**Op Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Op Windows:**

Installeer Python 3.8+ van [python.org](https://www.python.org/downloads/)

#### 2. Installeer Python-afhankelijkheden

**Op Linux (met virtuele omgeving - aanbevolen):**

```bash
# Creëer virtuele omgeving
python3 -m venv venv

# Activeer virtuele omgeving
source venv/bin/activate

# Installeer afhankelijkheden
pip install flet scapy
```

**Op Linux (systeembrede installatie):**

```bash
pip3 install flet scapy --break-system-packages
```

**Op Windows:**

```bash
pip install flet scapy
```

#### 3. De Applicatie Uitvoeren

Omdat het sniffen van netwerkverkeer verhoogde rechten vereist, moet u de applicatie als root of administrator uitvoeren.

**Op Linux (met virtuele omgeving):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Op Linux (systeembrede installatie):**

```bash
sudo python3 albion_insight/main.py
```

**Op Windows (Voer Command Prompt/PowerShell uit als Administrator):**

```bash
python albion_insight/main.py
```

The application will open in a native desktop window.

## Hoe een Uitvoerbaar Bestand te Bouwen

De applicatie kan worden verpakt in een zelfstandig uitvoerbaar bestand met **PyInstaller**. Dit stelt gebruikers in staat om de applicatie uit te voeren zonder Python of de bijbehorende afhankelijkheden te installeren.

Voor gedetailleerde instructies over het bouwen van uitvoerbare bestanden voor Linux, Windows en macOS, zie de **[PACKAGING.md](PACKAGING.md)** gids.

### Snelle Bouw (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Het uitvoerbare bestand bevindt zich in de `dist/` map.

## Projectstructuur

De volledige applicatie is voor de eenvoud in één enkel bestand opgenomen:

| Bestand | Beschrijving |
| :--- | :--- |
| `albion_insight/main.py` | Het hoofdbestand van de applicatie met alle logica (Modellen, Netwerk Tracker, Flet UI). |
|| `README.md` | Dit documentatiebestand. |
| `README.pt-BR.md` | Dit documentatiebestand in het Braziliaans Portugees. |
| `CONTRIBUTING.md` | Richtlijnen voor bijdragen aan het project. |
| `CODE_OF_CONDUCT.md` | De gedragscode van het project. |
| `SECURITY.md` | Beleid voor het melden van beveiligingskwetsbaarheden. |

## Huidige Status (Real-Time Gegevens)

De applicatie bevat nu de **Photon Protocol Decoding** logica, vertaald vanuit het originele C# project. Dit stelt de applicatie in staat om real-time gebeurtenissen zoals `UpdateMoney`, `UpdateFame`, `KilledPlayer` en `Died` rechtstreeks uit het netwerkverkeer te verwerken.

**Opmerking:** De volledige vertaling van elke afzonderlijke gevechtsgebeurtenis (zoals `CastHit`, `Attack`) is een doorlopend proces. De huidige implementatie richt zich op de kernstatistieken en de structuur voor de Damage Meter. De DPS-berekening van de Damage Meter is gebaseerd op de gedecodeerde gebeurtenissen.

## Bijdragen

We verwelkomen bijdragen van de gemeenschap! Of je nu een ontwikkelaar, ontwerper of gewoon een Albion Online-liefhebber bent, er zijn veel manieren om Albion Insight te helpen verbeteren.

Lees onze [Richtlijnen voor Bijdragen](CONTRIBUTING.md) voor gedetailleerde informatie over hoe u kunt bijdragen aan dit project.

### Snelstart voor Bijdragers:

1.  Fork de repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Kloon je fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Maak een nieuwe tak: `git checkout -b feature/your-feature-name`
4.  Maak je wijzigingen en commit: `git commit -m "Add your feature"`
5.  Push naar je fork: `git push origin feature/your-feature-name`
6.  Open een Pull Request op de hoofdrepository

## Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het [LICENSE](LICENSE) bestand voor details.

## Erkenningen

- Origineel project: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) door Triky313
- Gebouwd met [Flet](https://flet.dev/) framework
- Netwerkanalyse aangedreven door [Scapy](https://scapy.net/)

---
*Een cross-platform oplossing voor de Albion Online-gemeenschap.*
