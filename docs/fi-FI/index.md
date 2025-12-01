# Tervetuloa Albion Insight -dokumentaatioon

Albion Insight on alustariippumaton (Linux, Windows, macOS) tilastoanalyysityökalu Albion Online -peliin. Se on toteutettu Pythonilla käyttäen Flet-kehystä.

Työkalu on suunniteltu seuraamaan reaaliaikaisia pelin sisäisiä tilastoja, kuten hopeaa, mainetta ja taistelutietoja (Damage Meter), analysoimalla verkkoliikennettä.

## Asennus

### Windows

1. Lataa uusin suoritettava tiedosto [julkaisusivulta](https://github.com/dexcarva/AlbionInsight/releases).
2. Pura tiedosto haluamaasi kansioon.
3. Suorita `AlbionInsight.exe`.

### Linux ja macOS

1. Varmista, että sinulla on Python 3.10+ asennettuna.
2. Kloonaa tämä arkisto:
   ```bash
   git clone https://github.com/dexcarva/AlbionInsight.git
   cd AlbionInsight
   ```
3. Luo ja aktivoi virtuaaliympäristö:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Asenna riippuvuudet:
   ```bash
   pip install -r requirements.txt
   ```
5. Suorita sovellus:
   ```bash
   python3 -m albion_insight
   ```

## Käyttö

Albion Insight toimii sieppaamalla Albion Online -pelin lähettämän ja vastaanottaman verkkoliikenteen. Se vaatii järjestelmänvalvojan oikeudet (tai vastaavat oikeudet Linuxissa/macOS:ssä) verkkoliikenteen sieppaamiseen.

**Huomautus:** Tämä työkalu on täysin passiivinen ja lukee vain verkkopaketteja. Se ei lähetä mitään tietoja takaisin peliin, mikä tekee siitä turvallisen käyttää.

## Osallistuminen

Olet lämpimästi tervetullut osallistumaan projektiin! Katso [CONTRIBUTING.md](contributing.md) saadaksesi lisätietoja.
