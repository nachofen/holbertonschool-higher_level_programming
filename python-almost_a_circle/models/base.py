#!/usr/bin/python3
"""Base class"""


Class base:
    """represents base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor
        arg: id(int)
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
