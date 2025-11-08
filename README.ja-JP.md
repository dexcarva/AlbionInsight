# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in English (英語で読む)](README.md)**
**[Read this in German (ドイツ語で読む)](README.de-DE.md)**
**[Read this in Portuguese (ポルトガル語で読む)](README.pt-BR.md)**
**[Read this in Spanish (スペイン語で読む)](README.es-ES.md)**
**[Read this in French (フランス語で読む)](README.fr-FR.md)**
**[Read this in Italian (イタリア語で読む)](README.it-IT.md)**
**[Read this in Simplified Chinese (簡体字中国語で読む)](README.zh-CN.md)**
**[Read this in Russian (ロシア語で読む)](README.ru-RU.md)**
**[Read this in Japanese (日本語で読む)]**

**Albion Insight** は、ゲーム **Albion Online** のクロスプラットフォーム（Linux、Windows、macOS）統計分析ツールであり、**Flet** フレームワークを使用して **Python** で再実装されました。ネットワークトラフィックを分析することにより、シルバー、名声、戦闘データ（ダメージメーター）などのリアルタイムのゲーム内統計を追跡するように設計されています。

このプロジェクトは、元の C#/WPF ベースの `AlbionOnline-StatisticsAnalysis` ツールに代わる、最新のオープンソースの代替手段であり、マルチプラットフォームの互換性と使いやすさに焦点を当てています。

## 特徴

*   **クロスプラットフォームの互換性:** Linux、Windows、macOS でネイティブに動作します。
*   **リアルタイム追跡:** `Scapy` ライブラリを使用して、Albion Online のポート（5055、5056、5058）上の UDP パケットをスニッフィングします。
*   **ダメージメーター構造:** ライブ戦闘統計（与ダメージ、回復量、DPS）を表示するための必要なデータ構造と UI が含まれています。
*   **モダンな UI:** Flet で構築されており、高速でネイティブな外観のデスクトップアプリケーションを提供します。
*   **セッション管理:** セッション統計の開始、停止、リセット、保存が可能です。

## 前提条件

*   Python 3.8+
*   **Flet** および **Scapy** ライブラリ。
*   **ルート/管理者権限:** ネットワークパケットキャプチャに必要です。

## インストールとセットアップ

### オプション 1: クイックインストール（Linux - 推奨）

Linux ユーザー向けに、自動インストールスクリプトを提供しています。

```bash
# 1. リポジトリをクローンします
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. インストールスクリプトを実行します
./install.sh

# 3. アプリケーションを実行します
./run.sh
```

`install.sh` スクリプトは以下を実行します。
- システム依存関係（`libpcap-dev`、`python3-pip`、`python3-venv`）をインストールします
- Python 仮想環境を作成します
- 必要なすべての Python パッケージ（Flet、Scapy）をインストールします

`run.sh` スクリプトは、自動的にルート権限を要求し、アプリケーションを実行します。

### オプション 2: 手動インストール

#### 1. システム依存関係のインストール

**Linux (Debian/Ubuntu) の場合:**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windows の場合:**

[python.org](https://www.python.org/downloads/) から Python 3.8+ をインストールします

#### 2. Python 依存関係のインストール

**Linux (仮想環境を使用 - 推奨) の場合:**

```bash
# 仮想環境を作成します
python3 -m venv venv

# 仮想環境をアクティブ化します
source venv/bin/activate

# 依存関係をインストールします
pip install flet scapy
```

**Linux (システム全体へのインストール) の場合:**

```bash
pip3 install flet scapy --break-system-packages
```

**Windows の場合:**

```bash
pip install flet scapy
```

#### 3. アプリケーションの実行

**Linux の場合:**

```bash
# 仮想環境がアクティブであることを確認してください
sudo python3 albion_insight/albion_insight.py
```

**Windows の場合:**

```bash
python albion_insight/albion_insight.py
```

## 貢献

貢献は大歓迎です！バグ報告、機能リクエスト、コードの改善など、どのような形でも構いません。

貢献する前に、[CONTRIBUTING.md](CONTRIBUTING.md) をお読みください。

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています - 詳細については [LICENSE](LICENSE) ファイルを参照してください。

## 謝辞

*   オリジナルの `AlbionOnline-StatisticsAnalysis` プロジェクトを作成した **Triky313** に感謝します。
*   このプロジェクトの UI フレームワークである **Flet** の開発者に感謝します。
*   ネットワークパケットキャプチャを可能にする **Scapy** ライブラリに感謝します。
*   すべての貢献者とユーザーに感謝します！
