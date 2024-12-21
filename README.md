# 音声テキスト変換アプリの使い方

このアプリは、OpenAIのWhisper APIを使用して、音声ファイルをテキストに変換するPythonスクリプトです。

## 概要

- **スクリプト名:** `stt.py`
- **機能:** 音声ファイルをテキストに変換し、指定されたディレクトリに出力します。
- **使用API:** OpenAI Whisper API

## 使い方

1.  **必要な環境:**
    - Python 3.6以上
    - OpenAI Pythonライブラリ (`openai`)
    - OpenAI APIキー

2.  **環境設定:**
    - OpenAI APIキーを環境変数に設定する必要があります。
      ```bash
      export OPENAI_API_KEY="YOUR_API_KEY"
      ```
      または、スクリプト内で直接設定することもできますが、推奨されません。

3.  **スクリプトの実行:**
    - `stt.py`スクリプトを実行します。
      ```bash
      python stt.py
      ```
    - デフォルトでは、`secand.mp3`という音声ファイルが変換され、`output`ディレクトリに`output.txt`として出力されます。

4.  **出力:**
    - 変換されたテキストは、`output/output.txt`に保存されます。

## 注意点

-   音声ファイルは、スクリプトと同じディレクトリに配置するか、スクリプト内でパスを指定してください。
-   出力ディレクトリは、スクリプト内で指定できます。
-   OpenAI APIの利用には料金が発生する場合があります。

## その他

-   必要に応じて、スクリプト内の`audio_file_path`と`output_dir`変数を変更してください。