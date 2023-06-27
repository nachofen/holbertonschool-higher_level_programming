#!/usr/bin/python3
""" Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """new square constructor
        Args:
            size (int): The size of the new square.
            x (int): The x coordinate of the new square.
            y (int): The y coordinate of the new square.
            id (int): The identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """get and set for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
