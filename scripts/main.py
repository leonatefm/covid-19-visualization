import json
from datapackage import Package
from pathlib import Path

def get_package(package_name):
    package = Package('https://datahub.io/core/covid-19/datapackage.json')
    package = package.get_resource(package_name);
    package_data = package.read(keyed=True)
    return package_data


def split_data(input):
    output = []
    for key, value in input.items():
        if key != 'Date' and key != 'Increase rate':
            output.append({'date': str(input['Date']), 'type':key.lower(), 'value': value})
    return output


def format_data(list):
    new_data_list = []
    for item in list:
        new_data_list += split_data(item)
    return new_data_list


def write_json(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def file_path(filename):
    rootPath = Path(__file__).parents[1]
    targetDir = rootPath.joinpath('src/data')
    filepath = f'{targetDir}/{filename}.json'
    return filepath



def main():
    # package = Package('https://datahub.io/core/covid-19/datapackage.json')
    # print list of all resources:
    # print(package.resource_names)
  
    package_name = 'worldwide-aggregated_csv'
    worldwide_aggregated = get_package(package_name)
    # print(worldwide_aggregated)
    
    format_worldwide_data = format_data(worldwide_aggregated)
   
    filename = 'world_aggregated'
    write_json(file_path(filename), format_worldwide_data)
   
    


if __name__ == '__main__':
    main()

