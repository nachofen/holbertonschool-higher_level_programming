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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                file.write(Base.to_json_string(dict_list))
