# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** on alustariippumaton (Linux, Windows, macOS) tilastoanalyysityökalu Albion Online -peliin, joka on toteutettu uudelleen **Pythonilla** käyttäen **Flet**-kehystä. Se on suunniteltu seuraamaan reaaliaikaisia pelin sisäisiä tilastoja, mukaan lukien hopea, maine ja taistelutiedot (Damage Meter), analysoimalla verkkoliikennettä.

Tämä projekti on moderni, avoimen lähdekoodin vaihtoehto alkuperäiselle C#/WPF-pohjaiselle `AlbionOnline-StatisticsAnalysis`-työkalulle, keskittyen monialustayhteensopivuuteen ja helppokäyttöisyyteen.

## Ominaisuudet

*   **Alustariippumattomuus:** Toimii natiivisti Linuxissa, Windowsissa ja macOS:ssä.
*   **Reaaliaikainen seuranta:** Käyttää `Scapy`-kirjastoa nuuskimaan UDP-paketteja Albion Onlinen porteissa (5055, 5056, 5058).
*   **Vahinkomittarin rakenne:** Sisältää tarvittavat tietorakenteet ja käyttöliittymän reaaliaikaisten taistelutilastojen (tehdyt vahingot, parannukset, DPS) näyttämiseen.
*   **Moderni käyttöliittymä:** Rakennettu Fletillä, tarjoten nopean, natiivin näköisen työpöytäsovelluksen.
*   **Istunnonhallinta:** Mahdollistaa istuntotilastojen käynnistämisen, pysäyttämisen, nollaamisen ja tallentamisen.

## Edellytykset

*   Python 3.8+
*   **Flet** ja **Scapy** -kirjastot.
*   **Pääkäyttäjän/Järjestelmänvalvojan oikeudet:** Tarvitaan verkkopakettien kaappaamiseen.

## Asennus ja käyttöönotto

### Vaihtoehto 1: Nopea asennus (Linux - Suositeltu)

Linux-käyttäjille tarjoamme automatisoidut asennusskriptit:

