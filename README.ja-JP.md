# Albion Insight - アルビオン・オンライン統計分析ツール

Albion Insightは、人気MMORPG「アルビオン・オンライン」のプレイヤー向けに設計された、オープンソースの統計分析ツールです。このツールは、ゲームのネットワークトラフィックを監視し、貴重なゲーム内データ（マーケット情報、戦利品ログ、ダンジョン追跡など）を収集して分析します。

## 主な機能

*   **マーケットデータ分析:** リアルタイムのオークションハウスデータを追跡し、取引の意思決定を支援します。
*   **戦利品ロガー:** ダンジョンやPvEアクティビティからの戦利品を自動的に記録します。
*   **ダンジョン追跡:** 完了したダンジョンと関連する統計を監視します。
*   **クロスプラットフォーム対応:** Pythonで開発されており、Windows、Linux、macOSで動作します。

## インストール

Albion Insightをインストールするには、以下の手順に従ってください。

### 前提条件

*   Python 3.10以上
*   `pip` (Pythonパッケージインストーラ)

### クイックインストール（推奨）

`install.sh` スクリプトを使用して、必要な依存関係を自動的に設定できます。

```bash
./install.sh
```

### 手動インストール

1.  リポジトリをクローンします:
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  仮想環境を作成し、アクティブ化します:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```
3.  依存関係をインストールします:
    ```bash
    pip install -r requirements.txt
    ```

## 実行

アプリケーションを実行するには、アクティブ化された仮想環境内で `run.sh` スクリプトを使用します。

```bash
./run.sh
```

## 貢献

私たちはコミュニティからの貢献を歓迎します！バグ報告、機能提案、コードの貢献など、お気軽にお寄せください。

*   **バグ報告:** [Issues](https://github.com/dexcarva/AlbionInsight/issues) ページを使用してください。
*   **コード貢献:** [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下でライセンスされています。

---
**注:** このツールは、ゲームのネットワークトラフィックを読み取ることで動作します。これは、アルビオン・オンラインの利用規約で許可されている「サードパーティ製ツール」のガイドラインに準拠しています。
