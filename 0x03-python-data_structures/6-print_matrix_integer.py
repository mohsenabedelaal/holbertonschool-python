#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print('')
    for i in matrix:
        for j in range(0, len(i)):
            if j == len(i)-1:
                print('{}'.format(i[j]), end='\n')
            else:
                print('{}'.format(i[j]), end=' ')
