# Albion Insight

*Een platformonafhankelijke oplossing voor de Albion Online-gemeenschap.*

Albion Insight is een open-source, platformonafhankelijke tool voor Albion Online, ontworpen om netwerkverkeer te analyseren en real-time statistieken te bieden, zoals schade, genezing, en economische gegevens. Het is een port van het originele C#-project, **AlbionOnline-StatisticsAnalysis**, naar Python, waardoor het op Linux, macOS en Windows kan draaien.

## Functies

- **Real-Time Netwerk Sniffing:** Verwerkt Photon Protocol-gebeurtenissen om in-game statistieken te decoderen.
- **Platformonafhankelijk:** Draait op Linux, macOS en Windows.
- **Gebruikersinterface:** Gebouwd met het Flet-framework voor een native desktop-ervaring.
- **Economische Gegevens:** Volgt gebeurtenissen zoals `UpdateMoney`, `UpdateFame`, `KilledPlayer`, en `Died`.
- **Schademeter (In Ontwikkeling):** De structuur is aanwezig en de DPS-berekening is gebaseerd op gedecodeerde gebeurtenissen.

## Installatie

### Optie 1: Snelstart (Aanbevolen voor Linux)

Deze methode gebruikt de meegeleverde scripts om de omgeving snel in te stellen.

```bash
# 1. Kloon de repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Installeer afhankelijkheden
./install.sh

# 3. Start de applicatie
./run.sh
```

Het `install.sh`-script zal:
- Systeemafhankelijkheden installeren (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Een Python virtuele omgeving aanmaken
- Alle vereiste Python-pakketten installeren (Flet, Scapy)

Het `run.sh`-script zal automatisch root-rechten aanvragen en de applicatie starten.

### Optie 2: Handmatige Installatie

#### 1. Installeer Systeemafhankelijkheden

**Op Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```
**Op Windows:**
Installeer Python 3.8+ van [python.org](https://www.python.org/downloads/)

#### 2. Installeer Python Afhankelijkheden

**Op Linux (met virtuele omgeving - aanbevolen):**
```bash
# Maak virtuele omgeving
python3 -m venv venv
# Activeer virtuele omgeving
source venv/bin/activate
# Installeer afhankelijkheden
pip install flet scapy
```
**Op Linux (systeemwijde installatie):**
```bash
pip3 install flet scapy --break-system-packages
```
**Op Windows:**
```bash
pip install flet scapy
```

#### 3. De Applicatie Starten

Aangezien netwerk sniffing verhoogde rechten vereist, moet u de applicatie als root of beheerder uitvoeren.

**Op Linux (met virtuele omgeving):**
```bash
sudo venv/bin/python3 -m albion_insight
```
**Op Linux (systeemwijde installatie):**
```bash
sudo python3 -m albion_insight
```
**Op Windows (Start Opdrachtprompt/PowerShell als Beheerder):**
```bash
python -m albion_insight
```
De applicatie zal openen in een native desktopvenster.

## Hoe een Uitvoerbaar Bestand te Bouwen

De applicatie kan worden verpakt in een zelfstandig uitvoerbaar bestand met behulp van **PyInstaller**. Dit stelt gebruikers in staat de applicatie uit te voeren zonder Python of de afhankelijkheden te installeren.

Voor gedetailleerde instructies over het bouwen van uitvoerbare bestanden voor Linux, Windows en macOS, zie de **[PACKAGING.md](PACKAGING.md)** gids.

### Snelle Build (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```
Het uitvoerbare bestand zal zich in de map `dist/` bevinden.

## Projectstructuur

De applicatie is gestructureerd in modulaire componenten voor betere onderhoudbaarheid en schaalbaarheid:

| Bestand | Beschrijving |
| :--- | :--- |
| `albion_insight/core/` | Kernlogica, netwerk tracking, datamodellen en protocoldecodering. |
| `albion_insight/ui/` | Gebruikersinterfacecomponenten gebouwd met Flet. |
| `albion_insight/utils/` | Hulpprogrammafuncties, configuratie en logging. |
| `albion_insight/__main__.py` | Startpunt voor de applicatie. |
| `README.md` | Dit documentatiebestand. |
| `CONTRIBUTING.md` | Richtlijnen voor het bijdragen aan het project. |
| `CODE_OF_CONDUCT.md` | De gedragscode van het project. |
| `SECURITY.md` | Beleid voor het melden van beveiligingslekken. |
| `README.it-IT.md` | Documentatie in het Italiaans. |
| `README.pt-BR.md` | Documentatie in het Braziliaans Portugees. |
| `README.ru-RU.md` | Documentatie in het Russisch. |
| `README.fr-FR.md` | Documentatie in het Frans. |
| `README.zh-CN.md` | Documentatie in het Vereenvoudigd Chinees. |
| `README.ko-KR.md` | Documentatie in het Koreaans. |
| `README.es-ES.md` | Documentatie in het Spaans. |
| `README.nl-NL.md` | Documentatie in het Nederlands. |

## Huidige Status (Real-Time Gegevens)

De applicatie bevat nu de **Photon Protocol Decodering** logica, vertaald vanuit het originele C#-project. Dit stelt de applicatie in staat om real-time gebeurtenissen zoals `UpdateMoney`, `UpdateFame`, `KilledPlayer`, en `Died` direct uit het netwerkverkeer te verwerken.

**Opmerking:** De volledige vertaling van elke individuele gevechtsgebeurtenis (zoals `CastHit`, `Attack`) is een doorlopende inspanning. De huidige implementatie richt zich op de kernstatistieken en de structuur voor de Schademeter. De DPS-berekening van de Schademeter is gebaseerd op de gedecodeerde gebeurtenissen.

## Bijdragen

We verwelkomen bijdragen van de gemeenschap! Of u nu een ontwikkelaar, ontwerper of gewoon een Albion Online-enthousiasteling bent, er zijn veel manieren om Albion Insight te helpen verbeteren.

Lees onze [Bijdragerichtlijnen](CONTRIBUTING.md) voor gedetailleerde informatie over hoe u kunt bijdragen aan dit project.

### Snelstart voor Bijdragers:
1.  Fork de repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Kloon uw fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Maak een nieuwe branch: `git checkout -b feature/uw-functienaam`
4.  Voer uw wijzigingen door en commit: `git commit -m "Voeg uw functie toe"`
5.  Push naar uw fork: `git push origin feature/uw-functienaam`
6.  Open een Pull Request op de hoofdrepository

## Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het [LICENSE](LICENSE)-bestand voor details.

## Erkenningen

- Origineel project: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) door Triky313
- Gebouwd met het [Flet](https://flet.dev/) framework
- Netwerkanalyse aangedreven door [Scapy](https://scapy.net/)
---
*Een platformonafhankelijke oplossing voor de Albion Online-gemeenschap.*
