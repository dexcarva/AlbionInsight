# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** er et plattformuavhengig (Linux, Windows, macOS) verktøy for statistikk-analyse for spillet Albion Online, gjenimplementert i **Python** ved bruk av **Flet**-rammeverket. Det er designet for å spore sanntidsstatistikk i spillet, inkludert sølv, berømmelse og kampdata (Damage Meter), ved å analysere nettverkstrafikk.

Dette prosjektet er et moderne, åpen kildekode-alternativ til det originale C#/WPF-baserte verktøyet `AlbionOnline-StatisticsAnalysis`, med fokus på kompatibilitet på tvers av plattformer og brukervennlighet.

## Funksjoner

*   **Plattformuavhengig kompatibilitet:** Kjører naturlig på Linux, Windows og macOS.
*   **Sanntidssporing:** Bruker `Scapy`-biblioteket for å sniffe UDP-pakker på Albion Online-porter (5055, 5056, 5058).
*   **Skaderegistreringsstruktur (Damage Meter):** Inkluderer nødvendige datastrukturer og brukergrensesnitt for å vise live kampstatistikk (Utført skade, Utført helbredelse, DPS).
*   **Moderne brukergrensesnitt:** Bygget med Flet, som gir en rask, innfødt-lignende skrivebordsapplikasjon.
*   **Sesjonsadministrasjon:** Tillater start, stopp, tilbakestilling og lagring av sesjonsstatistikk.

## Forutsetninger

*   Python 3.8+
*   **Flet** og **Scapy** biblioteker.
*   **Root/Administratorrettigheter:** Nødvendig for nettverkspakkeopptak.

## Installasjon og Oppsett

### Alternativ 1: Rask installasjon (Linux - Anbefalt)

For Linux-brukere tilbyr vi automatiserte installasjonsskript:

