#!/usr/bin/python3
"""
    4-square.py
    Module that defines a Square with getter and setter
"""


class Square():
    """This is An Square Class Based On The
    Square Class"""
    def __init__(self, size=0):
        """This is init function of this Class
        that sets the Value of size"""
        self.size = size

    @property
    def size(self):
        """Gets The Value Of The __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets The Value Of The private size Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print out the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
