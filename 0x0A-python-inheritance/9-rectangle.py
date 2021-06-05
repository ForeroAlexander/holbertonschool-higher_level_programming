#!/usr/bin/python3
""" module Rectangle class that inherits from
    class Base Geometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a rectangle """

    def __init__(self, width, height):
        """ initializes a rectangle method and validate
        if its arguments are positive integer """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns the print() and str() representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    