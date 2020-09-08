#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = (map((lambda inner: [item ** 2 for item in inner]), matrix))
    new_matrix = list(new_matrix)
    return new_matrix
