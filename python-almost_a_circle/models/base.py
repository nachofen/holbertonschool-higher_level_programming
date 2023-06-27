#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """represents base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor
        arg: id(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
