import urllib.request
import datetime

def download():
    url = "http://namaristats.com/datatable.csv"
    date = datetime.date.today().strftime("%Y%m%d")
    savename = "lang" + date + ".csv"
    print(savename)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', headers["User-Agent"])]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, savename)

if __name__ == '__main__':
    download()