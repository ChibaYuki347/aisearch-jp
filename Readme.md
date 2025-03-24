# 概要

AI Search日本語のクエリ検索の調査内容です。

インフラの作成とテストデータの入力を可能にしています。

## インフラの作成

azdを使っています。

ログイン

```bash
azd auth login
```

その上で

```bash
azd provision
```

こちらでインフラの作成を行います。

## テストデータの入力

二つのShellスクリプトを用意しています。

1. script/initial_setup_ai_search.sh
こちらはAzure AI Searchのインデックスを作成し、サンプルデータを登録します。

2. script/search_documents.sh
こちらはAzure AI Searchのインデックスに対してクエリを投げ検索内容に応じてinputのパラメーターととoutputのパラメーターをjsonをファイル保存します。

実行にあたりShellスクリプトの権限を付与して下さい。
Pythonスクリプトを動かしているため、Pythonの環境が必要です。

```bash
chmod +x script/initial_setup_ai_search.sh
chmod +x script/search_documents.sh
```

その上でテストデータの入力を行います。

```bash
./script/initial_setup_ai_search.sh
```

## クエリの実行

```bash
./script/search_documents.sh
```

こちらでクエリを実行し、結果を確認することができます。

## 実行結果について

実行結果は`/samples`以下に保存されています。
実行結果の説明は[こちら](./docs/Morphological-Analysis-ja.md)