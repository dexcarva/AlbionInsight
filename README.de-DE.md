[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in English (Auf Englisch lesen)](README.md)**
**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**
**[Read this in Spanish (Leer en Español)](README.es-ES.md)**
**[Read this in French (Lire en Français)](README.fr-FR.md)**
**[Read this in Italian (Leggi in Italiano)](README.it-IT.md)**

# Albion Insight (DE)

**Albion Insight** ist ein plattformübergreifendes (Linux, Windows, macOS) Statistik-Analyse-Tool für das Spiel Albion Online, das in **Python** unter Verwendung des **Flet** Frameworks neu implementiert wurde. Es wurde entwickelt, um Echtzeit-Statistiken im Spiel, einschließlich Silber, Ruhm und Kampfdaten (Schadenszähler), durch die Analyse des Netzwerkverkehrs zu verfolgen.

Dieses Projekt ist eine moderne, quelloffene Alternative zum ursprünglichen C#/WPF-basierten `AlbionOnline-StatisticsAnalysis`-Tool, wobei der Fokus auf Multi-Plattform-Kompatibilität und Benutzerfreundlichkeit liegt.

## Funktionen

*   **Plattformübergreifende Kompatibilität:** Läuft nativ auf Linux, Windows und macOS.
*   **Echtzeit-Verfolgung:** Verwendet die `Scapy`-Bibliothek, um UDP-Pakete auf den Albion Online Ports (5055, 5056, 5058) zu sniffen.
*   **Schadenszähler-Struktur:** Enthält die notwendigen Datenstrukturen und die Benutzeroberfläche zur Anzeige von Live-Kampfstatistiken (Verursachter Schaden, Geheilter Schaden, DPS).
*   **Moderne Benutzeroberfläche:** Mit Flet erstellt, bietet es eine schnelle, nativ aussehende Desktop-Anwendung.
*   **Sitzungsverwaltung:** Ermöglicht das Starten, Stoppen, Zurücksetzen und Speichern von Sitzungsstatistiken.

## Voraussetzungen

*   Python 3.8+
*   **Flet** und **Scapy** Bibliotheken.
*   **Root-/Administratorrechte:** Notwendig für die Erfassung von Netzwerkpaketen.

## Installation und Einrichtung

### Option 1: Schnellinstallation (Linux - Empfohlen)

Für Linux-Benutzer stellen wir automatisierte Installationsskripte bereit:

```bash
# 1. Repository klonen
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Installationsskript ausführen
./install.sh

# 3. Anwendung ausführen
./run.sh
```

Das `install.sh`-Skript wird:
- Systemabhängigkeiten installieren (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Eine virtuelle Python-Umgebung erstellen
- Alle erforderlichen Python-Pakete installieren (Flet, Scapy)

Das `run.sh`-Skript fordert automatisch Root-Rechte an und führt die Anwendung aus.

### Option 2: Manuelle Installation

#### 1. Systemabhängigkeiten installieren

**Unter Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Unter Windows:**

Installieren Sie Python 3.8+ von [python.org](https://www.python.org/downloads/)

#### 2. Python-Abhängigkeiten installieren

**Unter Linux (mit virtueller Umgebung - empfohlen):**

```bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Virtuelle Umgebung aktivieren
source venv/bin/activate

# Abhängigkeiten installieren
pip install flet scapy
```

**Unter Linux (systemweit):**

```bash
pip3 install flet scapy --break-system-packages
```

**Unter Windows:**

```bash
pip install flet scapy
```

#### 3. Anwendung ausführen

Da das Sniffing von Netzwerken erhöhte Rechte erfordert, müssen Sie die Anwendung als Root oder Administrator ausführen.

**Unter Linux (mit virtueller Umgebung):**

```bash
sudo venv/bin/python3 albion_insight.py
```

**Unter Linux (systemweit):**

```bash
sudo python3 albion_insight.py
```

**Unter Windows (Eingabeaufforderung/PowerShell als Administrator ausführen):**

```bash
python albion_insight.py
```

Die Anwendung wird in einem nativen Desktop-Fenster geöffnet.

## Wie man eine ausführbare Datei erstellt

Die Anwendung kann mit **PyInstaller** in eine eigenständige ausführbare Datei verpackt werden. Dies ermöglicht es Benutzern, die Anwendung auszuführen, ohne Python oder seine Abhängigkeiten installieren zu müssen.

Detaillierte Anweisungen zum Erstellen von ausführbaren Dateien für Linux, Windows und macOS finden Sie in der Anleitung **[PACKAGING.md](PACKAGING.md)**.

### Schnelle Erstellung (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```

Die ausführbare Datei befindet sich im Ordner `dist/`.

## Projektstruktur

Die gesamte Anwendung ist zur Vereinfachung in einer einzigen Datei enthalten:

| Datei | Beschreibung |
| :--- | :--- |
| `albion_insight.py` | Die Hauptanwendungsdatei, die die gesamte Logik (Modelle, Netzwerk-Tracker, Flet UI) enthält. |
| `README.md` | Diese Dokumentationsdatei. |

## Aktueller Status (Echtzeitdaten)

Die Anwendung enthält nun die Logik zur **Photon-Protokoll-Dekodierung**, die aus dem ursprünglichen C#-Projekt übersetzt wurde. Dies ermöglicht es der Anwendung, Echtzeit-Ereignisse wie `UpdateMoney`, `UpdateFame`, `KilledPlayer` und `Died` direkt aus dem Netzwerkverkehr zu verarbeiten.

**Hinweis:** Die vollständige Übersetzung jedes einzelnen Kampfereignisses (wie `CastHit`, `Attack`) ist ein fortlaufendes Unterfangen. Die aktuelle Implementierung konzentriert sich auf die Kernstatistiken und die Struktur für den Schadenszähler. Die DPS-Berechnung des Schadenszählers basiert auf den dekodierten Ereignissen.

## Mitwirken

Wir freuen uns über Beiträge aus der Community! Egal, ob Sie Entwickler, Designer oder einfach nur ein Albion Online-Enthusiast sind, es gibt viele Möglichkeiten, Albion Insight zu verbessern.

Bitte lesen Sie unsere [Richtlinien für Mitwirkende](CONTRIBUTING.md) für detaillierte Informationen, wie Sie zu diesem Projekt beitragen können.

### Schnellstart für Mitwirkende:

1.  Forken Sie das Repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klonen Sie Ihren Fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Erstellen Sie einen neuen Branch: `git checkout -b feature/ihr-feature-name`
4.  Nehmen Sie Ihre Änderungen vor und committen Sie: `git commit -m "Füge dein Feature hinzu"`
5.  Pushen Sie zu Ihrem Fork: `git push origin feature/ihr-feature-name`
6.  Öffnen Sie einen Pull Request im Haupt-Repository

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die Datei [LICENSE](LICENSE) für Details.

## Danksagungen

- Ursprüngliches Projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) von Triky313
- Erstellt mit dem [Flet](https://flet.dev/) Framework
- Netzwerkanalyse unterstützt durch [Scapy](https://scapy.net/)

---
*Eine plattformübergreifende Lösung für die Albion Online Community.*
