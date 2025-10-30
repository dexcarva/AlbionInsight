# Packaging Albion Insight as a Standalone Executable

This guide explains how to create a standalone executable for **Albion Insight** using **PyInstaller**. This allows users to run the application without installing Python or its dependencies.

## Prerequisites

*   Python 3.8+ installed
*   Virtual environment with all dependencies installed (run `./install.sh` first)

## Installation

First, install PyInstaller in your virtual environment:

```bash
source venv/bin/activate
pip install pyinstaller
```

## Building the Executable

### Linux

```bash
source venv/bin/activate
pyinstaller --name "AlbionInsight" \
            --onefile \
            --windowed \
            --add-data "README.md:." \
            --add-data "README.pt-BR.md:." \
            --hidden-import scapy.layers.all \
            --hidden-import scapy.layers.inet \
            albion_insight.py
```

The executable will be located in `dist/AlbionInsight`.

**Note:** On Linux, the executable still requires root privileges to capture network packets:

```bash
sudo ./dist/AlbionInsight
```

### Windows

```bash
venv\Scripts\activate
pyinstaller --name "AlbionInsight" ^
            --onefile ^
            --windowed ^
            --add-data "README.md;." ^
            --add-data "README.pt-BR.md;." ^
            --hidden-import scapy.layers.all ^
            --hidden-import scapy.layers.inet ^
            albion_insight.py
```

The executable will be located in `dist\AlbionInsight.exe`.

**Note:** On Windows, you must run the executable as Administrator (right-click → Run as Administrator).

### macOS

```bash
source venv/bin/activate
pyinstaller --name "AlbionInsight" \
            --onefile \
            --windowed \
            --add-data "README.md:." \
            --add-data "README.pt-BR.md:." \
            --hidden-import scapy.layers.all \
            --hidden-import scapy.layers.inet \
            albion_insight.py
```

The executable will be located in `dist/AlbionInsight`.

## PyInstaller Options Explained

*   `--name "AlbionInsight"`: Sets the name of the executable file.
*   `--onefile`: Creates a single executable file (easier distribution).
*   `--windowed`: Hides the console window (for desktop apps).
*   `--add-data`: Includes additional files (like README) in the executable.
*   `--hidden-import`: Explicitly includes modules that PyInstaller might miss (Scapy layers).

## Troubleshooting

### "Module not found" errors

If you encounter errors about missing modules, add them with `--hidden-import`:

```bash
--hidden-import module_name
```

### Large executable size

The executable will be around 50-100 MB due to Flet and Scapy dependencies. This is normal for Python applications packaged with PyInstaller.

### Antivirus false positives

Some antivirus software may flag the executable as suspicious. This is a known issue with PyInstaller. You can:

1.  Add an exception in your antivirus software.
2.  Sign the executable with a code signing certificate (for production releases).

## Distribution

After building, you can distribute the executable from the `dist/` folder. Users will not need to install Python or any dependencies.

**Important:** Always include a README file explaining:

*   The application requires root/administrator privileges.
*   How to run the application (e.g., `sudo ./AlbionInsight` on Linux).
*   Any system-specific requirements (e.g., `libpcap` on Linux).

## Creating a Release

To create a GitHub release with the executable:

```bash
# 1. Build the executable
./build.sh  # Or follow the steps above

# 2. Create a release on GitHub
gh release create v0.0.2-beta \
    --title "Beta Release 0.0.2 - Standalone Executable" \
    --notes "Includes standalone executable for Linux/Windows/macOS" \
    dist/AlbionInsight  # Attach the executable
```

---

For more information, see the [PyInstaller documentation](https://pyinstaller.org/en/stable/).

