#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new = a_dictionary.copy()
        for x, y in new.items():
            y = y * 2
            new[x] = y
        return new
    return a_dictionary
