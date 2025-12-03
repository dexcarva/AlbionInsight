# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** 是为游戏《阿尔比恩OL》（Albion Online）设计的跨平台（Linux, Windows, macOS）统计分析工具，使用 **Python** 和 **Flet** 框架重新实现。它旨在通过分析网络流量，实时跟踪游戏内统计数据，包括银币、声望和战斗数据（伤害统计）。

本项目是基于 C#/WPF 的原始工具 `AlbionOnline-StatisticsAnalysis` 的一个现代化、开源替代品，专注于多平台兼容性和易用性。

## 特性 (Features)

*   **跨平台兼容性:** 可在 Linux, Windows 和 macOS 上原生运行。
*   **实时跟踪:** 使用 `Scapy` 库嗅探《阿尔比恩OL》端口 (5055, 5056, 5058) 上的 UDP 数据包。
*   **伤害统计结构:** 包含必要的数据结构和用户界面，用于显示实时战斗统计数据（造成伤害、治疗量、DPS）。
*   **现代用户界面:** 使用 Flet 构建，提供快速、外观原生的桌面应用程序。
*   **会话管理:** 允许开始、停止、重置和保存会话统计数据。

## 先决条件 (Prerequisites)

*   Python 3.8+
*   **Flet** 和 **Scapy** 库。
*   **Root/管理员权限:** 网络数据包捕获所必需。

## 安装与设置 (Installation and Setup)

### 选项 1: 快速安装 (Linux - 推荐)

对于 Linux 用户，我们提供了自动化安装脚本：

```bash
# 1. 克隆仓库
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 运行安装脚本
./install.sh

# 3. 运行应用程序
./run.sh
```

`install.sh` 脚本将：
- 安装系统依赖项 (`libpcap-dev`, `python3-pip`, `python3-venv`)
- 创建 Python 虚拟环境
- 安装所有必需的 Python 包 (Flet, Scapy)

`run.sh` 脚本将自动请求 Root 权限并运行应用程序。

### 选项 2: 手动安装 (Manual Installation)

#### 1. 安装系统依赖项

**在 Linux (Debian/Ubuntu) 上:**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**在 Windows 上:**

从 [python.org](https://www.python.org/downloads/) 安装 Python 3.8+

#### 2. 安装 Python 依赖项

**在 Linux 上 (使用虚拟环境 - 推荐):**

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖项
pip install flet scapy
```

**在 Linux 上 (系统范围安装):**

```bash
pip3 install flet scapy --break-system-packages
```

**在 Windows 上:**

```bash
pip install flet scapy
```

#### 3. 运行应用程序

由于网络嗅探需要提升权限，您必须以 root 或管理员身份运行应用程序。

**在 Linux 上 (使用虚拟环境):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**在 Linux 上 (系统范围安装):**

```bash
sudo python3 -m albion_insight
```

**在 Windows 上 (以管理员身份运行命令提示符/PowerShell):**

```bash
python -m albion_insight
```

应用程序将在原生桌面窗口中打开。

## 如何构建可执行文件 (How to Build an Executable)

可以使用 **PyInstaller** 将应用程序打包成独立的可执行文件。这允许用户无需安装 Python 或其依赖项即可运行应用程序。

有关构建 Linux, Windows 和 macOS 可执行文件的详细说明，请参阅 **[PACKAGING.md](PACKAGING.md)** 指南。

### 快速构建 (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

可执行文件将位于 `dist/` 文件夹中。

## 项目结构 (Project Structure)

应用程序被构建为模块化组件，以实现更好的可维护性和可扩展性：

| 文件 | 描述 |
| :--- | :--- |
| `albion_insight/core/` | 核心逻辑、网络跟踪、数据模型和协议解码。 |
| `albion_insight/ui/` | 使用 Flet 构建的用户界面组件。 |
| `albion_insight/utils/` | 实用函数、配置和日志记录。 |
| `albion_insight/__main__.py` | 应用程序的入口点。 |
| `README.md` | 此文档文件。 |
| `CONTRIBUTING.md` | 贡献指南。 |
| `CODE_OF_CONDUCT.md` | 项目的行为准则。 |
| `SECURITY.md` | 报告安全漏洞的政策。 |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档。 |

## 当前状态 (实时数据) (Current Status - Real-Time Data)

应用程序现在包含了从原始 C# 项目翻译过来的 **Photon 协议解码**逻辑。这使得应用程序能够直接从网络流量中处理实时事件，例如 `UpdateMoney` (更新银币), `UpdateFame` (更新声望), `KilledPlayer` (击杀玩家) 和 `Died` (死亡)。

**注意:** 并非所有战斗事件（如 `CastHit`, `Attack`）的完整翻译都在进行中。当前的实现侧重于核心统计数据和伤害统计的结构。伤害统计的 DPS 计算基于已解码的事件。

## 贡献 (Contributing)

我们欢迎社区的贡献！无论您是开发人员、设计师，还是仅仅是《阿尔比恩OL》的爱好者，都有许多方法可以帮助改进 Albion Insight。

请阅读我们的 [贡献指南](CONTRIBUTING.md)，了解如何为本项目做出贡献的详细信息。

### 贡献者快速入门:

1.  Fork 仓库: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  克隆您的 Fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  创建新分支: `git checkout -b feature/your-feature-name`
4.  进行更改并提交: `git commit -m "Add your feature"`
5.  推送到您的 Fork: `git push origin feature/your-feature-name`
6.  在主仓库上打开 Pull Request

## 许可证 (License)

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 致谢 (Acknowledgments)

- 原始项目: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- 使用 [Flet](https://flet.dev/) 框架构建
- 网络分析由 [Scapy](https://scapy.net/) 提供支持

---
*为《阿尔比恩OL》社区提供的跨平台解决方案。*
