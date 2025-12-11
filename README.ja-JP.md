# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** は、ゲーム『Albion Online』用のクロスプラットフォーム（Linux、Windows、macOS）統計分析ツールであり、**Flet** フレームワークを使用して **Python** で再実装されました。ネットワークトラフィックを分析することで、シルバー、名声、戦闘データ（ダメージメーター）など、リアルタイムのゲーム内統計を追跡するように設計されています。

このプロジェクトは、元の C#/WPF ベースの `AlbionOnline-StatisticsAnalysis` ツールに代わる、モダンでオープンソースな代替手段であり、マルチプラットフォームの互換性と使いやすさに焦点を当てています。

## 特徴 (Features)

*   **クロスプラットフォーム互換性:** Linux、Windows、macOS でネイティブに動作します。
*   **リアルタイム追跡:** `Scapy` ライブラリを使用して、Albion Online のポート（5055、5056、5058）上の UDP パケットをスニッフィングします。
*   **ダメージメーター構造:** ライブ戦闘統計（与ダメージ、回復量、DPS）を表示するために必要なデータ構造と UI が含まれています。
*   **モダンな UI:** Flet で構築されており、高速でネイティブな外観のデスクトップアプリケーションを提供します。
*   **セッション管理:** セッション統計の開始、停止、リセット、保存が可能です。

## 前提条件 (Prerequisites)

*   Python 3.8+
*   **Flet** および **Scapy** ライブラリ。
*   **ルート/管理者権限:** ネットワークパケットキャプチャに必要です。

## インストールとセットアップ (Installation and Setup)

### オプション 1: クイックインストール (Linux - 推奨)

Linux ユーザー向けに、自動インストールスクリプトを提供しています。

\`\`\`bash
# 1. リポジトリをクローンする
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. インストールスクリプトを実行する
./install.sh

# 3. アプリケーションを実行する
./run.sh
\`\`\`

`install.sh` スクリプトは以下を実行します。
- システム依存関係 (`libpcap-dev`、`python3-pip`、`python3-venv`) をインストールします。
- Python 仮想環境を作成します。
- 必要なすべての Python パッケージ (Flet、Scapy) をインストールします。

`run.sh` スクリプトは、自動的にルート権限を要求し、アプリケーションを実行します。

### オプション 2: 手動インストール (Windows/macOS/Linux)

1.  **リポジトリをクローンする:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`

2.  **仮想環境を作成し、アクティブ化する:**
    \`\`\`bash
    python3 -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    \`\`\`

3.  **依存関係をインストールする:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4.  **アプリケーションを実行する:**
    \`\`\`bash
    # Windows: 管理者として実行する必要があります
    flet run albion_insight/main.py
    # Linux/macOS: root/sudo 権限が必要です
    sudo flet run albion_insight/main.py
    \`\`\`

## 貢献 (Contributing)

貢献を歓迎します！バグ報告、機能リクエスト、コードの改善など、お気軽にご参加ください。詳細については、[CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス (License)

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

## 謝辞 (Acknowledgments)

*   元の C#/WPF プロジェクト `AlbionOnline-StatisticsAnalysis` の作成者である **Triky313** に感謝します。
*   ネットワークパケットキャプチャ機能を提供する **Scapy** チームに感謝します。
*   クロスプラットフォーム UI を可能にする **Flet** チームに感謝します。
