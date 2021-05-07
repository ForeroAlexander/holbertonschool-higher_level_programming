#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    new = a_dictionary.copy()
    for x, y in a_dictionary.items():
        if isinstance(y, int) is False:
            del new[x]
    if new is None:
        return None
    a = sorted(new, key=new.get)
    return a[-1]
