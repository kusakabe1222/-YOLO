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

YOLOの特徴は一定水準の精度を保ちつつも高速・軽量に動作することです。YOLOにはv5から11まで存在しますがラズベリーパイの処理速度を鑑みて1番軽いv5を主にして使用しています。一応v5の他にv8、11のウェイトは用意しています。
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
 ダウンロードが終わったらインストールします。インストール時は必ずAdd Python 3.x to PATHをクリックしてください。<img width="1115" alt="installer-win" src="https://github.com/user-attachments/assets/20159ee1-0829-4faa-a540-2fb44c5ad413" />その後はコマンドプロンプトを開き

``` python
python
```
と入力して下さい。入力したとき、Pythonが起動せずに、次のようにMicrosoft Store の画面が表示されてしまうことがあります。その場合はもう一度pythonをインストールしなおしてください。PowerShellでスクリプトの実行を許可しておきます。

スタートメニューで Windows PowerShell | Windows PowerShell を起動し、次のコマンドを実行します。
``` python
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
これでpythonの初期設定は終わりです。
 </br></br>
- 次に[Visual Studio Code](https://code.visualstudio.com/)をダウンロードします。最新バージョンでないと動作しないことがありますので、ダウンロード時の最新バージョンをダウンロードしてください。VScodeをダウンロード後は初期設定として日本語化のインストールやPython類のツール等インストールを行ってください。ラズベリーパイにVScodeを入れる場合、ネットではなくコマンドで入れるので、ネットを参考にして下さい。
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
- ライブラリのインストール
</br>
次にライブラリをインストールします。</br>

```
pip install ultralytics
pip cv2
```
これでYOLOの機能を使用することが可能になります。試しにサンプルプログラムを動かしてみましょう。
- 物体検出
</br>
まずは物体検出を実行してみます。</br>

``` python
from ultralytics import YOLO

# Load a model
source = "https://ultralytics.com/images/bus.jpg"
model = YOLO('yolov8n.pt')  # load an official model

# Predict with the model
results = model.predict(source, save=True, imgsz=320, conf=0.5)

