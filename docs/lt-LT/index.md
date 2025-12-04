# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** yra kelių platformų (Linux, Windows, macOS) statistikos analizės įrankis, skirtas žaidimui Albion Online, perrašytas **Python** kalba, naudojant **Flet** karkasą. Jis skirtas stebėti realaus laiko žaidimo statistiką, įskaitant sidabrą, šlovę ir kovos duomenis (Žalos Matuoklį), analizuojant tinklo srautą.

Šis projektas yra moderni, atvirojo kodo alternatyva originaliam C#/WPF pagrindu sukurtam `AlbionOnline-StatisticsAnalysis` įrankiui, orientuota į kelių platformų suderinamumą ir paprastą naudojimą.

## Savybės

*   **Kelių Platformų Suderinamumas:** Veikia natūraliai Linux, Windows ir macOS sistemose.
*   **Realaus Laiko Stebėjimas:** Naudoja `Scapy` biblioteką UDP paketų uostuose (5055, 5056, 5058) uostuose uostuose.
*   **Žalos Matuoklio Struktūra:** Apima reikalingas duomenų struktūras ir vartotojo sąsają, skirtą rodyti gyvą kovos statistiką (Padaryta Žala, Atliktas Gydymas, DPS).
*   **Moderni Vartotojo Sąsaja:** Sukurta su Flet, suteikianti greitą, natūraliai atrodančią darbalaukio programą.
*   **Sesijos Valdymas:** Leidžia pradėti, sustabdyti, atstatyti ir išsaugoti sesijos statistiką.

## Būtinos Sąlygos

*   Python 3.8+
*   **Flet** ir **Scapy** bibliotekos.
*   **Root/Administratoriaus Teisės:** Būtinos tinklo paketų fiksavimui.

## Įdiegimas ir Nustatymai

### 1 Galimybė: Greitas Įdiegimas (Linux - Rekomenduojama)

Linux vartotojams siūlome automatizuotus diegimo scenarijus:

\`\`\`bash
# 1. Klonuokite saugyklą
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Paleiskite diegimo scenarijų
./install.sh

# 3. Paleiskite programą
./run.sh
\`\`\`

`install.sh` scenarijus:
- Įdiegs sistemos priklausomybes (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Sukurs Python virtualią aplinką
- Įdiegs visus reikalingus Python paketus (Flet, Scapy)

`run.sh` scenarijus automatiškai paprašys root teisių ir paleis programą.

### 2 Galimybė: Rankinis Įdiegimas (Visos Platformos)

1.  **Klonuokite Saugyklą:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`

2.  **Sukurkite ir Aktyvuokite Virtualią Aplinką:**
    \`\`\`bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate   # Windows
    \`\`\`

3.  **Įdiekite Priklausomybes:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4.  **Paleiskite:**
    \`\`\`bash
    # Paleiskite su Root/Administratoriaus teisėmis
    sudo python3 -m albion_insight
    \`\`\`

## Prisidėjimas

Laukiame jūsų indėlio! Prieš pradėdami, perskaitykite [CONTRIBUTING.md](CONTRIBUTING.md) failą.

## Licencija

Šis projektas yra licencijuotas pagal [MIT Licenciją](LICENSE).

## Padėkos

- Originalus projektas: Triky313 sukurtas [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- Sukurta su [Flet](https://flet.dev/) karkasu
- Tinklo analizė palaikoma [Scapy](https://scapy.net/)
