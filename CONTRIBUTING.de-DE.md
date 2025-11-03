**[Read in English](CONTRIBUTING.md)**
**[Leia em Português](CONTRIBUTING.pt-BR.md)**
**[Leer en Español](CONTRIBUTING.es-ES.md)**
**[Lire en Français](CONTRIBUTING.fr-FR.md)**

Zunächst einmal vielen Dank, dass Sie in Erwägung ziehen, zu Albion Insight beizutragen! Es sind Menschen wie Sie, die Albion Insight zu einem so großartigen Werkzeug für die Albion Online Community machen.

## Inhaltsverzeichnis

- [Verhaltenskodex](#verhaltenskodex)
- [Wie kann ich beitragen?](#wie-kann-ich-beitragen)
  - [Fehler melden](#fehler-melden)
  - [Funktionen vorschlagen](#funktionen-vorschlagen)
  - [Code-Beiträge](#code-beiträge)
  - [Dokumentation](#dokumentation)
- [Entwicklungsumgebung einrichten](#entwicklungsumgebung-einrichten)
- [Codierungsstandards](#codierungsstandards)
- [Commit-Nachrichten](#commit-nachrichten)
- [Pull-Request-Prozess](#pull-request-prozess)

## Verhaltenskodex

Dieses Projekt und alle daran Beteiligten unterliegen unserem Verhaltenskodex. Durch Ihre Teilnahme wird erwartet, dass Sie diesen Kodex einhalten. Bitte melden Sie inakzeptables Verhalten den Projektbetreuern.

## Wie kann ich beitragen?

### Fehler melden

Bevor Sie Fehlerberichte erstellen, überprüfen Sie bitte die bestehenden Issues, um Duplikate zu vermeiden. Wenn Sie einen Fehlerbericht erstellen, fügen Sie bitte so viele Details wie möglich unter Verwendung der Fehlerberichtsvorlage bei.

**Gute Fehlerberichte enthalten:**
- Einen klaren und beschreibenden Titel
- Genaue Schritte zur Reproduktion des Problems
- Erwartetes vs. tatsächliches Verhalten
- Screenshots, falls zutreffend
- Details zu Ihrer Umgebung (Betriebssystem, Python-Version usw.)
- Relevante Protokolle oder Fehlermeldungen

### Funktionen vorschlagen

Funktionsvorschläge sind willkommen! Bitte verwenden Sie die Vorlage für Funktionsanfragen und geben Sie Folgendes an:
- Eine klare Beschreibung der Funktion
- Das Problem, das sie löst
- Mögliche Implementierungsansätze
- Alle Alternativen, die Sie in Betracht gezogen haben

### Code-Beiträge

Wir freuen uns über Code-Beiträge! So können Sie beginnen:

1. **Forken Sie das Repository** und erstellen Sie Ihren Branch von `master`
2. **Richten Sie Ihre Entwicklungsumgebung ein** (siehe Entwicklungsumgebung einrichten unten)
3. **Nehmen Sie Ihre Änderungen vor** und halten Sie sich an unsere Codierungsstandards
4. **Testen Sie Ihre Änderungen** gründlich
5. **Aktualisieren Sie die Dokumentation**, falls erforderlich
6. **Reichen Sie einen Pull Request ein** unter Verwendung unserer PR-Vorlage

### Dokumentation

Verbesserungen an der Dokumentation werden immer geschätzt! Dazu gehören:
- README-Dateien
- Wiki-Seiten
- Code-Kommentare
- Tutorials und Anleitungen
- Übersetzungen in andere Sprachen

## Entwicklungsumgebung einrichten

### Voraussetzungen

- Python 3.8 oder höher
- Git
- Root-/Administratorrechte (für die Paketerfassung)

### Einrichten Ihrer Umgebung

```bash
# Klonen Sie Ihren Fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Erstellen Sie eine virtuelle Umgebung
python3 -m venv venv

# Aktivieren Sie die virtuelle Umgebung
# Unter Linux/macOS:
source venv/bin/activate
# Unter Windows:
venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Entwicklungsabhängigkeiten installieren
pip install pylint flake8 black pytest
```

### Ausführen der Anwendung

```bash
# Unter Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Unter Windows (als Administrator):
python albion_insight.py
```

## Codierungsstandards

Wir folgen den PEP 8 Style-Richtlinien für Python-Code. Bitte stellen Sie sicher, dass Ihr Code diesen Standards entspricht:

- Verwenden Sie 4 Leerzeichen für die Einrückung (keine Tabs)
- Maximale Zeilenlänge von 100 Zeichen
- Verwenden Sie aussagekräftige Variablen- und Funktionsnamen
- Fügen Sie Docstrings zu allen Funktionen und Klassen hinzu
- Fügen Sie Typ-Hinweise hinzu, wo angebracht
- Halten Sie Funktionen fokussiert und prägnant

**Hilfswerkzeuge:**
```bash
# Formatieren Sie Ihren Code mit black
black albion_insight.py

# Überprüfen Sie auf Stilprobleme
flake8 albion_insight.py

# Führen Sie den Linter aus
pylint albion_insight.py
```

## Commit-Nachrichten

Schreiben Sie klare und aussagekräftige Commit-Nachrichten:

- Verwenden Sie die Gegenwartsform ("Füge Funktion hinzu" statt "Funktion hinzugefügt")
- Verwenden Sie den Imperativ ("Bewege Cursor zu..." statt "Bewegt Cursor zu...")
- Beschränken Sie die erste Zeile auf 72 Zeichen
- Verweisen Sie auf Issues und Pull Requests, wenn relevant

**Beispiele:**
```
Füge Exportfunktion für Schadenszähler hinzu

Behebe Netzwerkpaket-Parsing für IPv6-Verbindungen

Aktualisiere README mit Installationsanweisungen für macOS

Schließt #123
```

## Pull-Request-Prozess

1. **Aktualisieren Sie die Dokumentation** für alle Änderungen an der Funktionalität
2. **Fügen Sie Tests hinzu** für neue Funktionen oder Fehlerbehebungen
3. **Stellen Sie sicher, dass alle Tests bestanden werden**, bevor Sie einreichen
4. **Aktualisieren Sie die README.md**, falls erforderlich
5. **Füllen Sie die PR-Vorlage** vollständig aus
6. **Verknüpfen Sie verwandte Issues** in Ihrer PR-Beschreibung
7. **Fordern Sie eine Überprüfung** von den Betreuern an
8. **Gehen Sie zeitnah und professionell auf Feedback ein**

### PR-Checkliste

Stellen Sie vor dem Einreichen Ihres PR sicher:
- [ ] Der Code folgt den Stilrichtlinien des Projekts
- [ ] Die Selbstüberprüfung wurde abgeschlossen
- [ ] Kommentare wurden zu komplexen Codeabschnitten hinzugefügt
- [ ] Die Dokumentation wurde aktualisiert
- [ ] Es wurden keine neuen Warnungen generiert
- [ ] Tests wurden hinzugefügt und bestanden
- [ ] Abhängige Änderungen wurden zusammengeführt

## Fragen?

Zögern Sie nicht, Fragen zu stellen! Sie können:
- Ein Issue mit dem Label "question" öffnen
- An unseren Community-Diskussionen teilnehmen
- Die Betreuer kontaktieren

Vielen Dank für Ihren Beitrag zu Albion Insight! Ihre Bemühungen tragen dazu bei, dieses Tool für die gesamte Albion Online Community besser zu machen.
