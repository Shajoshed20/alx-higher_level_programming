#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """To compute the square of all integers in a matrix."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
