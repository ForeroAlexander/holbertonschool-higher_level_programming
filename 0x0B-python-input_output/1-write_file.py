#!/usr/bin/python3
""" writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """write a files"""
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
