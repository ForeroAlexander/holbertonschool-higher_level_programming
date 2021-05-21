#!/usr/bin/python3
""" This is an empty class that defines a rectangle"""


class Rectangle:
    """docstring for a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize of a rectangle
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
        """property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value: size of width
        Raises:
            TypeError: if value is not an integer
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
        TypeError: when value is not an integer
        ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
