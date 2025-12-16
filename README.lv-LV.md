# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** ir starpplatformu (Linux, Windows, macOS) statistikas analīzes rīks spēlei Albion Online, kas no jauna ieviests **Python** valodā, izmantojot **Flet** ietvaru. Tas ir paredzēts, lai sekotu līdzi reāllaika spēles statistikai, ieskaitot sudrabu, slavu un kaujas datus (Damage Meter), analizējot tīkla trafiku.

Šis projekts ir moderna, atvērtā koda alternatīva oriģinālajam C#/WPF rīkam `AlbionOnline-StatisticsAnalysis`, koncentrējoties uz vairāku platformu saderību un lietošanas ērtumu.

## Funkcijas

*   **Starpplatformu saderība:** Darbojas dabiski uz Linux, Windows un macOS.
*   **Reāllaika izsekošana:** Izmanto `Scapy` bibliotēku, lai pārtvertu UDP paketes Albion Online portos (5055, 5056, 5058).
*   **Kaitējuma mērītāja struktūra:** Ietver nepieciešamās datu struktūras un lietotāja saskarni, lai parādītu tiešraides kaujas statistiku (Nodarītais kaitējums, Dziedināšana, DPS).
*   **Mūsdienīga lietotāja saskarne:** Veidota ar Flet, nodrošinot ātru, dabiski izskatošu darbvirsmas lietojumprogrammu.
*   **Sesiju pārvaldība:** Ļauj sākt, apturēt, atiestatīt un saglabāt sesijas statistiku.

## Priekšnosacījumi

*   Python 3.8+
*   **Flet** un **Scapy** bibliotēkas.
*   **Root/Administratora tiesības:** Nepieciešamas tīkla pakešu uztveršanai.

## Instalēšana un iestatīšana

### 1. iespēja: Ātrā instalēšana (Linux - ieteicams)

Linux lietotājiem mēs piedāvājam automatizētus instalācijas skriptus:

\`\`\`bash
# 1. Klonējiet repozitoriju
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Palaidiet instalācijas skriptu
./install.sh

# 3. Palaidiet lietojumprogrammu
./run.sh
\`\`\`

`install.sh` skripts:
- Instalēs sistēmas atkarības (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Izveidos Python virtuālo vidi
- Instalēs visas nepieciešamās Python pakotnes (Flet, Scapy)

`run.sh` skripts automātiski pieprasīs root tiesības un palaidīs lietojumprogrammu.

### 2. iespēja: Manuāla instalēšana

#### 1. Instalējiet sistēmas atkarības

**Uz Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Uz Windows:**

Instalējiet Python 3.8+ no [python.org](https://www.python.org/downloads/)

#### 2. Instalējiet Python atkarības

**Uz Linux (izmantojot virtuālo vidi - ieteicams):**

\`\`\`bash
# Izveidojiet virtuālo vidi
python3 -m venv venv

# Aktivizējiet virtuālo vidi
source venv/bin/activate

# Instalējiet atkarības
pip install flet scapy
\`\`\`

**Uz Linux (sistēmas mēroga instalēšana):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Uz Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Lietojumprogrammas palaišana

Tā kā tīkla pārtveršanai nepieciešamas paaugstinātas tiesības, lietojumprogramma jāpalaiž kā root vai administrators.

**Uz Linux (ar virtuālo vidi):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Uz Linux (sistēmas mēroga instalēšana):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Uz Windows (Palaidiet komandu uzvedni/PowerShell kā administrators):**

\`\`\`bash
python -m albion_insight
\`\`\`

Lietojumprogramma atvērsies dabiskā darbvirsmas logā.

## Kā izveidot izpildāmu failu

Lietojumprogrammu var iepakot atsevišķā izpildāmā failā, izmantojot **PyInstaller**. Tas ļauj lietotājiem palaist lietojumprogrammu bez Python vai tā atkarību instalēšanas.

Detalizētus norādījumus par izpildāmo failu veidošanu Linux, Windows un macOS skatiet **[PACKAGING.md](PACKAGING.md)** rokasgrāmatā.

### Ātrā veidošana (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Izpildāmais fails atradīsies mapē `dist/`.

## Projekta struktūra

Lietojumprogramma ir strukturēta modulāros komponentos labākai uzturēšanai un mērogojamībai:

| Fails | Apraksts |
| :--- | :--- |
| `albion_insight/core/` | Galvenā loģika, tīkla izsekošana, datu modeļi un protokola dekodēšana. |
| `albion_insight/ui/` | Lietotāja saskarnes komponenti, kas veidoti ar Flet. |
| `albion_insight/utils/` | Lietderības funkcijas, konfigurācija un žurnālu veidošana. |
| `albion_insight/__main__.py` | Lietojumprogrammas sākumpunkts. |
| `README.md` | Šis dokumentācijas fails. |
| `CONTRIBUTING.md` | Vadlīnijas projekta ieguldīšanai. |
| `CODE_OF_CONDUCT.md` | Projekta rīcības kodekss. |
| `SECURITY.md` | Politika drošības ievainojamību ziņošanai. |
| `README.lv-LV.md` | Dokumentācija latviešu valodā. |
| (Citas valodu READMEs) | (Citas valodu READMEs) |

## Pašreizējais statuss (Reāllaika dati)

Lietojumprogramma tagad ietver **Photon protokola dekodēšanas** loģiku, kas tulkota no oriģinālā C# projekta. Tas ļauj lietojumprogrammai apstrādāt reāllaika notikumus, piemēram, `UpdateMoney`, `UpdateFame`, `KilledPlayer` un `Died` tieši no tīkla trafika.

**Piezīme:** Pilnīga katra kaujas notikuma (piemēram, `CastHit`, `Attack`) tulkošana ir notiekošs darbs. Pašreizējā ieviešana koncentrējas uz galveno statistiku un Kaitējuma mērītāja struktūru. Kaitējuma mērītāja DPS aprēķins ir balstīts uz dekodētajiem notikumiem.

## Ieguldīšana

Mēs atzinīgi vērtējam kopienas ieguldījumu! Neatkarīgi no tā, vai esat izstrādātājs, dizainers vai tikai Albion Online entuziasts, ir daudz veidu, kā palīdzēt uzlabot Albion Insight.

Lūdzu, izlasiet mūsu [Ieguldīšanas vadlīnijas](CONTRIBUTING.md), lai iegūtu detalizētu informāciju par to, kā ieguldīt šajā projektā.

### Ātrais sākums ieguldītājiem:

1.  Forkojiet repozitoriju: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klonējiet savu fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Izveidojiet jaunu zaru: `git checkout -b feature/your-feature-name`
4.  Veiciet izmaiņas un komitojiet: `git commit -m "Pievienojiet savu funkciju"`
5.  Pārsūtiet uz savu fork: `git push origin feature/your-feature-name`
6.  Atveriet Pull Request galvenajā repozitorijā

## Licence

Šis projekts ir licencēts saskaņā ar MIT licenci - sīkāku informāciju skatiet failā [LICENSE](LICENSE).

## Pateicības

- Oriģinālais projekts: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) no Triky313
- Veidots ar [Flet](https://flet.dev/) ietvaru
- Tīkla analīze, ko nodrošina [Scapy](https://scapy.net/)

---
*Starpplatformu risinājums Albion Online kopienai.*
