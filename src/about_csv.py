import pandas as pd
import os
import datetime
import requests
from requests import HTTPError


class AboutCsv:
    def __init__(self, url):
        self.url = url

    def download_csv(self):
        request = requests.get(self.url)
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

    def read_csv(self, csv_path):
        csv_lst = pd.read_csv(csv_path).values.tolist()
        program_language = list()
        program_rep = list()
        for i in range(20):
            program_language.append(csv_lst[i][0])
            program_rep.append(csv_lst[i][1])
        return program_language, program_rep
