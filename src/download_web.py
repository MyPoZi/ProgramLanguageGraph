import pandas as pd
import sys
import requests
import subprocess
import os
import datetime
from requests import HTTPError

import check_update
import data_storage
import config


def download_csv():
    url = 'http://namaristats.com/datatable.csv'
    request = requests.get(url)
    date = datetime.date.today().strftime('%Y%m%d')
    save_name = '/home/kit/python/data/' + 'lang' + date + '.csv'
    try:
        with open(save_name, 'wb') as f:
            f.write(request.content)
            print('csv_saved')
        return save_name
    except (OSError, HTTPError) as e:
        print('csv_ERROR:{0}'.format(e))
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
    check_html = check_update.CheckUpdate(config.check_url['url'], config.check_url['path'])
    if not check_html.download_check_html():  # true=>更新されているためcsvファイルを取ってくる処理に移行
        sys.exit()
    save_name = download_csv()
    program_language, program_rep = read_csv(save_name)
    database = data_storage.DataStorage(config.db_config['db_file_path'], config.db_config['db_path'])
    database.create_file()
    database.insert_in_database(program_language, program_rep)


if __name__ == '__main__':
    main()
