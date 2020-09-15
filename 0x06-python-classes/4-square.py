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
    def __init__(self, size=0):
        """this is an constructor for the class Square. 
        """
        self.size = size
    @property
    def size(self):
        """Get the private size value """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the value of the private size based on given conditions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """find the area of the square"""
        return self.__size * self.__size
