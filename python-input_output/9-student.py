#!/usr/bin/python3
"""task 9- student to json
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

    def to_json(self):
        return self.__dict__
