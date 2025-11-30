# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in German (Lesen Sie dies auf Deutsch)](README.de-DE.md)**
**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**
**[Read this in Spanish (Leer en Español)](README.es-ES.md)**
**[Read this in French (Lire en Français)](README.fr-FR.md)**
**[Read this in Italian (Leggi in Italiano)](README.it-IT.md)**
**[Read this in Simplified Chinese (阅读简体中文)](README.zh-CN.md)**
**[Read this in Traditional Chinese (閱讀繁體中文)](README.zh-TW.md)**
**[Read this in Russian (Прочитать на русском)](README.ru-RU.md)**
**[Read this in Japanese (日本語で読む)](README.ja-JP.md)**
**[Read this in Arabic (اقرأ هذا بالعربية)](README.ar-SA.md)**
**[Read this in Turkish (Türkçe Oku)](README.tr-TR.md)**
**[Read this in Korean (한국어로 읽기)](README.ko-KR.md)**
**[Read this in Dutch (Lees dit in het Nederlands)](README.nl-NL.md)**
**[Read this in Polish (Czytaj po polsku)](README.pl-PL.md)**
**[Read this in Hindi (इसे हिंदी में पढ़ें)](README.hi-IN.md)**
**[Read this in Swedish (Läs detta på svenska)](README.sv-SE.md)**
**[Read this in Vietnamese (Đọc bằng tiếng Việt)](README.vi-VN.md)**
**[Read this in Greek (Διαβάστε στα Ελληνικά)](README.el-GR.md)**

**Albion Insight** 是一個跨平台（Linux、Windows、macOS）的遊戲《阿爾比恩：王者榮耀》（Albion Online）統計分析工具，使用 **Python** 和 **Flet** 框架重新實現。它旨在通過分析網絡流量，實時追蹤遊戲內的統計數據，包括銀幣、聲望和戰鬥數據（傷害計數器）。

這個項目是原始 C#/WPF 版本 `AlbionOnline-StatisticsAnalysis` 工具的一個現代、開源替代品，專注於多平台兼容性和易用性。

## 特點 (Features)

*   **跨平台兼容性：** 可在 Linux、Windows 和 macOS 上原生運行。
*   **實時追蹤：** 使用 `Scapy` 庫嗅探《阿爾比恩：王者榮耀》端口（5055、5056、5058）上的 UDP 數據包。
*   **傷害計數器結構：** 包含必要的數據結構和用戶界面，以顯示實時戰鬥統計數據（造成傷害、治療量、DPS）。
*   **現代用戶界面：** 使用 Flet 構建，提供快速、外觀原生的桌面應用程序。
*   **會話管理：** 允許開始、停止、重置和保存會話統計數據。

## 先決條件 (Prerequisites)

*   Python 3.8+
*   **Flet** 和 **Scapy** 庫。
*   **Root/管理員權限：** 網絡數據包捕獲所必需。

## 安裝與設置 (Installation and Setup)

### 選項 1：快速安裝（Linux - 推薦）

對於 Linux 用戶，我們提供了自動化安裝腳本：

```bash
# 1. 克隆倉庫
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 運行安裝腳本
./install.sh

# 3. 運行應用程序
./run.sh
```

`install.sh` 腳本將會：
- 安裝系統依賴項（`libpcap-dev`、`python3-pip`、`python3-venv`）
- 創建一個 Python 虛擬環境
- 安裝所有必需的 Python 包（Flet、Scapy）

`run.sh` 腳本將自動請求 Root 權限並運行應用程序。

### 選項 2：手動安裝 (Manual Installation)

#### 1. 安裝系統依賴項 (Install System Dependencies)

**在 Linux (Debian/Ubuntu) 上：**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**在 Windows 上：**

從 [python.org](https://www.python.org/downloads/) 安裝 Python 3.8+

#### 2. 安裝 Python 依賴項 (Install Python Dependencies)

**在 Linux 上（使用虛擬環境 - 推薦）：**

```bash
# 創建虛擬環境
python3 -m venv venv

# 激活虛擬環境
source venv/bin/activate

# 安裝依賴項
pip install flet scapy
```

**在 Linux 上（系統範圍安裝）：**

```bash
pip3 install flet scapy --break-system-packages
```

**在 Windows 上：**

```bash
pip install flet scapy
```

#### 3. 運行應用程序 (Running the Application)

由於網絡嗅探需要提升的權限，您必須以 Root 或管理員身份運行應用程序。

**在 Linux 上（使用虛擬環境）：**

```bash
sudo venv/bin/python3 -m albion_insight
```

**在 Linux 上（系統範圍安裝）：**

```bash
sudo python3 -m albion_insight
```

**在 Windows 上（以管理員身份運行命令提示符/PowerShell）：**

```bash
python -m albion_insight
```

應用程序將在原生桌面窗口中打開。

## 如何構建可執行文件 (How to Build an Executable)

應用程序可以使用 **PyInstaller** 打包成獨立的可執行文件。這允許用戶無需安裝 Python 或其依賴項即可運行應用程序。

有關構建 Linux、Windows 和 macOS 可執行文件的詳細說明，請參閱 **[PACKAGING.md](PACKAGING.md)** 指南。

### 快速構建（Linux）

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
```

可執行文件將位於 `dist/` 文件夾中。

## 項目結構 (Project Structure)

整個應用程序包含在一個單一文件中，以簡化：

| 文件 | 描述 |
| :--- | :--- |
| `-m albion_insight` | 包含所有邏輯（模型、網絡追蹤器、Flet 用戶界面）的主應用程序文件。 |
| `README.md` | 此文檔文件。 |
| `README.zh-TW.md` | 此文檔文件的繁體中文版本。 |
| `CONTRIBUTING.md` | 貢獻本項目的指南。 |
| `CODE_OF_CONDUCT.md` | 項目的行為準則。 |
| `SECURITY.md` | 報告安全漏洞的政策。 |

## 當前狀態（實時數據）(Current Status (Real-Time Data))

應用程序現在包含了從原始 C# 項目翻譯過來的 **Photon 協議解碼**邏輯。這使得應用程序能夠直接從網絡流量中處理實時事件，例如 `UpdateMoney`、`UpdateFame`、`KilledPlayer` 和 `Died`。

**注意：** 完整翻譯每一個戰鬥事件（如 `CastHit`、`Attack`）是一項持續進行的工作。當前的實現專注於核心統計數據和傷害計數器的結構。傷害計數器的 DPS 計算基於已解碼的事件。

## 貢獻 (Contributing)

我們歡迎社區的貢獻！無論您是開發人員、設計師，還是僅僅是《阿爾比恩：王者榮耀》的愛好者，都有許多方法可以幫助改進 Albion Insight。

請閱讀我們的 [貢獻指南](CONTRIBUTING.md)，以獲取有關如何為此項目貢獻的詳細信息。

### 貢獻者快速入門：

1.  Fork 倉庫：[github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  克隆您的 Fork：`git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  創建一個新分支：`git checkout -b feature/your-feature-name`
4.  進行更改並提交：`git commit -m "Add your feature"`
5.  推送到您的 Fork：`git push origin feature/your-feature-name`
6.  在主倉庫上開啟一個 Pull Request

## 許可證 (License)

本項目採用 MIT 許可證授權 - 有關詳細信息，請參閱 [LICENSE](LICENSE) 文件。

## 致謝 (Acknowledgments)

- 原始項目：[AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- 使用 [Flet](https://flet.dev/) 框架構建
- 網絡分析由 [Scapy](https://scapy.net/) 提供支持

---
*為《阿爾比恩：王者榮耀》社區提供的跨平台解決方案。*
