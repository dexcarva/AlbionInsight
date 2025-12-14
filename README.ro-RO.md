
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** este un instrument de analiză statistică multi-platformă (Linux, Windows, macOS) pentru jocul Albion Online, re-implementat în **Python** folosind cadrul **Flet**. Este conceput pentru a urmări statisticile în timp real din joc, inclusiv argintul, faima și datele de luptă (Damage Meter), prin analiza traficului de rețea.

Acest proiect este o alternativă modernă, open-source, la instrumentul original bazat pe C#/WPF, `AlbionOnline-StatisticsAnalysis`, concentrându-se pe compatibilitatea multi-platformă și ușurința în utilizare.

## Caracteristici

*   **Compatibilitate Multi-Platformă:** Rulează nativ pe Linux, Windows și macOS.
*   **Urmărire în Timp Real:** Utilizează biblioteca `Scapy` pentru a intercepta pachetele UDP pe porturile Albion Online (5055, 5056, 5058).
*   **Structura Contorului de Daune (Damage Meter):** Include structurile de date necesare și interfața de utilizare pentru a afișa statistici de luptă în direct (Daune Provocate, Vindecare Efectuată, DPS).
*   **Interfață de Utilizare Modernă:** Construit cu Flet, oferind o aplicație desktop rapidă, cu aspect nativ.
*   **Gestionarea Sesiunilor:** Permite pornirea, oprirea, resetarea și salvarea statisticilor sesiunii.

## Pre-condiții

*   Python 3.8+
*   Bibliotecile **Flet** și **Scapy**.
*   **Privilegii de Root/Administrator:** Necesare pentru capturarea pachetelor de rețea.

## Instalare și Configurare

### Opțiunea 1: Instalare Rapidă (Linux - Recomandat)

Pentru utilizatorii de Linux, oferim scripturi de instalare automate:

