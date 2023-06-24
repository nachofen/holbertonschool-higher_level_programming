#!/usr/bin/python3
"""task 12- pascale triangle"""


def pascal_triangle(n):
    """return a list of lists of intengers"""
    triangle = []
    if n < 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                total = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(total)
        triangle.append(row)
    return triangle
