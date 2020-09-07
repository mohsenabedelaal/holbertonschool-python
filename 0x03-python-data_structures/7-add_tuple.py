#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a1 = 0
        a2 = 0
    elif len(tuple_a) < 2 and len(tuple_a) > 0:
        a1 = tuple_a[0]
        a2 = 0
    elif len(tuple_a) >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    if len(tuple_b) == 0:
        b1 = 0
        b2 = 0
    elif len(tuple_b) < 2 and len(tuple_a) > 0:
        b1 = tuple_b[0]
        b2 = 0
    elif len(tuple_b) >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    return (a1+b1, a2+b2)