\`\`\`bash
# 1. Clonează depozitul
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Rulează scriptul de instalare
./install.sh

# 3. Rulează aplicația
./run.sh
\`\`\`

Scriptul `install.sh` va:
- Instala dependențele de sistem (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Crea un mediu virtual Python
- Instala toate pachetele Python necesare (Flet, Scapy)

Scriptul `run.sh` va solicita automat privilegii de root și va rula aplicația.

### Opțiunea 2: Instalare Manuală

#### 1. Instalează Dependențele de Sistem

**Pe Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Pe Windows:**

Instalează Python 3.8+ de pe [python.org](https://www.python.org/downloads/)

#### 2. Instalează Dependențele Python

**Pe Linux (folosind mediul virtual - recomandat):**

\`\`\`bash
# Creează mediul virtual
python3 -m venv venv

# Activează mediul virtual
source venv/bin/activate

# Instalează dependențele
pip install flet scapy
\`\`\`

**Pe Linux (instalare la nivel de sistem):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Pe Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Rularea Aplicației

Deoarece interceptarea rețelei necesită privilegii ridicate, trebuie să rulați aplicația ca root sau administrator.

**Pe Linux (cu mediu virtual):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Pe Linux (instalare la nivel de sistem):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Pe Windows (Rulează Command Prompt/PowerShell ca Administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

Aplicația se va deschide într-o fereastră desktop nativă.

## Cum să Construiești un Executabil

Aplicația poate fi împachetată într-un executabil autonom folosind **PyInstaller**. Acest lucru permite utilizatorilor să ruleze aplicația fără a instala Python sau dependențele sale.

Pentru instrucțiuni detaliate despre construirea executabilelor pentru Linux, Windows și macOS, consultați ghidul **[PACKAGING.md](PACKAGING.md)**.

### Construire Rapidă (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Executabilul va fi localizat în folderul `dist/`.

## Structura Proiectului

Aplicația este structurată în componente modulare pentru o mai bună mentenabilitate și scalabilitate:

| Fișier | Descriere |
| :--- | :--- |
| `albion_insight/core/` | Logica de bază, urmărirea rețelei, modele de date și decodarea protocolului. |
| `albion_insight/ui/` | Componente de interfață de utilizare construite cu Flet. |
| `albion_insight/utils/` | Funcții utilitare, configurare și înregistrare (logging). |
| `albion_insight/__main__.py` | Punctul de intrare pentru aplicație. |
| `README.md` | Acest fișier de documentație. |
| `CONTRIBUTING.md` | Ghiduri pentru contribuția la proiect. |
| `CODE_OF_CONDUCT.md` | Codul de Conduită al proiectului. |
| `SECURITY.md` | Politica pentru raportarea vulnerabilităților de securitate. |
| `README.it-IT.md` | Documentație în italiană. |
| `README.pt-BR.md` | Documentație în portugheză braziliană. |
| `README.ru-RU.md` | Documentație în rusă. |
| `README.fr-FR.md` | Documentație în franceză. |
| `README.zh-CN.md` | Documentație în chineză simplificată. |
| `README.ko-KR.md` | Documentație în coreeană. |
| `README.es-ES.md` | Documentație în spaniolă. |
| `README.de-DE.md` | Documentație în germană. |
| `README.pl-PL.md` | Documentație în poloneză. |
| `README.sv-SE.md` | Documentație în suedeză. |
| `README.vi-VN.md` | Documentație în vietnameză. |
| `README.ar-SA.md` | Documentație în arabă. |
| `README.pt-PT.md` | Documentație în portugheză europeană. |
| `README.hi-IN.md` | Documentație în hindi. |
| `README.hu-HU.md` | Documentație în maghiară. |
| `README.th-TH.md` | Documentație în thailandeză. |
| `README.ja-JP.md` | Documentație în japoneză. |
| `README.tr-TR.md` | Documentație în turcă. |
| `README.id-ID.md` | Documentație în indoneziană. |
| `README.sk-SK.md` | Documentație în slovacă. |
| `README.cs-CZ.md` | Documentație în cehă. |
| `README.fi-FI.md` | Documentație în finlandeză. |
| `README.nl-NL.md` | Documentație în olandeză. |
| `README.zh-TW.md` | Documentație în chineză tradițională. |
| `README.el-GR.md` | Documentație în greacă. |
| `README.ro-RO.md` | Documentație în română. |

## Starea Actuală (Date în Timp Real)

Aplicația include acum logica de **Decodare a Protocolului Photon**, tradusă din proiectul original C#. Acest lucru permite aplicației să proceseze evenimente în timp real precum `UpdateMoney`, `UpdateFame`, `KilledPlayer` și `Died` direct din traficul de rețea.

**Notă:** Traducerea completă a fiecărui eveniment de luptă (precum `CastHit`, `Attack`) este un efort în curs. Implementarea actuală se concentrează pe statisticile de bază și pe structura pentru Contorul de Daune. Calculul DPS al Contorului de Daune se bazează pe evenimentele decodate.

## Contribuții

Salutăm contribuțiile din partea comunității! Fie că sunteți un dezvoltator, designer sau doar un entuziast al Albion Online, există multe modalități de a ajuta la îmbunătățirea Albion Insight.

Vă rugăm să citiți [Ghidul nostru de Contribuție](CONTRIBUTING.md) pentru informații detaliate despre cum să contribuiți la acest proiect.

### Pornire Rapidă pentru Contribuitori:

1.  Fork-uiți depozitul: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clonați fork-ul dumneavoastră: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Creați o ramură nouă: `git checkout -b feature/numele-caracteristicii-dumneavoastra`
4.  Faceți modificările și comiteți: `git commit -m "Adaugă caracteristica ta"`
5.  Împingeți către fork-ul dumneavoastră: `git push origin feature/numele-caracteristicii-dumneavoastra`
6.  Deschideți un Pull Request pe depozitul principal

## Licență

Acest proiect este licențiat sub Licența MIT - consultați fișierul [LICENSE](LICENSE) pentru detalii.

## Mulțumiri

- Proiectul original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) de Triky313
- Construit cu cadrul [Flet](https://flet.dev/)
- Analiza rețelei este alimentată de [Scapy](https://scapy.net/)

---
*O soluție multi-platformă pentru comunitatea Albion Online.*
