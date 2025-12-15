# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**I-Albion Insight** iyithuluzi lokuhlaziya izibalo elisebenza ezinkundleni ezahlukene (i-Linux, i-Windows, ne-macOS) lomdlalo i-Albion Online, elenziwe kabusha nge-**Python** kusetshenziswa uhlaka lwe-**Flet**. Lwenzelwe ukulandelela izibalo zomdlalo ngesikhathi sangempela, okuhlanganisa i-silver, i-fame, nedatha yokulwa (i-Damage Meter), ngokuhlaziya ithrafikhi yenethiwekhi.

Le phrojekthi iyindlela yesimanje, evulekile (open-source) esikhundleni sethuluzi langempela le-C#/WPF elithi `AlbionOnline-StatisticsAnalysis`, eligxile ekuhambisaneni kwezinkundla eziningi kanye nokusebenziseka kalula.

## Izici

*   **Ukuhambisana Kwezinkundla Ezahlukene:** Isebenza ngokwemvelo ku-Linux, Windows, naku-macOS.
*   **Ukulandelela Ngesikhathi Sangempela:** Isebenzisa umtapo wezincwadi we-`Scapy` ukuze ihogele amaphakethe e-UDP kumachweba e-Albion Online (5055, 5056, 5058).
*   **Isakhiwo Se-Damage Meter:** Kuhlanganisa izakhiwo zedatha ezidingekayo kanye ne-UI ukuze kuboniswe izibalo zokulwa ezibukhoma (I-Damage Eyenziwe, I-Healing Eyenziwe, i-DPS).
*   **I-UI Yesimanje:** Yakhiwe nge-Flet, inikeza uhlelo lokusebenza lwedeskithophu olusheshayo, olubukeka njengolwendabuko.
*   **Ukuphathwa Kweseshini:** Ivumela ukuqala, ukumisa, ukusetha kabusha, nokulondoloza izibalo zeseshini.

## Izidingo Zangaphambili

*   I-Python 3.8+
*   Imitapo yezincwadi ye-**Flet** ne-**Scapy**.
*   **Amalungelo Omsuka/Omlawuli:** Ayadingeka ukuze kuthwetshulwe amaphakethe enethiwekhi.

## Ukufaka Nokumisa

### Inketho 1: Ukufaka Okusheshayo (I-Linux - Kunconywa)

Kubasebenzisi be-Linux, sinikeza imibhalo yokufaka ezenzakalelayo:

