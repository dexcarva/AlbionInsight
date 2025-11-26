<h1 align="center">Albion Insight</h1>

<p align="center">
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version"></a>
    <a href="https://github.com/dexcarva/AlbionInsight"><img src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg" alt="Platform"></a>
    <a href="https://github.com/dexcarva/AlbionInsight/issues"><img src="https://img.shields.io/github/issues/dexcarva/AlbionInsight" alt="GitHub Issues"></a>
    <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg" alt="Contributions Welcome"></a>
</p>

<details>
<summary>他の言語で読む</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)** | **[Finnish](README.fi-FI.md)**

</details>

**Albion Insight** は、Albion Online ゲーム用のクロスプラットフォーム（Linux、Windows、macOS）統計分析ツールであり、**Flet** フレームワークを使用して **Python** で再実装されました。ネットワークトラフィックを分析することで、シルバー、名声、戦闘データ（ダメージメーター）などのリアルタイムのゲーム内統計を追跡するように設計されています。

このプロジェクトは、元の C#/WPF ベースの `AlbionOnline-StatisticsAnalysis` ツールに代わる、最新のオープンソースの代替手段であり、マルチプラットフォームの互換性と使いやすさに焦点を当てています。

## 特徴

*   **クロスプラットフォームの互換性:** Linux、Windows、macOS でネイティブに動作します。
*   **リアルタイム追跡:** `Scapy` ライブラリを使用して、Albion Online のポート（5055、5056、5058）で UDP パケットをスニッフィングします。
*   **ダメージメーター構造:** ライブ戦闘統計（与ダメージ、回復量、DPS）を表示するための必要なデータ構造と UI が含まれています。
*   **モダンな UI:** Flet で構築されており、高速でネイティブな外観のデスクトップアプリケーションを提供します。
*   **セッション管理:** セッション統計の開始、停止、リセット、保存が可能です。

## 前提条件

*   Python 3.8+
*   **Flet** および **Scapy** ライブラリ。
*   **ルート/管理者権限:** ネットワークパケットキャプチャに必要です。

## インストールとセットアップ

### オプション 1: クイックインストール（Linux - 推奨）

Linux ユーザー向けに、自動化されたインストールスクリプトを提供しています。

```bash
# 1. リポジトリをクローンする
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. インストールスクリプトを実行する
./install.sh

# 3. アプリケーションを実行する
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

**Linux (仮想環境の使用 - 推奨) の場合:**

```bash
# 仮想環境を作成する
python3 -m venv venv

# 仮想環境をアクティブ化する
source venv/bin/activate

# 依存関係をインストールする
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

ネットワークスニッフィングには昇格された権限が必要なため、アプリケーションをルートまたは管理者として実行する必要があります。

**Linux (仮想環境を使用) の場合:**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Linux (システム全体へのインストール) の場合:**

```bash
sudo python3 -m albion_insight
```

**Windows (管理者としてコマンドプロンプト/PowerShell を実行) の場合:**

```bash
python -m albion_insight
```

アプリケーションはネイティブのデスクトップウィンドウで開きます。

## 実行可能ファイルのビルド方法

アプリケーションは、**PyInstaller** を使用してスタンドアロンの実行可能ファイルにパッケージ化できます。これにより、ユーザーは Python やその依存関係をインストールせずにアプリケーションを実行できます。

Linux、Windows、macOS 用の実行可能ファイルのビルドに関する詳細な手順については、**[PACKAGING.md](PACKAGING.md)** ガイドを参照してください。

### クイックビルド（Linux）

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

実行可能ファイルは `dist/` フォルダにあります。

## プロジェクト構造

アプリケーションは、保守性と拡張性を向上させるためにモジュラーコンポーネントに構造化されています。

| ファイル | 説明 |
| :--- | :--- |
| `albion_insight/core/` | コアロジック、ネットワーク追跡、データモデル、プロトコルデコード。 |
| `albion_insight/ui/` | Flet で構築されたユーザーインターフェイスコンポーネント。 |
| `albion_insight/utils/` | ユーティリティ関数、構成、ロギング。 |
| `albion_insight/__main__.py` | アプリケーションのエントリポイント。 |
| `README.md` | このドキュメントファイル。 |
| `README.pt-BR.md` | このドキュメントファイル（ブラジルポルトガル語）。 |
| `README.fil-PH.md` | このドキュメントファイル（フィリピン語/タガログ語）。 |
| `README.pt-PT.md` | このドキュメントファイル（ポルトガル語）。 |
| `README.sv-SE.md` | このドキュメントファイル（スウェーデン語）。 |
| `CONTRIBUTING.sv-SE.md` | スウェーデン語でのプロジェクトへの貢献ガイドライン。 |
| `CONTRIBUTING.md` | プロジェクトへの貢献ガイドライン。 |
| `CODE_OF_CONDUCT.md` | プロジェクトの行動規範。 |
| `SECURITY.md` | セキュリティ脆弱性の報告に関するポリシー。 |

## 現在のステータス（リアルタイムデータ）

アプリケーションには、元の C# プロジェクトから翻訳された **Photon プロトコルデコード** ロジックが含まれるようになりました。これにより、アプリケーションは `UpdateMoney`、`UpdateFame`、`KilledPlayer`、`Died` などのリアルタイムイベントをネットワークトラフィックから直接処理できます。

**注:** すべての戦闘イベント（`CastHit`、`Attack` など）の完全な翻訳は進行中の作業です。現在の実装は、コア統計とダメージメーターの構造に焦点を当てています。ダメージメーターの DPS 計算は、デコードされたイベントに基づいています。

## 貢献

コミュニティからの貢献を歓迎します！開発者、デザイナー、または単なる Albion Online の愛好家であるかどうかにかかわらず、Albion Insight の改善に役立つ多くの方法があります。

このプロジェクトに貢献する方法の詳細については、[貢献ガイドライン](CONTRIBUTING.md)をお読みください。

### 貢献者向けのクイックスタート:

1.  リポジトリをフォークする: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  フォークをクローンする: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  新しいブランチを作成する: `git checkout -b feature/your-feature-name`
4.  変更を加えてコミットする: `git commit -m "Add your feature"`
5.  フォークにプッシュする: `git push origin feature/your-feature-name`
6.  メインリポジトリでプルリクエストを開く

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

## 謝辞

-   元のプロジェクト: Triky313 による [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
-   [Flet](https://flet.dev/) フレームワークで構築
-   [Scapy](https://scapy.net/) を利用したネットワーク分析

---
*Albion Online コミュニティ向けのクロスプラットフォームソリューション。*
