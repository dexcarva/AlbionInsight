# Albion Insight (Norsk)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Les dette på andre språk</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Portuguese (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)**

</details>

**Albion Insight** er et kryssplattform (Linux, Windows, macOS) statistikk-analyseverktøy for spillet Albion Online, gjenimplementert i **Python** ved hjelp av **Flet**-rammeverket. Det er designet for å spore sanntidsstatistikk i spillet, inkludert sølv, berømmelse og kampdata (Skademåler), ved å analysere nettverkstrafikk.

Dette prosjektet er et moderne, åpen kildekode-alternativ til det originale C#/WPF-baserte `AlbionOnline-StatisticsAnalysis`-verktøyet, med fokus på kompatibilitet på tvers av plattformer og brukervennlighet.

## Funksjoner

*   **Kryssplattformkompatibilitet:** Kjører naturlig på Linux, Windows og macOS.
*   **Sanntidssporing:** Bruker `Scapy`-biblioteket for å sniffe UDP-pakker på Albion Online-porter (5055, 5056, 5058).
*   **Struktur for Skademåler:** Inkluderer nødvendige datastrukturer og brukergrensesnitt for å vise live kampstatistikk (Påført Skade, Helbredelse Utført, DPS).
*   **Moderne Brukergrensesnitt:** Bygget med Flet, og gir en rask, innfødt-lignende skrivebordsapplikasjon.
*   **Økthåndtering:** Tillater start, stopp, tilbakestilling og lagring av øktstatistikk.

## Forutsetninger

*   Python 3.8+
*   **Flet** og **Scapy** biblioteker.
*   **Root/Administratorrettigheter:** Nødvendig for nettverkspakkeopptak.

## Installasjon og Oppsett

### Alternativ 1: Rask Installasjon (Linux - Anbefalt)

For Linux-brukere tilbyr vi automatiserte installasjonsskript:

```bash
# 1. Klon repositoriet
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kjør installasjonsskriptet
./install.sh

# 3. Kjør applikasjonen
./run.sh
```

### Alternativ 2: Manuell Installasjon (Alle Plattformmer)

1.  **Klon repositoriet:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Installer avhengigheter:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Kjør applikasjonen:**
    ```bash
    python main.py
    ```

## Bidrag

Vi ønsker bidrag velkommen! Se `CONTRIBUTING.md` for detaljer om hvordan du kan hjelpe.

## Lisens

Dette prosjektet er lisensiert under MIT-lisensen - se `LICENSE` filen for detaljer.
