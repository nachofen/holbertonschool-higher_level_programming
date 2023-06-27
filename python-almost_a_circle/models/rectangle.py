#!/usr/bin/python3
""" Rectangle """


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """new rectangle constructor
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get and set for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get and set for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get and set for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get and set for x"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """display the rectangle with #"""
        char = "#"
        for xs in range(self.y):
            print()
        for col in range(self.height):
            for spaces in range(self.x):
                print(" ", end="")
            for row in range(self.width):
                print("{}".format(char), end="")
            print()

    def __str__(self):
        """overriding __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints):
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs arguments in dictionary format"""
        if args and len(args) != 0:
            args_number = len(args)
            if args_number == 0:
                return
            if args_number >= 1:
                self.id = args[0]
            if args_number >= 2:
                self.width = args[1]
            if args_number >= 3:
                self.height = args[2]
            if args_number >= 4:
                self.x = args[3]
            if args_number >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id" and value is not None:
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
