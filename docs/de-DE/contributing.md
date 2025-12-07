**[Read in English](../../CONTRIBUTING.md)** | **[Leia em Português (Brasil)](../pt-BR/contributing.md)** | **[Leia em Português (Portugal)](../pt-PT/contributing.md)**
**[Leer en Español](../es-ES/contributing.md)**
**[Lire en Français](../fr-FR/contributing.md)**
**[Read in Arabic (اقرأ بالعربية)](../ar-SA/contributing.md)**
**[Czytaj po Polsku](../pl-PL/contributing.md)**
**[Read in Hindi (हिंदी में पढ़ें)](../hi-IN/contributing.md)**
**[Read in Thai (อ่านเป็นภาษาไทย)](../th-TH/contributing.md)**
**[Read in Korean (한국어로 읽기)](../ko-KR/contributing.md)**
**[Přečtěte si v Češtině](../cs-CZ/contributing.md)**
**[Læs på Dansk](../da-DK/contributing.md)**
**[Διαβάστε στα Ελληνικά](../el-GR/contributing.md)**
**[بخوانید به فارسی](../fa-IR/contributing.md)**
**[Lue Suomeksi](../fi-FI/contributing.md)**
**[Basahin sa Filipino](../fil-PH/contributing.md)**
**[קראו בעברית](../he-IL/contributing.md)**
**[Baca dalam Bahasa Melayu](../ms-MY/contributing.md)**
**[Монгол хэлээр унших](../mn-MN/contributing.md)**
**[Citiți în Română](../ro-RO/contributing.md)**
**[Читати Українською](../uk-UA/contributing.md)**

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
pip install -r requirements-dev.txt

# Richten Sie Pre-Commit-Hooks ein (optional, aber empfohlen)
pre-commit install
```

### Ausführen der Anwendung

```bash
# Unter Linux/macOS:
sudo venv/bin/python3 -m albion_insight

# Unter Windows (als Administrator):
python -m albion_insight
```

## Codierungsstandards

Wir folgen den PEP 8 Style-Richtlinien für Python-Code. Bitte stellen Sie sicher, dass Ihr Code diesen Standards entspricht:

- Verwenden Sie 4 Leerzeichen für die Einrückung (keine Tabs)
- Maximale Zeilenlänge von 100 Zeichen
- Verwenden Sie aussagekräftige Variablen- und Funktionsnamen
- Fügen Sie Docstrings zu allen Funktionen und Klassen hinzu
- Fügen Sie Typ-Hinweise hinzu, wo angebracht
- Halten Sie Funktionen fokussiert und prägnant

**Hilfswerkzeuge (vor dem Committen ausführen):**

```bash
# Formatieren Sie Ihren Code mit black und isort
black albion_insight/
isort albion_insight/

# Überprüfen Sie auf Stilprobleme
flake8 albion_insight/

# Führen Sie die Typprüfung durch
mypy albion_insight/

# Führen Sie den Linter aus
pylint albion_insight/
```

**Automatisierte Qualitätsprüfungen:**

Wir verwenden `pre-commit` Hooks, um die Codequalität automatisch vor Commits zu prüfen. Wenn Sie Pre-Commit-Hooks installiert haben, werden sie automatisch bei `git commit` ausgeführt. Um sie manuell auszuführen:

```bash
pre-commit run --all-files
```

## Commit-Nachrichten

Wir folgen der **Conventional Commits** Spezifikation für klare und strukturierte Commit-Nachrichten:

**Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Typen:**
- `feat:` Eine neue Funktion
- `fix:` Eine Fehlerbehebung
- `docs:` Änderungen an der Dokumentation
- `style:` Code-Stil-Änderungen (Formatierung, fehlende Semikola usw.)
- `refactor:` Code-Umgestaltung ohne Funktionsänderungen
- `perf:` Leistungsverbesserungen
- `test:` Hinzufügen oder Aktualisieren von Tests
- `chore:` Build-Prozess, Abhängigkeiten oder Tooling-Änderungen

**Beispiele:**
```
feat(damage-meter): Exportfunktion für DPS-Berichte hinzufügen

Implementieren Sie CSV-Exportfunktion für Schadenszähler-Daten,
wodurch Benutzer Kampfstatistiken zur Analyse speichern können.

Schließt #123

fix(network): IPv6-Paketanalyse-Problem beheben

Aktualisieren Sie den Paketparser, um IPv6-Adressen korrekt zu verarbeiten
in der Netzwerkverkehrsanalyse.

docs(readme): macOS-Installationsanweisungen hinzufügen

style(code): Importe mit isort formatieren

refactor(core): Netzwerkverfolgungsmodul neu organisieren
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
