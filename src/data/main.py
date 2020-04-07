import csv
import requests
import json

csv_url = 'https://pkgstore.datahub.io/core/covid-19/worldwide-aggregated_csv/data/8c5dc6c56dcbe2b467d1527a38fd0eeb/worldwide-aggregated_csv.csv'

with requests.Session() as s:
    download = s.get(csv_url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    my_list = list(cr)
    # for row in my_list:
    #     print(row)
    # print(my_list)

def write_json(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def file_path(filename):
    new_filepath = f'./src/data/{filename}.json'
    return new_filepath


def main():
    filename = 'world_aggregated'
    write_json(file_path(filename), my_list)



if __name__ == '__main__':
    main()

