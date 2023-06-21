#!/usr/bin/python3
"""task 4"""


def inherits_from(obj, a_class):
    """define inherits_from"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
