# Bidra till Albion Insight

**[Läs detta på Svenska](CONTRIBUTING.sv-SE.md)**

Först och främst, tack för att du överväger att bidra till Albion Insight! Det är människor som du som gör Albion Insight till ett så bra verktyg för Albion Online-communityn.

## Innehållsförteckning

- [Uppförandekod](#uppförandekod)
- [Hur kan jag bidra?](#hur-kan-jag-bidra)
  - [Rapportera Buggar](#rapportera-buggar)
  - [Föreslå Funktioner](#föreslå-funktioner)
  - [Kodbidrag](#kodbidrag)
  - [Dokumentation](#dokumentation)
- [Utvecklingsmiljö](#utvecklingsmiljö)
- [Kodstandarder](#kodstandarder)
- [Commit-meddelanden](#commit-meddelanden)
- [Pull Request-processen](#pull-request-processen)

## Uppförandekod

Detta projekt och alla som deltar i det styrs av vår Uppförandekod. Genom att delta förväntas du upprätthålla denna kod. Vänligen rapportera oacceptabelt beteende till projektets underhållare.

## Hur kan jag bidra?

### Rapportera Buggar

Innan du skapar buggrapporter, vänligen kontrollera de befintliga ärendena för att undvika dubbletter. När du skapar en buggrapport, inkludera så många detaljer som möjligt med hjälp av mallen för buggrapporter.

**Bra buggrapporter inkluderar:**
- En tydlig och beskrivande titel
- Exakta steg för att återskapa problemet
- Förväntat kontra faktiskt beteende
- Skärmdumpar om tillämpligt
- Dina miljödetaljer (OS, Python-version, etc.)
- Relevanta loggar eller felmeddelanden

### Föreslå Funktioner

Funktionsförslag välkomnas! Använd mallen för funktionsförfrågan och ange:
- En tydlig beskrivning av funktionen
- Problemet den löser
- Möjliga implementeringsmetoder
- Eventuella alternativ du har övervägt

### Kodbidrag

Vi älskar kodbidrag! Så här kommer du igång:

1. **Fork:a repot** och skapa din gren från `master`
2. **Ställ in din utvecklingsmiljö** (se Utvecklingsmiljö nedan)
3. **Gör dina ändringar** enligt våra kodstandarder
4. **Testa dina ändringar** noggrant
5. **Uppdatera dokumentationen** vid behov
6. **Skicka in en pull request** med hjälp av vår PR-mall

### Dokumentation

Förbättringar av dokumentationen uppskattas alltid! Detta inkluderar:
- README-filer
- Wiki-sidor
- Kodkommentarer
- Handledningar och guider
- Översättningar till andra språk

## Utvecklingsmiljö

### Förutsättningar

- Python 3.8 eller högre
- Git
- Root/Administratörsrättigheter (för paketfångst)

### Ställa in din miljö

```bash
# Klona din fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Skapa en virtuell miljö
python3 -m venv venv

# Aktivera den virtuella miljön
# På Linux/macOS:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installera beroenden
pip install -r requirements.txt

# Installera utvecklingsberoenden
pip install pylint flake8 black pytest
```

### Köra Applikationen

```bash
# På Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# På Windows (som Administratör):
python albion_insight.py
```

## Kodstandarder

Vi följer PEP 8 stilriktlinjer för Python-kod. Se till att din kod följer dessa standarder:

- Använd 4 mellanslag för indrag (inga tabbar)
- Maximal radlängd på 100 tecken
- Använd meningsfulla variabel- och funktionsnamn
- Lägg till docstrings till alla funktioner och klasser
- Inkludera typ-hänvisningar där det är lämpligt
- Håll funktioner fokuserade och koncisa

**Verktyg som hjälper:**
```bash
# Formatera din kod med black
black albion_insight.py

# Kontrollera stilproblem
flake8 albion_insight.py

# Kör linter
pylint albion_insight.py
```

## Commit-meddelanden

Skriv tydliga och meningsfulla commit-meddelanden:

- Använd presens ("Lägg till funktion" inte "Lade till funktion")
- Använd imperativ form ("Flytta markören till..." inte "Flyttar markören till...")
- Begränsa den första raden till 72 tecken
- Hänvisa till ärenden och pull requests när det är relevant

**Exempel:**
```
Lägg till exportfunktionalitet för skademätare

Fixa nätverkspaketparsning för IPv6-anslutningar

Uppdatera README med installationsinstruktioner för macOS

Stänger #123
```

## Pull Request-processen

1. **Uppdatera dokumentationen** för alla ändringar i funktionaliteten
2. **Lägg till tester** för nya funktioner eller buggfixar
3. **Se till att alla tester passerar** innan du skickar in
4. **Uppdatera README.md** vid behov
5. **Fyll i PR-mallen** fullständigt
6. **Länka relaterade ärenden** i din PR-beskrivning
7. **Begär granskning** från underhållare
8. **Hantera feedback** snabbt och professionellt

### PR Checklista

Innan du skickar in din PR, se till att:
- [ ] Koden följer projektets stilriktlinjer
- [ ] Självgranskning slutförd
- [ ] Kommentarer tillagda till komplexa kodavsnitt
- [ ] Dokumentation uppdaterad
- [ ] Inga nya varningar genererade
- [ ] Tester tillagda och passerar
- [ ] Beroende ändringar sammanfogade

## Frågor?

Tveka inte att ställa frågor! Du kan:
- Öppna ett ärende med etiketten "question"
- Gå med i våra communitydiskussioner
- Kontakta underhållarna

Tack för att du bidrar till Albion Insight! Dina ansträngningar hjälper till att göra detta verktyg bättre för hela Albion Online-communityn.
