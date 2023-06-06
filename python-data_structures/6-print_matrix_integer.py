#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_matrix in matrix:
        for item in sub_matrix:
            print("{:d}".format(item), end=" ")
        print("\n", end="")
