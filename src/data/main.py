import csv
import requests
import json

def write_json(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, indent=2)



def file_path(filename):
    new_filepath = f'./src/data/{filename}.json'
    return new_filepath



def main():

    csv_url = 'https://pkgstore.datahub.io/core/covid-19/worldwide-aggregated_csv/data/8c5dc6c56dcbe2b467d1527a38fd0eeb/worldwide-aggregated_csv.csv'

    with requests.Session() as s:
        download = s.get(csv_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    my_list = list(cr)
    my_list[0] = ['date', 'confirmed', 'recovered', 'deaths', 'increase_rate']

    data_list = []
    for i, row in enumerate(my_list):
        if i == 0:
            labels = row
        else:
            each_day_data = {}
            for j, value in enumerate(row):
                each_day_data[labels[j]] = value
            data_list.append(each_day_data)


    filename = 'world_aggregated'
    write_json(file_path(filename), data_list)



if __name__ == '__main__':
    main()

