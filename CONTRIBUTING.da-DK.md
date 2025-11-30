# Bidrag til Albion Insight

**[Læs på Engelsk](CONTRIBUTING.md)** | **[Læs på Portugisisk (Brasilien)](CONTRIBUTING.pt-BR.md)** | **[Læs på Portugisisk (Portugal)](CONTRIBUTING.pt-PT.md)**
<!-- Zde budou přidány další odkazy na překlady -->

Først og fremmest tak for at overveje at bidrage til Albion Insight! Det er folk som dig, der gør Albion Insight til et så fantastisk værktøj for Albion Online-fællesskabet.

## Indholdsfortegnelse
	
- [Etiske Retningslinjer](#etiske-retningslinjer)
- [Hvordan kan jeg bidrage?](#hvordan-kan-jeg-bidrage)
  - [Rapportering af fejl](#rapportering-af-fejl)
  - [Forslag til funktioner](#forslag-til-funktioner)
  - [Kodebidrag](#kodebidrag)
  - [Dokumentation](#dokumentation)
- [Udviklingsopsætning](#udviklingsopsætning)
- [Kodningsstandarder](#kodningsstandarder)
- [Commit-beskeder](#commit-beskeder)
- [Pull Request-proces](#pull-request-proces)

## Etiske Retningslinjer

Dette projekt og alle, der deltager i det, er styret af vores Etiske Retningslinjer. Ved at deltage forventes du at overholde denne kode. Rapporter venligst uacceptabel adfærd til projektets vedligeholdere.

## Hvordan kan jeg bidrage?

### Rapportering af fejl

Før du opretter fejlrapporter, skal du kontrollere de eksisterende problemer for at undgå dubletter. Når du opretter en fejlrapport, skal du inkludere så mange detaljer som muligt ved hjælp af skabelonen til fejlrapporter.

**Gode fejlrapporter inkluderer:**
- En klar og beskrivende titel
- Præcise trin til at reproducere problemet
- Forventet vs. faktisk adfærd
- Skærmbilleder, hvis relevant
- Dine miljødetaljer (OS, Python-version osv.)
- Relevante logfiler eller fejlmeddelelser

### Forslag til funktioner

Forslag til funktioner er velkomne! Brug venligst skabelonen til funktionsanmodninger og angiv:
- En klar beskrivelse af funktionen
- Problemet, den løser
- Mulige implementeringsmetoder
- Eventuelle alternativer, du har overvejet

### Kodebidrag

Vi elsker kodebidrag! Sådan kommer du i gang:

1. **Fork depotet** og opret din gren fra `master`
2. **Opsæt dit udviklingsmiljø** (se Udviklingsopsætning nedenfor)
3. **Foretag dine ændringer** i henhold til vores kodningsstandarder
4. **Test dine ændringer** grundigt
5. **Opdater dokumentationen**, hvis det er nødvendigt
6. **Indsend en pull request** ved hjælp af vores PR-skabelon

### Dokumentation

Forbedringer af dokumentationen er altid værdsat! Dette inkluderer:
- README-filer
- Wiki-sider
- Kodekommentarer
- Tutorials og vejledninger
- Oversættelser til andre sprog

## Udviklingsopsætning

### Forudsætninger

- Python 3.8 eller højere
- Git
- Root/Administratorrettigheder (til pakkeopsamling)

### Opsætning af dit miljø

```bash
# Klon din fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Opret et virtuelt miljø
python3 -m venv venv

# Aktiver det virtuelle miljø
# På Linux/macOS:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installer afhængigheder
pip install -r requirements.txt

# Installer udviklingsafhængigheder
pip install pylint flake8 black pytest
```

### Kørsel af applikationen

```bash
# På Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# På Windows (som administrator):
python albion_insight.py
```

## Kodningsstandarder

Vi følger PEP 8 stilretningslinjerne for Python-kode. Sørg for, at din kode overholder disse standarder:

- Brug 4 mellemrum til indrykning (ingen tabs)
- Maksimal linjelængde på 100 tegn
- Brug meningsfulde variabel- og funktionsnavne
- Tilføj docstrings til alle funktioner og klasser
- Inkluder type hints, hvor det er relevant
- Hold funktioner fokuserede og præcise

**Værktøjer til hjælp:**
```bash
# Formater din kode med black
black albion_insight.py

# Tjek for stilproblemer
flake8 albion_insight.py

# Kør linter
pylint albion_insight.py
```

## Commit-beskeder

Skriv klare og meningsfulde commit-beskeder:

- Brug nutid ("Tilføj funktion" ikke "Tilføjede funktion")
- Brug bydeform ("Flyt markøren til..." ikke "Flytter markøren til...")
- Begræns den første linje til 72 tegn
- Henvis til problemer og pull requests, når det er relevant

**Eksempler:**
```
Tilføj funktionalitet til eksport af skademåler
	
Ret netværkspakkeparsing for IPv6-forbindelser
	
Opdater README med installationsinstruktioner til macOS
	
Lukker #123
```

## Pull Request-proces

1. **Opdater dokumentationen** for eventuelle ændringer i funktionaliteten
2. **Tilføj tests** for nye funktioner eller fejlrettelser
3. **Sørg for, at alle tests passerer** før indsendelse
4. **Opdater README.md**, hvis det er nødvendigt
5. **Udfyld PR-skabelonen** fuldstændigt
6. **Link relaterede problemer** i din PR-beskrivelse
7. **Anmod om gennemgang** fra vedligeholdere
8. **Håndter feedback** hurtigt og professionelt

### PR Tjekliste

Før du indsender din PR, skal du sikre dig:
- [ ] Koden følger projektets stilretningslinjer
- [ ] Selvgennemgang afsluttet
- [ ] Kommentarer tilføjet til komplekse kodeafsnit
- [ ] Dokumentation opdateret
- [ ] Ingen nye advarsler genereret
- [ ] Tests tilføjet og bestået
- [ ] Afhængige ændringer flettet

## Spørgsmål?

Tøv ikke med at stille spørgsmål! Du kan:
- Oprette et problem med mærket "question"
- Deltage i vores fællesskabsdiskussioner
- Kontakte vedligeholderne

Tak for dit bidrag til Albion Insight! Din indsats hjælper med at gøre dette værktøj bedre for hele Albion Online-fællesskabet.
