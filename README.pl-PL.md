# Albion Insight (Wgląd w Albion)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in English (Czytaj po angielsku)](README.md)**
**[Read this in German (Czytaj po niemiecku)](README.de-DE.md)**
**[Read this in Portuguese (Czytaj po portugalsku)](README.pt-BR.md)**
**[Read this in Spanish (Czytaj po hiszpańsku)](README.es-ES.md)**
**[Read this in French (Czytaj po francusku)](README.fr-FR.md)**
**[Read this in Italian (Czytaj po włosku)](README.it-IT.md)**
**[Read this in Simplified Chinese (Czytaj po chińsku uproszczonym)](README.zh-CN.md)**
**[Read this in Russian (Czytaj po rosyjsku)](README.ru-RU.md)**
**[Read this in Japanese (Czytaj po japońsku)](README.ja-JP.md)**
**[Read this in Arabic (Czytaj po arabsku)](README.ar-SA.md)**
**[Read this in Turkish (Czytaj po turecku)](README.tr-TR.md)**
**[Read this in Korean (Czytaj po koreańsku)](README.ko-KR.md)**
**[Read this in Dutch (Czytaj po holendersku)](README.nl-NL.md)**
**[Read this in Polish (Czytaj po polsku)](README.pl-PL.md)**

**Albion Insight** to wieloplatformowe (Linux, Windows, macOS) narzędzie do analizy statystyk dla gry Albion Online, zaimplementowane na nowo w **Pythonie** przy użyciu frameworka **Flet**. Zostało zaprojektowane do śledzenia statystyk w grze w czasie rzeczywistym, w tym srebra, sławy i danych bojowych (Miernik Obrażeń), poprzez analizę ruchu sieciowego.

Ten projekt jest nowoczesną, otwartą alternatywą dla oryginalnego narzędzia `AlbionOnline-StatisticsAnalysis` opartego na C#/WPF, skupiającą się na kompatybilności z wieloma platformami i łatwości użytkowania.

## Funkcje

*   **Kompatybilność Międzyplatformowa:** Działa natywnie na systemach Linux, Windows i macOS.
*   **Śledzenie w Czasie Rzeczywistym:** Wykorzystuje bibliotekę `Scapy` do nasłuchiwania pakietów UDP na portach Albion Online (5055, 5056, 5058).
*   **Struktura Miernika Obrażeń:** Zawiera niezbędne struktury danych i interfejs użytkownika do wyświetlania statystyk bojowych na żywo (Zadane Obrażenia, Uzdrowienia, DPS).
*   **Nowoczesny Interfejs Użytkownika:** Zbudowany za pomocą Flet, zapewniający szybką, natywnie wyglądającą aplikację desktopową.
*   **Zarządzanie Sesjami:** Umożliwia rozpoczynanie, zatrzymywanie, resetowanie i zapisywanie statystyk sesji.

## Wymagania Wstępne

*   Python 3.8+
*   Biblioteki **Flet** i **Scapy**.
*   **Uprawnienia Root/Administratora:** Niezbędne do przechwytywania pakietów sieciowych.

## Instalacja i Konfiguracja

### Opcja 1: Szybka Instalacja (Linux - Zalecane)

Dla użytkowników Linuksa udostępniamy zautomatyzowane skrypty instalacyjne:

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Uruchom skrypt instalacyjny
./install.sh

# 3. Uruchom aplikację
./run.sh
```

Skrypt `install.sh` wykona:
- Zainstaluje zależności systemowe (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Utworzy wirtualne środowisko Pythona
- Zainstaluje wszystkie wymagane pakiety Pythona (Flet, Scapy)

Skrypt `run.sh` automatycznie poprosi o uprawnienia roota i uruchomi aplikację.

### Opcja 2: Instalacja Ręczna

#### 1. Zainstaluj Zależności Systemowe

**Na Linuksie (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Na Windowsie:**

Zainstaluj Python 3.8+ ze strony [python.org](https://www.python.org/downloads/)

#### 2. Zainstaluj Zależności Pythona

**Na Linuksie (używając wirtualnego środowiska - zalecane):**

```bash
# Utwórz wirtualne środowisko
python3 -m venv venv

# Aktywuj wirtualne środowisko
source venv/bin/activate