\`\`\`bash
# 1. Klon repositoriet
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kjør installasjonsskriptet
./install.sh

# 3. Kjør applikasjonen
./run.sh
\`\`\`

`install.sh`-skriptet vil:
- Installere systemavhengigheter (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Opprette et virtuelt Python-miljø
- Installere alle nødvendige Python-pakker (Flet, Scapy)

`run.sh`-skriptet vil automatisk be om root-rettigheter og kjøre applikasjonen.

### Alternativ 2: Manuell installasjon

#### 1. Installer systemavhengigheter

**På Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**På Windows:**

Installer Python 3.8+ fra [python.org](https://www.python.org/downloads/)

#### 2. Installer Python-avhengigheter

**På Linux (ved bruk av virtuelt miljø - anbefalt):**

\`\`\`bash
# Opprett virtuelt miljø
python3 -m venv venv

# Aktiver virtuelt miljø
source venv/bin/activate

# Installer avhengigheter
pip install flet scapy
\`\`\`

**På Linux (systemomfattende installasjon):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**På Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Kjøre applikasjonen

Siden nettverkssniffing krever forhøyede rettigheter, må du kjøre applikasjonen som root eller administrator.

**På Linux (med virtuelt miljø):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**På Linux (systemomfattende installasjon):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**På Windows (Kjør ledetekst/PowerShell som administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

Applikasjonen vil åpnes i et innfødt skrivebordsvindu.

## Hvordan bygge en kjørbar fil

Applikasjonen kan pakkes inn i en frittstående kjørbar fil ved hjelp av **PyInstaller**. Dette lar brukere kjøre applikasjonen uten å installere Python eller dets avhengigheter.

For detaljerte instruksjoner om bygging av kjørbare filer for Linux, Windows og macOS, se veiledningen **[PACKAGING.md](PACKAGING.md)**.

### Rask bygging (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Den kjørbare filen vil være plassert i mappen `dist/`.

## Prosjektstruktur

Applikasjonen er strukturert i modulære komponenter for bedre vedlikeholdbarhet og skalerbarhet:

| Fil | Beskrivelse |
| :--- | :--- |
| `albion_insight/core/` | Kjernelogikk, nettverkssporing, datamodeller og protokollkoding. |
| `albion_insight/ui/` | Brukergrensesnittkomponenter bygget med Flet. |
| `albion_insight/utils/` | Verktøyfunksjoner, konfigurasjon og logging. |
| `albion_insight/__main__.py` | Inngangspunkt for applikasjonen. |
| `README.md` | Denne dokumentasjonsfilen. |
| `CONTRIBUTING.md` | Retningslinjer for bidrag til prosjektet. |
| `CODE_OF_CONDUCT.md` | Prosjektets etiske retningslinjer. |
| `SECURITY.md` | Retningslinjer for rapportering av sikkerhetssårbarheter. |
| `README.it-IT.md` | Dokumentasjon på italiensk. |
| `README.pt-BR.md` | Dokumentasjon på brasiliansk portugisisk. |
| `README.ru-RU.md` | Dokumentasjon på russisk. |
| `README.fr-FR.md` | Dokumentasjon på fransk. |
| `README.zh-CN.md` | Dokumentasjon på forenklet kinesisk. |
| `README.ko-KR.md` | Dokumentasjon på koreansk. |
| `README.es-ES.md` | Dokumentasjon på spansk. |
| `README.de-DE.md` | Dokumentasjon på tysk. |
| `README.pl-PL.md` | Dokumentasjon på polsk. |
| `README.sv-SE.md` | Dokumentasjon på svensk. |
| `README.vi-VN.md` | Dokumentasjon på vietnamesisk. |
| `README.ar-SA.md` | Dokumentasjon på arabisk. |
| `README.pt-PT.md` | Dokumentasjon på europeisk portugisisk. |
| `README.hi-IN.md` | Dokumentasjon på hindi. |
| `README.hu-HU.md` | Dokumentasjon på ungarsk. |
| `README.th-TH.md` | Dokumentasjon på thai. |
| `README.ja-JP.md` | Dokumentasjon på japansk. |
| `README.tr-TR.md` | Dokumentasjon på tyrkisk. |
| `README.id-ID.md` | Dokumentasjon på indonesisk. |
| `README.cs-CZ.md` | Dokumentasjon på tsjekkisk. |
| `README.fi-FI.md` | Dokumentasjon på finsk. |
| `README.nl-NL.md` | Dokumentasjon på nederlandsk. |
| `README.no-NO.md` | Dokumentasjon på norsk (Bokmål). |

## Gjeldende Status (Sanntidsdata)

Applikasjonen inkluderer nå logikken for **Photon Protocol Decoding**, oversatt fra det originale C#-prosjektet. Dette gjør at applikasjonen kan behandle sanntidshendelser som `UpdateMoney`, `UpdateFame`, `KilledPlayer` og `Died` direkte fra nettverkstrafikken.

**Merk:** Den fullstendige oversettelsen av hver enkelt kamphendelse (som `CastHit`, `Attack`) er et pågående arbeid. Den nåværende implementasjonen fokuserer på kjernestatistikken og strukturen for Skaderegistreringen (Damage Meter). Skaderegistreringens DPS-beregning er basert på de dekodede hendelsene.

## Bidra

Vi ønsker bidrag fra fellesskapet velkommen! Enten du er en utvikler, designer, eller bare en Albion Online-entusiast, er det mange måter å hjelpe til med å forbedre Albion Insight.

Vennligst les våre [Retningslinjer for bidrag](CONTRIBUTING.md) for detaljert informasjon om hvordan du kan bidra til dette prosjektet.

### Rask Start for Bidragsytere:

1.  Fork repositoriet: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klon din fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Opprett en ny gren: `git checkout -b feature/ditt-funksjonsnavn`
4.  Gjør dine endringer og commit: `git commit -m "Legg til din funksjon"`
5.  Push til din fork: `git push origin feature/ditt-funksjonsnavn`
6.  Åpne en Pull Request på hovedrepositoriet

## Lisens

Dette prosjektet er lisensiert under MIT-lisensen - se filen [LICENSE](LICENSE) for detaljer.

## Anerkjennelser

- Originalt prosjekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) av Triky313
- Bygget med [Flet](https://flet.dev/)-rammeverket
- Nettverksanalyse drevet av [Scapy](https://scapy.net/)

---
*En plattformuavhengig løsning for Albion Online-fellesskapet.*
