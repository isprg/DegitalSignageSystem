# デジタルサイネージシステム

このリポジトリはシンプルなデジタルサイネージ（動画表示）アプリケーションです。Flask を使った管理・配信用のサーバと、表示用のテンプレートを含みます。ローカルや小規模ネットワーク上で動画を配信する用途に向いています。

## 主な機能

- 動画一覧の取得と選択
- 表示用ビューの提供（フルスクリーン表示などに利用）
- 現在再生中の動画パスを JSON で取得可能

## 動作環境

- Python 3.8 以上

## セットアップ

1. 仮想環境を作成・有効化（推奨）

- Windows (PowerShell):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

- macOS / Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

1. 依存パッケージをインストール

   ```bash
   pip install -r requirements.txt
   ```

## 実行方法

- 本番向け（Waitress を使う、ポート 80）:

 ```bash
 python main.py
 ```

- 開発用（デバッグモード、ポート 5000）:

 ```bash
 
 python app/server.py
 ```

これにより、デフォルトでホスト `0.0.0.0` にアプリケーションが公開されます。

## 主要な URL と API

- `/` : 管理/選択用のページ（`index.html`）。クエリ文字列 `?video=ファイル名` を渡すと表示対象の動画が切り替わります。
- `/view` : 表示専用ページ（`view.html`）。フルスクリーン表示などに利用できます。
- `/video` : 現在再生中の動画パスを JSON で返します。例: `{ "video_path": "static/videos/xxx.mp4" }`

## 動画の追加・管理

- 動画ファイルは `static/videos/` フォルダに配置してください。
- デフォルト動画は `static/videos/white.mp4` に設定されています。
- サーバは `app.lib.load_video.load_videos()` を呼んでディレクトリ内の動画一覧を生成します（既存の命名規則に従ってください）。

## プロジェクト構成（抜粋）

- `main.py` — Waitress でアプリを起動するエントリポイント
- `app/server.py` — Flask アプリ本体（ルート定義）
- `app/lib/load_video.py` — 動画一覧を読み込むユーティリティ
- `static/` — 静的ファイル（`videos/`, `css/`, `js/`）
- `templates/` — `index.html`, `view.html` などのテンプレート

## 補足・開発メモ

- 開発中にテンプレートや静的ファイルを編集した場合、`app/server.py` を直接実行するとデバッグモードで自動リロードされ便利です。
- ポートやホストを変更する場合は `main.py` または `app/server.py` の起動引数を編集してください。
