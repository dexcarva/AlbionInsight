# Architectuur Overzicht

Het Albion Insight-project volgt een modulair ontwerp om de zorgen over de gebruikersinterface, netwerklogica en gegevensbeheer te scheiden.

## Module Structuur

| Bestand | Verantwoordelijkheid | Details |
| :--- | :--- | :--- |
| `albion_insight/main.py` | **Gebruikersinterface (UI)** | Bevat de initialisatielogica van de Flet-applicatie en de constructie van alle visuele componenten (knoppen, lijsten, meters). Het communiceert met de `NetworkTracker` om gegevens op te halen en het scherm bij te werken. |
| `albion_insight/core/network_tracker.py` | **Netwerk Tracking en Protocol** | Verantwoordelijk voor het starten en stoppen van het pakket *sniffing* (`scapy`), het toepassen van BPF-filters en het decoderen van het **Photon**-protocol dat door Albion Online wordt gebruikt. Het vertaalt ruwe pakketten naar game-evenementen (schade, genezing, nieuwe spelers). |
| `albion_insight/core/models.py` | **Gegevensmodellen** | Bevat de pure gegevensklassen, zoals `PlayerStats` (individuele schade/genezing statistieken) en `SessionStats` (beheer van alle sessiestatistieken, duur, opslag). Dit zorgt ervoor dat de gegevenslogica onafhankelijk is van de UI en het netwerk. |

## Gegevensstroom

1.  **`albion_insight/main.py`** (UI) roept `tracker.start_sniffing(interface)` aan.
2.  **`albion_insight/core/network_tracker.py`** start een *sniffing* *thread* die UDP-pakketten vastlegt.
3.  De pakketten worden verwerkt door de `PhotonParser` om game-evenementen te extraheren.
4.  Gevechtsevenementen werken de `PlayerStats` instanties binnen `SessionStats` bij (in `albion_insight/core/models.py`).
5.  De `network_tracker.py` roept de `update_callback` aan (wat `AlbionInsightApp.update_ui` is in `albion_insight/main.py`).
6.  De UI (`albion_insight/main.py`) vraagt de geformatteerde gegevens op van `tracker.get_damage_meter_data()` en werkt de weergave bij.
