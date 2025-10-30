# Albion Insight

**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**

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
sudo venv/bin/python3 albion_insight.py
```

**On Linux (system-wide installation):**

```bash
sudo python3 albion_insight.py
```

**On Windows (Run Command Prompt/PowerShell as Administrator):**

```bash
python albion_insight.py
```

The application will open in a native desktop window.

## How to Build an Executable

The application can be packaged into a standalone executable using **PyInstaller**. This allows users to run the application without installing Python or its dependencies.

For detailed instructions on building executables for Linux, Windows, and macOS, see the **[PACKAGING.md](PACKAGING.md)** guide.

### Quick Build (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```

The executable will be located in the `dist/` folder.

## Project Structure

The entire application is contained within a single file for simplicity:

| File | Description |
| :--- | :--- |
| `albion_insight.py` | The main application file containing all logic (Models, Network Tracker, Flet UI). |
| `README.md` | This documentation file. |

## Current Status (Real-Time Data)

The application now includes the **Photon Protocol Decoding** logic, translated from the original C# project. This allows the application to process real-time events like `UpdateMoney`, `UpdateFame`, `KilledPlayer`, and `Died` directly from the network traffic.

**Note:** The full translation of every single combat event (like `CastHit`, `Attack`) is an ongoing effort. The current implementation focuses on the core statistics and the structure for the Damage Meter. The Damage Meter's DPS calculation is based on the decoded events.

## Contributing

We welcome contributions from the community! Whether you're a developer, designer, or just an Albion Online enthusiast, there are many ways to help improve Albion Insight.

### How You Can Contribute:

*   **Report Bugs:** Found a bug? Open an issue on our [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues) page with detailed steps to reproduce it.
*   **Suggest Features:** Have an idea for a new feature? Share it in the Issues section with the "enhancement" label.
*   **Improve Documentation:** Help us improve the README, add tutorials, or translate the documentation to other languages.
*   **Code Contributions:** Fork the repository, make your changes, and submit a Pull Request. Make sure to follow the coding style and include tests if applicable.
*   **Test on Different Platforms:** Help us test the application on various Linux distributions, Windows versions, and macOS to ensure compatibility.
*   **Decode More Events:** The Photon Protocol has hundreds of event types. Help us translate more event handlers from the original C# code to Python.

### Getting Started:

1.  Fork the repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone your fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Create a new branch: `git checkout -b feature/your-feature-name`
4.  Make your changes and commit: `git commit -m "Add your feature"`
5.  Push to your fork: `git push origin feature/your-feature-name`
6.  Open a Pull Request on the main repository

---
*A cross-platform solution for the Albion Online community.*

