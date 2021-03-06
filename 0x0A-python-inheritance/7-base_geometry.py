#!/usr/bin/python3
""" defines a geometry class """


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """ function that calculates the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks for validity an integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greather than 0".format(name))
