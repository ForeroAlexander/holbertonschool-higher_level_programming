#!/usr/bin/python3
"""Write a class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherited from BaseGeometry """
    def __init__(self, width, height):
        """ initialize the Rectangle """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
