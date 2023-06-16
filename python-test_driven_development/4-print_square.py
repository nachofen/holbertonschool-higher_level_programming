#!/usr/bin/python3
"""
shebang
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    char = "#"
    for col in range(size):
        for row in range(size):
            print("{}".format(char), end="")
        print()
