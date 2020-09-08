#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = sorted(my_list)
    prev = 0
    sum = 0
    for i in new:
        if i == prev:
            continue
        else:
            sum = sum + i
            prev = i
    return sum
