_Esta é uma tradução gerada pela comunidade. Pode não estar 100% precisa ou atualizada. Para a versão mais recente, por favor, consulte o [README em inglês](README.md)._

# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in German (Lesen Sie dies auf Deutsch)](README.de-DE.md)**\
**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**
**[Read this in Spanish (Leer en Español)](README.es-ES.md)**
**[Read this in French (Lire en Français)](README.fr-FR.md)**
**[Read this in Italian (Leggi in Italiano)](README.it-IT.md)**\
**[Read this in Simplified Chinese (阅读简体中文)](README.zh-CN.md)**\
**[Read this in Russian (Прочитать на русском)](README.ru-RU.md)**\
**[Read this in Japanese (日本語で読む)](README.ja-JP.md)**\
**[Read this in Arabic (اقرأ هذا بالعربية)](README.ar-SA.md)**\
**[Read this in Turkish (Türkçe Oku)](README.tr-TR.md)**\
**[Read this in Korean (한국어로 읽기)](README.ko-KR.md)**\
**[Read this in Dutch (Lees dit in het Nederlands)](README.nl-NL.md)**\
**[Read this in Polish (Czytaj po polsku)](README.pl-PL.md)**
**[Read this in Hindi (इसे हिंदी में पढ़ें)](README.hi-IN.md)**
**[Read this in Swedish (Läs detta på svenska)](README.sv-SE.md)**\
**[Read this in Vietnamese (Đọc bằng tiếng Việt)](README.vi-VN.md)**

**Albion Insight**は、ゲーム「アルビオン・オンライン」向けのクロスプラットフォーム（Linux、Windows、macOS）統計分析ツールで、**Python**と**Flet**フレームワークを使用して再実装されました。ネットワークトラフィックを分析することで、シルバー、名声、戦闘データ（ダメージメーター）などのリアルタイムのゲーム内統計を追跡するように設計されています。

このプロジェクトは、元のC#/WPFベースの`AlbionOnline-StatisticsAnalysis`ツールに代わる、マルチプラットフォーム互換性と使いやすさに焦点を当てた、現代的でオープンソースの代替手段です。

## 特徴

*   **クロスプラットフォーム互換性:** Linux、Windows、macOSでネイティブに動作します。
*   **リアルタイム追跡:** `Scapy`ライブラリを使用して、アルビオン・オンラインのポート（5055、5056、5058）でUDPパケットをスニッフィングします。
*   **ダメージメーター構造:** ライブ戦闘統計（与ダメージ、回復量、DPS）を表示するために必要なデータ構造とUIが含まれています。
*   **モダンなUI:** Fletで構築され、高速でネイティブな外観のデスクトップアプリケーションを提供します。
*   **セッション管理:** セッション統計の開始、停止、リセット、保存が可能です。

## 前提条件

*   Python 3.8+
*   **Flet**および**Scapy**ライブラリ。
*   **ルート/管理者権限:** ネットワークパケットキャプチャに必要です。

## インストールとセットアップ

### オプション1：クイックインストール（Linux - 推奨）

Linuxユーザー向けに、自動インストールスクリプトを提供しています：

```bash
# 1. リポジトリをクローンする
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. インストールスクリプトを実行する
./install.sh

# 3. アプリケーションを実行する
./run.sh
```

`install.sh`スクリプトは次のことを行います：
- システム依存関係（`libpcap-dev`、`python3-pip`、`python3-venv`）をインストールします
- Python仮想環境を作成します
- 必要なすべてのPythonパッケージ（Flet、Scapy）をインストールします

`run.sh`スクリプトは自動的にルート権限を要求し、アプリケーションを実行します。

### オプション2：手動インストール

#### 1. システム依存関係のインストール

**Linux（Debian/Ubuntu）の場合：**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windowsの場合：**

