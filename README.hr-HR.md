# Albion Insight

[![Licenca: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Verzija](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platforma](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Problemi](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Doprinosi Dobrodošli](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** je alat za analizu statistike za igru Albion Online, dostupan na više platformi (Linux, Windows, macOS), ponovno implementiran u **Pythonu** koristeći **Flet** okvir. Dizajniran je za praćenje statistike u igri u stvarnom vremenu, uključujući srebro, slavu i podatke o borbi (Damage Meter), analizom mrežnog prometa.

Ovaj projekt je moderna, otvorena alternativa izvornom alatu `AlbionOnline-StatisticsAnalysis` baziranom na C#/WPF-u, fokusirajući se na kompatibilnost s više platformi i jednostavnost korištenja.

## Značajke

*   **Kompatibilnost s više platformi:** Radi izvorno na Linuxu, Windowsu i macOS-u.
*   **Praćenje u stvarnom vremenu:** Koristi biblioteku `Scapy` za njuškanje UDP paketa na Albion Online portovima (5055, 5056, 5058).
*   **Struktura Mjerača Šteta (Damage Meter):** Uključuje potrebne strukture podataka i korisničko sučelje za prikaz statistike borbe uživo (Nanesena Šteta, Izliječeno, DPS).
*   **Moderno Korisničko Sučelje:** Izgrađeno s Fletom, pružajući brzu, izvornu desktop aplikaciju.
*   **Upravljanje Sesijama:** Omogućuje pokretanje, zaustavljanje, resetiranje i spremanje statistike sesije.

## Preduvjeti

*   Python 3.8+
*   Biblioteke **Flet** i **Scapy**.
*   **Root/Administratorske privilegije:** Potrebne za hvatanje mrežnih paketa.

## Instalacija i Postavljanje

### Opcija 1: Brza Instalacija (Linux - Preporučeno)

Za korisnike Linuxa nudimo automatizirane skripte za instalaciju:

\`\`\`bash
# 1. Klonirajte repozitorij
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Pokrenite skriptu za instalaciju
./install.sh

# 3. Pokrenite aplikaciju
./run.sh
\`\`\`

Skripta `install.sh` će:
- Instalirati sistemske ovisnosti (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Stvoriti Python virtualno okruženje
- Instalirati sve potrebne Python pakete (Flet, Scapy)

Skripta `run.sh` automatski će zatražiti root privilegije i pokrenuti aplikaciju.

### Opcija 2: Ručna Instalacija

#### 1. Instalirajte Sistemske Ovisnosti

**Na Linuxu (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Na Windowsu:**

Instalirajte Python 3.8+ s [python.org](https://www.python.org/downloads/)

#### 2. Instalirajte Python Ovisnosti

**Na Linuxu (koristeći virtualno okruženje - preporučeno):**

\`\`\`bash
# Stvorite virtualno okruženje
python3 -m venv venv

# Aktivirajte virtualno okruženje
source venv/bin/activate

# Instalirajte ovisnosti
pip install flet scapy
\`\`\`

**Na Linuxu (instalacija na cijelom sustavu):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Na Windowsu:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Pokretanje Aplikacije

Budući da njuškanje mreže zahtijeva povišene privilegije, morate pokrenuti aplikaciju kao root ili administrator.

**Na Linuxu (s virtualnim okruženjem):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Na Linuxu (instalacija na cijelom sustavu):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Na Windowsu (Pokrenite Command Prompt/PowerShell kao Administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

Aplikacija će se otvoriti u izvornom desktop prozoru.

## Struktura Projekta

Aplikacija je strukturirana u modularne komponente radi bolje održivosti i skalabilnosti:

| Datoteka | Opis |
| :--- | :--- |
| `albion_insight/core/` | Osnovna logika, praćenje mreže, modeli podataka i dekodiranje protokola. |
| `albion_insight/ui/` | Komponente korisničkog sučelja izgrađene s Fletom. |
| `albion_insight/utils/` | Pomoćne funkcije, konfiguracija i bilježenje. |
| `albion_insight/__main__.py` | Ulazna točka za aplikaciju. |
| `README.md` | Ova dokumentacijska datoteka (Engleski). |
| `CONTRIBUTING.md` | Smjernice za doprinos projektu. |
| `CODE_OF_CONDUCT.md` | Kodeks ponašanja projekta. |
| `SECURITY.md` | Pravila za prijavljivanje sigurnosnih ranjivosti. |
| `README.hr-HR.md` | Dokumentacija na hrvatskom jeziku (Croatian documentation). |

*(Ostatak tablice s jezicima je izostavljen radi sažetosti, ali bi bio dodan u stvarnom README.hr-HR.md)*

## Trenutni Status (Podaci u Stvarnom Vremenu)

Aplikacija sada uključuje logiku **Dekodiranja Photon Protokola**, prevedenu iz izvornog C# projekta. To omogućuje aplikaciji obradu događaja u stvarnom vremenu kao što su `UpdateMoney`, `UpdateFame`, `KilledPlayer` i `Died` izravno iz mrežnog prometa.

**Napomena:** Potpuni prijevod svakog pojedinog borbenog događaja (poput `CastHit`, `Attack`) je u tijeku. Trenutna implementacija fokusira se na osnovnu statistiku i strukturu za Mjerač Šteta. Izračun DPS-a Mjerača Šteta temelji se na dekodiranim događajima.

## Doprinos

Pozdravljamo doprinose zajednice! Bilo da ste programer, dizajner ili samo entuzijast Albion Onlinea, postoji mnogo načina da pomognete poboljšati Albion Insight.

Molimo pročitajte naše [Smjernice za Doprinos](CONTRIBUTING.md) za detaljne informacije o tome kako doprinijeti ovom projektu.

### Brzi Početak za Doprinositelje:

1.  Forkajte repozitorij: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klonirajte svoj fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Stvorite novu granu: `git checkout -b feature/naziv-vase-znacajke`
4.  Napravite svoje promjene i commitajte: `git commit -m "Dodajte svoju značajku"`
5.  Gurnite na svoj fork: `git push origin feature/naziv-vase-znacajke`
6.  Otvorite Pull Request na glavnom repozitoriju

## Licenca

Ovaj projekt je licenciran pod MIT Licencom - pogledajte datoteku [LICENSE](LICENSE) za detalje.

## Zahvale

- Izvorni projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) od Triky313
- Izgrađeno s okvirom [Flet](https://flet.dev/)
- Mrežna analiza pokretana s [Scapy](https://scapy.net/)

---
*Rješenje na više platformi za zajednicu Albion Online.*
