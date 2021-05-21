#!/usr/bin/python3
""" this is an empty class that defines a rectangle """


class Rectangle:
    """creates base height and width of the rectangle
    Attributes
        number_of_instances: number of instanes
        print_symbol: symbol of #
    """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        result = str(self.print_symbol) * self.width
        return '\n'.join(list(result for i in range(self.height)))

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delete the square inputed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle
        Args:
            rect_1: the first rectangle input
            rect_2: the second rectangle input
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new square instance
        Args:
            size: size of square
        """
        return cls(size, size)
