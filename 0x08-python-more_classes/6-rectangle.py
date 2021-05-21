#!/usr/bin/python3
""" This is an empty class that defines a rectangle"""


class Rectangle:
    """ Represents a rectangle
    Attribute:
        __width (int)
        __height (int)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize a rectangle
        Args:
            widt (int)
            height (int)
        """
        self.__width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        string = "{}".format(
            '\n'.join(['#' * self.__width for row in range(0, self.__height)]))
        return string

    def __repr__(self):
        return (
            "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            Value : width of the rectangle
        Returns:
            None
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    # get method
    @property
    def height(self):
        """ getter of __height
        Returns the height of a rectangle
        """
        return self.__height

    # set method
    @height.setter
    def height(self, value):
        """ setter of __height
        Args:
            Value: height of the rectangle
        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns Rectangles Area """
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
