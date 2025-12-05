# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** är ett plattformsoberoende (Linux, Windows, macOS) statistikverktyg för spelet Albion Online, omimplementerat i **Python** med **Flet**-ramverket. Det är utformat för att spåra statistik i realtid i spelet, inklusive silver, fame och stridsdata (Damage Meter), genom att analysera nätverkstrafik.

Detta projekt är ett modernt, öppen källkods-alternativ till det ursprungliga C#/WPF-baserade verktyget `AlbionOnline-StatisticsAnalysis`, med fokus på kompatibilitet över flera plattformar och användarvänlighet.

## Funktioner

*   **Plattformsoberoende Kompatibilitet:** Körs nativt på Linux, Windows och macOS.
*   **Spårning i Realtid:** Använder `Scapy`-biblioteket för att sniffa UDP-paket på Albion Online-portar (5055, 5056, 5058).
*   **Damage Meter Struktur:** Inkluderar nödvändiga datastrukturer och användargränssnitt för att visa live stridsstatistik (Utdelad Skada, Läkt, DPS).
*   **Modernt Användargränssnitt:** Byggt med Flet, vilket ger en snabb, nativ-liknande skrivbordsapplikation.
*   **Sessionshantering:** Tillåter start, stopp, återställning och sparande av sessionsstatistik.

## Förutsättningar

*   Python 3.8+
*   **Flet** och **Scapy** bibliotek.
*   **Root/Administratörsrättigheter:** Nödvändigt för nätverkspaketfångst.

## Installation och Konfiguration

### Alternativ 1: Snabbinstallation (Linux - Rekommenderas)

För Linux-användare tillhandahåller vi automatiserade installationsskript:

```bash
# 1. Klona repot
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kör installationsskriptet
./install.sh

# 3. Kör applikationen
./run.sh
```

Skriptet `install.sh` kommer att:
- Installera systemberoenden (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Skapa en virtuell Python-miljö
- Installera alla nödvändiga Python-paket (Flet, Scapy)

Skriptet `run.sh` kommer automatiskt att begära root-rättigheter och köra applikationen.

### Alternativ 2: Manuell Installation

#### 1. Installera Systemberoenden

**På Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**På Windows:**

Installera Python 3.8+ från [python.org](https://www.python.org/downloads/)

#### 2. Installera Python-beroenden

**På Linux (med virtuell miljö - rekommenderas):**

```bash
# Skapa virtuell miljö
python3 -m venv venv

# Aktivera virtuell miljö
source venv/bin/activate

# Installera beroenden
pip install flet scapy
```

**På Linux (systemomfattande installation):**

```bash
pip3 install flet scapy --break-system-packages
```

**På Windows:**

```bash
pip install flet scapy
```

#### 3. Köra Applikationen

Eftersom nätverkssniffning kräver förhöjda privilegier måste du köra applikationen som root eller administratör.

**På Linux (med virtuell miljö):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**På Linux (systemomfattande installation):**

```bash
sudo python3 -m albion_insight
```

**På Windows (Kör Kommandotolken/PowerShell som Administratör):**

```bash
python -m albion_insight
```

Applikationen öppnas i ett nativt skrivbordsfönster.

## Hur man bygger en Körbar Fil (Executable)

Applikationen kan paketeras till en fristående körbar fil med hjälp av **PyInstaller**. Detta gör att användare kan köra applikationen utan att installera Python eller dess beroenden.

För detaljerade instruktioner om hur man bygger körbara filer för Linux, Windows och macOS, se guiden **[PACKAGING.md](PACKAGING.md)**.

### Snabbbygge (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Den körbara filen kommer att finnas i mappen `dist/`.

## Projektstruktur

Applikationen är strukturerad i modulära komponenter för bättre underhållbarhet och skalbarhet:

| Fil | Beskrivning |
| :--- | :--- |
| `albion_insight/core/` | Kärnlogik, nätverksspårning, datamodeller och protokollavkodning. |
| `albion_insight/ui/` | Användargränssnittskomponenter byggda med Flet. |
| `albion_insight/utils/` | Verktygsfunktioner, konfiguration och loggning. |
| `albion_insight/__main__.py` | Startpunkt för applikationen. |
| `README.md` | Denna dokumentationsfil. |
| `CONTRIBUTING.md` | Riktlinjer för att bidra till projektet. |
| `CODE_OF_CONDUCT.md` | Projektets uppförandekod. |
| `SECURITY.md` | Policy för rapportering av säkerhetsbrister. |
| `README.sv-SE.md` | Dokumentation på svenska. |

## Aktuell Status (Realtidsdata)

Applikationen inkluderar nu logiken för **Photon Protokollavkodning**, översatt från det ursprungliga C#-projektet. Detta gör att applikationen kan bearbeta händelser i realtid som `UpdateMoney`, `UpdateFame`, `KilledPlayer` och `Died` direkt från nätverkstrafiken.

**Obs:** Den fullständiga översättningen av varje enskild stridshändelse (som `CastHit`, `Attack`) är ett pågående arbete. Den nuvarande implementeringen fokuserar på kärnstatistiken och strukturen för Damage Meter. Damage Meters DPS-beräkning baseras på de avkodade händelserna.

## Bidra

Vi välkomnar bidrag från communityn! Oavsett om du är en utvecklare, designer eller bara en Albion Online-entusiast, finns det många sätt att hjälpa till att förbättra Albion Insight.

Vänligen läs våra [Bidragsriktlinjer](CONTRIBUTING.md) för detaljerad information om hur du bidrar till detta projekt.

### Snabbstart för Bidragsgivare:

1.  Fork repot: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klona din fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Skapa en ny gren: `git checkout -b feature/your-feature-name`
4.  Gör dina ändringar och committa: `git commit -m "Lägg till din funktion"`
5.  Pusha till din fork: `git push origin feature/your-feature-name`
6.  Öppna en Pull Request i huvudrepot

## Licens

Detta projekt är licensierat under MIT-licensen - se filen [LICENSE](LICENSE) för detaljer.

## Tack

- Ursprungligt projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) av Triky313
- Byggt med [Flet](https://flet.dev/) ramverket
- Nätverksanalys drivs av [Scapy](https://scapy.net/)

---
*En plattformsoberoende lösning för Albion Online-communityn.*
