# Osallistuminen Albion Insightiin

**[Lue Englanniksi](CONTRIBUTING.md)** | **[Lue Portugaliksi (Brasilia)](CONTRIBUTING.pt-BR.md)** | **[Lue Portugaliksi (Portugali)](CONTRIBUTING.pt-PT.md)**
<!-- Tähän lisätään lisää käännöslinkkejä -->

Ensinnäkin, kiitos, että harkitset osallistumista Albion Insightiin! Juuri kaltaisesi ihmiset tekevät Albion Insightista niin hienon työkalun Albion Online -yhteisölle.

## Sisällysluettelo
	
- [Käytännesäännöt](#käytännesäännöt)
- [Miten voin osallistua?](#miten-voin-osallistua)
  - [Virheiden raportointi](#virheiden-raportointi)
  - [Ominaisuuksien ehdottaminen](#ominaisuuksien-ehdottaminen)
  - [Koodiosallistumiset](#koodiosallistumiset)
  - [Dokumentaatio](#dokumentaatio)
- [Kehitysympäristön asennus](#kehitysympäristön-asennus)
- [Koodausstandardit](#koodausstandardit)
- [Commit-viestit](#commit-viestit)
- [Pull Request -prosessi](#pull-request--prosessi)

## Käytännesäännöt

Tätä projektia ja kaikkia siihen osallistuvia ohjaa Käytännesääntömme. Osallistumalla sinun odotetaan noudattavan tätä koodia. Ilmoita sopimattomasta käytöksestä projektin ylläpitäjille.

## Miten voin osallistua?

### Virheiden raportointi

Ennen virheraporttien luomista, tarkista olemassa olevat ongelmat päällekkäisyyksien välttämiseksi. Kun luot virheraportin, sisällytä mahdollisimman paljon yksityiskohtia käyttämällä virheraporttimallia.

**Hyvät virheraportit sisältävät:**
- Selkeän ja kuvaavan otsikon
- Tarkat vaiheet ongelman toistamiseksi
- Odotettu vs. todellinen käyttäytyminen
- Kuvakaappaukset, jos sovellettavissa
- Ympäristösi tiedot (käyttöjärjestelmä, Python-versio jne.)
- Asiaankuuluvat lokit tai virheilmoitukset

### Ominaisuuksien ehdottaminen

Ominaisuusehdotukset ovat tervetulleita! Käytä ominaisuuspyyntömallia ja anna:
- Selkeä kuvaus ominaisuudesta
- Ongelma, jonka se ratkaisee
- Mahdolliset toteutustavat
- Kaikki harkitsemasi vaihtoehdot

### Koodiosallistumiset

Rakastamme koodiosallistumisia! Näin pääset alkuun:

1. **Forkkaa arkisto** ja luo oma haarasi `master`-haarasta
2. **Asenna kehitysympäristösi** (katso Kehitysympäristön asennus alla)
3. **Tee muutoksesi** noudattaen koodausstandardejamme
4. **Testaa muutoksesi** perusteellisesti
5. **Päivitä dokumentaatio** tarvittaessa
6. **Lähetä pull request** käyttämällä PR-malliamme

### Dokumentaatio

Dokumentaation parannukset ovat aina tervetulleita! Tämä sisältää:
- README-tiedostot
- Wiki-sivut
- Koodikommentit
- Oppaat ja ohjeet
- Käännökset muille kielille

## Kehitysympäristön asennus

### Edellytykset

- Python 3.8 tai uudempi
- Git
- Root/Järjestelmänvalvojan oikeudet (pakettien kaappaamiseen)

### Ympäristön asennus

```bash
# Kloonaa forkisi
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Luo virtuaalinen ympäristö
python3 -m venv venv

# Aktivoi virtuaalinen ympäristö
# Linuxissa/macOS:
source venv/bin/activate
# Windowsissa:
venv\Scripts\activate

# Asenna riippuvuudet
pip install -r requirements.txt

# Asenna kehitysriippuvuudet
pip install pylint flake8 black pytest
```

### Sovelluksen suorittaminen

```bash
# Linuxissa/macOS:
sudo venv/bin/python3 albion_insight.py

# Windowsissa (Järjestelmänvalvojana):
python albion_insight.py
```

## Koodausstandardit

Noudatamme PEP 8 -tyyliohjeita Python-koodille. Varmista, että koodisi noudattaa näitä standardeja:

- Käytä 4 välilyöntiä sisentämiseen (ei sarkaimia)
- Enimmäisrivin pituus 100 merkkiä
- Käytä merkityksellisiä muuttuja- ja funktionimiä
- Lisää docstringit kaikkiin funktioihin ja luokkiin
- Sisällytä tyyppivihjeet tarvittaessa
- Pidä funktiot keskittyneinä ja ytimekkäinä

**Työkalut avuksi:**
```bash
# Muotoile koodisi black-työkalulla
black albion_insight.py

# Tarkista tyyliongelmat
flake8 albion_insight.py

# Suorita linter
pylint albion_insight.py
```

## Commit-viestit

Kirjoita selkeät ja merkitykselliset commit-viestit:

- Käytä preesensiä ("Lisää ominaisuus" ei "Lisäsi ominaisuuden")
- Käytä imperatiivia ("Siirrä kohdistin kohtaan..." ei "Siirtää kohdistimen kohtaan...")
- Rajoita ensimmäinen rivi 72 merkkiin
- Viittaa ongelmiin ja pull requesteihin tarvittaessa

**Esimerkkejä:**
```
Lisää vahinkomittarin vientitoiminto
	
Korjaa verkkopakettien jäsentäminen IPv6-yhteyksille
	
Päivitä README macOS-asennusohjeilla
	
Sulkee #123
```

## Pull Request -prosessi

1. **Päivitä dokumentaatio** kaikista toiminnallisuuden muutoksista
2. **Lisää testejä** uusille ominaisuuksille tai virheenkorjauksille
3. **Varmista, että kaikki testit läpäisevät** ennen lähettämistä
4. **Päivitä README.md** tarvittaessa
5. **Täytä PR-malli** kokonaan
6. **Linkitä liittyvät ongelmat** PR-kuvaukseesi
7. **Pyydä tarkistus** ylläpitäjiltä
8. **Käsittele palaute** nopeasti ja ammattimaisesti

### PR-tarkistuslista

Varmista ennen PR:n lähettämistä, että:
- [ ] Koodi noudattaa projektin tyyliohjeita
- [ ] Itsearviointi suoritettu
- [ ] Kommentit lisätty monimutkaisiin koodiosiin
- [ ] Dokumentaatio päivitetty
- [ ] Uusia varoituksia ei ole luotu
- [ ] Testit lisätty ja läpäisty
- [ ] Riippuvaiset muutokset yhdistetty

## Kysymyksiä?

Älä epäröi kysyä! Voit:
- Avata ongelman "question"-tunnisteella
- Liittyä yhteisökeskusteluihimme
- Ottaa yhteyttä ylläpitäjiin

Kiitos osallistumisestasi Albion Insightiin! Ponnistelusi auttavat tekemään tästä työkalusta paremman koko Albion Online -yhteisölle.
