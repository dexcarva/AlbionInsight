# Albion Insight

**Albion Insight** és una eina d'anàlisi d'estadístiques multiplataforma (Linux, Windows, macOS) per al joc Albion Online, reimplementada en **Python** utilitzant el *framework* **Flet**. Està dissenyada per rastrejar estadístiques en temps real dins del joc, incloent plata, fama i dades de combat (Mesurador de Dany), mitjançant l'anàlisi del trànsit de xarxa.

Aquest projecte és una alternativa moderna i de codi obert a l'original `AlbionOnline-StatisticsAnalysis` basat en C#/WPF, centrant-se en la compatibilitat multiplataforma i la facilitat d'ús.

## Característiques

*   **Compatibilitat Multiplataforma:** S'executa de forma nativa a Linux, Windows i macOS.
*   **Rastreig en Temps Real:** Utilitza la llibreria `Scapy` per interceptar paquets UDP als ports d'Albion Online (5055, 5056, 5058).
*   **Estructura del Mesurador de Dany:** Inclou les estructures de dades i la interfície d'usuari necessàries per mostrar estadístiques de combat en viu (Dany Realitzat, Curació Realitzada, DPS).
*   **Interfície d'Usuari Moderna:** Construïda amb Flet, proporcionant una aplicació d'escriptori ràpida i amb aparença nativa.
*   **Gestió de Sessions:** Permet iniciar, aturar, restablir i desar estadístiques de sessió.

## Prerequisits

*   Python 3.8+
*   Llibreries **Flet** i **Scapy**.
*   **Privilegis de Root/Administrador:** Necessaris per a la captura de paquets de xarxa.

## Instal·lació i Configuració

*(Per a instruccions detallades, consulteu la secció d'Instal·lació Manual al README principal.)*

## Com Construir un Executable

L'aplicació es pot empaquetar en un executable independent utilitzant **PyInstaller**.

*(Per a instruccions detallions, consulteu la guia **PACKAGING.md**.)*

## Estructura del Projecte

El projecte està estructurat en components modulars per a una millor mantenibilitat i escalabilitat.

## Estat Actual (Dades en Temps Real)

L'aplicació ara inclou la **Lògica de Descodificació del Protocol Photon**, traduïda del projecte original en C#. Això permet que l'aplicació processi esdeveniments en temps real com `UpdateMoney`, `UpdateFame`, `KilledPlayer` i `Died` directament des del trànsit de xarxa.

## Contribució

Donem la benvinguda a les contribucions de la comunitat!

Si us plau, llegiu les nostres [Guies de Contribució](CONTRIBUTING.md) per obtenir informació detallada sobre com contribuir a aquest projecte.

## Llicència

Aquest projecte té llicència MIT - consulteu el fitxer [LICENSE](LICENSE) per a més detalls.

## Agraïments

*   Projecte original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) per Triky313
*   Construït amb el *framework* [Flet](https://flet.dev/)
*   Anàlisi de xarxa impulsada per [Scapy](https://scapy.net/)

---
*Una solució multiplataforma per a la comunitat d'Albion Online.*
