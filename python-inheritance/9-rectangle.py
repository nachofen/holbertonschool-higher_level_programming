#!/usr/bin/python3
"""task 9"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """constructor for new rectangle
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the prints message"""
        return "[Rectangle] {}/{}>".format(self.__width, self.__height)
