# Albion Insight
*Egy platformfüggetlen megoldás az Albion Online közösség számára.*

Az Albion Insight egy nyílt forráskódú, platformfüggetlen asztali alkalmazás, amely valós idejű statisztikákat gyűjt az Albion Online játékmenetéből a hálózati forgalom elemzésével.

Ez a projekt a [Triky313/AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) C# projekt Python portja, amely a Flet keretrendszert használja a modern, natív asztali felhasználói felülethez.

## Főbb Jellemzők
*   **Valós idejű Hálózati Forgalom Elemzés:** A Scapy segítségével elemzi a hálózati csomagokat.
*   **Photon Protokoll Dekódolás:** Dekódolja az Albion Online által használt Photon protokoll eseményeit.
*   **Keresztplatformos Felület:** Natív asztali alkalmazás Windows, Linux és macOS rendszerekre a Flet segítségével.
*   **Sérülésmérő (Damage Meter):** Valós idejű DPS és HPS mérés.
*   **Szezonális Statisztikák:** Képesség a teljesítmény és a munkamenet-statisztikák mentésére.

## Előfeltételek
*   Python 3.8+
*   **Flet** és **Scapy** könyvtárak.
*   **Root/Rendszergazdai Jogosultságok:** Szükséges a hálózati csomagok rögzítéséhez.

## Telepítés és Konfiguráció
### 1. Lehetőség: Gyors Telepítés (Linux - Ajánlott)
Linux felhasználók számára automatizált telepítési szkripteket biztosítunk:
```bash
# 1. Klónozza a tárolót
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight
# 2. Futtassa a telepítő szkriptet
./install.sh
# 3. Futtassa az alkalmazást
./run.sh
```
Az `install.sh` szkript a következőket teszi:
- Telepíti a rendszerfüggőségeket (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Létrehoz egy Python virtuális környezetet
- Telepíti az összes szükséges Python csomagot (Flet, Scapy)
A `run.sh` szkript automatikusan root jogosultságot kér, és elindítja az alkalmazást.

### 2. Lehetőség: Manuális Telepítés
#### 1. Rendszerfüggőségek Telepítése
**Linuxon (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```
**Windowson:**
Telepítse a Python 3.8+-t a [python.org](https://www.python.org/downloads/) oldalról.

#### 2. Python Függőségek Telepítése
**Linuxon (virtuális környezet használatával - ajánlott):**
```bash
# Virtuális környezet létrehozása
python3 -m venv venv
# Virtuális környezet aktiválása
source venv/bin/activate
# Függőségek telepítése
pip install flet scapy
```
**Linuxon (rendszer szintű telepítés):**
```bash
pip3 install flet scapy --break-system-packages
```
**Windowson:**
```bash
pip install flet scapy
```

#### 3. Az Alkalmazás Futtatása
Mivel a hálózati rögzítés emelt szintű jogosultságokat igényel, az alkalmazást rootként vagy rendszergazdaként kell futtatnia.
**Linuxon (virtuális környezettel):**
```bash
sudo venv/bin/python3 -m albion_insight
```
**Linuxon (rendszer szintű telepítés):**
```bash
sudo python3 -m albion_insight
```
**Windowson (Futtassa a Parancssort/PowerShellt Rendszergazdaként):**
```bash
python -m albion_insight
```
Az alkalmazás natív asztali ablakban nyílik meg.

## Végrehajtható Fájl Létrehozása
Az alkalmazás önálló végrehajtható fájlba csomagolható a **PyInstaller** segítségével. Ez lehetővé teszi a felhasználók számára, hogy a Python vagy annak függőségeinek telepítése nélkül futtassák az alkalmazást.
A Linux, Windows és macOS rendszerekre vonatkozó végrehajtható fájlok létrehozásának részletes útmutatóját lásd a **[PACKAGING.md](PACKAGING.md)** útmutatóban (angol nyelven).

### Gyors Fordítás (Linux)
```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
```
A végrehajtható fájl a `dist/` mappában található.

## Projekt Struktúra
Az egész alkalmazás egyetlen fájlban található az egyszerűség kedvéért:
| Fájl | Leírás |
| :--- | :--- |
| `-m albion_insight` | Az alkalmazás fő fájlja, amely tartalmazza az összes logikát (modellek, hálózati nyomkövető, Flet felület). |
| `README.md` | Ez a dokumentációs fájl (angol nyelven). |
| `README.pt-BR.md` | Ez a dokumentációs fájl (portugál nyelven). |
| `README.hu-HU.md` | Ez a dokumentációs fájl (magyar nyelven). |
| `README.it-IT.md` | Ez a dokumentációs fájl (olasz nyelven). |

## Jelenlegi Állapot (Valós idejű Adatok)
Az alkalmazás most már tartalmazza a **Photon Protokoll Dekódolási** logikát, amelyet az eredeti C# projektből fordítottak le. Ez lehetővé teszi az alkalmazás számára, hogy valós idejű eseményeket dolgozzon fel, mint például az `UpdateMoney`, `UpdateFame`, `KilledPlayer` és `Died` közvetlenül a hálózati forgalomból.
**Megjegyzés:** Az összes harci esemény (például `CastHit`, `Attack`) teljes fordítása folyamatos erőfeszítést igényel. A jelenlegi megvalósítás a fő statisztikákra és a Sérülésmérő szerkezetére összpontosít. A Sérülésmérő DPS számítása a dekódolt eseményeken alapul.

## Hozzájárulás
Szívesen fogadjuk a közösség hozzájárulásait! Legyen Ön fejlesztő, tervező vagy csak egy Albion Online rajongó, sokféleképpen segíthet az Albion Insight fejlesztésében.
Kérjük, olvassa el a [Hozzájárulási Irányelveinket](CONTRIBUTING.pt-BR.md) a projekthez való hozzájárulás részletes információiért.

### Gyors Indítás a Közreműködőknek:
1.  Forkolja a tárolót: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klónozza a forkot: `git clone https://github.com/AZ_ÖN_FELHASZNÁLÓNEVE/AlbionInsight.git`
3.  Hozzon létre egy új ágat: `git checkout -b feature/az-ön-funkciójának-neve`
4.  Végezze el a módosításokat és commitálja: `git commit -m "Hozzáadja az Ön funkcióját"`
5.  Töltse fel a forkjába: `git push origin feature/az-ön-funkciójának-neve`
6.  Nyisson egy Pull Requestet a fő tárolóban

## Licenc
Ez a projekt az MIT Licenc alatt van licencelve - lásd a [LICENSE](LICENSE) fájlt a részletekért.

## Köszönetnyilvánítás
- Eredeti projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) (Triky313)
- Épült a [Flet](https://flet.dev/) keretrendszerrel
- Hálózati elemzés a [Scapy](https://scapy.net/) segítségével
---
*Egy platformfüggetlen megoldás az Albion Online közösség számára.*
