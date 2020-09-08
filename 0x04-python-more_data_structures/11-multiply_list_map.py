#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list and number is not None:
        new = my_list[:]
        new = list(map((lambda x: x*number), new))
        return new
    return my_list
