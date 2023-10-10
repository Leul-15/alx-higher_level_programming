#!/usr/bin/python3
"""add item"""


import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fn = "add_item.json"
if os.path.isfile(fn):
    ob = load_from_json_file(fn)
else:
    ob = []
ob.extend(sys.argv[1:])
save_to_json_file(ob, fn)
