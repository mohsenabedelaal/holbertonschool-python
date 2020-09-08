#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = ""
        max_value = 0
        for x, y in a_dictionary.items():
            if y >= max_value:
                max_value = y
                max = x
        return max
    return None
