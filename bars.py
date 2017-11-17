import json
import sys
from math import sqrt


def load_from_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            result_of_load = json.loads(json_file.read())
    except IOError:
        print('No such file or directory')
    except ValueError:
        print('File is empty')
    else:
        return result_of_load


def get_biggest_bar(json_data):
    print(max(json_data['features'], key=lambda count:
          count['properties']['Attributes']['SeatsCount']))


def get_smallest_bar(json_data):
    print(min(json_data['features'], key=lambda count:
          count['properties']['Attributes']['SeatsCount']))


def get_closest_bar(json_data, my_place_longitude, my_place_latitude):
    for bars in json_data['features']:
        bar_longitude = bars['geometry']['coordinates'][0]
        bar_latitude = bars['geometry']['coordinates'][1]
        distance_from_my_place = (sqrt((bar_longitude -
                                        float(my_place_longitude))**2 +
                                       (bar_latitude -
                                        float(my_place_latitude))**2))
        bars['geometry'].update({'distance_from_me': distance_from_my_place})
    print(min(json_data['features'], key=lambda count:
          count['geometry']['distance_from_me']))


if __name__ == '__main__':
    if sys.argv[1] == 'max':
        get_biggest_bar(load_from_json_file(sys.argv[2]))
    elif sys.argv[1] == 'min':
        get_smallest_bar(load_from_json_file(sys.argv[2]))
    elif sys.argv[1] == 'closest':
        get_closest_bar(load_from_json_file(sys.argv[4]),
                        sys.argv[2], sys.argv[3])
