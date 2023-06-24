#!/usr/bin/python3
"""task 11- student to disk and reload
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """returns the dictionary description with simple data structure

        args:
        first_name: the first name of student
        last_name: the last name of student
         age: the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a student"""
        if isinstance(attrs, list):
            validator = 0
            for ele in attrs:
                if isinstance(ele, str):
                    continue
                else:
                    validator += 1
            if validator == 0:
                json_dict = {}
                for name in attrs:
                    if name in self.__dict__:
                        json_dict[name] = getattr(self, name)
                return json_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
