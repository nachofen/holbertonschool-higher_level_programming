#!/usr/bin/python3
"""Base class"""
import json
import os


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
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        my_list = []
        if json_string is None or len(json_string) < 1:
            return my_list
        else:
            return json.loads(json_string)
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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_square = cls(**dictionary)
        dummy_square.__dict__.update(**dictionary)
        return dummy_square
    
    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        file_name = cls.__name__ + ".json"
        if os.path.exists(file_name):
            ins_list = []
            with open(file_name) as file:
                my_dict = cls.from_json_string(file.read())
                for dicts in my_dict:
                    ins_list.append(cls.create(**dicts))
            return ins_list
        else:
            return []