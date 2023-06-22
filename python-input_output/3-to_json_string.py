#!/usr/bin/python3
"""Task 3- to JSON string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object(string)"""
    my_json_obj = json.dumps(my_obj)
    return (my_json_obj)
