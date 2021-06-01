#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """ Read a file UFT-8 """
    with open(filename, 'r') as f:
        print(f.read(), end="")
