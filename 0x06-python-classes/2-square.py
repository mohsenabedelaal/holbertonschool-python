#!/usr/bin/python3
"""
    0-square.py
    Module defining square
    return {}
"""


class Square:
    """Square class.
       It defines a square and returns an empty block.
    """
    def __init__(self, size = 0):
        if isinstance(size, int) and size > 0:
            self.size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
