#!/usr/bin/python3
"""
This is the "Rectangle with width and height validation"  module.
"""


class Rectangle:
    """ a class that defines a rectangle with width and height as args"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1 

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.width * self.height
        return(area)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            peri = 0
            return peri
        peri = (self.width * 2) + (self.height * 2)
        return (peri)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width
            rectangle_str += "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1
