#!/usr/bin/python3
"""
This is the "Square with size validation"  module.

This module provides a Square class with size attribute
wich needs to be validated and add def area.
"""


class Square:
    """ a class that defines a square with size as arg"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @size.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        spaces = " " * self.__position[0]
        for i in range(self.size):
            print("{}".format(spaces), end="")
            for j in range(self.size):
                print("#", end="")
            print()
