# ルーレットで入場したダンジョンを一発検索

## 概要
このアプリケーションは、スクリーンショットからゲーム内のダンジョン名を認識し、そのダンジョン名に基づいて`fF14予習室様の攻略ページ`を自動的に開くことができます。  
主に、ゲーム内でのダンジョン名を認識し、関連する攻略サイトをブラウザで開くために使用されます。

## 特徴
- ユーザーがスクリーンショットを撮影するための簡単な操作  
- OCR（光学文字認識）を利用したテキスト認識  
- 認識したダンジョン名に基づいて攻略サイトを自動で開く

## 使用方法
1. アプリケーションを開くと、メインウィンドウが表示されます。
2. 「Rec」ボタンをクリックしてスクリーンショットの選択を開始します。
3. ゲーム内でダンジョン名が表示されている部分をマウスで選択してください。
4. 選択範囲からダンジョン名が認識されると、関連する攻略サイトが自動的にブラウザで開きます。

## インストール方法
このアプリケーションを使用するには、Tesseract-OCRがシステムにインストールされている必要があります。インストール方法は以下の通りです。

### Tesseract-OCRのインストール
Tesseract-OCRは、[公式サイト](https://github.com/tesseract-ocr/tesseract)から使用している環境に合わせてダウンロードしてください。  
windowsの場合は、[ここ](https://github.com/UB-Mannheim/tesseract/wiki)からダウンロードしてください。  
インストール後、以下の環境変数を設定する必要があります。  
`C:\Program Files\Tesseract-OCR\tesseract.exe`　　

### [リリース](https://github.com/me846/FF14-Beginner-Dungeon-Search/releases/tag/FBDS)から`FF14-BDS.exe`をDLし、起動してください

## 注意事項
- このアプリケーションは、特定の解像度やフォントサイズで最適に動作するように設計されています。異なる環境では、調整が必要になる場合があります。  
- ウイルス対策ソフトウェアによっては、実行ファイルが誤検出されることがありますので例外設定を行ってください。
- このアプリケーションはサードパーティ製です。FF14の規約上違反に当てはまります。自己責任の上で使用してください。

## 開発貢献について
このプロジェクトはオープンソースであり、コミュニティからの貢献を歓迎しています。
バグ報告や機能提案があれば、[Issues](https://github.com/me846/FF14-Beginner-Dungeon-Search/issues)にて報告してください。
機能提案する場合は、クリーンなものでお願いします。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。


