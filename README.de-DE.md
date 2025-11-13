# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Lesen Sie dies auf Deutsch (Read this in German)](README.de-DE.md)**\n**[Lesen Sie dies auf Portugiesisch (Leia em Português)](README.pt-BR.md)**
**[Lesen Sie dies auf Spanisch (Leer en Español)](README.es-ES.md)**
**[Lesen Sie dies auf Französisch (Lire en Français)](README.fr-FR.md)**
**[Lesen Sie dies auf Italienisch (Leggi in Italiano)](README.it-IT.md)**\n**[Lesen Sie dies auf Vereinfachtem Chinesisch (阅读简体中文)](README.zh-CN.md)**\n**[Lesen Sie dies auf Russisch (Прочитать на русском)](README.ru-RU.md)**\n**[Lesen Sie dies auf Japanisch (日本語で読む)](README.ja-JP.md)**\n**[Lesen Sie dies auf Arabisch (اقرأ هذا بالعربية)](README.ar-SA.md)**\n**[Lesen Sie dies auf Türkisch (Türkçe Oku)](README.tr-TR.md)**\n**[Lesen Sie dies auf Koreanisch (한국어로 읽기)](README.ko-KR.md)**\n**[Lesen Sie dies auf Niederländisch (Lees dit in het Nederlands)](README.nl-NL.md)**\n**[Lesen Sie dies auf Polnisch (Czytaj po polsku)](README.pl-PL.md)**

**Albion Insight** ist ein plattformübergreifendes (Linux, Windows, macOS) Statistik-Analyse-Tool für das Spiel Albion Online, neu implementiert in **Python** unter Verwendung des **Flet** Frameworks. Es wurde entwickelt, um Echtzeit-Statistiken im Spiel zu verfolgen, einschließlich Silber, Ruhm und Kampfdaten (Damage Meter), durch die Analyse des Netzwerkverkehrs.

Dieses Projekt ist eine moderne, quelloffene Alternative zum ursprünglichen C#/WPF-basierten Tool `AlbionOnline-StatisticsAnalysis`, wobei der Fokus auf plattformübergreifender Kompatibilität und Benutzerfreundlichkeit liegt.

## Funktionen

*   **Plattformübergreifende Kompatibilität:** Läuft nativ auf Linux, Windows und macOS.
*   **Echtzeit-Verfolgung:** Verwendet die `Scapy`-Bibliothek, um UDP-Pakete auf den Albion Online Ports (5055, 5056, 5058) zu sniffen.
*   **Damage Meter Struktur:** Enthält die notwendigen Datenstrukturen und die Benutzeroberfläche, um Live-Kampfstatistiken (Verursachter Schaden, Geheilter Schaden, DPS) anzuzeigen.
*   **Moderne Benutzeroberfläche:** Erstellt mit Flet, bietet eine schnelle, nativ aussehende Desktop-Anwendung.
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

Das Skript `install.sh` wird:
- Systemabhängigkeiten installieren (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Eine virtuelle Python-Umgebung erstellen
- Alle erforderlichen Python-Pakete (Flet, Scapy) installieren

Das Skript `run.sh` fordert automatisch Root-Rechte an und führt die Anwendung aus.

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

**Unter Linux (systemweite Installation):**

```bash
pip3 install flet scapy --break-system-packages
```

**Unter Windows:**

```bash
pip install flet scapy
```

#### 3. Anwendung ausführen

Da das Sniffing des Netzwerks erhöhte Rechte erfordert, müssen Sie die Anwendung als Root oder Administrator ausführen.

**Unter Linux (mit virtueller Umgebung):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Unter Linux (systemweite Installation):**

```bash
sudo python3 albion_insight/main.py
```

**Unter Windows (Eingabeaufforderung/PowerShell als Administrator ausführen):**

```bash
python albion_insight/main.py
```

Die Anwendung wird in einem nativen Desktop-Fenster geöffnet.

## Erstellen einer ausführbaren Datei

Die Anwendung kann mit **PyInstaller** in eine eigenständige ausführbare Datei verpackt werden. Dies ermöglicht es Benutzern, die Anwendung auszuführen, ohne Python oder seine Abhängigkeiten installieren zu müssen.

Detaillierte Anweisungen zum Erstellen ausführbarer Dateien für Linux, Windows und macOS finden Sie in der Anleitung **[PACKAGING.md](PACKAGING.md)**.

### Schnellstart (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Die ausführbare Datei befindet sich im Ordner `dist/`.

## Projektstruktur

Die gesamte Anwendung ist der Einfachheit halber in einer einzigen Datei enthalten:

| Datei | Beschreibung |
| :--- | :--- |
| `albion_insight/main.py` | Die Hauptanwendungsdatei, die die gesamte Logik (Modelle, Netzwerk-Tracker, Flet-Benutzeroberfläche) enthält. |
| `README.md` | Diese Dokumentationsdatei. |
| `README.pt-BR.md` | Diese Dokumentationsdatei in brasilianischem Portugiesisch. |
| `CONTRIBUTING.md` | Richtlinien für die Mitwirkung am Projekt. |
| `CODE_OF_CONDUCT.md` | Der Verhaltenskodex des Projekts. |
| `SECURITY.md` | Richtlinie zur Meldung von Sicherheitslücken. |

## Aktueller Status (Echtzeitdaten)

Die Anwendung enthält nun die Logik zur **Photon-Protokoll-Dekodierung**, die aus dem ursprünglichen C#-Projekt übersetzt wurde. Dies ermöglicht es der Anwendung, Echtzeit-Ereignisse wie `UpdateMoney`, `UpdateFame`, `KilledPlayer` und `Died` direkt aus dem Netzwerkverkehr zu verarbeiten.

**Hinweis:** Die vollständige Übersetzung jedes einzelnen Kampfereignisses (wie `CastHit`, `Attack`) ist ein fortlaufender Aufwand. Die aktuelle Implementierung konzentriert sich auf die Kernstatistiken und die Struktur für das Damage Meter. Die DPS-Berechnung des Damage Meters basiert auf den dekodierten Ereignissen.

## Mitwirken

Wir freuen uns über Beiträge aus der Community! Egal, ob Sie Entwickler, Designer oder einfach nur ein Albion Online-Enthusiast sind, es gibt viele Möglichkeiten, Albion Insight zu verbessern.

Bitte lesen Sie unsere [Richtlinien für Mitwirkende](CONTRIBUTING.md) für detaillierte Informationen, wie Sie zu diesem Projekt beitragen können.

### Schnellstart für Mitwirkende:

1.  Forken Sie das Repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klonen Sie Ihren Fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Erstellen Sie einen neuen Branch: `git checkout -b feature/ihr-feature-name`
4.  Nehmen Sie Ihre Änderungen vor und committen Sie: `git commit -m "Fügen Sie Ihre Funktion hinzu"`
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
