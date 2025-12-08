# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

Az **Albion Insight** egy platformfüggetlen (Linux, Windows, macOS) statisztikai elemző eszköz az Albion Online játékhoz, amelyet **Python** nyelven, a **Flet** keretrendszer használatával valósítottak meg. Célja a valós idejű játékon belüli statisztikák, beleértve az ezüstöt, a hírnevet és a harci adatokat (Sebzésmérő), hálózati forgalom elemzésével történő nyomon követése.

Ez a projekt a modern, nyílt forráskódú alternatívája az eredeti C#/WPF alapú `AlbionOnline-StatisticsAnalysis` eszköznek, a többplatformos kompatibilitásra és a könnyű használatra összpontosítva.

## Jellemzők

*   **Platformfüggetlen Kompatibilitás:** Natívan fut Linux, Windows és macOS rendszereken.
*   **Valós Idejű Követés:** A `Scapy` könyvtárat használja az Albion Online portokon (5055, 5056, 5058) érkező UDP csomagok elemzésére.
*   **Sebzésmérő Struktúra:** Tartalmazza a szükséges adatstruktúrákat és felhasználói felületet az élő harci statisztikák (Okozott sebzés, Gyógyítás, DPS) megjelenítéséhez.
*   **Modern Felhasználói Felület:** A Flet segítségével készült, gyors, natív megjelenésű asztali alkalmazást biztosítva.
*   **Munkamenet Kezelés:** Lehetővé teszi a munkamenet statisztikák indítását, leállítását, visszaállítását és mentését.

## Előfeltételek

*   Python 3.8+
*   **Flet** és **Scapy** könyvtárak.
*   **Root/Rendszergazdai Jogosultságok:** Szükséges a hálózati csomagok rögzítéséhez.

## Telepítés és Beállítás

### 1. Opció: Gyors Telepítés (Linux - Ajánlott)

Linux felhasználók számára automatizált telepítési szkripteket biztosítunk:

\`\`\`bash
# 1. Klónozza a tárolót
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Futtassa a telepítő szkriptet
./install.sh

# 3. Futtassa az alkalmazást
./run.sh
\`\`\`

Az `install.sh` szkript a következőket végzi el:
- Rendszerfüggőségek telepítése (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Python virtuális környezet létrehozása
- Az összes szükséges Python csomag (Flet, Scapy) telepítése

A `run.sh` szkript automatikusan root jogosultságot kér és elindítja az alkalmazást.

### 2. Opció: Manuális Telepítés

#### 1. Rendszerfüggőségek Telepítése

**Linuxon (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Windowson:**

Telepítse a Python 3.8+-t a [python.org](https://www.python.org/downloads/) oldalról

#### 2. Python Függőségek Telepítése

**Linuxon (virtuális környezet használatával - ajánlott):**

\`\`\`bash
# Virtuális környezet létrehozása
python3 -m venv venv

# Virtuális környezet aktiválása
source venv/bin/activate

# Függőségek telepítése
pip install flet scapy
\`\`\`

**Linuxon (rendszer szintű telepítés):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Windowson:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Az Alkalmazás Futtatása

Mivel a hálózati csomagok rögzítése emelt szintű jogosultságokat igényel, az alkalmazást rootként vagy rendszergazdaként kell futtatnia.

**Linuxon (virtuális környezettel):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Linuxon (rendszer szintű telepítés):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Windowson (Futtassa a Parancssort/PowerShellt Rendszergazdaként):**

\`\`\`bash
python -m albion_insight
\`\`\`

Az alkalmazás natív asztali ablakban nyílik meg.

## Végrehajtható Fájl Készítése

Az alkalmazás önálló végrehajtható fájlba csomagolható a **PyInstaller** segítségével. Ez lehetővé teszi a felhasználók számára, hogy Python vagy annak függőségeinek telepítése nélkül futtassák az alkalmazást.

A Linux, Windows és macOS rendszerekre vonatkozó részletes utasításokért lásd a **[PACKAGING.md](PACKAGING.md)** útmutatót.

### Gyors Építés (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

A végrehajtható fájl a `dist/` mappában található.

## Projekt Struktúra

Az alkalmazás moduláris komponensekre van felépítve a jobb karbantarthatóság és skálázhatóság érdekében:

| Fájl | Leírás |
| :--- | :--- |
| `albion_insight/core/` | Alapvető logika, hálózati követés, adatmodellek és protokoll dekódolás. |
| `albion_insight/ui/` | A Flet segítségével épített felhasználói felület komponensei. |
| `albion_insight/utils/` | Segédfüggvények, konfiguráció és naplózás. |
| `albion_insight/__main__.py` | Az alkalmazás belépési pontja. |
| `README.md` | Ez a dokumentációs fájl. |
| `CONTRIBUTING.md` | Útmutató a projekthez való hozzájáruláshoz. |
| `CODE_OF_CONDUCT.md` | A projekt magatartási kódexe. |
| `SECURITY.md` | Biztonsági sebezhetőségek bejelentésére vonatkozó irányelv. |
| `README.hu-HU.md` | Dokumentáció magyar nyelven. |

## Jelenlegi Állapot (Valós Idejű Adatok)

Az alkalmazás most már tartalmazza a **Photon Protokoll Dekódolási** logikát, amelyet az eredeti C# projektből fordítottak le. Ez lehetővé teszi az alkalmazás számára, hogy a hálózati forgalomból közvetlenül feldolgozza a valós idejű eseményeket, mint például az `UpdateMoney`, `UpdateFame`, `KilledPlayer` és `Died`.

**Megjegyzés:** Az összes harci esemény (például `CastHit`, `Attack`) teljes fordítása folyamatban lévő munka. A jelenlegi megvalósítás az alapvető statisztikákra és a Sebzésmérő struktúrájára összpontosít. A Sebzésmérő DPS számítása a dekódolt eseményeken alapul.

## Hozzájárulás

Szívesen fogadjuk a közösség hozzájárulásait! Legyen szó fejlesztőről, tervezőről vagy csak egy Albion Online rajongóról, sokféleképpen segítheti az Albion Insight fejlesztését.

Kérjük, olvassa el a [Hozzájárulási Útmutatónkat](CONTRIBUTING.md) a projekthez való hozzájárulás részletes információiért.

### Gyors Indítás a Hozzájárulók Számára:

1.  Forkolja a tárolót: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klónozza a forkot: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Hozzon létre egy új ágat: `git checkout -b feature/az-ön-funkciójának-neve`
4.  Végezze el a módosításokat és véglegesítse: `git commit -m "Adja hozzá a funkcióját"`
5.  Töltse fel a forkjára: `git push origin feature/az-ön-funkciójának-neve`
6.  Nyisson egy Pull Requestet a fő tárolóban

## Licenc

Ez a projekt az MIT Licenc alatt van licencelve - a részletekért lásd a [LICENSE](LICENSE) fájlt.

## Köszönetnyilvánítás

- Eredeti projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) Triky313-tól
- A [Flet](https://flet.dev/) keretrendszerrel készült
- Hálózati elemzés a [Scapy](https://scapy.net/) segítségével

---
*Platformfüggetlen megoldás az Albion Online közösség számára.*
