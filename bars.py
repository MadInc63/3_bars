import json
import sys
from math import sqrt


def load_data(filepath):
    try:
        with open(filepath, 'r') as json_file:
            json_data = json.loads(json_file.read())
#            get_biggest_bar(json_data)
#            get_smallest_bar(json_data)
            longitude = 37
            latitude = 55
            get_closest_bar(json_data, longitude, latitude)
    except IOError:
        print('No such file or directory')
    except ValueError:
        print('File is empty')


def get_biggest_bar(json_data):
    print(max(json_data['features'], key=lambda count:count['properties']['Attributes']['SeatsCount']))

def get_smallest_bar(json_data):
    print(min(json_data['features'], key=lambda count:count['properties']['Attributes']['SeatsCount']))

def get_closest_bar(json_data, longitude, latitude):

    for bars in json_data['features']:
        bar_longitude = bars['geometry']['coordinates'][0]
        bar_latitude = bars['geometry']['coordinates'][1]
        print(sqrt((bar_longitude-longitude)**2 + (bar_latitude-latitude)**2))

if __name__ == '__main__':
    load_data('bars.json')
#    load_data(sys.argv[1])
