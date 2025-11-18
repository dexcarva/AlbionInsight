# Albion Insight (Română)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Citiți acest lucru în Engleză (Read this in English)](README.md)**

**Albion Insight** este un instrument de analiză statistică multi-platformă (Linux, Windows, macOS) pentru jocul Albion Online, re-implementat în **Python** folosind framework-ul **Flet**. Este conceput pentru a urmări statisticile în joc în timp real, inclusiv argintul, faima și datele de luptă (Damage Meter), prin analiza traficului de rețea.

Acest proiect este o alternativă modernă, open-source, la instrumentul original bazat pe C#/WPF, `AlbionOnline-StatisticsAnalysis`, concentrându-se pe compatibilitatea multi-platformă și ușurința în utilizare.

## Funcționalități

*   **Compatibilitate Multi-Platformă:** Rulează nativ pe Linux, Windows și macOS.
*   **Urmărire în Timp Real:** Utilizează biblioteca `Scapy` pentru a intercepta pachetele UDP pe porturile Albion Online (5055, 5056, 5058).
*   **Structură Damage Meter:** Include structurile de date și interfața de utilizare necesare pentru a afișa statisticile de luptă în direct (Daune cauzate, Vindecare efectuată, DPS).
*   **Interfață Modernă:** Construită cu Flet, oferind o aplicație desktop rapidă, cu aspect nativ.
*   **Gestionarea Sesiunilor:** Permite pornirea, oprirea, resetarea și salvarea statisticilor sesiunii.

## Cerințe Prealabile

*   Python 3.8+
*   Bibliotecile **Flet** și **Scapy**.
*   **Privilegii de Root/Administrator:** Necesare pentru capturarea pachetelor de rețea.

## Instalare și Configurare

### Opțiunea 1: Instalare Rapidă (Linux - Recomandat)

Pentru utilizatorii de Linux, oferim scripturi de instalare automate:

```bash
# 1. Clonează depozitul
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Rulează scriptul de instalare
./install.sh

# 3. Rulează aplicația
./run.sh
```

Scriptul `install.sh` va:
- Instala dependențele de sistem (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Crea un mediu virtual Python
- Instala toate pachetele Python necesare (Flet, Scapy)

Scriptul `run.sh` va solicita automat privilegii de root și va rula aplicația.

### Opțiunea 2: Instalare Manuală

#### 1. Instalează Dependențele de Sistem

**Pe Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Pe Windows:**

Instalează Python 3.8+ de pe [python.org](https://www.python.org/downloads/)

#### 2. Instalează Dependențele Python

**Pe Linux (folosind mediu virtual - recomandat):**

```bash
# Creează mediu virtual
python3 -m venv venv

# Activează mediul virtual
source venv/bin/activate

# Instalează dependențele
pip install flet scapy
```

**Pe Linux (instalare la nivel de sistem):**

```bash
pip3 install flet scapy --break-system-packages
```

**Pe Windows:**

```bash
pip install flet scapy
```

#### 3. Rularea Aplicației

Deoarece interceptarea traficului de rețea necesită privilegii ridicate, trebuie să rulați aplicația ca root sau administrator.

**Pe Linux (cu mediu virtual):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Pe Linux (instalare la nivel de sistem):**

```bash
sudo python3 albion_insight/main.py
```

**Pe Windows (Rulează Command Prompt/PowerShell ca Administrator):**

```bash
python albion_insight/main.py
```

Aplicația se va deschide într-o fereastră desktop nativă.

## Cum să Construiești un Executabil

Aplicația poate fi împachetată într-un executabil autonom folosind **PyInstaller**. Acest lucru permite utilizatorilor să ruleze aplicația fără a instala Python sau dependențele sale.

Pentru instrucțiuni detaliate despre construirea executabilelor pentru Linux, Windows și macOS, consultați ghidul **[PACKAGING.md](PACKAGING.md)**.

### Construire Rapidă (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Executabilul va fi localizat în directorul `dist/`.

## Structura Proiectului

Întreaga aplicație este conținută într-un singur fișier pentru simplitate:

| Fișier | Descriere |
| :--- | :--- |
| `albion_insight/main.py` | Fișierul principal al aplicației care conține toată logica (Modele, Network Tracker, Interfață Flet). |
| `README.md` | Acest fișier de documentație (Engleză). |
| `README.ro-RO.md` | Acest fișier de documentație în Română. |
| `CONTRIBUTING.md` | Ghid pentru contribuția la proiect. |
| `CODE_OF_CONDUCT.md` | Codul de Conduită al proiectului. |
| `SECURITY.md` | Politica pentru raportarea vulnerabilităților de securitate. |

## Starea Actuală (Date în Timp Real)

Aplicația include acum logica de **Decodare a Protocolului Photon**, tradusă din proiectul original C#. Acest lucru permite aplicației să proceseze evenimente în timp real precum `UpdateMoney`, `UpdateFame`, `KilledPlayer` și `Died` direct din traficul de rețea.

**Notă:** Traducerea completă a fiecărui eveniment de luptă (precum `CastHit`, `Attack`) este un efort în curs. Implementarea actuală se concentrează pe statisticile de bază și pe structura pentru Damage Meter. Calculul DPS al Damage Meter se bazează pe evenimentele decodate.

## Contribuții

Salutăm contribuțiile din partea comunității! Fie că sunteți dezvoltator, designer sau doar un entuziast Albion Online, există multe modalități de a ajuta la îmbunătățirea Albion Insight.

Vă rugăm să citiți [Ghidul de Contribuție](CONTRIBUTING.md) pentru informații detaliate despre cum să contribuiți la acest proiect.

### Pornire Rapidă pentru Contribuitori:

1.  Fork-uiți depozitul: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clonați fork-ul vostru: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Creați o ramură nouă: `git checkout -b feature/numele-funcționalității-voastre`
4.  Faceți modificările și comiteți: `git commit -m "Adaugă funcționalitatea ta"`
5.  Împingeți în fork-ul vostru: `git push origin feature/numele-funcționalității-voastre`
6.  Deschideți un Pull Request pe depozitul principal

## Licență

Acest proiect este licențiat sub Licența MIT - consultați fișierul [LICENSE](LICENSE) pentru detalii.

## Mulțumiri

- Proiectul original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) de Triky313
- Construit cu framework-ul [Flet](https://flet.dev/)
- Analiza de rețea este asigurată de [Scapy](https://scapy.net/)

---
*O soluție multi-platformă pentru comunitatea Albion Online.*
