#!/usr/bin/python3
'''
defining task 5 and 6 functions
'''
import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file
arglist = list(sys.argv[1:])
try:
    load_data = load_from_json_file('add_item.json')
except Exception:
    load_data = []

load_data.extend(arglist)
save_to_json_file(load_data, 'add_item.json')
