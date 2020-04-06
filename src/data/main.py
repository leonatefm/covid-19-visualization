# from datapackage import Package

# package = Package('https://datahub.io/core/covid-19/datapackage.json')

# # print list of all resources:
# print(package.resource_names)

# # print processed tabular data (if exists any)
# for resource in list:
#     if resource.descriptor['datahub']['type'] == 'derived/csv':
#         print(resource.read())

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
    print(my_list)

def write_json(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

filepath = 'world_aggregated.json'
write_json(filepath, my_list)