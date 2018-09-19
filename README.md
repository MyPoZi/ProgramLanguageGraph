ProgramLanguageGraph
====

- [@here -> ココ!](http://namaristats.com/datatable)から毎日csvファイルをダウンロードして上位20言語とリポジトリ数データベースに格納するプログラム　

## Demo


## Requirement
Docker 18.06.1-ce  

## Usage

データベース表示方法

`$ docker start language-python && docker attach language-python`  

`$ cd /home/kit/python/db && sqlite3 language.db`  
`> select * from language;`  

ボリュームの場所を確認  
`$ docker inspect language-data`

## Install
`$ git clone https://github.com/MyPoZi/ProgramLanguageGraph`  

`$ cd ProgramLanguageGraph`  

`$ docker build -t language-python:3.6 .`  

`$ docker run -it --name "language-python" -v language-data:/home/kit/python language-python:3.6 /bin/bash`  

毎日16時に実行  
```
$ crontab -e  
0 16 * * * docker start language-python && docker exec language-python python3 /home/kit/python/src/download_web.py && docker stop language-python  
```
再起動してもコンテナが自動で建てられ、スクリプトを実行し、コンテナを止めるので、建てたままよりサーバーリソースに優しいと思う  

## Unstall

`$ docker rm language-python`  

`$ docker rmi language-python:3.6`  

※python3.6のイメージを消したい場合  
`$ docker rmi python:3.6`  

データ永続化のためのボリュームを削除(language-pythonで使ったデータベースとcsvファイルとsrcを削除)  
`$ docker volume rm language-data`  

最後にcronを消去  

## Licence

[MIT]()

## Author

[MyPoZi](https://github.com/mypozi)
  

- [x] データベース作成自動化完成:tada:
```
$ crontab -e  
0 */8 * * * python3 /home/kit/python/src/download_web.py  
```
8時間ごとにホームページが更新されていないか確認し、更新されていればcsvファイルを取ってきて、上位20言語とリポジトリ数をデータベースに格納する  
cronするときはconfig.pyなど全てのパスを絶対パスで書かなければならない  

httpレスポンスヘッダのlast-modifiedを使ってバリデートする方法もある

グラフ表示  

`$ sudo yum install tkinter`  
`$ sudo yum install python36u-tkinter`  
