#!/usr/bin/python3
"""task 7"""


class BaseGeometry:
    """Basegeometry class"""

    def area(self):
        """def area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """def integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
