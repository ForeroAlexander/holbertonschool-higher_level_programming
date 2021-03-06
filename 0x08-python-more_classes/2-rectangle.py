#!/usr/bin/python3
""" This is an empty class that defines a rectangle"""


class Rectangle:
    """ docstring for a rectangle
    Attributes:
        __width (int)
        __heihgt (int)
    """

    def __init__(self, width=0, height=0):
        """ initialize rectangle
        Args:
            width(int)
            height(int)
        """
        self.height = height
        self.width = width

    # get method
    @property
    def width(self):
        """ getter of __width
        Returns the width of the rectangle
        """
        return self.__width

    # set method
    @width.setter
    def width(self, value):
        """ setter of __width
        Args:
            value: width of the rectangle
        Returns:
            None
        """
        if value < 0:
            raise ValueError(" width must be >= 0")
        if not isinstance(value, int,):
            raise TypeError("width must be an integer")
        self.__width = value

    # get method
    @property
    def height(self):
        """ getter of height
        Returns the height of the rectangle
        """
        return self.__height

    # set method
    @height.setter
    def height(self, value):
        """ setter of height
        Args:
            Value: The height of the rectangle
        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width)*2
