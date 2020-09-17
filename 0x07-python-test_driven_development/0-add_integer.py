#!/usr/bin/python3
"""
    0-add_integer.py
    Module defining add integer
    return result (a + b)
"""


def add_integer(a, b = 98):
    """Adding a + b """
    if not a:
        raise TypeError("a must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return int(a + b)
