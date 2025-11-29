# Albion Insight - Project Overview

<details>
<summary>Read this in other languages</summary>

**[Portuguese (Brazil)](Home.pt-BR.md)** | **[English](Home.md)** | **[Ukrainian](Home.uk-UA.md)**

</details>

**Albion Insight** is a cross-platform (Linux, Windows, macOS) open-source statistics analysis tool, developed in **Python** with the **Flet** framework, dedicated to the **Albion Online** game community. Its purpose is to track and display real-time statistics, such as combat data (Damage Meter), silver and fame gains, by analyzing the game's network traffic.

This project represents a modernization and portability effort of the original C# project (`AlbionOnline-StatisticsAnalysis`), overcoming platform limitations and promoting community collaboration.

## 🎯 Key Objectives

1.  **Portability:** Ensure native operation on Linux, Windows, and macOS.
2.  **Transparency:** Be an open-source and auditable alternative.
3.  **Functionality:** Provide an accurate Damage Meter and a reliable session statistics tracker.
4.  **Modularity:** Maintain a clean and modular code structure to facilitate maintenance and contribution.

## 🗺️ Wiki Map

The project Wiki is your complete guide to understanding, using, and contributing to Albion Insight.

| Seção | Descrição | Status |
| :--- | :--- | :--- |
| **[Usage Guide](Usage-Guide.md)** | Step-by-step instructions on how to install, configure, and use the application. | ✅ Complete |
| **[Installation Guide](Installation-Guide.md)** | Details on prerequisites and installation methods for different operating systems. | ✅ Complete |
| **[Architecture Overview](Architecture-Overview.md)** | Overview of the code structure, modules, and data flow. | ✅ Complete |
| **[Photon Protocol Decoding](Photon-Protocol-Decoding.md)** | Technical explanation of how Albion Online traffic is decoded. | ✅ Complete |
| **[Frequently Asked Questions (FAQ)](FAQ.md)** | Answers to the most common community questions. | ✅ Complete |
| **[Contribution Guide](Contribution-Guide.md)** | How to set up the development environment, code standards, and Pull Request process. | ✅ Complete |
| **[Troubleshooting](Troubleshooting.md)** | Solutions for common errors and configuration issues. | ✅ Complete |
| **[Roadmap](Roadmap.md)** | Planned features and the future of the project. | ✅ Complete |

## 💖 Open Source Philosophy and Community

**Albion Insight** was born from the belief that the best tools are those built by the community that uses them. We believe in the power of collaboration to create transparent, secure solutions that meet the real needs of Albion Online players.

Our philosophy is based on three pillars:

1.  **Total Transparency:** All source code is open and auditable. We want you to know exactly how your data is processed, with no black boxes or surprises.
2.  **Security First:** Unlike closed-source tools, the open nature of Albion Insight allows the community to review and validate the code's security, ensuring it does not perform malicious actions or violate the game's terms of service.
3.  **Built for the Community, by the Community:** The project evolves based on user feedback and contributions. Every suggestion, bug report, or pull request is valued and contributes to the future of the tool.

By using and contributing to Albion Insight, you are not just getting a tool, but becoming part of a movement for a more open and secure tool ecosystem for the Albion Online community.

## 🤝 How to Contribute

Albion Insight thrives on community collaboration. As an open-source project, it ensures **transparency** in data processing and allows anyone to audit the code, guaranteeing the tool's security and integrity. We actively encourage contributions, whether through bug reports, feature suggestions, or code. Your involvement is fundamental to the project's success and longevity.

## 🌟 Best Contribution Practices

To ensure the quality and consistency of the project, we ask contributors to follow these guidelines:

*   **Communicate:** Use [Issues](https://github.com/dexcarva/AlbionInsight/issues) to discuss major changes before starting to code.
*   **Code Standards:** Follow the Python code style defined by `black` and `isort`.
*   **Tests:** Include unit tests for new features or bug fixes.
*   **Commits:** Use clear commit messages without unnecessary line breaks, following the **Conventional Commits** standard (e.g., `feat: Add new feature` or `fix: Fix import error`).

## 🛠️ Technical Details

Albion Insight is built on the following technologies:

*   **Language:** Python 3.8+
*   **Graphical Interface:** [Flet](https://flet.dev/) (for a native and cross-platform UI)
*   **Network Analysis:** [Scapy](https://scapy.net/) (for packet capture and manipulation)
*   **Protocol:** Implementation of **Photon** protocol decoding for Albion Online.

---
*Last updated: November 28, 2025*
