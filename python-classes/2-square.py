#!/usr/bin/python3
"""
This is the "Square with size validation"  module.

This module provides a Square class with size attribute
and needs to be validated.
"""


class Square:
    """ a class that defines a square with size as arg"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must b >= 0")
        self.__size = size
