# Albion Insight (Česky)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Přečtěte si toto v jiných jazycích</summary>

**[Arabština](README.ar-SA.md)** | **[Němčina](README.de-DE.md)** | **[Řečtina](README.el-GR.md)** | **[Španělština](README.es-ES.md)** | **[Francouzština](README.fr-FR.md)** | **[Hindština](README.hi-IN.md)** | **[Maďarština](README.hu-HU.md)** | **[Indonéština](README.id-ID.md)** | **[Italština](README.it-IT.md)** | **[Japonština](README.ja-JP.md)** | **[Korejština](README.ko-KR.md)** | **[Holandština](README.nl-NL.md)** | **[Polština](README.pl-PL.md)** | **[Portugalština (Brazílie)](README.pt-BR.md)** | **[Rumunština](README.ro-RO.md)** | **[Ruština](README.ru-RU.md)** | **[Švédština](README.sv-SE.md)** | **[Thajština](README.th-TH.md)** | **[Turečtina](README.tr-TR.md)** | **[Vietnamština](README.vi-VN.md)** | **[Čínština (Zjednodušená)](README.zh-CN.md)** | **[Čínština (Tradiční)](README.zh-TW.md)** | **[Čínština (Tradiční - Hong Kong)](README.zh-HK.md)** | **[Čeština](README.cs-CZ.md)**

</details>

**Albion Insight** je multiplatformní (Linux, Windows, macOS) nástroj pro analýzu statistik pro hru Albion Online, znovu implementovaný v **Pythonu** s použitím frameworku **Flet**. Je navržen tak, aby sledoval herní statistiky v reálném čase, včetně stříbra, slávy a bojových dat (Damage Meter), analýzou síťového provozu.

Tento projekt je moderní, open-source alternativou k původnímu nástroji `AlbionOnline-StatisticsAnalysis` založenému na C#/WPF, zaměřenou na multiplatformní kompatibilitu a snadné použití.

## Funkce

*   **Multiplatformní kompatibilita:** Běží nativně na Linuxu, Windows a macOS.
*   **Sledování v reálném čase:** Používá knihovnu `Scapy` k odposlechu UDP paketů na portech Albion Online (5055, 5056, 5058).
*   **Struktura Damage Meteru:** Zahrnuje potřebné datové struktury a uživatelské rozhraní pro zobrazení živých bojových statistik (Udělené poškození, Uzdravení, DPS).
*   **Moderní UI:** Vytvořeno pomocí Flet, poskytující rychlou, nativně vypadající desktopovou aplikaci.
*   **Správa relací:** Umožňuje spouštění, zastavování, resetování a ukládání statistik relací.

## Předpoklady

*   Python 3.8+
*   Knihovny **Flet** a **Scapy**.
*   **Oprávnění root/administrátora:** Nezbytné pro zachytávání síťových paketů.

## Instalace a nastavení

### Možnost 1: Rychlá instalace (Linux - Doporučeno)

Pro uživatele Linuxu poskytujeme automatizované instalační skripty:

```bash
# 1. Naklonujte repozitář
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Spusťte instalační skript
./install.sh

# 3. Spusťte aplikaci
./run.sh
```

