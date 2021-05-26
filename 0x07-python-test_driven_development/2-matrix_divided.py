#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """ function that divide a matrix"""
    newone = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if not isinstance(matrix[col][row], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")

        for row in matrix:
            if len(row) != len(matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
    for x in matrix:
        newone.append(list(map(lambda x: round(x / div, 2), x)))
    return newone
