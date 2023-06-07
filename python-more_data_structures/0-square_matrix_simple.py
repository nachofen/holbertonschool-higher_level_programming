#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for line in matrix:
        num_row = []
        for num in line:
            sq_num = num ** 2
            num_row.append(sq_num)
        matrix_2.append(num_row)
    return (matrix_2)
