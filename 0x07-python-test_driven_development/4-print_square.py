#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """function that prints a square with the character"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
