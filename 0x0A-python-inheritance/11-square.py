#!/usr/bin/python3
""" module square """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ subclass square """
    def __init__(self, size):
        """ initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ the string return from class rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
