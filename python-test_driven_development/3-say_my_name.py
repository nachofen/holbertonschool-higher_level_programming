#!/usr/bin/python3
"""
shebang
"""


def say_my_name(first_name, last_name=""):
    """Print My name is (first) (last) if given, else print error.
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
