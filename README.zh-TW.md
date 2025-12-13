# Albion Insight (繁體中文)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** 是一個跨平台（Linux、Windows、macOS）的 **Albion Online** 遊戲統計分析工具，使用 **Python** 和 **Flet** 框架重新實現。它旨在透過分析網路流量，追蹤即時的遊戲內統計數據，包括銀幣、聲望和戰鬥數據（傷害計數器）。

這個專案是原始基於 C#/WPF 的 `AlbionOnline-StatisticsAnalysis` 工具的現代、開源替代品，專注於多平台相容性和易用性。

## 功能特色

*   **跨平台相容性：** 可在 Linux、Windows 和 macOS 上原生運行。
*   **即時追蹤：** 使用 `Scapy` 函式庫嗅探 Albion Online 埠（5055, 5056, 5058）上的 UDP 封包。
*   **傷害計數器結構：** 包含必要的資料結構和使用者介面，以顯示即時戰鬥統計數據（造成傷害、治療量、DPS）。
*   **現代使用者介面：** 使用 Flet 構建，提供快速、外觀原生的桌面應用程式。
*   **會話管理：** 允許開始、停止、重置和儲存會話統計數據。

## 先決條件

*   Python 3.8+
*   **Flet** 和 **Scapy** 函式庫。
*   **Root/管理員權限：** 網路封包捕獲所必需。

## 安裝與設定

### 選項 1：快速安裝（Linux - 推薦）

對於 Linux 用戶，我們提供了自動化安裝腳本：

\`\`\`bash
# 1. 克隆儲存庫
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 運行安裝腳本
./install.sh

# 3. 運行應用程式
./run.sh
\`\`\`

`install.sh` 腳本將會：
- 安裝系統依賴項（`libpcap-dev`、`python3-pip`、`python3-venv`）
- 建立 Python 虛擬環境
- 安裝所有必需的 Python 套件（Flet、Scapy）

`run.sh` 腳本將自動請求 Root 權限並運行應用程式。

### 選項 2：手動安裝

#### 1. 安裝系統依賴項

**在 Linux (Debian/Ubuntu) 上：**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**在 Windows 上：**

從 [python.org](https://www.python.org/downloads/) 安裝 Python 3.8+

#### 2. 安裝 Python 依賴項

**在 Linux (使用虛擬環境 - 推薦) 上：**

\`\`\`bash
# 建立虛擬環境
python3 -m venv venv

# 啟用虛擬環境
source venv/bin/activate

# 安裝依賴項
pip install flet scapy
\`\`\`

**在 Linux (系統範圍安裝) 上：**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**在 Windows 上：**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. 運行應用程式

由於網路嗅探需要提升的權限，您必須以 Root 或管理員身份運行應用程式。

**在 Linux (使用虛擬環境) 上：**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**在 Linux (系統範圍安裝) 上：**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**在 Windows (以管理員身份運行命令提示字元/PowerShell) 上：**

\`\`\`bash
python -m albion_insight
\`\`\`

應用程式將在原生桌面視窗中開啟。

## 如何建立可執行檔

應用程式可以使用 **PyInstaller** 打包成獨立的可執行檔。這允許用戶無需安裝 Python 或其依賴項即可運行應用程式。

有關為 Linux、Windows 和 macOS 建立可執行檔的詳細說明，請參閱 **[PACKAGING.md](PACKAGING.md)** 指南。

### 快速建立（Linux）

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

可執行檔將位於 `dist/` 資料夾中。

## 專案結構

應用程式被結構化為模組化組件，以實現更好的可維護性和可擴展性：

| 檔案 | 描述 |
| :--- | :--- |
| `albion_insight/core/` | 核心邏輯、網路追蹤、資料模型和協定解碼。 |
| `albion_insight/ui/` | 使用 Flet 構建的使用者介面組件。 |
| `albion_insight/utils/` | 實用函式、配置和日誌記錄。 |
| `albion_insight/__main__.py` | 應用程式的入口點。 |
| `README.md` | 此文件。 |
| `CONTRIBUTING.md` | 貢獻專案的指南。 |
| `CODE_OF_CONDUCT.md` | 專案的行為準則。 |
| `SECURITY.md` | 報告安全漏洞的政策。 |
| `README.it-IT.md` | Documentazione in italiano (義大利語文件). |
| `README.pt-BR.md` | Documentação em português do Brasil (巴西葡萄牙語文件). |
| `README.ru-RU.md` | Документация на русском языке (俄語文件). |
| `README.fr-FR.md` | Documentation en français (法語文件). |
| `README.zh-CN.md` | 简体中文文档 (簡體中文文件). |
| `README.ko-KR.md` | 한국어 문서 (韓語文件). |
| `README.es-ES.md` | Documentación en español (西班牙語文件). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (德語文件). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (波蘭語文件). |
| `README.sv-SE.md` | Dokumentation på svenska (瑞典語文件). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (越南語文件). |
| `README.ar-SA.md` | توثيق باللغة العربية (阿拉伯語文件). |
| `README.pt-PT.md` | Documentação em português europeu (歐洲葡萄牙語文件). |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (印地語文件). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (匈牙利語文件). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (泰語文件). |
| `README.ja-JP.md` | 日本語のドキュメント (日語文件). |
| `README.tr-TR.md` | Türkçe dokümantasyon (土耳其語文件). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia (印尼語文件). |
| `README.sk-SK.md` | Dokumentácia v slovenčine (斯洛伐克語文件). |
| `README.cs-CZ.md` | Dokumentace v češtině (捷克語文件). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (芬蘭語文件). |
| `README.nl-NL.md` | Documentatie in het Nederlands (荷蘭語文件). |
| `README.zh-TW.md` | 繁體中文文件 (Traditional Chinese documentation). |

## 當前狀態（即時數據）

應用程式現在包含了從原始 C# 專案翻譯過來的 **Photon 協定解碼**邏輯。這使得應用程式能夠直接從網路流量處理即時事件，例如 `UpdateMoney`、`UpdateFame`、`KilledPlayer` 和 `Died`。

**注意：** 每個單一戰鬥事件（如 `CastHit`、`Attack`）的完整翻譯仍在進行中。目前的實現專注於核心統計數據和傷害計數器的結構。傷害計數器的 DPS 計算基於已解碼的事件。

## 貢獻

我們歡迎社區的貢獻！無論您是開發人員、設計師，還是僅僅是 Albion Online 的愛好者，都有許多方法可以幫助改進 Albion Insight。

請閱讀我們的 [貢獻指南](CONTRIBUTING.md)，以獲取有關如何為此專案做出貢獻的詳細資訊。

### 貢獻者快速入門：

1.  Fork 儲存庫：[github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  克隆您的 Fork：`git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  建立一個新分支：`git checkout -b feature/your-feature-name`
4.  進行更改並提交：`git commit -m "Add your feature"`
5.  推送到您的 Fork：`git push origin feature/your-feature-name`
6.  在主儲存庫上開啟一個 Pull Request

## 許可證

本專案根據 MIT 許可證授權 - 有關詳細資訊，請參閱 [LICENSE](LICENSE) 檔案。

## 致謝

- 原始專案：Triky313 的 [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- 使用 [Flet](https://flet.dev/) 框架構建
- 網路分析由 [Scapy](https://scapy.net/) 提供支援

---
*為 Albion Online 社區提供的跨平台解決方案。*
