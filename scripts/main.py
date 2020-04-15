import json
from datapackage import Package
from pathlib import Path

def get_resource(package, resource_name):
    resource = package.get_resource(resource_name);
    resource_data = resource.read(keyed=True)
    return resource_data

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

def format_countries_data(list):
    output = []
    for item in list:
        output.append({'date': str(item['Date']), 'country': item['Country'], 'confirmed': item['Confirmed'], 'recovered': item['Recovered'], 'deaths': item['Deaths']})
    return output   

def lower_key_countries_data(input):
    output_list = []
    output = {}
    for key, val in input.items():
        if key == "Date":
            output[key.lower()] = str(val)
        else:
            output[key.lower()] = val
    output_list.append(output)
    return output_list

def format_key_countries_data(list):
    new_data_list = []
    for item in list:
        new_data_list += lower_key_countries_data(item)
    return new_data_list

def file_path(filename):
    rootPath = Path(__file__).parents[1]
    targetDir = rootPath.joinpath('src/data')
    filepath = f'{targetDir}/{filename}.json'
    return filepath

def write_json(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def main():
    package = Package('https://datahub.io/core/covid-19/datapackage.json')
 
    # worldwide aggregated data
    resource_name = 'worldwide-aggregated_csv'  
    worldwide_aggregated = get_resource(package, resource_name)
    
    format_worldwide_data = format_data(worldwide_aggregated)
   
    filename = 'world_aggregated'
    write_json(file_path(filename), format_worldwide_data)
   
    # countries aggregated data
    resource_name = 'countries-aggregated_csv'
    countries_aggregated = get_resource(package, resource_name)

    format_countries_aggregated = format_countries_data(countries_aggregated)
    
    filename = 'countries-aggregated'
    write_json(file_path(filename), format_countries_aggregated)

    # Key Countries
    resource_name = 'key-countries-pivoted_csv'
    key_countries = get_resource(package, resource_name)
    
    format_key_countries = format_key_countries_data(key_countries)

    filename = 'key_countries'
    write_json(file_path(filename), format_key_countries)

    # US confirmed
    # resource_name = 'us_confirmed_csv'
    # us_confirmed = get_resource(package, resource_name)
    # print(us_confirmed)








    # print(package.resource_names)   # print list of all resources
    # # print(json.dumps(package.descriptor, indent=2))
if __name__ == '__main__':
    main()

