#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list[:]
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        for i in range(0, len(new)):
            if idx == i:
                new[i] = element
                return new
        return my_list
