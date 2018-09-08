import sys

import check_update
import about_csv
import data_storage
import config


def main():
    check_html = check_update.CheckUpdate(config.check_url['url'], config.check_url['path'])
    if not check_html.download_check_html():  # true=>更新されているためcsvファイルを取ってくる処理に移行
        sys.exit()
    csv = about_csv.AboutCsv(config.download_csv['url'])
    csv_path = csv.download_csv()
    program_language, program_rep = csv.read_csv(csv_path)
    database = data_storage.DataStorage(config.db_config['db_file_path'], config.db_config['db_path'])
    database.create_file()
    database.insert_in_database(program_language, program_rep)


if __name__ == '__main__':
    main()
