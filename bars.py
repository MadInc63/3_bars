import json
import argparse
from math import sqrt


def load_data(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)


def get_biggest_bar(json_data):
    return max(json_data['features'], key=lambda count:
               count['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data['features'], key=lambda count:
               count['properties']['Attributes']['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    return (min(json_data['features'], key=lambda bar: sqrt(
                (float(longitude)-bar['geometry']['coordinates'][0])**2 +
                (float(latitude)-bar['geometry']['coordinates'][1])**2)))


def print_bar_info(bar):
    print('Bar name: {name}\nAddress: {address}'
          .format(name=bar['properties']['Attributes']['Name'],
                  address=bar['properties']['Attributes']['Address']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str,
                        help='path to file JSON format')
    args = parser.parse_args()
    print_bar_info(get_biggest_bar(load_data(args.path)))

#    try:
#        file_to_path = sys.argv[1]
#        bars_list = load_data(file_to_path)
#        print_bar_info(get_biggest_bar(bars_list))
#        print_bar_info(get_smallest_bar(bars_list))
#        print_bar_info(get_closest_bar(bars_list, sys.argv[3], sys.argv[4]))
#    except IndexError:
#        print("You must enter a path to data file.")
#    except OSError:
#        print("{} - File not found.".format(sys.argv[1]))
#    except ValueError:
#        print("You must enter valid coordinates values.")
