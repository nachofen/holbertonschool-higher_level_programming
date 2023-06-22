#!/usr/bin/python3
"""task 11"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square using Rectangle"""

    def __init__(self, size):
        """Initialize a new square.

        Arg:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        """this line could be super() too but witout self as arg"""
        self.__size = size

    def area(self):
        """returns the square area"""
        return (self.__size * self.__size)

    def __str__(self):
        """returns the prints message"""
        return "[Square] {}/{}".format(self.__size, self.__size)
