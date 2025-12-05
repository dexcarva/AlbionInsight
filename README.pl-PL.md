# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** to wieloplatformowe (Linux, Windows, macOS) narzędzie do analizy statystyk dla gry Albion Online, zaimplementowane w **Pythonie** przy użyciu frameworku **Flet**. Zostało zaprojektowane do śledzenia statystyk w grze w czasie rzeczywistym, w tym srebra, sławy i danych bojowych (Damage Meter), poprzez analizę ruchu sieciowego.

Ten projekt jest nowoczesną, otwartą alternatywą dla oryginalnego narzędzia `AlbionOnline-StatisticsAnalysis` opartego na C#/WPF, skupiającą się na kompatybilności z wieloma platformami i łatwości użytkowania.

## Funkcje

*   **Kompatybilność Międzyplatformowa:** Działa natywnie na systemach Linux, Windows i macOS.
*   **Śledzenie w Czasie Rzeczywistym:** Wykorzystuje bibliotekę `Scapy` do nasłuchiwania pakietów UDP na portach Albion Online (5055, 5056, 5058).
*   **Struktura Licznika Obrażeń (Damage Meter):** Zawiera niezbędne struktury danych i interfejs użytkownika do wyświetlania statystyk bojowych na żywo (zadane obrażenia, wyleczone obrażenia, DPS).
*   **Nowoczesny Interfejs Użytkownika:** Zbudowany z Flet, zapewniający szybką, natywnie wyglądającą aplikację desktopową.
*   **Zarządzanie Sesjami:** Umożliwia rozpoczynanie, zatrzymywanie, resetowanie i zapisywanie statystyk sesji.

## Wymagania Wstępne

*   Python 3.8+
*   Biblioteki **Flet** i **Scapy**.
*   **Uprawnienia Root/Administratora:** Niezbędne do przechwytywania pakietów sieciowych.

## Instalacja i Konfiguracja

### Opcja 1: Szybka Instalacja (Linux - Zalecane)

Dla użytkowników Linuksa udostępniamy zautomatyzowane skrypty instalacyjne:

\`\`\`bash
# 1. Sklonuj repozytorium
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Uruchom skrypt instalacyjny
./install.sh

# 3. Uruchom aplikację
./run.sh
\`\`\`

Skrypt `install.sh` wykona:
- Instalację zależności systemowych (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Utworzenie wirtualnego środowiska Pythona
- Instalację wszystkich wymaganych pakietów Pythona (Flet, Scapy)

Skrypt `run.sh` automatycznie poprosi o uprawnienia roota i uruchomi aplikację.

### Opcja 2: Instalacja Ręczna

#### 1. Zainstaluj Zależności Systemowe

**Na Linuksie (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Na Windowsie:**

Zainstaluj Python 3.8+ ze strony [python.org](https://www.python.org/downloads/)

#### 2. Zainstaluj Zależności Pythona

**Na Linuksie (używając wirtualnego środowiska - zalecane):**

\`\`\`bash
# Utwórz wirtualne środowisko
python3 -m venv venv

# Aktywuj wirtualne środowisko
source venv/bin/activate

# Zainstaluj zależności
pip install flet scapy
\`\`\`

**Na Linuksie (instalacja globalna):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Na Windowsie:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Uruchamianie Aplikacji

Ponieważ nasłuchiwanie sieci wymaga podwyższonych uprawnień, musisz uruchomić aplikację jako root lub administrator.

**Na Linuksie (z wirtualnym środowiskiem):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Na Linuksie (instalacja globalna):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Na Windowsie (Uruchom Wiersz Poleceń/PowerShell jako Administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

Aplikacja otworzy się w natywnym oknie desktopowym.

## Jak Zbudować Plik Wykonywalny

Aplikacja może zostać spakowana w samodzielny plik wykonywalny za pomocą **PyInstaller**. Pozwala to użytkownikom uruchomić aplikację bez instalowania Pythona i jego zależności.

Szczegółowe instrukcje dotyczące budowania plików wykonywalnych dla systemów Linux, Windows i macOS znajdują się w przewodniku **[PACKAGING.md](PACKAGING.md)**.

### Szybka Kompilacja (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Plik wykonywalny znajdzie się w folderze `dist/`.

## Struktura Projektu

Aplikacja jest podzielona na modułowe komponenty dla lepszej utrzymywalności i skalowalności:

| Plik | Opis |
| :--- | :--- |
| `albion_insight/core/` | Logika rdzenia, śledzenie sieci, modele danych i dekodowanie protokołu. |
| `albion_insight/ui/` | Komponenty interfejsu użytkownika zbudowane z Flet. |
| `albion_insight/utils/` | Funkcje narzędziowe, konfiguracja i logowanie. |
| `albion_insight/__main__.py` | Punkt wejścia dla aplikacji. |
| `README.md` | Ten plik dokumentacji. |
| `CONTRIBUTING.md` | Wytyczne dotyczące wkładu w projekt. |
| `CODE_OF_CONDUCT.md` | Kodeks Postępowania projektu. |
| `SECURITY.md` | Polityka zgłaszania luk w zabezpieczeniach. |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档 (Simplified Chinese documentation). |
| `README.ko-KR.md` | 한국어 문서 (Korean documentation). |
| `README.es-ES.md` | Documentación en español (Spanish documentation). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |

## Aktualny Status (Dane w Czasie Rzeczywistym)

Aplikacja zawiera teraz logikę **Dekodowania Protokołu Photon**, przetłumaczoną z oryginalnego projektu C#. Pozwala to aplikacji przetwarzać zdarzenia w czasie rzeczywistym, takie jak `UpdateMoney`, `UpdateFame`, `KilledPlayer` i `Died`, bezpośrednio z ruchu sieciowego.

**Uwaga:** Pełne tłumaczenie każdego pojedynczego zdarzenia bojowego (jak `CastHit`, `Attack`) jest w toku. Obecna implementacja skupia się na podstawowych statystykach i strukturze dla Licznika Obrażeń. Obliczanie DPS w Liczniku Obrażeń opiera się na zdekodowanych zdarzeniach.

## Współpraca

Zapraszamy do współpracy ze społecznością! Niezależnie od tego, czy jesteś programistą, projektantem, czy po prostu entuzjastą Albion Online, istnieje wiele sposobów, aby pomóc ulepszyć Albion Insight.

Prosimy o zapoznanie się z naszymi [Wytycznymi dotyczącymi Wkładu](CONTRIBUTING.md), aby uzyskać szczegółowe informacje na temat wkładu w ten projekt.

### Szybki Start dla Współpracowników:

1.  Sklonuj repozytorium: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Sklonuj swój fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Utwórz nową gałąź: `git checkout -b feature/twoja-nazwa-funkcji`
4.  Wprowadź zmiany i zatwierdź: `git commit -m "Dodaj swoją funkcję"`
5.  Wypchnij do swojego forka: `git push origin feature/twoja-nazwa-funkcji`
6.  Otwórz Pull Request w głównym repozytorium

## Licencja

Ten projekt jest objęty Licencją MIT - szczegóły znajdują się w pliku [LICENSE](LICENSE).

## Podziękowania

*   Oryginalny projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) autorstwa Triky313
*   Zbudowany z frameworkiem [Flet](https://flet.dev/)
*   Analiza sieci wspierana przez [Scapy](https://scapy.net/)

---
*Wieloplatformowe rozwiązanie dla społeczności Albion Online.*
