import requests
import os
from pprint import pprint


class CheckUpdate:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def download_check_html(self):
        url = self.url
        path = self.path
        response = requests.get(url)
        if os.path.isfile(path):
            with open("new.html", "w") as new:
                new.write(response.text)
                print("new.html新規作成")
        else:
            with open(path, "w") as old:
                old.write(response.text)
                print("old.html新規作成")
                return True

        with open("new.html", "r") as new:
            with open(path, "r") as old:  # r+だとwriteした時に追記される
                if new.read() == old.read():
                    print("更新されていない(new == old)")
                    return False
        with open(path, "w") as old:
            old.write(response.text)
            print("更新されている(new != old)")
            return True
