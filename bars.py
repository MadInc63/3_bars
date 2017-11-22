import json
import argparse
from math import sqrt


def creat_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='path to file JSON format')
    subparsers = parser.add_subparsers(dest='command')
    biggest_parser = subparsers.add_parser('biggest')
    smallest_parser = subparsers.add_parser('smallest')
    closest_parser = subparsers.add_parser('closest')
    closest_parser.add_argument('longitude', help='my place longitude')
    closest_parser.add_argument('latitude', help='my place latitude')
    return parser.parse_args()


def load_data(file_path):
    with open(file_path, 'r', encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        return json_data


def get_biggest_bar(json_data):
    return max(json_data['features'], key=lambda count:
               count['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data['features'], key=lambda count:
               count['properties']['Attributes']['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    return min(json_data['features'], key=lambda bar: sqrt(
               (float(longitude)-bar['geometry']['coordinates'][0])**2 +
               (float(latitude)-bar['geometry']['coordinates'][1])**2))


def print_bar_info(bar):
    print('Bar name: {name}\nAddress: {address}'
          .format(name=bar['properties']['Attributes']['Name'],
                  address=bar['properties']['Attributes']['Address']))


if __name__ == '__main__':
    path_to_file = creat_parser().path
    bars_dict = load_data(path_to_file)
    if creat_parser().command == 'biggest':
        print_bar_info(get_biggest_bar(bars_dict))
    elif creat_parser().command == 'smallest':
        print_bar_info(get_smallest_bar(bars_dict))
    elif creat_parser().command == 'closest':
        print_bar_info(get_closest_bar(bars_dict, creat_parser().longitude,
                                       creat_parser().latitude))
