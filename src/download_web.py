import datetime
import pandas as pd
import sys
import sqlite3
import requests
from requests import HTTPError

dbpath = '/home/kit/python/db/language.db'


def insert_in_database(language, rep):
    date = datetime.date.today().strftime("%Y/%m/%d")

    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()
    for (l, r) in zip(language, rep):
        sql = 'INSERT INTO LANGUAGE (time, language, value) values (?,?,?)'
        value = (date, l, r)
        try:
            cursor.execute(sql, value)

        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

    connection.commit()
    connection.close()


def download_csv():
    url = "http://namaristats.com/datatable.csv"
    request = requests.get(url)
    date = datetime.date.today().strftime("%Y%m%d")
    save_name = "/home/kit/python/data/"+"lang" + date + ".csv"
    try:
        with open(save_name, "wb") as f:
            f.write(request.content)
            print("saved")
        return save_name
    except (OSError, HTTPError) as e:
        print("ERROR")
        sys.exit()


def read_csv(data):
    csv_lst = pd.read_csv(data).values.tolist()
    program_language = list()
    program_rep = list()

    for i in range(20):
        program_language.append(csv_lst[i][0])
        program_rep.append(csv_lst[i][1])
    return program_language, program_rep


def main():
    save_name = download_csv()
    program_language, program_rep = read_csv(save_name)
    insert_in_database(program_language, program_rep)


if __name__ == '__main__':
    main()
