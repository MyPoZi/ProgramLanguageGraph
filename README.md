ProgramLanguageGraph
====

Overview

- [@here -> ココ!](http://namaristats.com/datatable)から毎日csvファイルをダウンロードして上位20言語とリポジトリ数データベースに格納するプログラム　

## Demo


## Requirement
Docker 18.06.1-ce  

## Usage

## Install
`$ git clone https://github.com/MyPoZi/ProgramLanguageGraph`  

`$ docker build -t language-python:3.6 .`  


cron  
`$ docker run -it --name "language-python" language-python:3.6 bin/bash`  
まだかけてない

## Licence

[MIT]()

## Author

[MyPoZi](https://github.com/mypozi)
  
なぜ  
`* * * * * wget -qO foo- "date +\%Y\%m\%d\%H\%M\%S\".html http://www.example.jp/`  
ではないのか(\`\`の都合で""に)  
pythonで書いたほうがダウンロード出来なかった場合の例外処理が書きやすく、cronも.pyの指定だけでいいため?  

- [x] データベース作成自動化完成:tada:
```
$ crontab -e  
0 */8 * * * python3 /home/kit/python/src/download_web.py  
```
8時間ごとにホームページが更新されていないか確認し、更新されていればcsvファイルを取ってきて、上位20言語とリポジトリ数をデータベースに格納する  
cronするときはconfig.pyなど全てのパスを絶対パスで書かなければならない

グラフ表示  

`$ sudo yum install tkinter`  
`$ sudo yum install python36u-tkinter`  
