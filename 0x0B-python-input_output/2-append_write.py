#!/usr/bin/python3
""" This function appends a file"""


def append_write(filename="", text=""):
    """ append to file"""
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
