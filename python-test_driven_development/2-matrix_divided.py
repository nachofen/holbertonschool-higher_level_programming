#!/usr/bin/python3
"""
shebang
"""


def matrix_divided(matrix, div):
    """matrix divided by a number func"""
    row_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    matrix_size = len(matrix[0])
    for col in matrix:
        if matrix_size != len(col):
            raise TypeError("Each row of the matrix must have the same size")
        for row in col:
            if not isinstance(row, (int, float)):
                raise TypeError(error)
        if matrix_size != len(col):
            raise TypeError("Each row of the matrix must have the same size")
    for col in matrix:
        new_matrix = []
        for row in col:
            new_matrix.append(round(row / div, 2))
        row_matrix.append(new_matrix)
    return (row_matrix)
