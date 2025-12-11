# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** er et tværplatformsværktøj (Linux, Windows, macOS) til statistikanalyse for spillet Albion Online, genimplementeret i **Python** ved hjælp af **Flet**-frameworket. Det er designet til at spore realtidsstatistik i spillet, herunder sølv, berømmelse og kampdata (Damage Meter), ved at analysere netværkstrafik.

Dette projekt er et moderne, open source-alternativ til det originale C#/WPF-baserede `AlbionOnline-StatisticsAnalysis`-værktøj, med fokus på kompatibilitet på tværs af platforme og brugervenlighed.

## Funktioner

*   **Tværplatformskompatibilitet:** Kører naturligt på Linux, Windows og macOS.
*   **Realtidssporing:** Bruger `Scapy`-biblioteket til at sniffe UDP-pakker på Albion Online-porte (5055, 5056, 5058).
*   **Skadesmålerstruktur (Damage Meter):** Inkluderer de nødvendige datastrukturer og brugerflade til at vise live kampstatistik (Udført Skade, Udført Heling, DPS).
*   **Moderne Brugerflade:** Bygget med Flet, hvilket giver en hurtig, indbygget-lignende desktop-applikation.
*   **Sessionsstyring:** Tillader start, stop, nulstilling og lagring af sessionsstatistik.

## Forudsætninger

*   Python 3.8+
*   **Flet** og **Scapy** biblioteker.
*   **Root/Administratorrettigheder:** Nødvendigt for netværkspakkefangst.

## Installation og Opsætning

### Mulighed 1: Hurtig Installation (Linux - Anbefalet)

For Linux-brugere tilbyder vi automatiserede installationsscripts:

