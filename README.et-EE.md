---

# Albion Insight

[![Litsents: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versioon](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platvorm](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Probleemid](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Panused on teretulnud](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** on platvormideülene (Linux, Windows, macOS) statistika analüüsi tööriist Albion Online mängule, ümber kirjutatud **Pythonis** kasutades **Flet** raamistikku. See on loodud reaalajas mängusiseste statistiliste andmete jälgimiseks, sealhulgas hõbe, kuulsus ja võitluse andmed (Damage Meter), analüüsides võrguliiklust.

See projekt on kaasaegne, avatud lähtekoodiga alternatiiv originaalsele C#/WPF-põhisele `AlbionOnline-StatisticsAnalysis` tööriistale, keskendudes mitme platvormi ühilduvusele ja kasutusmugavusele.

## Omadused

*   **Platvormideülene ühilduvus:** Jookseb natiivina Linuxis, Windowsis ja macOS-is.
*   **Reaalajas jälgimine:** Kasutab `Scapy` raamatukogu UDP pakettide nuusutamiseks Albion Online portidel (5055, 5056, 5058).
*   **Damage Meter struktuur:** Sisaldab vajalikke andmestruktuure ja kasutajaliidest elavate võitluse statistika kuvamiseks (tehtud kahju, tehtud ravi, DPS).
*   **Kaasaegne kasutajaliides:** Ehitatud Fletiga, pakkudes kiiret, natiivset töölauarakendust.
*   **Sessiooni haldus:** Võimaldab alustada, peatada, lähtestada ja salvestada sessiooni statistikat.

## Nõuded

*   Python 3.8+
*   **Flet** ja **Scapy** raamatukogud.
*   **Root/Administratiivsed õigused:** Vajalikud võrgupakettide püüdmise jaoks.

## Paigaldus ja seadistamine

### Variant 1: Kiire paigaldus (Linux - soovitatav)

Linuxi kasutajatele pakume automatiseeritud paigaldusskripte:

```bash
# 1. Klooni hoidla
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Käivita paigaldusskript
./install.sh

# 3. Käivita rakendus
./run.sh
```

`install.sh` skript teeb järgmist:
- Paigaldab süsteemi sõltuvused (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Loob Python virtuaalkeskkonna
- Paigaldab kõik vajalikud Python paketid (Flet, Scapy)

`run.sh` skript küsib automaatselt root õigusi ja käivitab rakenduse.

### Variant 2: Käsitsi paigaldus

#### 1. Paigalda süsteemi sõltuvused

**Linuxis (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windowsis:**

Paigalda Python 3.8+ aadressilt [python.org](https://www.python.org/downloads/)

#### 2. Paigalda Python sõltuvused

**Linuxis (virtuaalkeskkonna kasutamine - soovitatav):**

```bash
# Loo virtuaalkeskkond
python3 -m venv venv

# Aktiveeri virtuaalkeskkond
source venv/bin/activate

# Paigalda sõltuvused
pip install flet scapy
```

**Linuxis (süsteemi ulatuses paigaldamine):**

```bash
pip3 install flet scapy --break-system-packages
```

**Windowsis:**

```bash
pip install flet scapy
```

#### 3. Rakenduse käivitamine

Kuna võrguliikluse nuusutamine nõuab kõrgendatud õigusi, tuleb rakendus käivitada root või administraatori õigustes.

**Linuxis (virtuaalkeskkonnaga):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Linuxis (süsteemi ulatuses paigaldamisega):**

```bash
sudo python3 -m albion_insight
```

**Windowsis (käivita Command Prompt/PowerShell administraatorina):**

```bash
python -m albion_insight
```

Rakendus avaneb natiivse töölaua aknas.

## Kuidas ehitada käivitatav fail

Rakendust saab pakendada iseseisvaks käivitatavaks failiks kasutades **PyInstaller**i. See võimaldab kasutajatel rakendust käivitada ilma Pythonit või selle sõltuvusi paigaldamata.

Üksikasjalike juhiste jaoks Linuxi, Windowsi ja macOS-i käivitatavate failide ehitamiseks vaata **[PACKAGING.md](PACKAGING.md)** juhendit.

### Kiire ehitus (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Käivitatav fail asub `dist/` kaustas.

## Projekti struktuur

Rakendus on üles ehitatud mooduliteks parema hooldatavuse ja laiendatavuse tagamiseks:

| Fail | Kirjeldus |
| :--- | :--- |
| `albion_insight/core/` | Tuumikloogika, võrgu jälgimine, andmemudelid ja protokolli dekodeerimine. |
| `albion_insight/ui/` | Kasutajaliidese komponendid, ehitatud Fletiga. |
| `albion_insight/utils/` | Abifunktsioonid, konfiguratsioon ja logimine. |
| `albion_insight/__main__.py` | Rakenduse sisenemispunkt. |
| `README.md` | See dokumentatsioonifail (inglise keeles). |
| `CONTRIBUTING.md` | Juhised panustamiseks projekti. |
| `CODE_OF_CONDUCT.md` | Projekti käitumisreeglid. |
| `SECURITY.md` | Turvaaukude teatamise poliitika. |
| `README.ar-SA.md` | توثيق باللغة العربية (Araabia dokumentatsioon). |
| `README.ca-ES.md` | Documentació en català (Katalaani dokumentatsioon). |
| `README.cs-CZ.md` | Dokumentace v češtině (Tšehhi dokumentatsioon). |
| `README.da-DK.md` | Dokumentation på dansk (Taani dokumentatsioon). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (Saksa dokumentatsioon). |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (Kreeka dokumentatsioon). |
| `README.es-ES.md` | Documentación en español (Hispaania dokumentatsioon). |
| `README.fa-IR.md` | مستندات به زبان فارسی (Pärsia dokumentatsioon). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (Soome dokumentatsioon). |
| `README.fi.md` | Dokumentaatio suomeksi (Soome dokumentatsioon - üldine). |
| `README.fil-PH.md` | Dokumentasyon sa Filipino (Filipiini dokumentatsioon). |
| `README.fr-FR.md` | Documentation en français (Prantsuse dokumentatsioon). |
| `README.he-IL.md` | תיעוד בעברית (Heebrea dokumentatsioon). |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Hindi dokumentatsioon). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Ungari dokumentatsioon). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia (Indoneesia dokumentatsioon). |
| `README.it-IT.md` | Documentazione in italiano (Itaalia dokumentatsioon). |
| `README.ja-JP.md` | 日本語のドキュメント (Jaapani dokumentatsioon). |
| `README.ko-KR.md` | 한국어 문서 (Korea dokumentatsioon). |
| `README.lt-LT.md` | Dokumentacija lietuvių kalba (Leedu dokumentatsioon). |
| `README.lv-LV.md` | Dokumentācija latviešu valodā (Läti dokumentatsioon). |
| `README.ne-NP.md` | नेपालीमा कागजात (Nepali dokumentatsioon). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Hollandi dokumentatsioon). |
| `README.no-NO.md` | Dokumentasjon på norsk (Norra dokumentatsioon). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Poola dokumentatsioon). |
| `README.pt-BR.md` | Documentação em português do Brasil (Brasiilia portugali dokumentatsioon). |
| `README.pt-PT.md` | Documentação em português europeu (Euroopa portugali dokumentatsioon). |
| `README.ro-RO.md` | Documentație în română (Rumeenia dokumentatsioon). |
| `README.ru-RU.md` | Документация на русском языке (Vene dokumentatsioon). |
| `README.sk-SK.md` | Dokumentácia v slovenčine (Slovaki dokumentatsioon). |
| `README.sv-SE.md` | Dokumentation på svenska (Rootsi dokumentatsioon). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Tai dokumentatsioon). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Türgi dokumentatsioon). |
| `README.uk-UA.md` | Документація українською мовою (Ukraina dokumentatsioon). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnami dokumentatsioon). |
| `README.zh-CN.md` | 简体中文文档 (Lihtsustatud hiina dokumentatsioon). |
| `README.zh-TW.md` | 繁體中文文件 (Traditsiooniline hiina dokumentatsioon). |
| `README.gl-ES.md` | Documentación en galego (Galiitsia dokumentatsioon). |
| `README.zu-ZA.md` | Imibhalo ngolimi lwesiZulu (Zulu dokumentatsioon). |

