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

    def update(self, *args, **kwargs):
        """Update the Square.
            Args:
            *args (ints):
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3th argument represents x attribute
                - 4th argument represents y attribute
            **kwargs arguments in dictionary format"""
        if args and len(args) != 0:
            args_number = len(args)
            if args_number == 0:
                return
            if args_number >= 1:
                self.id = args[0]
            if args_number >= 2:
                self.size = args[1]
            if args_number >= 3:
                self.x = args[2]
            if args_number >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id" and value is not None:
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
