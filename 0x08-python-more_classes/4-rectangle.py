#!/usr/bin/python3
""" this is an empty class that defines a rectangle """


class Rectangle:
    """ docstring for Rentangle """

    def __init__(self, width=0, height=0):
        """Institation of rectangle
        Args:
            width: size of width
            height: size of height
        Attributes:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value: size of width
        Raises:
            TypeError: when value is not an int
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value: size of height
        Raises:
            TypeError: when value is not an int
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """gets the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """return string of rectangles with #"""
        if self.width == 0 or self.height == 0:
            return ""
        result = '#' * self.width
        return '\n'.join(list(result for i in range(self.height)))

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
