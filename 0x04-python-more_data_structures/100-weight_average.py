#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        result_1 = 0
        result_2 = 0
        for i in my_list:
            x, y = i
            result_1 = result_1 + (x * y)
            result_2 = result_2 + y
        total = result_1/result_2
        return total
    return 0
