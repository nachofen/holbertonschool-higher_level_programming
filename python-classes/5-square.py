#!/usr/bin/python3
"""
This is the "Square with size validation"  module.

This module provides a Square class with size attribute
wich needs to be validated and add def area.
"""


class Square:
    """ a class that defines a square with size as arg"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
