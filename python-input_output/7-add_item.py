#!/usr/bin/python3
"""Task 7- load, add ,save"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    loadfrom_jsonfile = __import__("6-load_from_json_file").load_from_json_file
    try:
        items = loadfrom_jsonfile("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
