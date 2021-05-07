#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    j = 0
    for item in new:
        if item == search:
            new[j] = replace
        j += 1
    return new
