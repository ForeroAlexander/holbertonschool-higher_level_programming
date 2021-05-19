#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ class square with constuctor method"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size: size of a side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size**2

    def my_print(self):
        """ 
        prints the square checking position
        """

    if self.size == 0:
        print("")
    else:
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" "* self.__position[0], end="")
            for i in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        """
        getter function of position
        Returns:
            position of the square
        """

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        getter function of size
        Returns:
            size of the square
        """

    @size.setter
    def size(self, value):
        """setter function of attribute size
        Args:
            value: value for __size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val