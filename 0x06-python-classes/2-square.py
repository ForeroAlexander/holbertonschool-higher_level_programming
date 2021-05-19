#!/usr/bin/python3
"""Define a class as square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initialize a square
        Args:
            size (int): size of a side of the square
        Returns:
        None"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be positive")
        else:
                self.__size = size
