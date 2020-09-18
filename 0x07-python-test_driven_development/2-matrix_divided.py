#!/usr/bin/python3
"""
    2-matrix_divided.py
    Module defining matrix with divided number
    return divided list elements
"""


def matrix_divided(matrix, div):
    """Each element will be divided with the given number div """
    if not matrix :
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    result = []
    prev = None
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i in matrix:
            temp = []
            if not isinstance(i, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if prev is None:
                prev = i
            if len(prev) != len(i):
                prev = i
                raise TypeError("Each row of the matrix must have the same size")
            else:
                for j in range(0, len(i)):
                    if not isinstance(i[j], (int, float)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                    else:
                        temp.append(round(i[j]/div, 2))
                        if j == len(i)-1:
                            result.append(temp)
        return result
