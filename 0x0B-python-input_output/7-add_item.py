#!/usr/bin/python3
import json
import sys

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)

    def load_from_json_file(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)

    arg_list = load_from_json_file('add_item.json') if sys.path.isfile('add_item.json') else []
    arg_list.extend(sys.argv[1:])
    save_to_json_file(arg_list, 'add_item.json')