```
コードを実行するとこのような結果が得られます。
![bus-4-768x1024](https://github.com/user-attachments/assets/6c32dd52-4e03-41f3-929f-515255a8a637)</br>
無事検出されていることがわかったらYOLOの準備完了です。ここでエラーを吐いた場合は頑張ってください。後は配布したプログラムは動くはずです。
## ラズベリーパイで実行する
ではラズベリーパイでプログラムを実行する方法について説明していきます。
- VScodeの導入
  まずはラズベリーパイにVScodeを導入していきます。コマンドを開き以下のコードを入力します。
  ```
  sudo apt install code
  ```
  ![2022-01-06-222259_1920x1080_scrot_01-1](https://github.com/user-attachments/assets/65d1f5f5-08b3-47d5-930b-870c5e55baa9)
![2022-02-07-181514_1920x1080_scrot_00](https://github.com/user-attachments/assets/671389a9-133d-45f8-a9d2-4a48b9af3ce3)
</br>
コマンドラインで処理が終了したら[スタートメニュー]から、[プログラミング] – [Visual Studio Code]を選択します。

![Screenshot-from-2022-02-07-18-17-33_00](https://github.com/user-attachments/assets/c0fd578a-8efc-4807-9608-b6fa98cd6b47)
起動後は日本語表示にするなどしてください。

- 仮想環境の構築
  ラズベリーパイだと仮想環境の構築のプログラミングがwindowsと異なるため、こちらのプログラムを入力していきます。
  まずは
  ```
  	python3.12 -m venv env
  ```
  と打ちます。envフォルダが作成されます。pythonの後の数字はpythonバージョンで、ターミナル[python]と打つと確認できます。次には
  ```
  source env/bin/activate
  ```
  と打ちます。これで仮想環境をアクティベートできました。ライブラリをインストールし、上記のプログラムを入力して試してみてください。
  -GPIOピン
  ステッピングモータ等を動かすためにラズベリーパイのピンを使用します。ピンに関しては正直よくわかっていないため、chat gpt等にテンプレートのプログラムを出力させ、その内容によってピンを使用したほうがいいです。
![raspberrypi-gpio-04-1](https://github.com/user-attachments/assets/0f5adfe8-053b-4f84-9b9f-c629702c2b16)</br>
今回使用したステッピングモータ、ドライバボードは28BYJ-48 ステッピングモーターを ULN2003 ドライバボードです。
配布したプログラムの中にステッピングモータを動かすためのプログラムもあるので活用してください。
今回ラズベリーパイ4を使いました。ラズベリーパイ5を使用しようとしたら私の環境の場合使えませんでした。おそらく5からGPIOが変わっているため使えませんでした。動作は遅くなりますが仕方がなく4を使います。

# ウェイトの作成(ラベリング)
 ウェイト、重みの作成方法について説明します。いろいろサイトを参考にしながらやりましたが正しい方法についてはよくわからなかったため我流にはなりますがその方法について説明します。
まずはラベリングのやり方です。検出するものの写真を撮り、AIに学習させる作業です。写真を撮るのですが最低100枚、よくて1000枚程度必要になるので根気強くやらなければならなりません。
- Roboflow
  Roboflowはラベリングと学習をサイト上でやってくれる便利なサイトです。チュートリアルもあるので参考にしながらやってみてください。
![スクリーンショット 2025-01-23 222329](https://github.com/user-attachments/assets/0a1badfc-d099-4ace-8f01-92fa74bc101d)</br>
画像はペットボトルと缶のラベリング作業です。このように物体を囲んで、タグをつけています。単調作業ですがのちの制度に影響してくるので丁寧にラベリングしてください。その後は案内に従い、トレインを開始してください。トレインが終わったら画像を挿入して物体検出ができているか確認できます。</br>
それではデータを用いてウェイトを作成していきます。Roboflowからウェイトをダウングレードする方法がわからなかったのでプログラムでウェイトを作成していきます。
![スクリーンショット 2025-01-23 222420](https://github.com/user-attachments/assets/4d246c43-9a83-4b21-84ce-84456d1d2ba1)</br>
画像のように学習するモデルを選択し(今回の場合YOLO11)zipファイルをダウンロードします。Roboflowの良いところはここからzipをダウンロードすれば勝手にフォルダのディレクトリの配置をしてくれるのでプログラム時に便利です。
![スクリーンショット 2025-01-23 222507](https://github.com/user-attachments/assets/d30c9ec8-644e-46f5-9ce3-230ffd7716c5)</br>
zipフォルダを展開するとこのようになっています。READMEの2つはいらないので消してください。

# ウェイトの作成(Visual Studio Code)
VScodeでウェイトの作成を行っていきます。AIの学習にはGPUやNPUが必須になります。普通VScodeはCPUで動作するので機械学習がとても遅く、あまりこの方法はお勧めしません。一つの手段として目を通してください。
手順は公式のサイトを参考にします。[Ultralytics-Train](https://docs.ultralytics.com/modes/train/#usage-examples)</br>
先ほどの展開したフォルダをVScodeで開きます。次に使用方法でも記述したように仮想環境の構築からUltralyticsのインストールまで行ってください。YAMLファイルの変更をします。</br>

``` python
path: C:/Users/kusakabe/Desktop/test weights
train: C:/Users/kusakabe/Desktop/test weights/train
val: C:/Users/kusakabe/Desktop/test weights/valid
test: C:/Users/kusakabe/Desktop/test weights/test

names:
  0: can
  1: pet
```
すでにRoboflowによる文章がありますが置き換えて書いてください。それぞれパスの位置を個人で設定してください。namesも設定したいラベルに変更してください。ここで注意なのですがwindowsでパスをコピーするとスラッシュが\になっています。￥がバックスラッシュになるのが原因です。エラーが発生するのでスラッシュに書き換えてください。</br>
![スクリーンショット 2025-01-30 221915](https://github.com/user-attachments/assets/bb2289f8-72fc-4d65-9e16-11dd30e3cfda)</br>
次にプログラムを実行します。
``` python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt") 

results = model.train(data="data.yaml", epochs=100, imgsz=640)
```
- modelは使用するモデルを選択します。今回は最新のyolo11nを使用します。
- resultでは「YAMLファイルの選択」、「epochs(機械学習の回数)」、「画像サイズの選択」を設定しています。特に数値はいじらなくてもいいと思います。学習の回数は多ければいいというわけでもなく多すぎると過学習になってしまうので加減を見て設定してください。私は多くて300に設定しました。</br>
プログラムとYAMLファイルでエラー問題がなければこのような表示が出ます。</br>
![スクリーンショット 2025-01-30 222957](https://github.com/user-attachments/assets/4b835581-2821-4174-bfa6-ba5b21c4734a)</br>
なんの設定などもせずに行うとCPUで学習が始まります。ですがこれだとあまりにも遅いのでGPUが使えるGoogle Colabのやり方について説明します。

