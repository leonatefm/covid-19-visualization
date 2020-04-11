import csv
import requests
import json

def split_data(input):
    output = []
    for key, value in input.items():
        if key != 'date':
            output.append({'date': input['date'], 'type':key, 'value': value})
    return output

def format_data(list):
    new_data_list = []
    for item in list:
        new_data_list += split_data(item)
    return new_data_list


# def format_world_aggregated(dict_list):
#     new_data_list = []
#     for dict in dict_list:
#         confirmed = {'date': dict['date'], 'type': 'confirmed', 'value': dict['confirmed']}
#         recovered = {'date': dict['date'], 'type': 'recovered', 'value': dict['recovered']}
#         deaths = {'date': dict['date'], 'type': 'confirmed', 'value': dict['confirmed']}
#         increase_rate = {'date': dict['date'], 'type': 'increase_rate', 'value': dict['increase_rate']}
#         new_data_list.append(confirmed)
#         new_data_list.append(recovered)
#         new_data_list.append(deaths)
#         new_data_list.append(increase_rate)
#     return new_data_list


def read_csv(csv_url):
    with requests.Session() as s:
        download = s.get(csv_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data_list = list(cr)
    return data_list


def write_json(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def file_path(filename):
    new_filepath = f'./src/data/{filename}.json'
    return new_filepath


def main():

    # download online csv file - world_aggregated dataset
    csv_url = 'https://pkgstore.datahub.io/core/covid-19/worldwide-aggregated_csv/data/8c5dc6c56dcbe2b467d1527a38fd0eeb/worldwide-aggregated_csv.csv'
    # print(f'world_aggregated dataset = {read_csv(csv_url)}')

    # format original data
    my_list = read_csv(csv_url)
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
    
    new_data = format_data(data_list)
    # print(format_data(data_list))
    # print(new_data)
 
    # write json file
    filename = 'world_aggregated'
    write_json(file_path(filename), new_data)



    # csv_url = 'https://pkgstore.datahub.io/core/covid-19/countries-aggregated_csv/data/04199d42a81a20a7f3f2088453dfd6c1/countries-aggregated_csv.csv'


if __name__ == '__main__':
    main()