# Zainstaluj zależności
pip install flet scapy
```

**Na Linuksie (instalacja systemowa):**

```bash
pip3 install flet scapy --break-system-packages
```

**Na Windowsie:**

```bash
pip install flet scapy
```

#### 3. Uruchamianie Aplikacji

Ponieważ nasłuchiwanie sieci wymaga podwyższonych uprawnień, musisz uruchomić aplikację jako root lub administrator.

**Na Linuksie (z wirtualnym środowiskiem):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Na Linuksie (instalacja systemowa):**

```bash
sudo python3 -m albion_insight
```

**Na Windowsie (Uruchom Wiersz Polecenia/PowerShell jako Administrator):**

```bash
python -m albion_insight
```

Aplikacja otworzy się w natywnym oknie desktopowym.

## Jak Zbudować Plik Wykonywalny

Aplikacja może zostać spakowana w samodzielny plik wykonywalny za pomocą **PyInstaller**. Pozwala to użytkownikom na uruchomienie aplikacji bez instalowania Pythona lub jego zależności.

Szczegółowe instrukcje dotyczące budowania plików wykonywalnych dla systemów Linux, Windows i macOS znajdują się w przewodniku **[PACKAGING.md](PACKAGING.md)**.

### Szybka Kompilacja (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
```

Plik wykonywalny znajdzie się w folderze `dist/`.

## Struktura Projektu

Cała aplikacja jest zawarta w jednym pliku dla uproszczenia:

| Plik | Opis |
| :--- | :--- |
| `-m albion_insight` | Główny plik aplikacji zawierający całą logikę (Modele, Śledzenie Sieci, Interfejs Użytkownika Flet). |
| `README.md` | Ten plik dokumentacji. |
| `README.pt-BR.md` | Ten plik dokumentacji w języku portugalskim (brazylijskim). |
| `CONTRIBUTING.md` | Wytyczne dotyczące wkładu w projekt. |
| `CODE_OF_CONDUCT.md` | Kodeks Postępowania projektu. |
| `SECURITY.md` | Polityka zgłaszania luk w zabezpieczeniach. |

## Aktualny Status (Dane w Czasie Rzeczywistym)

Aplikacja zawiera teraz logikę **Dekodowania Protokołu Photon**, przetłumaczoną z oryginalnego projektu C#. Pozwala to aplikacji na przetwarzanie zdarzeń w czasie rzeczywistym, takich jak `UpdateMoney`, `UpdateFame`, `KilledPlayer` i `Died` bezpośrednio z ruchu sieciowego.

**Uwaga:** Pełne tłumaczenie każdego pojedynczego zdarzenia bojowego (jak `CastHit`, `Attack`) jest w toku. Obecna implementacja skupia się na podstawowych statystykach i strukturze Miernika Obrażeń. Obliczanie DPS Miernika Obrażeń opiera się na zdekodowanych zdarzeniach.

## Współpraca

Zapraszamy do współpracy ze strony społeczności! Niezależnie od tego, czy jesteś programistą, projektantem, czy po prostu entuzjastą Albion Online, istnieje wiele sposobów, aby pomóc ulepszyć Albion Insight.

Prosimy o zapoznanie się z naszymi [Wytycznymi Dotyczącymi Wkładu](CONTRIBUTING.md), aby uzyskać szczegółowe informacje na temat tego, jak przyczynić się do tego projektu.

### Szybki Start dla Współpracowników:

1.  Utwórz fork repozytorium: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Sklonuj swój fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Utwórz nową gałąź: `git checkout -b feature/twoja-nazwa-funkcji`
4.  Wprowadź zmiany i zatwierdź: `git commit -m "Dodaj swoją funkcję"`
5.  Wypchnij do swojego forka: `git push origin feature/twoja-nazwa-funkcji`
6.  Otwórz Pull Request w głównym repozytorium

## Licencja

Ten projekt jest licencjonowany na podstawie Licencji MIT - zobacz plik [LICENSE](LICENSE) po szczegóły.

## Podziękowania

- Oryginalny projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) autorstwa Triky313
- Zbudowany za pomocą frameworka [Flet](https://flet.dev/)
- Analiza sieci zasilana przez [Scapy](https://scapy.net/)

---
*Wieloplatformowe rozwiązanie dla społeczności Albion Online.*
