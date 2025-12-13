# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** je multiplatformový (Linux, Windows, macOS) nástroj na analýzu štatistík pre hru Albion Online, reimplementovaný v **Python** s použitím frameworku **Flet**. Je navrhnutý na sledovanie štatistík v hre v reálnom čase, vrátane striebra, slávy a bojových údajov (Damage Meter), prostredníctvom analýzy sieťovej prevádzky.

Tento projekt je moderná, open-source alternatíva k pôvodnému nástroju `AlbionOnline-StatisticsAnalysis` založenému na C#/WPF, so zameraním na kompatibilitu s viacerými platformami a jednoduché použitie.

## Funkcie (Features)

*   **Multiplatformová Kompatibilita:** Beží natívne na Linuxe, Windowse a macOS.
*   **Sledovanie v Reálnom Čase:** Používa knižnicu `Scapy` na odpočúvanie UDP paketov na portoch Albion Online (5055, 5056, 5058).
*   **Štruktúra Merača Poškodenia (Damage Meter):** Zahŕňa potrebné dátové štruktúry a UI na zobrazenie živých bojových štatistík (Udelené Poškodenie, Udelené Liečenie, DPS).
*   **Moderné UI:** Postavené s Flet, poskytujúce rýchlu, natívne vyzerajúcu desktopovú aplikáciu.
*   **Správa Relácií:** Umožňuje spustenie, zastavenie, resetovanie a ukladanie štatistík relácie.

## Predpoklady (Prerequisites)

*   Python 3.8+
*   Knižnice **Flet** a **Scapy**.
*   **Root/Administrátorské Práva:** Nevyhnutné pre zachytávanie sieťových paketov.

## Inštalácia a Nastavenie (Installation and Setup)

Podrobné pokyny nájdete v anglickom [README.md](README.md).

## Prispievanie (Contributing)

Vítame príspevky od komunity! Prečítajte si naše [Pokyny pre Prispievanie](CONTRIBUTING.md) pre podrobné informácie o tom, ako prispieť k tomuto projektu.

## Licencia (License)

Tento projekt je licencovaný pod licenciou MIT - podrobnosti nájdete v súbore [LICENSE](LICENSE).

## Poďakovanie (Acknowledgments)

- Pôvodný projekt: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) od Triky313
- Postavené s frameworkom [Flet](https://flet.dev/)
- Analýza siete poháňaná [Scapy](https://scapy.net/)

---
*Multiplatformové riešenie pre komunitu Albion Online.*
