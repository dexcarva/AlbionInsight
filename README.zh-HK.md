[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** 是一個跨平台（Linux、Windows、macOS）的統計分析工具，專為遊戲 Albion Online 設計，並使用 **Flet** 框架以 **Python** 重新實現。它旨在通過分析網絡流量，實時追蹤遊戲內的統計數據，包括銀幣、聲望和戰鬥數據（傷害計數器 Damage Meter）。

此項目是原始 C#/WPF 架構的 `AlbionOnline-StatisticsAnalysis` 工具的現代、開源替代品，專注於多平台兼容性和易用性。

## 功能特色

*   **跨平台兼容性：** 可在 Linux、Windows 和 macOS 上原生運行。
*   **實時追蹤：** 使用 `Scapy` 庫來嗅探 Albion Online 端口（5055, 5056, 5058）上的 UDP 數據包。
*   **傷害計數器結構：** 包含必要數據結構和用戶界面，以顯示實時戰鬥統計數據（造成傷害、治療量、DPS）。
*   **現代用戶界面：** 使用 Flet 構建，提供快速、外觀原生的桌面應用程序。
*   **會話管理：** 允許開始、停止、重置和保存會話統計數據。

## 先決條件

*   Python 3.8+
*   **Flet** 和 **Scapy** 庫。
*   **Root/管理員權限：** 網絡數據包捕獲所必需。

## 安裝與設置

### 選項 1：快速安裝（Linux - 推薦）

對於 Linux 用戶，我們提供自動化安裝腳本：

\`\`\`bash
# 1. 克隆倉庫
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 運行安裝腳本
./install.sh

# 3. 運行應用程序
./run.sh
\`\`\`

`install.sh` 腳本將會：
- 安裝系統依賴項（`libpcap-dev`、`python3-pip`、`python3-venv`）
- 創建 Python 虛擬環境
- 安裝所有必需的 Python 包（Flet、Scapy）

`run.sh` 腳本將自動請求 root 權限並運行應用程序。

### 選項 2：手動安裝

#### 1. 安裝系統依賴項

**在 Linux 上 (Debian/Ubuntu)：**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**在 Windows 上：**

從 [python.org](https://www.python.org/downloads/) 安裝 Python 3.8+

#### 2. 安裝 Python 依賴項

**在 Linux 上 (使用虛擬環境 - 推薦)：**

\`\`\`bash
# 創建虛擬環境
python3 -m venv venv

# 激活虛擬環境
source venv/bin/activate

# 安裝依賴項
pip install flet scapy
\`\`\`

**在 Linux 上 (系統範圍安裝)：**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**在 Windows 上：**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. 運行應用程序

由於網絡嗅探需要提升權限，您必須以 root 或管理員身份運行應用程序。

**在 Linux 上 (使用虛擬環境)：**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**在 Linux 上 (系統範圍安裝)：**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**在 Windows 上 (以管理員身份運行命令提示符/PowerShell)：**

\`\`\`bash
python -m albion_insight
\`\`\`

應用程序將在原生桌面窗口中打開。

## 如何構建可執行文件

應用程序可以使用 **PyInstaller** 打包成獨立的可執行文件。這允許用戶在不安裝 Python 或其依賴項的情況下運行應用程序。

有關構建 Linux、Windows 和 macOS 可執行文件的詳細說明，請參閱 **[PACKAGING.md](PACKAGING.md)** 指南。

### 快速構建（Linux）

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

可執行文件將位於 `dist/` 文件夾中。

## 項目結構

應用程序被構建成模塊化組件，以實現更好的可維護性和可擴展性：

| 文件 | 描述 |
| :--- | :--- |
| `albion_insight/core/` | 核心邏輯、網絡追蹤、數據模型和協議解碼。 |
| `albion_insight/ui/` | 使用 Flet 構建的用戶界面組件。 |
| `albion_insight/utils/` | 實用函數、配置和日誌記錄。 |
| `albion_insight/__main__.py` | 應用程序的入口點。 |
| `README.md` | 此文檔文件（英文）。 |
| `CONTRIBUTING.md` | 貢獻項目的指南。 |
| `CODE_OF_CONDUCT.md` | 項目的行為準則。 |
| `SECURITY.md` | 報告安全漏洞的政策。 |
| `README.ar-SA.md` | توثيق باللغة العربية (阿拉伯語文檔)。 |
| `README.ca-ES.md` | Documentació en català (加泰羅尼亞語文檔)。 |
| `README.cs-CZ.md` | Dokumentace v češtině (捷克語文檔)。 |
| `README.da-DK.md` | Dokumentation på dansk (丹麥語文檔)。 |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (德語文檔)。 |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (希臘語文檔)。 |
| `README.es-ES.md` | Documentación en español (西班牙語文檔)。 |
| `README.fa-IR.md` | مستندات به زبان فارسی (波斯語文檔)。 |
| `README.fi-FI.md` | Dokumentaatio suomeksi (芬蘭語文檔)。 |
| `README.fi.md` | Dokumentaatio suomeksi (芬蘭語文檔 - 一般)。 |
| `README.fil-PH.md` | Dokumentasyon sa Filipino (菲律賓語文檔)。 |
| `README.fr-FR.md` | Documentation en français (法語文檔)。 |
| `README.he-IL.md` | תיעוד בעברית (希伯來語文檔)。 |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (印地語文檔)。 |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (匈牙利語文檔)。 |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia (印尼語文檔)。 |
| `README.it-IT.md` | Documentazione in italiano (意大利語文檔)。 |
| `README.ja-JP.md` | 日本語のドキュメント (日語文檔)。 |
| `README.ko-KR.md` | 한국어 문서 (韓語文檔)。 |
| `README.lt-LT.md` | Dokumentacija lietuvių kalba (立陶宛語文檔)。 |
| `README.lv-LV.md` | Dokumentācija latviešu valodā (拉脫維亞語文檔)。 |
| `README.ne-NP.md` | नेपालीमा कागजात (尼泊爾語文檔)。 |
| `README.nl-NL.md` | Documentatie in het Nederlands (荷蘭語文檔)。 |
| `README.no-NO.md` | Dokumentasjon på norsk (挪威語文檔)。 |
| `README.pl-PL.md` | Dokumentacja w języku polskim (波蘭語文檔)。 |
| `README.pt-BR.md` | Documentação em português do Brasil (巴西葡萄牙語文檔)。 |
| `README.pt-PT.md` | Documentação em português europeu (歐洲葡萄牙語文檔)。 |
| `README.ro-RO.md` | Documentație în română (羅馬尼亞語文檔)。 |
| `README.ru-RU.md` | Документация на русском языке (俄語文檔)。 |
| `README.sk-SK.md` | Dokumentácia v slovenčine (斯洛伐克語文檔)。 |
| `README.sv-SE.md` | Dokumentation på svenska (瑞典語文檔)。 |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (泰語文檔)。 |
| `README.tr-TR.md` | Türkçe dokümantasyon (土耳其語文檔)。 |
| `README.uk-UA.md` | Документація українською мовою (烏克蘭語文檔)。 |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (越南語文檔)。 |
| `README.zh-CN.md` | 简体中文文档 (簡體中文文檔)。 |
| `README.zh-TW.md` | 繁體中文文件 (繁體中文文檔)。 |
| `README.gl-ES.md` | Documentación en galego (加利西亞語文檔)。 |
| `README.et-EE.md` | Dokumentatsioon eesti keeles (愛沙尼亞語文檔)。 |
| `README.zu-ZA.md` | Imibhalo ngolimi lwesiZulu (祖魯語文檔)。 |

## 當前狀態（實時數據）

應用程序現在包含了從原始 C# 項目翻譯過來的 **Photon 協議解碼** 邏輯。這使得應用程序能夠直接從網絡流量中處理實時事件，例如 `UpdateMoney`、`UpdateFame`、`KilledPlayer` 和 `Died`。

**注意：** 完整翻譯每一個戰鬥事件（例如 `CastHit`、`Attack`）是一項持續進行的工作。當前的實現專注於核心統計數據和傷害計數器的結構。傷害計數器的 DPS 計算基於已解碼的事件。

## 貢獻

我們歡迎社區的貢獻！無論您是開發人員、設計師，還是僅僅是 Albion Online 的愛好者，都有許多方法可以幫助改進 Albion Insight。

請閱讀我們的 [貢獻指南](CONTRIBUTING.md)，了解有關如何為此項目做出貢獻的詳細信息。

### 貢獻者快速入門：

1.  Fork 倉庫：[github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  克隆您的 Fork：`git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  創建一個新分支：`git checkout -b feature/您的功能名稱`
4.  進行更改並提交：`git commit -m "添加您的功能"`
5.  推送到您的 Fork：`git push origin feature/您的功能名稱`
6.  在主倉庫上打開 Pull Request

## 許可證

此項目根據 MIT 許可證授權 - 有關詳細信息，請參閱 [LICENSE](LICENSE) 文件。

## 致謝

- 原始項目：[AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- 使用 [Flet](https://flet.dev/) 框架構建
- 網絡分析由 [Scapy](https://scapy.net/) 提供支持

---
*為 Albion Online 社區提供的跨平台解決方案。*
