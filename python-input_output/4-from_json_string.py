#!/usr/bin/python3
"""Task 4- from JSON string to object"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON(string)"""
    my_obj = json.loads(my_str)
    return (my_obj)
