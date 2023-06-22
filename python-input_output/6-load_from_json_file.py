#!/usr/bin/python3
"""Task 6- create an object from json file"""
import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename) as file:
        return json.load(file)
