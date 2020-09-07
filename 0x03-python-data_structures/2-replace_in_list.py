#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        for i in range(0, len(my_list)):
            if idx == i:
                my_list[i] = element
                return my_list
        return my_list
