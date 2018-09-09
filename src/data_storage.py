import datetime
import sqlite3
import os


class DataStorage:
    def __init__(self, db_file_path, db_path):
        self.db_file_path = db_file_path
        self.db_path = db_path

    def mkdir_db(self):
        filename = self.db_path
        file_path = os.path.dirname(filename)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print("ディレクトリ作成:{0}".format(file_path))

    def insert_in_database(self, language, rep):
        date = datetime.date.today().strftime("%Y/%m/%d")

        connection = sqlite3.connect(self.db_path)  # ファイルがすでに存在するときはファイルを開く。ファイルがないときは新しいデータベースを作成する。
        cursor = connection.cursor()
        for (l, r) in zip(language, rep):
            sql = 'INSERT INTO LANGUAGE (date, language, value) values (?,?,?)'
            value = (date, l, r)
            try:
                cursor.execute('CREATE TABLE IF NOT EXISTS LANGUAGE (date text, language text, value integer)')
                cursor.execute(sql, value)

            except sqlite3.Error as e:
                print('sqlite3.Error occurred:', e.args[0])

        connection.commit()
        connection.close()
