# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** ni zana ya uchambuzi wa takwimu inayoweza kutumika kwenye mifumo mbalimbali (Linux, Windows, macOS) kwa ajili ya mchezo wa Albion Online, iliyotekelezwa upya kwa **Python** kwa kutumia mfumo wa **Flet**. Imeundwa kufuatilia takwimu za mchezo kwa wakati halisi, ikiwemo silver, fame, na data ya mapigano (Damage Meter), kwa kuchambua trafiki ya mtandao.

Mradi huu ni mbadala wa kisasa, huria kwa zana ya awali ya C#/WPF iitwayo `AlbionOnline-StatisticsAnalysis`, ukizingatia utangamano wa mifumo mbalimbali na urahisi wa matumizi.

## Vipengele

*   **Utangamano wa Mifumo Mbalimbali:** Inafanya kazi asili kwenye Linux, Windows, na macOS.
*   **Ufuatiliaji wa Wakati Halisi:** Inatumia maktaba ya `Scapy` kunusa pakiti za UDP kwenye bandari za Albion Online (5055, 5056, 5058).
*   **Muundo wa Mita ya Uharibifu (Damage Meter):** Inajumuisha miundo ya data na UI muhimu kuonyesha takwimu za mapigano moja kwa moja (Uharibifu Uliotolewa, Uponyaji Uliotolewa, DPS).
*   **UI ya Kisasa:** Imejengwa kwa Flet, ikitoa programu ya desktop inayoonekana kama asili na ya haraka.
*   **Usimamizi wa Kipindi:** Inaruhusu kuanza, kusimamisha, kuweka upya, na kuhifadhi takwimu za kipindi.

## Mahitaji ya Awali

*   Python 3.8+
*   Maktaba za **Flet** na **Scapy**.
*   **Haki za Mizizi/Msimamizi:** Ni muhimu kwa kunasa pakiti za mtandao.

## Ufungaji na Usanidi

### Chaguo la 1: Ufungaji wa Haraka (Linux - Inapendekezwa)

Kwa watumiaji wa Linux, tunatoa hati za ufungaji otomatiki:

\`\`\`bash
# 1. Clone the repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Run the installation script
./install.sh

# 3. Run the application
./run.sh
\`\`\`

Hati ya `install.sh` itafanya yafuatayo:
- Kufunga vitegemezi vya mfumo (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Kuunda mazingira ya Python ya mtandaoni (virtual environment)
- Kufunga vifurushi vyote vya Python vinavyohitajika (Flet, Scapy)

Hati ya `run.sh` itaomba moja kwa moja haki za mizizi na kuendesha programu.

### Chaguo la 2: Ufungaji wa Mwongozo

#### 1. Funga Vitegemezi vya Mfumo

**Kwenye Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Kwenye Windows:**

Funga Python 3.8+ kutoka [python.org](https://www.python.org/downloads/)

#### 2. Funga Vitegemezi vya Python

**Kwenye Linux (kwa kutumia mazingira ya mtandaoni - inapendekezwa):**

\`\`\`bash
# Unda mazingira ya mtandaoni
python3 -m venv venv

# Amilisha mazingira ya mtandaoni
source venv/bin/activate

# Funga vitegemezi
pip install flet scapy
\`\`\`

**Kwenye Linux (ufungaji wa mfumo mzima):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Kwenye Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Kuendesha Programu

Kwa kuwa kunusa mtandao kunahitaji haki za juu, lazima uendeshe programu kama mizizi au msimamizi.

**Kwenye Linux (na mazingira ya mtandaoni):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Kwenye Linux (ufungaji wa mfumo mzima):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Kwenye Windows (Endesha Command Prompt/PowerShell kama Msimamizi):**

\`\`\`bash
python -m albion_insight
\`\`\`

Programu itafunguka kwenye dirisha la desktop asili.

## Jinsi ya Kujenga Faili Inayoweza Kuendesha (Executable)

Programu inaweza kufungashwa kuwa faili inayoweza kuendesha peke yake kwa kutumia **PyInstaller**. Hii inaruhusu watumiaji kuendesha programu bila kufunga Python au vitegemezi vyake.

Kwa maelekezo ya kina juu ya kujenga faili zinazoweza kuendesha kwa Linux, Windows, na macOS, angalia mwongozo wa **[PACKAGING.md](PACKAGING.md)**.

### Ujenzi wa Haraka (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Faili inayoweza kuendesha itapatikana kwenye folda ya `dist/`.

## Muundo wa Mradi

Programu imeundwa katika vipengele vya moduli kwa ajili ya matengenezo bora na uwezo wa kupanuka:

| Faili | Maelezo |
| :--- | :--- |
| `albion_insight/core/` | Mantiki ya msingi, ufuatiliaji wa mtandao, mifumo ya data, na usimbaji wa itifaki. |
| `albion_insight/ui/` | Vipengele vya kiolesura cha mtumiaji vilivyojengwa kwa Flet. |
| `albion_insight/utils/` | Kazi za matumizi, usanidi, na ukataji wa kumbukumbu. |
| `albion_insight/__main__.py` | Sehemu ya kuingilia kwa programu. |
| `README.md` | Hati hii ya nyaraka (Kiingereza). |
| `CONTRIBUTING.md` | Miongozo ya kuchangia kwenye mradi. |
| `CODE_OF_CONDUCT.md` | Kanuni za Maadili za mradi. |
| `SECURITY.md` | Sera ya kuripoti udhaifu wa usalama. |
| `README.sw-KE.md` | Nyaraka kwa lugha ya Kiswahili (Swahili documentation). |

## Hali ya Sasa (Data ya Wakati Halisi)

Programu sasa inajumuisha mantiki ya **Kusimbua Itifaki ya Photon** (Photon Protocol Decoding), iliyotafsiriwa kutoka kwa mradi wa awali wa C#. Hii inaruhusu programu kuchakata matukio ya wakati halisi kama `UpdateMoney`, `UpdateFame`, `KilledPlayer`, na `Died` moja kwa moja kutoka kwa trafiki ya mtandao.

**Kumbuka:** Tafsiri kamili ya kila tukio la mapigano (kama `CastHit`, `Attack`) ni juhudi inayoendelea. Utekelezaji wa sasa unazingatia takwimu za msingi na muundo wa Mita ya Uharibifu. Hesabu ya DPS ya Mita ya Uharibifu inategemea matukio yaliyosimbuliwa.

## Kuchangia

Tunakaribisha michango kutoka kwa jamii! Iwe wewe ni msanidi programu, mbunifu, au shabiki tu wa Albion Online, kuna njia nyingi za kusaidia kuboresha Albion Insight.

Tafadhali soma [Miongozo yetu ya Kuchangia](CONTRIBUTING.md) kwa maelezo ya kina juu ya jinsi ya kuchangia kwenye mradi huu.

### Mwongozo wa Haraka kwa Wachangiaji:

1.  Fork the repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone your fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Create a new branch: `git checkout -b feature/your-feature-name`
4.  Make your changes and commit: `git commit -m "Add your feature"`
5.  Push to your fork: `git push origin feature/your-feature-name`
6.  Open a Pull Request on the main repository

## Leseni

Mradi huu una leseni ya MIT - angalia faili ya [LICENSE](LICENSE) kwa maelezo.

## Shukrani

- Mradi wa awali: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) na Triky313
- Imejengwa kwa mfumo wa [Flet](https://flet.dev/)
- Uchambuzi wa mtandao unaendeshwa na [Scapy](https://scapy.net/)

---
*Suluhisho la mifumo mbalimbali kwa jamii ya Albion Online.*
