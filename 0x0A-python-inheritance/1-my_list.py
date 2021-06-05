#!/usr/bin/python3
"""class defining list """


class MyList(list):
    """function to print a sorted list """

    def print_sorted(self):
        """ prints a list sorted"""
        print(sorted(self))
