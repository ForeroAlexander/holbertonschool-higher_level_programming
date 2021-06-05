#!/usr/bin/python3
""" This function add an attribute"""


def add_attribute(obj, attribute, value):
    """ Add an attribute"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
