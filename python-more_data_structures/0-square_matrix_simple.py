#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for line in matrix:
        for num in line:
            matrix_2.append(num ** 2)
    return (matrix_2)
