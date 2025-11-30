# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Read this in other languages</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)** | **[Finnish](README.fi-FI.md)** | **[Polish](README.pl-PL.md)** | **[Danish](README.da-DK.md)** | **[Ukrainian](README.uk-UA.md)** | **[Malay](README.ms-MY.md)** | **[Estonian](README.et-EE.md)** | **[Mongolian](README.mn-MN.md)**

</details>

**Albion Insight** ist ein plattformübergreifendes (Linux, Windows, macOS) Statistik-Analyse-Tool für das Spiel Albion Online, das in **Python** unter Verwendung des **Flet**-Frameworks neu implementiert wurde. Es wurde entwickelt, um Echtzeit-Statistiken im Spiel zu verfolgen, einschließlich Silber, Ruhm und Kampfdaten (Schadenszähler), durch die Analyse des Netzwerkverkehrs.

Dieses Projekt ist eine moderne, Open-Source-Alternative zum ursprünglichen C#/WPF-basierten Tool `AlbionOnline-StatisticsAnalysis` und konzentriert sich auf Multi-Plattform-Kompatibilität und Benutzerfreundlichkeit.

## Funktionen

*   **Plattformübergreifende Kompatibilität:** Läuft nativ unter Linux, Windows und macOS.
*   **Echtzeit-Verfolgung:** Verwendet die `Scapy`-Bibliothek, um UDP-Pakete auf den Albion Online-Ports (5055, 5056, 5058) abzufangen.
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

**Unter Linux (systemweite Installation):**

```bash
pip3 install flet scapy --break-system-packages
```

**Unter Windows:**

```bash
pip install flet scapy
```

#### 3. Anwendung ausführen

Da das Abfangen von Netzwerkpaketen erhöhte Berechtigungen erfordert, müssen Sie die Anwendung als Root oder Administrator ausführen.

**Unter Linux (mit virtueller Umgebung):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Unter Linux (systemweite Installation):**

```bash
sudo python3 -m albion_insight
```

**Unter Windows (Eingabeaufforderung/PowerShell als Administrator ausführen):**

```bash
python -m albion_insight
```

Die Anwendung wird in einem nativen Desktop-Fenster geöffnet.

## Erstellen einer ausführbaren Datei

Die Anwendung kann mit **PyInstaller** in eine eigenständige ausführbare Datei verpackt werden. Dies ermöglicht es Benutzern, die Anwendung auszuführen, ohne Python oder seine Abhängigkeiten installieren zu müssen.

Detaillierte Anweisungen zum Erstellen ausführbarer Dateien für Linux, Windows und macOS finden Sie in der Anleitung **[PACKAGING.md](PACKAGING.md)**.

### Schnellerstellung (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Die ausführbare Datei befindet sich im Ordner `dist/`.

## Projektstruktur

Die Anwendung ist in modulare Komponenten für bessere Wartbarkeit und Skalierbarkeit strukturiert:

| Datei | Beschreibung |
| :--- | :--- |
| `albion_insight/core/` | Kernlogik, Netzwerkverfolgung, Datenmodelle und Protokolldecodierung. |
| `albion_insight/ui/` | Benutzeroberflächenkomponenten, erstellt mit Flet. |
| `albion_insight/utils/` | Dienstfunktionen, Konfiguration und Protokollierung. |
| `albion_insight/__main__.py` | Einstiegspunkt für die Anwendung. |
| `README.md` | Diese Dokumentationsdatei. |
| `README.pt-BR.md` | Diese Dokumentationsdatei in brasilianischem Portugiesisch. |
| `README.fil-PH.md` | Diese Dokumentationsdatei in Filipino (Tagalog). |
| `README.pt-PT.md` | Diese Dokumentationsdatei in portugiesischem Portugiesisch. |
| `README.ko-KR.md` | Diese Dokumentationsdatei in Koreanisch. |
| `README.sv-SE.md` | Diese Dokumentationsdatei in Schwedisch. |
| `README.da-DK.md` | Diese Dokumentationsdatei in Dänisch. |
| `CONTRIBUTING.sv-SE.md` | Richtlinien für die Mitarbeit am Projekt in Schwedisch. |
| `CONTRIBUTING.md` | Richtlinien für die Mitarbeit am Projekt. |
| `CODE_OF_CONDUCT.md` | Der Verhaltenskodex des Projekts. |
| `SECURITY.md` | Richtlinie zur Meldung von Sicherheitslücken. |

## Aktueller Status (Echtzeitdaten)

Die Anwendung enthält nun die Logik zur **Photon-Protokolldecodierung**, die aus dem ursprünglichen C#-Projekt übersetzt wurde. Dies ermöglicht es der Anwendung, Echtzeit-Ereignisse wie `UpdateMoney`, `UpdateFame`, `KilledPlayer` und `Died` direkt aus dem Netzwerkverkehr zu verarbeiten.

**Hinweis:** Die vollständige Übersetzung jedes einzelnen Kampfereignisses (wie `CastHit`, `Attack`) ist ein fortlaufendes Unterfangen. Die aktuelle Implementierung konzentriert sich auf die Kernstatistiken und die Struktur für den Schadenszähler. Die DPS-Berechnung des Schadenszählers basiert auf den decodierten Ereignissen.

## Mitwirken

Wir freuen uns über Beiträge aus der Community! Egal, ob Sie Entwickler, Designer oder einfach nur ein Albion Online-Enthusiast sind, es gibt viele Möglichkeiten, Albion Insight zu verbessern.

Bitte lesen Sie unsere [Beitragsrichtlinien](CONTRIBUTING.md) für detaillierte Informationen zur Mitarbeit an diesem Projekt.

### Schnellstart für Mitwirkende:

1.  Forken Sie das Repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Klonen Sie Ihren Fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Erstellen Sie einen neuen Branch: `git checkout -b feature/ihr-funktionsname`
4.  Nehmen Sie Ihre Änderungen vor und committen Sie: `git commit -m "Fügt Ihre Funktion hinzu"`
5.  Pushen Sie zu Ihrem Fork: `git push origin feature/ihr-funktionsname`
6.  Öffnen Sie einen Pull Request im Haupt-Repository

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die Datei [LICENSE](LICENSE) für Details.

## Danksagungen

- Ursprüngliches Projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) von Triky313
- Erstellt mit dem [Flet](https://flet.dev/) Framework
- Netzwerkanalyse unterstützt durch [Scapy](https://scapy.net/)

---
*Eine plattformübergreifende Lösung für die Albion Online-Community.*
