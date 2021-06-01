#!/usr/bin/python3
"""This is a class. I am braindead"""


class Student:
    """This is the student class"""

    def __init__(self, first_name, last_name, age):
        """this inits the class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this returns teh dict"""
        return self.__dict__
