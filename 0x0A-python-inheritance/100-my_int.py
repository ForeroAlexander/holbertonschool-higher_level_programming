#!/usr/bin/python3
""" module mu_int"""


class MyInt(int):
    """subclass"""
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x != other

    def __ne__(self, other):
        return self.x == other