[python.org](https://www.python.org/downloads/)からPython 3.8+をインストールします

#### 2. Python依存関係のインストール

**Linux（仮想環境を使用 - 推奨）：**

```bash
# 仮想環境を作成する
python3 -m venv venv

# 仮想環境をアクティブにする
source venv/bin/activate

# 依存関係をインストールする
pip install flet scapy
```

**Linux（システム全体へのインストール）：**

```bash
pip3 install flet scapy --break-system-packages
```

**Windowsの場合：**

```bash
pip install flet scapy
```

#### 3. アプリケーションの実行

ネットワークスニッフィングには昇格された権限が必要なため、アプリケーションをルートまたは管理者として実行する必要があります。

**Linux（仮想環境を使用）：**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Linux（システム全体へのインストール）：**

```bash
sudo python3 albion_insight/main.py
```

**Windows（コマンドプロンプト/PowerShellを管理者として実行）：**

```bash
python albion_insight/main.py
```

アプリケーションはネイティブのデスクトップウィンドウで開きます。

## 実行可能ファイルのビルド方法

アプリケーションは、**PyInstaller**を使用してスタンドアロンの実行可能ファイルにパッケージ化できます。これにより、ユーザーはPythonやその依存関係をインストールせずにアプリケーションを実行できます。

Linux、Windows、macOS用の実行可能ファイルのビルドに関する詳細な手順については、**[PACKAGING.md](PACKAGING.md)**ガイドを参照してください。

### クイックビルド（Linux）

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

実行可能ファイルは`dist/`フォルダにあります。

## プロジェクト構造

アプリケーション全体は、シンプルにするために単一のファイルに含まれています：

| ファイル | 説明 |
| :--- | :--- |
| `albion_insight/main.py` | すべてのロジック（モデル、ネットワークトラッカー、Flet UI）を含むメインアプリケーションファイル。 |
|| `README.md` | このドキュメントファイル。 |
| `README.pt-BR.md` | このドキュメントファイルのブラジルポルトガル語版。 |
| `CONTRIBUTING.md` | プロジェクトへの貢献に関するガイドライン。 |
| `CODE_OF_CONDUCT.md` | プロジェクトの行動規範。 |
| `SECURITY.md` | セキュリティ脆弱性の報告に関するポリシー。 |

## 現在のステータス（リアルタイムデータ）

アプリケーションには、元のC#プロジェクトから翻訳された**Photonプロトコルデコード**ロジックが含まれるようになりました。これにより、アプリケーションは`UpdateMoney`、`UpdateFame`、`KilledPlayer`、`Died`などのリアルタイムイベントをネットワークトラフィックから直接処理できます。

**注:** すべての戦闘イベント（`CastHit`、`Attack`など）の完全な翻訳は進行中の作業です。現在の実装は、コア統計とダメージメーターの構造に焦点を当てています。ダメージメーターのDPS計算は、デコードされたイベントに基づいています。

## 貢献

コミュニティからの貢献を歓迎します！開発者、デザイナー、または単なるアルビオン・オンラインの愛好家であっても、Albion Insightを改善するための多くの方法があります。

このプロジェクトへの貢献方法の詳細については、[貢献ガイドライン](CONTRIBUTING.md)をお読みください。

### 貢献者向けのクイックスタート：

1.  リポジトリをフォークする：[github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  フォークをクローンする：`git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  新しいブランチを作成する：`git checkout -b feature/your-feature-name`
4.  変更を加えてコミットする：`git commit -m "Add your feature"`
5.  フォークにプッシュする：`git push origin feature/your-feature-name`
6.  メインリポジトリでプルリクエストを開く

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細については[LICENSE](LICENSE)ファイルを参照してください。

## 謝辞

- 元のプロジェクト：Triky313による[AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- [Flet](https://flet.dev/)フレームワークで構築
- [Scapy](https://scapy.net/)によるネットワーク分析

---
*アルビオン・オンラインコミュニティ向けのクロスプラットフォームソリューション。*