## Praegune seis (reaalajas andmed)

Rakendus sisaldab nüüd **Photon protokolli dekodeerimise** loogikat, mis on tõlgitud originaalsest C# projektist. See võimaldab rakendusel töödelda reaalajas sündmusi nagu `UpdateMoney`, `UpdateFame`, `KilledPlayer` ja `Died` otse võrguliiklusest.

**Märkus:** Kõigi üksikute võitluse sündmuste (nt `CastHit`, `Attack`) täielik tõlkimine on pooleli. Praegune rakendus keskendub põhistatistikale ja Damage Meter struktuurile. Damage Meter DPS arvutus põhineb dekodeeritud sündmustel.

## Panustamine

Tervitame kogukonna panuseid! Olenemata sellest, kas oled arendaja, disainer või lihtsalt Albion Online fänn, on palju võimalusi aidata Albion Insighti paremaks muuta.

Palun loe meie [Panustamise juhiseid](CONTRIBUTING.md) üksikasjaliku info saamiseks, kuidas projekti panustada.

### Kiire algus panustajatele:

1.  Tee hoidlast fork: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klooni oma fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Loo uus haru: `git checkout -b feature/your-feature-name`
4.  Tee muudatused ja commiti: `git commit -m "Add your feature"`
5.  Lükka oma fork: `git push origin feature/your-feature-name`
6.  Ava Pull Request põhihoidlas

## Litsents

See projekt on litsentseeritud MIT litsentsi alusel - vaata üksikasju failist [LICENSE](LICENSE).

## Tänusõnad

- Originaalprojekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) autorilt Triky313
- Ehitatud kasutades [Flet](https://flet.dev/) raamistikku
- Võrgu analüüs kasutades [Scapy](https://scapy.net/)

---
*Platvormideülene lahendus Albion Online kogukonnale.*
