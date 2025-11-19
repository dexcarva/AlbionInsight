# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>以其他語言閱讀 (Read this in other languages)</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)**

</details>

**Albion Insight** 是一個跨平台（Linux、Windows、macOS）的 **Albion Online** 遊戲統計分析工具，使用 **Python** 和 **Flet** 框架重新實現。它旨在通過分析網絡流量，追蹤實時遊戲內統計數據，包括銀幣、聲望和戰鬥數據（傷害計量器）。

這個項目是原始 C#/WPF **`AlbionOnline-StatisticsAnalysis`** 工具的現代開源替代品，專注於多平台兼容性和易用性。

## 特點 (Features)

*   **跨平台兼容性 (Cross-Platform Compatibility):** 可在 Linux、Windows 和 macOS 上原生運行。
*   **實時追蹤 (Real-Time Tracking):** 使用 `Scapy` 庫嗅探 Albion Online 端口 (5055, 5056, 5058) 上的 UDP 數據包。
*   **傷害計量器結構 (Damage Meter Structure):** 包含必要的數據結構和用戶界面，以顯示實時戰鬥統計數據（造成傷害、治療量、DPS）。
*   **現代用戶界面 (Modern UI):** 使用 Flet 構建，提供快速、原生外觀的桌面應用程序。
*   **會話管理 (Session Management):** 允許開始、停止、重置和保存會話統計數據。

## 先決條件 (Prerequisites)

*   Python 3.8+
*   **Flet** 和 **Scapy** 庫。
*   **Root/管理員權限 (Root/Administrator Privileges):** 網絡數據包捕獲所必需。

## 安裝與設置 (Installation and Setup)

### 選項 1: 快速安裝 (Linux - 推薦)

對於 Linux 用戶，我們提供自動化安裝腳本：

```bash
# 1. 克隆倉庫 (Clone the repository)
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 運行安裝腳本 (Run the installation script)
./install.sh

# 3. 運行應用程序 (Run the application)
./run.sh
```

`install.sh` 腳本將會：
- 安裝系統依賴項 (`libpcap-dev`, `python3-pip`, `python3-venv`)
- 創建一個 Python 虛擬環境
- 安裝所有必需的 Python 包 (Flet, Scapy)

`run.sh` 腳本將自動請求 root 權限並運行應用程序。

### 選項 2: 手動安裝 (Manual Installation)

#### 1. 安裝系統依賴項 (Install System Dependencies)

**在 Linux 上 (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**在 Windows 上:**

從 [python.org](https://www.python.org/downloads/) 安裝 Python 3.8+

#### 2. 安裝 Python 依賴項 (Install Python Dependencies)

**在 Linux 上 (使用虛擬環境 - 推薦):**

```bash
# 創建虛擬環境 (Create virtual environment)
python3 -m venv venv

# 激活虛擬環境 (Activate virtual environment)
source venv/bin/activate

# 安裝依賴項 (Install dependencies)
pip install flet scapy
```

**在 Linux 上 (系統範圍安裝):**

```bash
pip3 install flet scapy --break-system-packages
```

**在 Windows 上:**

```bash
pip install flet scapy
```

#### 3. 運行應用程序 (Running the Application)

由於網絡嗅探需要提升的權限，您必須以 root 或管理員身份運行應用程序。

**在 Linux 上 (使用虛擬環境):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**在 Linux 上 (系統範圍安裝):**

```bash
sudo python3 albion_insight/main.py
```

**在 Windows 上 (以管理員身份運行命令提示符/PowerShell):**

```bash
python albion_insight/main.py
```

應用程序將在原生桌面窗口中打開。

## 如何構建可執行文件 (How to Build an Executable)

應用程序可以使用 **PyInstaller** 打包成獨立的可執行文件。這允許用戶無需安裝 Python 或其依賴項即可運行應用程序。

有關構建 Linux、Windows 和 macOS 可執行文件的詳細說明，請參閱 **[PACKAGING.md](PACKAGING.md)** 指南。

### 快速構建 (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

可執行文件將位於 `dist/` 文件夾中。

## 項目結構 (Project Structure)

為了簡潔起見，整個應用程序包含在一個文件中：

| 文件 | 描述 |
| :--- | :--- |
| `albion_insight/main.py` | 包含所有邏輯（模型、網絡追蹤器、Flet 用戶界面）的主應用程序文件。 |
| `README.md` | 此文檔文件。 |
| `README.pt-BR.md` | 此文檔文件的巴西葡萄牙語版本。 |
| `CONTRIBUTING.md` | 貢獻項目的指南。 |
| `CODE_OF_CONDUCT.md` | 項目的行為準則。 |
| `SECURITY.md` | 報告安全漏洞的政策。 |

## 當前狀態 (實時數據) (Current Status (Real-Time Data))

應用程序現在包含從原始 C# 項目翻譯過來的 **Photon 協議解碼** 邏輯。這使得應用程序能夠直接從網絡流量中處理實時事件，例如 `UpdateMoney`、`UpdateFame`、`KilledPlayer` 和 `Died`。

**注意:** 完整翻譯每一個戰鬥事件（如 `CastHit`、`Attack`）仍在進行中。當前的實現專注於核心統計數據和傷害計量器的結構。傷害計量器的 DPS 計算基於已解碼的事件。

## 貢獻 (Contributing)

我們歡迎社區的貢獻！無論您是開發人員、設計師，還是僅僅是 Albion Online 的愛好者，都有許多方法可以幫助改進 Albion Insight。

請閱讀我們的 [貢獻指南](CONTRIBUTING.md)，了解有關如何為此項目做出貢獻的詳細信息。

### 貢獻者快速入門 (Quick Start for Contributors):

1.  Fork 倉庫: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  克隆您的 Fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  創建一個新分支: `git checkout -b feature/your-feature-name`
4.  進行更改並提交: `git commit -m "Add your feature"`
5.  推送到您的 Fork: `git push origin feature/your-feature-name`
6.  在主倉庫上開啟一個 Pull Request

## 許可證 (License)

該項目根據 MIT 許可證授權 - 有關詳細信息，請參閱 [LICENSE](LICENSE) 文件。

## 致謝 (Acknowledgments)

- 原始項目: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- 使用 [Flet](https://flet.dev/) 框架構建
- 網絡分析由 [Scapy](https://scapy.net/) 提供支持

---
*一個為 Albion Online 社區提供的跨平台解決方案。*
