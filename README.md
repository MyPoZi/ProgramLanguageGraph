# ProgramLanguageGraph

なぜ  
`* * * * * wget -qO foo- "date +\%Y\%m\%d\%H\%M\%S\".html http://www.example.jp/`  
ではないのか(\`\`の都合で""に)

pythonで書いたほうがダウンロード出来なかった場合の例外処理が書きやすく、cronも.pyの指定だけでいいため?  

`$ sqlite3 language.db`  
`create table language(date text, language text, value integer);`  

`$ crontab -e`  
`0 3 * * * python3 /home/kit/python/src/download_web.py`  

毎日午前3時にcsvファイルを取ってきて、上位20言語とリポジトリ数をデータベースに格納する
cronするときは絶対パスで書かなければならない

グラフ表示  

`sudo yum install tkinter`  
`sudo yum install python36u-tkinter`  
