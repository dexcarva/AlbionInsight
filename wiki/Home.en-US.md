# Albion Insight - Project Overview

**Albion Insight** is an open-source, cross-platform statistics analysis tool, developed in **Python** with the **Flet** framework, dedicated to the **Albion Online** community. Its purpose is to track and display real-time statistics, such as combat data (Damage Meter), silver, and fame gains, by analyzing the game's network traffic.

This project represents an effort to modernize and port the original C# project (`AlbionOnline-StatisticsAnalysis`), overcoming platform limitations and fostering community collaboration.

## 🎯 Core Objectives

1.  **Portability:** Ensure native functionality on Linux, Windows, and macOS.
2.  **Transparency:** Be an open-source and auditable alternative.
3.  **Functionality:** Provide an accurate Damage Meter and a reliable session statistics tracker.
4.  **Modularity:** Maintain a clean and modular code structure to facilitate maintenance and contribution.

## 🗺️ Wiki Map (English)

The project Wiki is your complete guide to understanding, using, and contributing to Albion Insight.

| Section | Description | Status |
| :--- | :--- | :--- |
| **[Usage Guide](Usage-Guide.md)** | Step-by-step instructions on how to install, configure, and use the application. | ✅ Complete |
| **[Installation Guide](Installation-Guide.md)** | Details on prerequisites and installation methods for different operating systems. | ✅ Complete |
| **[Architecture Overview](Architecture-Overview.md)** | Overview of the code structure, modules, and data flow. | ✅ Complete |
| **[Photon Protocol Decoding](Photon-Protocol-Decoding.md)** | Technical explanation of how Albion Online's traffic is decoded. | ✅ Complete |
| **[Frequently Asked Questions (FAQ)](FAQ.md)** | Answers to the community's most common questions. | ✅ Complete |
| **[Contribution Guide](Contribution-Guide.md)** | How to set up the development environment, code standards, and the Pull Request process. | ✅ Complete |
| **[Troubleshooting](Troubleshooting.pt-BR.md)** | Solutions for common errors and configuration issues. | ✅ Complete |
| **[Roadmap](Roadmap.md)** | Planned features and the future of the project. | ✅ Complete |

## 🤝 Community and Open Source

Albion Insight thrives on community collaboration. As an open-source project, it ensures **transparency** in data processing and allows anyone to audit the code, guaranteeing the tool's security and integrity. We actively encourage contributions, whether through bug reports, feature suggestions, or code. Your involvement is fundamental to the project's success and longevity.

## 🛠️ Technical Details

Albion Insight is built upon the following technologies:

*   **Language:** Python 3.8+
*   **Graphical Interface:** [Flet](https://flet.dev/) (for a native, cross-platform UI)
*   **Network Analysis:** [Scapy](https://scapy.net/) (for packet capture and manipulation)
*   **Protocol:** Implementation of the **Photon** protocol decoding for Albion Online.

---
*Last updated: 22 November 2025*