\`\`\`bash
# 1. Kloonaa arkisto
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Suorita asennusskripti
./install.sh

# 3. Suorita sovellus
./run.sh
\`\`\`

`install.sh`-skripti:
- Asentaa järjestelmäriippuvuudet (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Luo Pythonin virtuaaliympäristön
- Asentaa kaikki tarvittavat Python-paketit (Flet, Scapy)

`run.sh`-skripti pyytää automaattisesti pääkäyttäjän oikeudet ja suorittaa sovelluksen.

### Vaihtoehto 2: Manuaalinen asennus

#### 1. Asenna järjestelmäriippuvuudet

**Linuxissa (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Windowsissa:**

Asenna Python 3.8+ osoitteesta [python.org](https://www.python.org/downloads/)

#### 2. Asenna Python-riippuvuudet

**Linuxissa (käyttäen virtuaaliympäristöä - suositeltu):**

\`\`\`bash
# Luo virtuaaliympäristö
python3 -m venv venv

# Aktivoi virtuaaliympäristö
source venv/bin/activate

# Asenna riippuvuudet
pip install flet scapy
\`\`\`

**Linuxissa (järjestelmänlaajuinen asennus):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Windowsissa:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Sovelluksen suorittaminen

Koska verkon nuuskiminen vaatii korotetut oikeudet, sinun on suoritettava sovellus pääkäyttäjänä tai järjestelmänvalvojana.

**Linuxissa (virtuaaliympäristön kanssa):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Linuxissa (järjestelmänlaajuinen asennus):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Windowsissa (Suorita komentokehote/PowerShell järjestelmänvalvojana):**

\`\`\`bash
python -m albion_insight
\`\`\`

Sovellus avautuu natiivissa työpöytäikkunassa.

## Kuinka rakentaa suoritettava tiedosto

Sovellus voidaan paketoida itsenäiseksi suoritettavaksi tiedostoksi käyttämällä **PyInstalleria**. Tämä mahdollistaa käyttäjien suorittaa sovelluksen asentamatta Pythonia tai sen riippuvuuksia.

Yksityiskohtaiset ohjeet suoritettavien tiedostojen rakentamiseen Linuxille, Windowsille ja macOS:lle löytyvät **[PACKAGING.md](PACKAGING.md)**-oppaasta.

### Nopea rakennus (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Suoritettava tiedosto sijaitsee `dist/`-kansiossa.

## Projektin rakenne

Sovellus on jäsennelty modulaarisiin komponentteihin paremman ylläpidettävyyden ja skaalautuvuuden vuoksi:

| Tiedosto | Kuvaus |
| :--- | :--- |
| `albion_insight/core/` | Ydinlogiikka, verkon seuranta, datamallit ja protokollan dekoodaus. |
| `albion_insight/ui/` | Käyttöliittymäkomponentit, jotka on rakennettu Fletillä. |
| `albion_insight/utils/` | Aputoiminnot, konfiguraatio ja lokitus. |
| `albion_insight/__main__.py` | Sovelluksen käynnistyspiste. |
| `README.md` | Tämä dokumentaatiotiedosto. |
| `CONTRIBUTING.md` | Ohjeet projektiin osallistumiseen. |
| `CODE_OF_CONDUCT.md` | Projektin käytännesäännöt. |
| `SECURITY.md` | Tietoturva-aukkojen ilmoittamiskäytäntö. |
| `README.it-IT.md` | Dokumentaatio italiaksi. |
| `README.pt-BR.md` | Dokumentaatio brasilianportugaliksi. |
| `README.ru-RU.md` | Dokumentaatio venäjäksi. |
| `README.fr-FR.md` | Dokumentaatio ranskaksi. |
| `README.zh-CN.md` | Dokumentaatio yksinkertaistetulla kiinalla. |
| `README.ko-KR.md` | Dokumentaatio koreaksi. |
| `README.es-ES.md` | Dokumentaatio espanjaksi. |
| `README.de-DE.md` | Dokumentaatio saksaksi. |
| `README.pl-PL.md` | Dokumentaatio puolaksi. |
| `README.sv-SE.md` | Dokumentaatio ruotsiksi. |
| `README.vi-VN.md` | Dokumentaatio vietnamiksi. |
| `README.ar-SA.md` | Dokumentaatio arabiaksi. |
| `README.pt-PT.md` | Dokumentaatio euroopanportugaliksi. |
| `README.hi-IN.md` | Dokumentaatio hindiksi. |
| `README.hu-HU.md` | Dokumentaatio unkariksi. |
| `README.th-TH.md` | Dokumentaatio thaiksi. |
| `README.ja-JP.md` | Dokumentaatio japaniksi. |
| `README.tr-TR.md` | Dokumentaatio turkiksi. |
| `README.id-ID.md` | Dokumentaatio indonesiaksi. |
| `README.cs-CZ.md` | Dokumentaatio tšekiksi. |
| `README.nl-NL.md` | Dokumentaatio hollanniksi. |
| `README.fi-FI.md` | Dokumentaatio suomeksi. |

## Nykyinen tila (Reaaliaikainen data)

Sovellus sisältää nyt **Photon-protokollan dekoodauslogiikan**, joka on käännetty alkuperäisestä C#-projektista. Tämä mahdollistaa sovelluksen käsittelemään reaaliaikaisia tapahtumia, kuten `UpdateMoney`, `UpdateFame`, `KilledPlayer` ja `Died`, suoraan verkkoliikenteestä.

**Huomautus:** Jokaisen yksittäisen taistelutapahtuman (kuten `CastHit`, `Attack`) täydellinen kääntäminen on jatkuva ponnistus. Nykyinen toteutus keskittyy ydintilastoihin ja vahinkomittarin rakenteeseen. Vahinkomittarin DPS-laskenta perustuu dekoodattuihin tapahtumiin.

## Osallistuminen

Toivotamme tervetulleeksi yhteisön panoksen! Olitpa sitten kehittäjä, suunnittelija tai vain Albion Online -harrastaja, on monia tapoja auttaa parantamaan Albion Insightia.

Lue [Osallistumisohjeemme](CONTRIBUTING.md) saadaksesi yksityiskohtaista tietoa siitä, miten voit osallistua tähän projektiin.

### Pika-aloitus osallistujille:

1.  Forkkaa arkisto: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Kloonaa forkki: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Luo uusi haara: `git checkout -b feature/your-feature-name`
4.  Tee muutokset ja commit: `git commit -m "Add your feature"`
5.  Pushaa forkkiisi: `git push origin feature/your-feature-name`
6.  Avaa Pull Request pääarkistoon

## Lisenssi

Tämä projekti on lisensoitu MIT-lisenssillä - katso [LICENSE](LICENSE)-tiedosto saadaksesi lisätietoja.

## Kiitokset

- Alkuperäinen projekti: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- Rakennettu [Flet](https://flet.dev/) -kehyksellä
- Verkon analysointi [Scapy](https://scapy.net/) -kirjaston avulla

---
*Alustariippumaton ratkaisu Albion Online -yhteisölle.*
