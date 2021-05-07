#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    new.update((x, y * 2) for x, y in new.items())
    return new
