# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in German (Lesen Sie dies auf Deutsch)](README.de-DE.md)**\n**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**
**[Read this in Spanish (Leer en Español)](README.es-ES.md)**
**[Read this in French (Lire en Français)](README.fr-FR.md)**
**[Read this in Italian (Leggi in Italiano)](README.it-IT.md)**\n**[Read this in Simplified Chinese (阅读简体中文)](README.zh-CN.md)**\n**[Read this in Russian (Прочитать на русском)](README.ru-RU.md)**\n**[Read this in Japanese (日本語で読む)](README.ja-JP.md)**\n**[Read this in Arabic (اقرأ هذا بالعربية)](README.ar-SA.md)**\n**[Read this in Turkish (Türkçe Oku)](README.tr-TR.md)**\n**[Read this in Korean (한국어로 읽기)](README.ko-KR.md)**\n**[Read this in Dutch (Lees dit in het Nederlands)](README.nl-NL.md)**\n**[Read this in Polish (Czytaj po polsku)](README.pl-PL.md)****[Read this in Hindi (इसे हिंदी में पढ़ें)](README.hi-IN.md)**
**[Read this in Swedish (Läs detta på svenska)](README.sv-SE.md)**\n**[Read this in Vietnamese (Đọc bằng tiếng Việt)](README.vi-VN.md)**

**Albion Insight** is a cross-platform (Linux, Windows, macOS) statistics analysis tool for the game Albion Online, re-implemented in **Python** using the **Flet** framework. It is designed to track real-time in-game statistics, including silver, fame, and combat data (Damage Meter), by analyzing network traffic.

This project is a modern, open-source alternative to the original C#/WPF-based `AlbionOnline-StatisticsAnalysis` tool, focusing on multi-platform compatibility and ease of use.

## Features

*   **Cross-Platform Compatibility:** Runs natively on Linux, Windows, and macOS.
*   **Real-Time Tracking:** Uses the `Scapy` library to sniff UDP packets on Albion Online ports (5055, 5056, 5058).
*   **Damage Meter Structure:** Includes the necessary data structures and UI to display live combat statistics (Damage Done, Healing Done, DPS).
*   **Modern UI:** Built with Flet, providing a fast, native-looking desktop application.
*   **Session Management:** Allows starting, stopping, resetting, and saving session statistics.

## Prerequisites

*   Python 3.8+
*   **Flet** and **Scapy** libraries.
*   **Root/Administrator Privileges:** Necessary for network packet capture.

## Installation and Setup

### Option 1: Quick Install (Linux - Recommended)

For Linux users, we provide automated installation scripts:

```bash
# 1. Clone the repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Run the installation script
./install.sh

# 3. Run the application
./run.sh
```

The `install.sh` script will:
- Install system dependencies (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Create a Python virtual environment
- Install all required Python packages (Flet, Scapy)

The `run.sh` script will automatically request root privileges and run the application.

### Option 2: Manual Installation

#### 1. Install System Dependencies

**On Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**On Windows:**

Install Python 3.8+ from [python.org](https://www.python.org/downloads/)

#### 2. Install Python Dependencies

**On Linux (using virtual environment - recommended):**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install flet scapy
```

**On Linux (system-wide installation):**

```bash
pip3 install flet scapy --break-system-packages
```

**On Windows:**

```bash
pip install flet scapy
```

#### 3. Running the Application

Since network sniffing requires elevated privileges, you must run the application as root or administrator.

**On Linux (with virtual environment):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**On Linux (system-wide installation):**

```bash
sudo python3 albion_insight/main.py
```

**On Windows (Run Command Prompt/PowerShell as Administrator):**

```bash
python albion_insight/main.py
```

The application will open in a native desktop window.

## How to Build an Executable

The application can be packaged into a standalone executable using **PyInstaller**. This allows users to run the application without installing Python or its dependencies.

For detailed instructions on building executables for Linux, Windows, and macOS, see the **[PACKAGING.md](PACKAGING.md)** guide.

### Quick Build (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

The executable will be located in the `dist/` folder.

## Project Structure

The entire application is contained within a single file for simplicity:

| File | Description |
| :--- | :--- |
| `albion_insight/main.py` | The main application file containing all logic (Models, Network Tracker, Flet UI). |
|| `README.md` | This documentation file. |
| `README.pt-BR.md` | This documentation file in Brazilian Portuguese. |
| `CONTRIBUTING.md` | Guidelines for contributing to the project. |
| `CODE_OF_CONDUCT.md` | The project's Code of Conduct. |
| `SECURITY.md` | Policy for reporting security vulnerabilities. |

## Current Status (Real-Time Data)

The application now includes the **Photon Protocol Decoding** logic, translated from the original C# project. This allows the application to process real-time events like `UpdateMoney`, `UpdateFame`, `KilledPlayer`, and `Died` directly from the network traffic.

**Note:** The full translation of every single combat event (like `CastHit`, `Attack`) is an ongoing effort. The current implementation focuses on the core statistics and the structure for the Damage Meter. The Damage Meter's DPS calculation is based on the decoded events.

## Contributing

We welcome contributions from the community! Whether you're a developer, designer, or just an Albion Online enthusiast, there are many ways to help improve Albion Insight.

Please read our [Contributing Guidelines](CONTRIBUTING.md) for detailed information on how to contribute to this project.

### Quick Start for Contributors:

1.  Fork the repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone your fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Create a new branch: `git checkout -b feature/your-feature-name`
4.  Make your changes and commit: `git commit -m "Add your feature"`
5.  Push to your fork: `git push origin feature/your-feature-name`
6.  Open a Pull Request on the main repository

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original project: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- Built with [Flet](https://flet.dev/) framework
- Network analysis powered by [Scapy](https://scapy.net/)

---
*A cross-platform solution for the Albion Online community.*

