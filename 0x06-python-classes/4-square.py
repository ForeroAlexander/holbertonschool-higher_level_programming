#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initialize a square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculate the area of the square
        Returns:
            The area of the square
        """

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): The size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be positive")
            else:
                self.__size = value
