# Albion Insight (Filipino)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** ay isang cross-platform (Linux, Windows, macOS) na tool sa pagsusuri ng istatistika para sa larong Albion Online, na muling ipinatupad sa **Python** gamit ang **Flet** framework. Ito ay dinisenyo upang subaybayan ang real-time na in-game statistics, kabilang ang silver, fame, at combat data (Damage Meter), sa pamamagitan ng pagsusuri ng network traffic.

Ang proyektong ito ay isang moderno, open-source na alternatibo sa orihinal na C#/WPF-based na `AlbionOnline-StatisticsAnalysis` tool, na nakatuon sa multi-platform compatibility at kadalian ng paggamit.

## Mga Tampok (Features)

*   **Cross-Platform Compatibility:** Tumatakbo nang native sa Linux, Windows, at macOS.
*   **Real-Time Tracking:** Gumagamit ng `Scapy` library upang suminghot ng UDP packets sa Albion Online ports (5055, 5056, 5058).
*   **Damage Meter Structure:** Kasama ang kinakailangang data structures at UI upang ipakita ang live combat statistics (Damage Done, Healing Done, DPS).
*   **Modern UI:** Binuo gamit ang Flet, nagbibigay ng mabilis, native-looking desktop application.
*   **Session Management:** Pinapayagan ang pagsisimula, paghinto, pag-reset, at pag-save ng session statistics.

## Mga Kinakailangan (Prerequisites)

*   Python 3.8+
*   **Flet** at **Scapy** libraries.
*   **Root/Administrator Privileges:** Kinakailangan para sa network packet capture.

## Pag-install at Setup (Installation and Setup)

Para sa detalyadong gabay sa pag-install, mangyaring tingnan ang pangunahing [README.md](README.md).

## Istruktura ng Proyekto (Project Structure)

Ang application ay naka-istruktura sa modular components para sa mas mahusay na maintainability at scalability.

## Kasalukuyang Katayuan (Current Status)

Ang application ngayon ay may kasamang **Photon Protocol Decoding** logic, na isinalin mula sa orihinal na C# project.

## Pag-ambag (Contributing)

Malugod naming tinatanggap ang mga kontribusyon mula sa komunidad! Mangyaring basahin ang aming [Contributing Guidelines](CONTRIBUTING.md) para sa detalyadong impormasyon.

## Lisensya (License)

Ang proyektong ito ay lisensyado sa ilalim ng MIT License - tingnan ang [LICENSE](LICENSE) file para sa mga detalye.

## Pagkilala (Acknowledgments)

*   Orihinal na proyekto: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) ni Triky313
*   Binuo gamit ang [Flet](https://flet.dev/) framework
*   Network analysis na pinapagana ng [Scapy](https://scapy.net/)

---
*Isang cross-platform na solusyon para sa komunidad ng Albion Online.*