\`\`\`bash
# 1. Klon repository'et
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kør installationsscriptet
./install.sh

# 3. Kør applikationen
./run.sh
\`\`\`

`install.sh`-scriptet vil:
- Installere systemafhængigheder (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Oprette et virtuelt Python-miljø
- Installere alle nødvendige Python-pakker (Flet, Scapy)

`run.sh`-scriptet vil automatisk anmode om root-rettigheder og køre applikationen.

### Mulighed 2: Manuel Installation

#### 1. Installer Systemafhængigheder

**På Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**På Windows:**

Installer Python 3.8+ fra [python.org](https://www.python.org/downloads/)

#### 2. Installer Python-afhængigheder

**På Linux (ved brug af virtuelt miljø - anbefalet):**

\`\`\`bash
# Opret virtuelt miljø
python3 -m venv venv

# Aktiver virtuelt miljø
source venv/bin/activate

# Installer afhængigheder
pip install flet scapy
\`\`\`

**På Linux (systemdækkende installation):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**På Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Kør Applikationen

Da netværkssniffing kræver forhøjede rettigheder, skal du køre applikationen som root eller administrator.

**På Linux (med virtuelt miljø):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**På Linux (systemdækkende installation):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**På Windows (Kør Kommandoprompt/PowerShell som administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

Applikationen åbnes i et indbygget desktop-vindue.

## Hvordan man bygger en eksekverbar fil

Applikationen kan pakkes til en selvstændig eksekverbar fil ved hjælp af **PyInstaller**. Dette giver brugerne mulighed for at køre applikationen uden at installere Python eller dets afhængigheder.

For detaljerede instruktioner om bygning af eksekverbare filer til Linux, Windows og macOS, se guiden **[PACKAGING.md](PACKAGING.md)**.

### Hurtig Bygning (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Den eksekverbare fil vil være placeret i mappen `dist/`.

## Projektstruktur

Applikationen er struktureret i modulære komponenter for bedre vedligeholdelse og skalerbarhed:

| Fil | Beskrivelse |
| :--- | :--- |
| `albion_insight/core/` | Kernlogik, netværkssporing, datamodeller og protokolafkodning. |
| `albion_insight/ui/` | Brugerfladekomponenter bygget med Flet. |
| `albion_insight/utils/` | Hjælpefunktioner, konfiguration og logning. |
| `albion_insight/__main__.py` | Indgangspunkt for applikationen. |
| `README.md` | Denne dokumentationsfil. |
| `CONTRIBUTING.md` | Retningslinjer for bidrag til projektet. |
| `CODE_OF_CONDUCT.md` | Projektets adfærdskodeks. |
| `SECURITY.md` | Politik for rapportering af sikkerhedssårbarheder. |
| `README.it-IT.md` | Dokumentation på italiensk. |
| `README.pt-BR.md` | Dokumentation på brasiliansk portugisisk. |
| `README.ru-RU.md` | Dokumentation på russisk. |
| `README.fr-FR.md` | Dokumentation på fransk. |
| `README.zh-CN.md` | Dokumentation på forenklet kinesisk. |
| `README.ko-KR.md` | Dokumentation på koreansk. |
| `README.es-ES.md` | Dokumentation på spansk. |
| `README.de-DE.md` | Dokumentation på tysk. |
| `README.pl-PL.md` | Dokumentation på polsk. |
| `README.sv-SE.md` | Dokumentation på svensk. |
| `README.vi-VN.md` | Dokumentation på vietnamesisk. |
| `README.ar-SA.md` | Dokumentation på arabisk. |
| `README.pt-PT.md` | Dokumentation på europæisk portugisisk. |
| `README.hi-IN.md` | Dokumentation på hindi. |
| `README.hu-HU.md` | Dokumentation på ungarsk. |
| `README.th-TH.md` | Dokumentation på thai. |
| `README.ja-JP.md` | Dokumentation på japansk. |
| `README.tr-TR.md` | Dokumentation på tyrkisk. |
| `README.id-ID.md` | Dokumentation på indonesisk. |
| `README.cs-CZ.md` | Dokumentation på tjekkisk. |
| `README.fi-FI.md` | Dokumentation på finsk. |
| `README.nl-NL.md` | Dokumentation på nederlandsk. |
| `README.no-NO.md` | Dokumentation på norsk (Bokmål). |
| `README.da-DK.md` | Dokumentation på dansk. |

## Aktuel Status (Realtidsdata)

Applikationen inkluderer nu logikken for **Photon Protocol Decoding**, oversat fra det originale C#-projekt. Dette gør det muligt for applikationen at behandle realtidsbegivenheder som `UpdateMoney`, `UpdateFame`, `KilledPlayer` og `Died` direkte fra netværkstrafikken.

**Bemærk:** Den fulde oversættelse af hver enkelt kampbegivenhed (som `CastHit`, `Attack`) er et igangværende arbejde. Den nuværende implementering fokuserer på kernestatistikken og strukturen for Skadesmåleren. Skadesmålerens DPS-beregning er baseret på de afkodede begivenheder.

## Bidrag

Vi byder bidrag fra fællesskabet velkommen! Uanset om du er udvikler, designer eller bare en Albion Online-entusiast, er der mange måder at hjælpe med at forbedre Albion Insight.

Læs venligst vores [Retningslinjer for Bidrag](CONTRIBUTING.md) for detaljeret information om, hvordan du bidrager til dette projekt.

### Hurtig Start for Bidragydere:

1.  Fork repository'et: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klon din fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Opret en ny gren: `git checkout -b feature/dit-funktionsnavn`
4.  Foretag dine ændringer og commit: `git commit -m "Tilføj din funktion"`
5.  Push til din fork: `git push origin feature/dit-funktionsnavn`
6.  Åbn en Pull Request på hovedrepository'et

## Licens

Dette projekt er licenseret under MIT-licensen - se filen [LICENSE](LICENSE) for detaljer.

## Anerkendelser

- Originalt projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) af Triky313
- Bygget med [Flet](https://flet.dev/)-frameworket
- Netværksanalyse drevet af [Scapy](https://scapy.net/)

---
*En tværplatformsløsning for Albion Online-fællesskabet.*
