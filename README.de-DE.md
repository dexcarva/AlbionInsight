# Albion Insight

[![Lizenz: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Plattform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Beiträge Willkommen](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** ist ein plattformübergreifendes Statistik-Analyse-Tool (Linux, Windows, macOS) für das Spiel Albion Online, neu implementiert in **Python** unter Verwendung des **Flet** Frameworks. Es wurde entwickelt, um Echtzeit-Statistiken im Spiel zu verfolgen, einschließlich Silber, Ruhm und Kampfdaten (Schadenszähler), durch die Analyse des Netzwerkverkehrs.

Dieses Projekt ist eine moderne, quelloffene Alternative zum ursprünglichen C#/WPF-basierten `AlbionOnline-StatisticsAnalysis`-Tool, mit Fokus auf Multiplattform-Kompatibilität und Benutzerfreundlichkeit.

## Funktionen

*   **Plattformübergreifende Kompatibilität:** Läuft nativ auf Linux, Windows und macOS.
*   **Echtzeit-Verfolgung:** Verwendet die `Scapy`-Bibliothek, um UDP-Pakete auf den Albion Online Ports (5055, 5056, 5058) zu erfassen.
*   **Schadenszähler-Struktur:** Enthält die notwendigen Datenstrukturen und die Benutzeroberfläche zur Anzeige von Live-Kampfstatistiken (Verursachter Schaden, Geheilte Menge, DPS).
*   **Moderne Benutzeroberfläche:** Erstellt mit Flet, bietet eine schnelle, nativ aussehende Desktop-Anwendung.
*   **Sitzungsverwaltung:** Ermöglicht das Starten, Stoppen, Zurücksetzen und Speichern von Sitzungsstatistiken.

## Voraussetzungen

*   Python 3.8+
*   **Flet** und **Scapy** Bibliotheken.
*   **Root-/Administratorrechte:** Notwendig für die Erfassung von Netzwerkpaketen.

## Installation und Einrichtung

### Option 1: Schnellinstallation (Linux - Empfohlen)

Für Linux-Benutzer stellen wir automatisierte Installationsskripte bereit:

\`\`\`bash
# 1. Repository klonen
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Installationsskript ausführen
./install.sh

# 3. Anwendung ausführen
./run.sh
\`\`\`

Das Skript `install.sh` wird:
- Systemabhängigkeiten installieren (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Eine virtuelle Python-Umgebung erstellen
- Alle erforderlichen Python-Pakete installieren (Flet, Scapy)

Das Skript `run.sh` fordert automatisch Root-Rechte an und führt die Anwendung aus.

### Option 2: Manuelle Installation

#### 1. Systemabhängigkeiten installieren

**Unter Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Unter Windows:**

Installieren Sie Python 3.8+ von [python.org](https://www.python.org/downloads/)

#### 2. Python-Abhängigkeiten installieren

**Unter Linux (mit virtueller Umgebung - empfohlen):**

\`\`\`bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Virtuelle Umgebung aktivieren
source venv/bin/activate

# Abhängigkeiten installieren
pip install flet scapy
\`\`\`

**Unter Linux (systemweite Installation):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Unter Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Anwendung ausführen

Da das Sniffing des Netzwerks erhöhte Rechte erfordert, müssen Sie die Anwendung als Root oder Administrator ausführen.

**Unter Linux (mit virtueller Umgebung):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Unter Linux (systemweite Installation):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Unter Windows (Eingabeaufforderung/PowerShell als Administrator ausführen):**

\`\`\`bash
python -m albion_insight
\`\`\`

Die Anwendung wird in einem nativen Desktop-Fenster geöffnet.

## Erstellung einer ausführbaren Datei

Die Anwendung kann mit **PyInstaller** in eine eigenständige ausführbare Datei verpackt werden. Dies ermöglicht es Benutzern, die Anwendung auszuführen, ohne Python oder seine Abhängigkeiten installieren zu müssen.

Detaillierte Anweisungen zur Erstellung ausführbarer Dateien für Linux, Windows und macOS finden Sie im Handbuch **[PACKAGING.md](PACKAGING.md)**.

### Schnellerstellung (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Die ausführbare Datei befindet sich im Ordner `dist/`.

## Projektstruktur

Die Anwendung ist in modulare Komponenten für bessere Wartbarkeit und Skalierbarkeit strukturiert:

| Datei | Beschreibung |
| :--- | :--- |
| `albion_insight/core/` | Kernlogik, Netzwerkverfolgung, Datenmodelle und Protokolldekodierung. |
| `albion_insight/ui/` | Benutzeroberflächenkomponenten, erstellt mit Flet. |
| `albion_insight/utils/` | Dienstfunktionen, Konfiguration und Protokollierung (Logging). |
| `albion_insight/__main__.py` | Einstiegspunkt für die Anwendung. |
| `README.md` | Diese Dokumentationsdatei (in Englisch). |
| `README.pt-BR.md` | Diese Dokumentationsdatei (in Brasilianischem Portugiesisch). |
| `README.de-DE.md` | Diese Dokumentationsdatei (in Deutsch). |
| `CONTRIBUTING.md` | Richtlinien für Beiträge zum Projekt. |
| `CODE_OF_CONDUCT.md` | Der Verhaltenskodex des Projekts. |
| `SECURITY.md` | Richtlinie zur Meldung von Sicherheitslücken. |

## Aktueller Status (Echtzeitdaten)

Die Anwendung enthält nun die Logik zur **Dekodierung des Photon-Protokolls**, übersetzt aus dem ursprünglichen C#-Projekt. Dies ermöglicht es der Anwendung, Echtzeit-Ereignisse wie `UpdateMoney`, `UpdateFame`, `KilledPlayer` und `Died` direkt aus dem Netzwerkverkehr zu verarbeiten.

**Hinweis:** Die vollständige Übersetzung jedes einzelnen Kampfereignisses (wie `CastHit`, `Attack`) ist ein fortlaufender Aufwand. Die aktuelle Implementierung konzentriert sich auf die Kernstatistiken und die Struktur für den Schadenszähler. Die DPS-Berechnung des Schadenszählers basiert auf den dekodierten Ereignissen.

## Mitwirken

Wir freuen uns über Beiträge aus der Community! Egal, ob Sie Entwickler, Designer oder einfach nur ein Albion Online-Enthusiast sind, es gibt viele Möglichkeiten, Albion Insight zu verbessern.

Bitte lesen Sie unsere [Beitragsrichtlinien](CONTRIBUTING.md) für detaillierte Informationen, wie Sie zu diesem Projekt beitragen können.

### Schnellstart für Mitwirkende:

1.  Forken Sie das Repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klonen Sie Ihren Fork: `git clone https://github.com/IHR_BENUTZERNAME/AlbionInsight.git`
3.  Erstellen Sie einen neuen Branch: `git checkout -b feature/ihr-funktionsname`
4.  Nehmen Sie Ihre Änderungen vor und committen Sie: `git commit -m "Fügen Sie Ihre Funktion hinzu"`
5.  Pushen Sie zu Ihrem Fork: `git push origin feature/ihr-funktionsname`
6.  Öffnen Sie einen Pull Request im Haupt-Repository

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die Datei [LICENSE](LICENSE) für Details.

## Danksagungen

- Originalprojekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) von Triky313
- Erstellt mit dem [Flet](https://flet.dev/) Framework
- Netzwerkanalyse unterstützt durch [Scapy](https://scapy.net/)

---
*Eine plattformübergreifende Lösung für die Albion Online Community.*
