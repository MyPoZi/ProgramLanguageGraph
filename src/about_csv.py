import pandas as pd
import os
import datetime
import requests
import sys
from requests import HTTPError


class AboutCsv:
    def __init__(self, csv_url, csv_path):
        self.csv_url = csv_url
        self.csv_path = csv_path

    def mkdir_csv(self):
        file_path = os.path.dirname(self.csv_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print("ディレクトリ作成:{0}".format(file_path))

    def download_csv(self):
        request = requests.get(self.csv_url)
        date = datetime.date.today().strftime('%Y%m%d')
        save_name = '/home/kit/python/csv/' + 'lang' + date + '.csv'
        try:
            with open(save_name, 'wb') as f:
                f.write(request.content)
                print('csv_saved')
            return save_name
        except (OSError, HTTPError) as e:
            print('csv_ERROR:{0}'.format(e))
            sys.exit()

    @staticmethod
    def read_csv(csv_path):
        csv_lst = pd.read_csv(csv_path).values.tolist()
        program_language = list()
        program_rep = list()
        for i in range(20):
            program_language.append(csv_lst[i][0])
            program_rep.append(csv_lst[i][1])
        return program_language, program_rep