\`\`\`bash
# 1. Clone the repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Run the installation script
./install.sh

# 3. Run the application
./run.sh
\`\`\`

Umbhalo we-`install.sh` uzokwenza:
- Faka izidingo zesistimu (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Dala indawo ebonakalayo ye-Python
- Faka wonke amaphakethe e-Python adingekayo (i-Flet, i-Scapy)

Umbhalo we-`run.sh` uzocela ngokuzenzakalelayo amalungelo omsuka bese uqhuba uhlelo lokusebenza.

### Inketho 2: Ukufaka Ngokwenza

#### 1. Faka Izidingo Zesistimu

**Ku-Linux (i-Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Ku-Windows:**

Faka i-Python 3.8+ kusuka ku-[python.org](https://www.python.org/downloads/)

#### 2. Faka Izidingo Ze-Python

**Ku-Linux (usebenzisa indawo ebonakalayo - kunconywa):**

\`\`\`bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install flet scapy
\`\`\`

**Ku-Linux (ukufaka kuyo yonke isistimu):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Ku-Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Ukuqhuba Uhlelo Lokusebenza

Njengoba ukuhogela kwenethiwekhi kudinga amalungelo aphakeme, kufanele uqhube uhlelo lokusebenza njengomsuka noma umlawuli.

**Ku-Linux (ngendawo ebonakalayo):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Ku-Linux (ukufaka kuyo yonke isistimu):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Ku-Windows (Qhuba i-Command Prompt/PowerShell njengoMlawuli):**

\`\`\`bash
python -m albion_insight
\`\`\`

Uhlelo lokusebenza luzovuleka efasiteleni ledeskithophu lendabuko.

## Indlela Yokwakha Okusebenzisekayo

Uhlelo lokusebenza lungapakishwa lube okusebenzisekayo okuzimele kusetshenziswa i-**PyInstaller**. Lokhu kuvumela abasebenzisi ukuthi baqhube uhlelo lokusebenza ngaphandle kokufaka i-Python noma izidingo zayo.

Ukuze uthole imiyalelo enemininingwane yokwakha okusebenzisekayo kwe-Linux, Windows, naku-macOS, bheka umhlahlandlela we-**[PACKAGING.md](PACKAGING.md)**.

### Ukwakha Okusheshayo (I-Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Okusebenzisekayo kuzotholakala kufolda ye-`dist/`.

## Isakhiwo Sephrojekthi

Uhlelo lokusebenza luhlelwe lube izingxenye ezinamamojula ukuze kube lula ukuligcina nokulikhulisa:

| Ifayela | Incazelo |
| :--- | :--- |
| `albion_insight/core/` | Umqondo oyinhloko, ukulandelela inethiwekhi, amamodeli edatha, nokudekhoda kwephrothokholi. |
| `albion_insight/ui/` | Izingxenye zesixhumi esibonakalayo somsebenzisi ezakhiwe nge-Flet. |
| `albion_insight/utils/` | Imisebenzi ewusizo, ukumisa, nokungena. |
| `albion_insight/__main__.py` | Indawo yokuqala yohlelo lokusebenza. |
| `README.md` | Leli fayela lemibhalo. |
| `CONTRIBUTING.md` | Imihlahlandlela yokufaka isandla kuphrojekthi. |
| `CODE_OF_CONDUCT.md` | Ikhodi Yokuziphatha yephrojekthi. |
| `SECURITY.md` | Inqubomgomo yokubika ubungozi bezokuphepha. |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档 (Simplified Chinese documentation). |
| `README.ko-KR.md` | 한국어 문서 (Korean documentation). |
| `README.es-ES.md` | Documentación en español (Spanish documentation). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (German documentation). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |
| `README.sv-SE.md` | Dokumentation på svenska (Swedish documentation). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnamese documentation). |
| `README.ar-SA.md` | توثيق باللغة العربية (Arabic documentation). |
| `README.pt-PT.md` | Documentação em português europeu. |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Hindi documentation). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Hungarian documentation). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Thai documentation). |
| `README.ja-JP.md` | 日本語のドキュメント (Japanese documentation). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Turkish documentation). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia. |
| `README.sk-SK.md` | Dokumentácia v slovenčine (Slovak documentation). |
| `README.cs-CZ.md` | Dokumentace v češtině (Czech documentation). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (Finnish documentation). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Dutch documentation). |
| `README.zh-TW.md` | 繁體中文文件 (Traditional Chinese documentation). |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (Greek documentation). |
| `README.fa-IR.md` | مستندات به زبان فارسی (Persian documentation). |
| `README.uk-UA.md` | Документація українською мовою (Ukrainian documentation). |
| `README.zu-ZA.md` | Imibhalo ngolimi lwesiZulu (Zulu documentation). |

## Isimo Samanje (Idatha Yesikhathi Sangempela)

Uhlelo lokusebenza manje luhlanganisa umqondo we-**Photon Protocol Decoding**, ohunyushwe kusuka kuphrojekthi yoqobo ye-C#. Lokhu kuvumela uhlelo lokusebenza ukuthi lucubungule imicimbi yesikhathi sangempela efana ne-`UpdateMoney`, `UpdateFame`, `KilledPlayer`, ne-`Died` ngokuqondile kusuka kuthrafikhi yenethiwekhi.

**Qaphela:** Ukuhunyushwa okuphelele kwawo wonke umcimbi wokulwa (njenge-`CastHit`, `Attack`) kuwumzamo oqhubekayo. Ukuqaliswa kwamanje kugxile ezibalweni eziyinhloko kanye nesakhiwo se-Damage Meter. Ukubalwa kwe-DPS kwe-Damage Meter kusekelwe emicimbini edekhodiwe.

## Ukufaka Isandla

Samukela iminikelo evela emphakathini! Kungakhathaliseki ukuthi ungumthuthukisi, umklami, noma umthandi nje we-Albion Online, kunezindlela eziningi zokusiza ukuthuthukisa i-Albion Insight.

Sicela ufunde [Imihlahlandlela Yokufaka Isandla](CONTRIBUTING.md) yethu ukuze uthole ulwazi oluningiliziwe lokuthi ungafaka kanjani isandla kule phrojekthi.

### Ukuqala Okusheshayo Kwabafaka Isandla:

1.  Fork the repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone your fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Create a new branch: `git checkout -b feature/your-feature-name`
4.  Make your changes and commit: `git commit -m "Add your feature"`
5.  Push to your fork: `git push origin feature/your-feature-name`
6.  Open a Pull Request on the main repository

## Ilayisense

Le phrojekthi inelayisense ngaphansi kwe-MIT License - bheka ifayela le-[LICENSE](LICENSE) ukuze uthole imininingwane.

## Ukubonga

- Iphrojekthi yoqobo: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) ngu-Triky313
- Yakhiwe ngohlaka lwe-[Flet](https://flet.dev/)
- Ukuhlaziya inethiwekhi kunikwe amandla yi-[Scapy](https://scapy.net/)

---
*Isixazululo esisebenza ezinkundleni ezahlukene somphakathi we-Albion Online.*
