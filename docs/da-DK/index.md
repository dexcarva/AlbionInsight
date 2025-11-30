# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Læs dette på andre sprog</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)** | **[Finnish](README.fi-FI.md)** | **[Polish](README.pl-PL.md)** | **[Danish](README.da-DK.md)**
</details>

**Albion Insight** er et krydsplatform (Linux, Windows, macOS) statistik-analyseværktøj til spillet Albion Online, genimplementeret i **Python** ved hjælp af **Flet**-rammeværket. Det er designet til at spore realtidsstatistik i spillet, herunder sølv, berømmelse og kampdata (Skademåler), ved at analysere netværkstrafik.

Dette projekt er et moderne, open source-alternativ til det originale C#/WPF-baserede `AlbionOnline-StatisticsAnalysis`-værktøj, med fokus på multi-platformskompatibilitet og brugervenlighed.

## Funktioner

*   **Krydsplatformskompatibilitet:** Kører naturligt på Linux, Windows og macOS.
*   **Realtidssporing:** Bruger `Scapy`-biblioteket til at sniffe UDP-pakker på Albion Online-porte (5055, 5056, 5058).
*   **Skademålerstruktur:** Inkluderer de nødvendige datastrukturer og UI til at vise live kampstatistik (Uddelt Skade, Udført Helbredelse, DPS).
*   **Moderne UI:** Bygget med Flet, hvilket giver en hurtig, indbygget-lignende desktop-applikation.
*   **Sessionsstyring:** Tillader start, stop, nulstilling og lagring af sessionsstatistik.

## Forudsætninger

*   Python 3.8+
*   **Flet** og **Scapy** biblioteker.
*   **Root/Administratorrettigheder:** Nødvendigt for netværkspakkefangst.

## Installation og Opsætning

### Mulighed 1: Hurtig Installation (Linux - Anbefalet)

For Linux-brugere tilbyder vi automatiserede installationsscripts:

```bash
# 1. Klon depotet
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kør installationsscriptet
./install.sh

# 3. Kør applikationen
./run.sh
```

`install.sh`-scriptet vil:
- Installere systemafhængigheder (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Oprette et Python virtuelt miljø
- Installere alle nødvendige Python-pakker (Flet, Scapy)

`run.sh`-scriptet vil automatisk anmode om root-rettigheder og køre applikationen.

### Mulighed 2: Manuel Installation

#### 1. Installer Systemafhængigheder

**På Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**På Windows:**

Installer Python 3.8+ fra [python.org](https://www.python.org/downloads/)

#### 2. Installer Python-afhængigheder

**På Linux (bruger virtuelt miljø - anbefalet):**

```bash
# Opret virtuelt miljø
python3 -m venv venv

# Aktiver virtuelt miljø
source venv/bin/activate

# Installer afhængigheder
pip install flet scapy
```

**På Linux (systemdækkende installation):**

```bash
pip3 install flet scapy --break-system-packages
```

**På Windows:**

```bash
pip install flet scapy
```

#### 3. Kørsel af Applikationen

Da netværkssniffing kræver forhøjede rettigheder, skal du køre applikationen som root eller administrator.

**På Linux (med virtuelt miljø):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**På Linux (systemdækkende installation):**

```bash
sudo python3 -m albion_insight
```

**På Windows (Kør kommandoprompt/PowerShell som administrator):**

```bash
python -m albion_insight
```

Applikationen åbnes i et indbygget desktop-vindue.

## Hvordan man bygger en eksekverbar fil

Applikationen kan pakkes i en selvstændig eksekverbar fil ved hjælp af **PyInstaller**. Dette giver brugerne mulighed for at køre applikationen uden at installere Python eller dens afhængigheder.

For detaljerede instruktioner om bygning af eksekverbare filer til Linux, Windows og macOS, se **[PACKAGING.md](PACKAGING.md)** guiden.

### Hurtig Bygning (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Den eksekverbare fil vil være placeret i `dist/`-mappen.

## Projektstruktur

Applikationen er struktureret i modulære komponenter for bedre vedligeholdelighed og skalerbarhed:

| Fil | Beskrivelse |
| :--- | :--- |
| `albion_insight/core/` | Kernlogik, netværkssporing, datamodeller og protokolafkodning. |
| `albion_insight/ui/` | Brugergrænsefladekomponenter bygget med Flet. |
| `albion_insight/utils/` | Hjælpefunktioner, konfiguration og logning. |
| `albion_insight/__main__.py` | Indgangspunkt for applikationen. |
| `README.md` | Denne dokumentationsfil. |
| `README.pt-BR.md` | Denne dokumentationsfil på brasiliansk portugisisk. |
| `README.fil-PH.md` | Denne dokumentationsfil på filippinsk (tagalog). |
| `README.pt-PT.md` | Denne dokumentationsfil på portugisisk (Portugal). |
| `README.sv-SE.md` | Denne dokumentationsfil på svensk. |
| `README.no-NO.md` | Denne dokumentationsfil på norsk. |
| `README.ko-KR.md` | Denne dokumentationsfil på koreansk. |
| `README.da-DK.md` | Denne dokumentationsfil på dansk. |
| `CONTRIBUTING.sv-SE.md` | Retningslinjer for bidrag til projektet på svensk. |
| `CONTRIBUTING.md` | Retningslinjer for bidrag til projektet. |
| `CODE_OF_CONDUCT.md` | Projektets etiske retningslinjer. |
| `SECURITY.md` | Retningslinjer for rapportering af sikkerhedssårbarheder. |

## Nuværende Status (Realtidsdata)

Applikationen inkluderer nu **Photon Protocol Decoding**-logikken, oversat fra det originale C#-projekt. Dette gør det muligt for applikationen at behandle realtidsbegivenheder som `UpdateMoney`, `UpdateFame`, `KilledPlayer` og `Died` direkte fra netværkstrafikken.

**Bemærk:** Den fulde oversættelse af hver enkelt kampbegivenhed (som `CastHit`, `Attack`) er en igangværende indsats. Den nuværende implementering fokuserer på kernestatistikken og strukturen for Skademåleren. Skademålerens DPS-beregning er baseret på de afkodede begivenheder.

## Bidrag

Vi byder bidrag fra fællesskabet velkommen! Uanset om du er udvikler, designer eller bare en Albion Online-entusiast, er der mange måder at hjælpe med at forbedre Albion Insight.

Læs venligst vores [Retningslinjer for Bidrag](CONTRIBUTING.md) for detaljeret information om, hvordan du bidrager til dette projekt.

### Hurtig Start for Bidragydere:

1.  Fork depotet: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klon din fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Opret en ny gren: `git checkout -b feature/your-feature-name`
4.  Foretag dine ændringer og commit: `git commit -m "Add your feature"`
5.  Push til din fork: `git push origin feature/your-feature-name`
6.  Åbn en Pull Request på hoveddepotet

## Licens

Dette projekt er licenseret under MIT-licensen - se [LICENSE](LICENSE)-filen for detaljer.

## Anerkendelser

- Originalt projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) af Triky313
- Bygget med [Flet](https://flet.dev/) rammeværk
- Netværksanalyse drevet af [Scapy](https://scapy.net/)

---
*En krydsplatformsløsning for Albion Online-fællesskabet.*
