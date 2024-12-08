# YOLO
4班の課題研究で使ったYOLOに関するプログラムを公開しています。オリジナルのデータセットやそのプログラムの使い方などをを書き込んでいます。

## 動作環境　

言語
- [Python>=3.8](https://www.python.org/) 

使用ソフト
- [Visual Studio Code](https://code.visualstudio.com/)

自分のPC
 - OS : windows 10 Pro
 - CPU : Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz
 - GPU : Nvidia GeForce GTX 1050ti
 - RAM : 16GB

  学校のラズベリーパイ
 - Raspberry Pi 4 8GB moddel

## 使用プログラム
- [Ultralytics](https://www.ultralytics.com/) [YOLO11](https://github.com/ultralytics/ultralytics)

## 説明

　今回YOLOを使用したのはなるべく簡単かつ、使用しやすい、動作が軽いという点でYOLOが優秀だったため使用しました。
 YOLOはYou Only Look Onceの略で、物体検出のための深層学習ベースのアルゴリズムの1つです。

その名の通り、画像を一度だけ見て物体を検出する特性があります。

YOLOの特徴は一定水準の精度を保ちつつも高速・軽量に動作することです。YOLOにはv5から11まで存在しますがラズベリーパイの処理速度を鑑みて1番軽いv5を種にして使用しています。一応v5の他にv8、11のウェイトは用意しています。
ウェイトは機械学習した結果のモデルで、プログラム上では(例)yolov5.ptのようにあります。YOLOv8にはCOCOやImageNetなどの代表的なサンプルデータを用い、既に学習済みのモデルが公開されています。これを利用することですぐに物体検出を実施できます。

実際のプログラムはこのようなプログラムが使用されます。
``` python
from ultralytics import YOLO

# Load a model
source = "https://ultralytics.com/images/bus.jpg"
model = YOLO('yolov5n.pt')  # load an official model

# Predict with the model
results = model.predict(source, save=True, imgsz=320, conf=0.5)
```

- from ではライブラリのインストールを行います。ライブラリとはPythonのライブラリとは、Pythonで開発を行うにあたって良く使われる関数やパッケージがまとめられたものを言います。 インターネットからダウンロードして使うものであり、ライブラリを活用することで、クラスなどを設定しなくてもプログラムが開発できます。
モデルの性能はYOLOv5n＜YOLOv5s＜YOLOv5m＜YOLOv5l＜YOLOv5xと増加しますが、反面、学習や推論に時間がかかってしまいます。

- sourceであるのはテンプレートの画像で、ここではバスの画像が用意されています。

- modelでは公式で用意されているモデルが使用されています。


　しかし実際にこのプログラムを動作させるためには他にも手順が必要なため、次の行から説明をします。

 ## 使用方法(VScode)
 ここでは完全に1からプログラムを動作をさせるために説明を開始していきます。
 </br></br>
- まずは[Python](https://www.python.org/) を実機にインストールしていきます。YOLOはPythonバージョン3.8以降で動作するのでダウンロードします。しかしバージョンが高すぎると逆にYOLOのほうが起動しなくなるため、その場合はダウングレードしてください。右のボタンからダウンロードします。
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)
 </br></br>
 ダウンロードが終わったらインストールします。インストール時は必ず  画像のようにwindows設定→アプリ→アプリと機能 にPythonがインストールされていることを確認してください。そうしたらアプリ実行エイリアスからpythonインストーラーをオフにしてください。こうしないとライブラリのインストールpipが上手く動作しないことがあります。
 </br></br>
- 次に[Visual Studio Code](https://code.visualstudio.com/)をダウンロードします。最新バージョンでないと動作しないことがありますので、ダウンロード時の最新バージョンをダウンロードしてください。VScodeをダウンロード後は初期設定として日本語化のインストールやPython類のツール等インストールを行ってください。
</br></br>
- 次にデスクトップ上にgithubからダウンロードしたファイルをおいてください。テンプレートとしてそのファイルをつかっていきます。VScode上で「ファイル→フォルダを開く」がらデスクトップ上においたフォルダを選択してください。では実際に画像処理を始めましょう。

 </br></br>
- 仮想環境の構築　</br></br>
ultralyticsライブラリは、インストールの過程で非常に多くの関連ライブラリをインストールします。すでにある環境に悪影響を及ぼしたり、そもそもライブラリがインストールされなかったりするので環境を構築します。</br>
プログラムとしてはまずこれでenvファイルを作成します。プログラムを打ち込む際はターミナルから入力してください。プログラム実行後はフォルダの中にenvファイルが作成されていることを確認してください。
``` python
python -m venv env
```
次にこのプログラムでenvファイルをアクティベートさせます。ここでコマンドラインの文字の先に(env)と表示されていたら成功です。エラーを吐いたらwindows側の問題があったりPowerShellに問題があったするのでエラー文を読み、適切な処置をしてください。
``` python
env\Scripts\Activate.ps1
```
</br></br>
- ライブラリのインストール
</br></br>

