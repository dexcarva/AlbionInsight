# Albion Insight

[![Litsents: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pythoni versioon](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platvorm](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHubi probleemid](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Kaastööd on oodatud](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.et-EE.md)

<details>
<summary>Loe seda teistes keeltes</summary>

**[Araabia](README.ar-SA.md)** | **[Saksa](README.de-DE.md)** | **[Kreeka](README.el-GR.md)** | **[Hispaania](README.es-ES.md)** | **[Prantsuse](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Ungari](README.hu-HU.md)** | **[Indoneesia](README.id-ID.md)** | **[Itaalia](README.it-IT.md)** | **[Jaapani](README.ja-JP.md)** | **[Korea](README.ko-KR.md)** | **[Hollandi](README.nl-NL.md)** | **[Poola](README.pl-PL.md)** | **[Portugali (Brasiilia)](README.pt-BR.md)** | **[Rumeenia](README.ro-RO.md)** | **[Vene](README.ru-RU.md)** | **[Rootsi](README.sv-SE.md)** | **[Tai](README.th-TH.md)** | **[Türgi](README.tr-TR.md)** | **[Vietnami](README.vi-VN.md)** | **[Hiina (lihtsustatud)](README.zh-CN.md)** | **[Hiina (traditsiooniline)](README.zh-TW.md)** | **[Hiina (traditsiooniline - Hongkong)](README.zh-HK.md)** | **[Tšehhi](README.cs-CZ.md)** | **[Pärsia (farsi)](README.fa-IR.md)** | **[Filipino (tagalogi)](README.fil-PH.md)** | **[Portugali (Portugal)](README.pt-PT.md)** | **[Heebrea](README.he-IL.md)** | **[Norra](README.no-NO.md)** | **[Soome](README.fi-FI.md)** | **[Poola](README.pl-PL.md)** | **[Taani](README.da-DK.md)** | **[Ukraina](README.uk-UA.md)** | **[Malai](README.ms-MY.md)** | **[Eesti](README.et-EE.md)**

</details>

**Albion Insight** on platvormiülene (Linux, Windows, macOS) statistikaanalüüsi tööriist mängule Albion Online, mis on uuesti implementeeritud **Pythonis**, kasutades **Flet** raamistikku. See on loodud reaalajas mängusiseste statistikate jälgimiseks, sealhulgas hõbe, kuulsus ja lahinguandmed (kahjumõõtur), analüüsides võrguliiklust.

See projekt on kaasaegne, avatud lähtekoodiga alternatiiv algsele C#/WPF-põhisele `AlbionOnline-StatisticsAnalysis` tööriistale, keskendudes mitme platvormi ühilduvusele ja kasutusmugavusele.

## Funktsioonid

*   **Platvormiülene ühilduvus:** Töötab natiivselt Linuxis, Windowsis ja macOS-is.
*   **Reaalajas jälgimine:** Kasutab `Scapy` teeki UDP-pakettide nuusutamiseks Albion Online'i portidel (5055, 5056, 5058).
*   **Kahjumõõturi struktuur:** Sisaldab vajalikke andmestruktuure ja kasutajaliidest reaalajas lahingustatistika kuvamiseks (tekitatud kahju, tehtud ravi, DPS).
*   **Kaasaegne kasutajaliides:** Ehitatud Fletiga, pakkudes kiiret ja natiivse välimusega töölauarakendust.
*   **Sessioonihaldus:** Võimaldab seansi statistika alustamist, peatamist, lähtestamist ja salvestamist.

## Eeldused

*   Python 3.8+
*   **Flet** ja **Scapy** teegid.
*   **Juur-/administraatoriõigused:** Vajalikud võrgupakettide püüdmiseks.

## Paigaldamine ja seadistamine

### Valik 1: Kiire paigaldus (Linux - soovitatav)

Linuxi kasutajatele pakume automatiseeritud paigaldusskripte:

```bash
# 1. Kloonige hoidla
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Käivitage paigaldusskript
./install.sh

# 3. Käivitage rakendus
./run.sh
```

`install.sh` skript teeb järgmist:
- Paigaldab süsteemi sõltuvused (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Loob Pythoni virtuaalse keskkonna
- Paigaldab kõik vajalikud Pythoni paketid (Flet, Scapy)

`run.sh` skript küsib automaatselt juurõigusi ja käivitab rakenduse.

### Valik 2: Käsitsi paigaldamine

#### 1. Paigaldage süsteemi sõltuvused

**Linuxis (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windowsis:**

Paigaldage Python 3.8+ aadressilt [python.org](https://www.python.org/downloads/)

#### 2. Paigaldage Pythoni sõltuvused

**Linuxis (kasutades virtuaalset keskkonda - soovitatav):**

```bash
# Looge virtuaalne keskkond
python3 -m venv venv

# Aktiveerige virtuaalne keskkond
source venv/bin/activate

# Paigaldage sõltuvused
pip install flet scapy
```

**Linuxis (süsteemiülene paigaldus):**

```bash
pip3 install flet scapy --break-system-packages
```

**Windowsis:**

```bash
pip install flet scapy
```

#### 3. Rakenduse käivitamine

Kuna võrgu nuusutamine nõuab kõrgendatud õigusi, peate rakenduse käivitama juur- või administraatorina.

**Linuxis (virtuaalse keskkonnaga):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Linuxis (süsteemiülene paigaldus):**

```bash
sudo python3 -m albion_insight
```

**Windowsis (käivitage käsuviip/PowerShell administraatorina):**

```bash
python -m albion_insight
```

Rakendus avaneb natiivses töölauaaknas.

## Kuidas ehitada käivitatavat faili

Rakenduse saab pakendada eraldiseisvaks käivitatavaks failiks, kasutades **PyInstalleri**. See võimaldab kasutajatel rakendust käivitada ilma Pythonit või selle sõltuvusi paigaldamata.

Üksikasjalikud juhised käivitatavate failide ehitamiseks Linuxile, Windowsile ja macOS-ile leiate **[PACKAGING.md](PACKAGING.md)** juhendist.

### Kiire ehitamine (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Käivitatav fail asub `dist/` kaustas.

## Projekti struktuur

Rakendus on parema hooldatavuse ja skaleeritavuse tagamiseks struktureeritud modulaarseteks komponentideks:

| Fail | Kirjeldus |
| :--- | :--- |
| `albion_insight/core/` | Tuumikloogika, võrgu jälgimine, andmemudelid ja protokolli dekodeerimine. |
| `albion_insight/ui/` | Fletiga ehitatud kasutajaliidese komponendid. |
| `albion_insight/utils/` | Utiliitfunktsioonid, konfiguratsioon ja logimine. |
| `albion_insight/__main__.py` | Rakenduse sisendpunkt. |
| `README.md` | See dokumentatsioonifail. |
| `README.pt-BR.md` | See dokumentatsioonifail Brasiilia portugali keeles. |
| `README.fil-PH.md` | See dokumentatsioonifail filipino (tagalogi) keeles. |
| `README.pt-PT.md` | See dokumentatsioonifail Portugali portugali keeles. |
| `README.sv-SE.md` | See dokumentatsioonifail rootsi keeles. |
| `README.da-DK.md` | See dokumentatsioonifail taani keeles. |
| `CONTRIBUTING.sv-SE.md` | Juhised projekti panustamiseks rootsi keeles. |
| `CONTRIBUTING.md` | Juhised projekti panustamiseks. |
| `CODE_OF_CONDUCT.md` | Projekti käitumisjuhend. |
| `SECURITY.md` | Turvanõrkustest teatamise poliitika. |
| `README.et-EE.md` | See dokumentatsioonifail eesti keeles. |

## Praegune olek (reaalajas andmed)

Rakendus sisaldab nüüd **Photoni protokolli dekodeerimise** loogikat, mis on tõlgitud algsest C# projektist. See võimaldab rakendusel töödelda reaalajas sündmusi nagu `UpdateMoney`, `UpdateFame`, `KilledPlayer` ja `Died` otse võrguliiklusest.

**Märkus:** Iga üksiku lahingusündmuse (nagu `CastHit`, `Attack`) täielik tõlkimine on pidev töö. Praegune implementatsioon keskendub põhistatistikale ja kahjumõõturi struktuurile. Kahjumõõturi DPS-i arvutamine põhineb dekodeeritud sündmustel.

## Panustamine

Ootame kogukonna panuseid! Olenemata sellest, kas olete arendaja, disainer või lihtsalt Albion Online'i entusiast, on Albion Insighti parendamiseks palju võimalusi.

Palun lugege meie [Panustamisjuhiseid](CONTRIBUTING.et-EE.md), et saada üksikasjalikku teavet selle projekti panustamise kohta.

### Kiirjuhend panustajatele:

1.  Tehke hoidlast kahvel: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Kloonige oma kahvel: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Looge uus haru: `git checkout -b feature/your-feature-name`
4.  Tehke oma muudatused ja tehke commit: `git commit -m "Add your feature"`
5.  Lükake oma kahvlisse: `git push origin feature/your-feature-name`
6.  Avage Pull Request põhihoidlas

## Litsents

See projekt on litsentsitud MIT-litsentsi alusel - üksikasju vaadake [LICENSE](LICENSE) failist.

## Tänusõnad

- Algne projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) autorilt Triky313
- Ehitatud [Flet](https://flet.dev/) raamistikuga
- Võrguanalüüs, mida toetab [Scapy](https://scapy.net/)

---
*Platvormiülene lahendus Albion Online'i kogukonnale.*
