#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) or idx < 0:
        return None
    else:
        for i in range(0, len(my_list)):
            if idx == i:
                return my_list[i]
        return None
