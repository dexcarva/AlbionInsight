# Bijdragen aan Albion Insight

**[Lees in het Nederlands](CONTRIBUTING.nl-NL.md)** | **[Lees in het Engels](CONTRIBUTING.md)**

Allereerst, bedankt dat u overweegt bij te dragen aan Albion Insight! Het zijn mensen zoals u die Albion Insight zo'n geweldige tool maken voor de Albion Online-gemeenschap.

## Inhoudsopgave

- [Gedragscode](#gedragscode)
- [Hoe kan ik bijdragen?](#hoe-kan-ik-bijdragen)
  - [Bugs melden](#bugs-melden)
  - [Functies voorstellen](#functies-voorstellen)
  - [Codebijdragen](#codebijdragen)
  - [Documentatie](#documentatie)
- [Ontwikkelingsinstellingen](#ontwikkelingsinstellingen)
- [Coderingsstandaarden](#coderingsstandaarden)
- [Commitberichten](#commitberichten)
- [Pull Request Proces](#pull-request-proces)

## Gedragscode

Dit project en iedereen die eraan deelneemt, wordt beheerst door onze Gedragscode. Door deel te nemen, wordt van u verwacht dat u deze code handhaaft. Meld onaanvaardbaar gedrag aan de projectbeheerders.

## Hoe kan ik bijdragen?

### Bugs melden

Voordat u bugrapporten maakt, controleer alstublieft de bestaande issues om duplicaten te voorkomen. Wanneer u een bugrapport maakt, vermeld dan zoveel mogelijk details met behulp van de bugrapportsjabloon.

**Goede bugrapporten bevatten:**
- Een duidelijke en beschrijvende titel
- Exacte stappen om het probleem te reproduceren
- Verwacht versus werkelijk gedrag
- Screenshots indien van toepassing
- Uw omgevingsdetails (OS, Python-versie, enz.)
- Relevante logs of foutmeldingen

### Functies voorstellen

Functievoorstellen zijn welkom! Gebruik alstublieft de functieverzoeksjabloon en geef:
- Een duidelijke beschrijving van de functie
- Het probleem dat het oplost
- Mogelijke implementatiebenaderingen
- Eventuele alternatieven die u hebt overwogen

### Codebijdragen

We houden van codebijdragen! Zo kunt u beginnen:

1. **Fork de repository** en creëer uw branch vanuit `master`
2. **Stel uw ontwikkelomgeving in** (zie Ontwikkelingsinstellingen hieronder)
3. **Breng uw wijzigingen aan** volgens onze coderingsstandaarden
4. **Test uw wijzigingen** grondig
5. **Update de documentatie** indien nodig
6. **Dien een pull request in** met behulp van onze PR-sjabloon

### Documentatie

Verbeteringen aan de documentatie worden altijd op prijs gesteld! Dit omvat:
- README-bestanden
- Wiki-pagina's
- Codecommentaar
- Tutorials en handleidingen
- Vertalingen naar andere talen

## Ontwikkelingsinstellingen

### Vereisten

- Python 3.8 of hoger
- Git
- Root/Administrator-rechten (voor pakketvastlegging)

### Uw Omgeving Instellen

```bash
# Kloon uw fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Creëer een virtuele omgeving
python3 -m venv venv

# Activeer de virtuele omgeving
# Op Linux/macOS:
source venv/bin/activate
# Op Windows:
venv\Scripts\activate

# Installeer afhankelijkheden
pip install -r requirements.txt

# Installeer ontwikkelingsafhankelijkheden
pip install pylint flake8 black pytest
```

### De Applicatie Uitvoeren

```bash
# Op Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Op Windows (als Beheerder):
python albion_insight.py
```

## Coderingsstandaarden

We volgen de PEP 8 stijlrichtlijnen voor Python-code. Zorg ervoor dat uw code voldoet aan deze standaarden:

- Gebruik 4 spaties voor inspringing (geen tabs)
- Maximale lijnlengte van 100 tekens
- Gebruik betekenisvolle variabele- en functienamen
- Voeg docstrings toe aan alle functies en klassen
- Voeg type-hints toe waar nodig
- Houd functies gefocust en beknopt

**Hulpmiddelen om te helpen:**
```bash
# Formatteer uw code met black
black albion_insight.py

# Controleer op stijlfouten
flake8 albion_insight.py

# Voer linter uit
pylint albion_insight.py
```

## Commitberichten

Schrijf duidelijke en betekenisvolle commitberichten:

- Gebruik de tegenwoordige tijd ("Voeg functie toe" niet "Voegde functie toe")
- Gebruik de gebiedende wijs ("Verplaats cursor naar..." niet "Verplaatst cursor naar...")
- Beperk de eerste regel tot 72 tekens
- Verwijs naar issues en pull requests wanneer relevant

**Voorbeelden:**
```
Voeg exportfunctionaliteit voor schade meter toe

Los netwerkpakketparsing voor IPv6-verbindingen op

Update README met macOS installatie-instructies

Sluit #123
```

## Pull Request Proces

1. **Update de documentatie** voor eventuele wijzigingen in de functionaliteit
2. **Voeg tests toe** voor nieuwe functies of bugfixes
3. **Zorg ervoor dat alle tests slagen** voordat u indient
4. **Update de README.md** indien nodig
5. **Vul de PR-sjabloon** volledig in
6. **Koppel gerelateerde issues** in uw PR-beschrijving
7. **Vraag om beoordeling** van beheerders
8. **Behandel feedback** snel en professioneel

### PR Checklist

Voordat u uw PR indient, zorg ervoor dat:
- [ ] Code voldoet aan de stijlrichtlijnen van het project
- [ ] Zelfbeoordeling voltooid
- [ ] Opmerkingen toegevoegd aan complexe codegedeelten
- [ ] Documentatie bijgewerkt
- [ ] Geen nieuwe waarschuwingen gegenereerd
- [ ] Tests toegevoegd en geslaagd
- [ ] Afhankelijke wijzigingen samengevoegd

## Vragen?

Aarzel niet om vragen te stellen! U kunt:
- Een issue openen met het label "vraag"
- Deelnemen aan onze gemeenschapsdiscussies
- Contact opnemen met de beheerders

Bedankt voor uw bijdrage aan Albion Insight! Uw inspanningen helpen deze tool beter te maken voor de hele Albion Online-gemeenschap.
