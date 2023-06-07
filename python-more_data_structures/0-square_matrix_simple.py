#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for line in matrix:
        for num in line:
            sq_num = num ** 2
            matrix_2.append(sq_num)
    return (matrix_2)
