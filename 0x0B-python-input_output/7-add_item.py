#!/usr/bin/python3
"""adds all arguments to a Python list, and then save """


from sys import argv

save_to_json_file = __import__('5_save_to_json_file').save_to_json_file
load_from_json_file = __import__('6_load_from_json_file').load_from_json_file

try:
    elemens_list = load_from_json_file("add_item.json")
except:
    elemens_list = []

for elems in (argv[1:]):
    elemens_list.append(elems)
    save_to_json_file(elemens_list, "add_item.json")
