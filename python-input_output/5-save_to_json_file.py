#!/usr/bin/python3
"""Task 5- save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