Skript `install.sh` provede:
- Instalaci systémových závislostí (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Vytvoření virtuálního prostředí Pythonu
- Instalaci všech požadovaných balíčků Pythonu (Flet, Scapy)

Skript `run.sh` automaticky požádá o oprávnění root a spustí aplikaci.

### Možnost 2: Ruční instalace

#### 1. Instalace systémových závislostí

**Na Linuxu (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Na Windows:**

Nainstalujte Python 3.8+ z [python.org](https://www.python.org/downloads/)

#### 2. Instalace závislostí Pythonu

**Na Linuxu (použití virtuálního prostředí - doporučeno):**

```bash
# Vytvořte virtuální prostředí
python3 -m venv venv

# Aktivujte virtuální prostředí
source venv/bin/activate

# Nainstalujte závislosti
pip install flet scapy
```

**Na Linuxu (systémová instalace):**

```bash
pip3 install flet scapy --break-system-packages
```

**Na Windows:**

```bash
pip install flet scapy
```

#### 3. Spuštění aplikace

Protože odposlech sítě vyžaduje zvýšená oprávnění, musíte aplikaci spustit jako root nebo administrátor.

**Na Linuxu (s virtuálním prostředím):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Na Linuxu (systémová instalace):**

```bash
sudo python3 -m albion_insight
```

**Na Windows (Spusťte Příkazový řádek/PowerShell jako administrátor):**

```bash
python -m albion_insight
```

Aplikace se otevře v nativním desktopovém okně.

## Jak vytvořit spustitelný soubor

Aplikace může být zabalena do samostatného spustitelného souboru pomocí **PyInstaller**. To umožňuje uživatelům spustit aplikaci bez instalace Pythonu nebo jeho závislostí.

Podrobné pokyny k vytváření spustitelných souborů pro Linux, Windows a macOS naleznete v průvodci **[PACKAGING.md](PACKAGING.md)**.

### Rychlé sestavení (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
```

Spustitelný soubor bude umístěn ve složce `dist/`.

## Struktura projektu

Aplikace je strukturována do modulárních komponent pro lepší udržovatelnost a škálovatelnost:

| Soubor | Popis |
| :--- | :--- |
| `albion_insight/core/` | Základní logika, sledování sítě, datové modely a dekódování protokolu. |
| `albion_insight/ui/` | Komponenty uživatelského rozhraní vytvořené pomocí Flet. |
| `albion_insight/utils/` | Pomocné funkce, konfigurace a logování. |
| `albion_insight/__main__.py` | Vstupní bod pro aplikaci. |
| `README.md` | Tato dokumentace. |
| `README.pt-BR.md` | Tato dokumentace v brazilské portugalštině. |
| `CONTRIBUTING.md` | Pokyny pro přispívání do projektu. |
| `CODE_OF_CONDUCT.md` | Kodex chování projektu. |
| `SECURITY.md` | Politika pro hlášení bezpečnostních zranitelností. |

## Aktuální stav (Data v reálném čase)

Aplikace nyní zahrnuje logiku **Dekódování protokolu Photon**, přeloženou z původního projektu C#. To umožňuje aplikaci zpracovávat události v reálném čase, jako jsou `UpdateMoney`, `UpdateFame`, `KilledPlayer` a `Died`, přímo ze síťového provozu.

**Poznámka:** Úplný překlad každé jednotlivé bojové události (jako `CastHit`, `Attack`) je probíhající úsilí. Současná implementace se zaměřuje na základní statistiky a strukturu pro Damage Meter. Výpočet DPS Damage Meteru je založen na dekódovaných událostech.

## Přispívání

Vítáme příspěvky od komunity! Ať už jste vývojář, designér, nebo jen nadšenec pro Albion Online, existuje mnoho způsobů, jak pomoci vylepšit Albion Insight.

Přečtěte si prosím naše [Pokyny pro přispívání](CONTRIBUTING.md) pro podrobné informace o tom, jak přispět k tomuto projektu.

### Rychlý start pro přispěvatele:

1.  Forkněte repozitář: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Naklonujte svůj fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Vytvořte novou větev: `git checkout -b feature/your-feature-name`
4.  Proveďte změny a commit: `git commit -m "Přidání vaší funkce"`
5.  Pushněte do svého forku: `git push origin feature/your-feature-name`
6.  Otevřete Pull Request v hlavním repozitáři

## Licence

Tento projekt je licencován pod licencí MIT - podrobnosti naleznete v souboru [LICENSE](LICENSE).

## Poděkování

- Původní projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) od Triky313
- Vytvořeno s frameworkem [Flet](https://flet.dev/)
- Analýza sítě je poháněna [Scapy](https://scapy.net/)

---
*Multiplatformní řešení pro komunitu Albion Online.*
