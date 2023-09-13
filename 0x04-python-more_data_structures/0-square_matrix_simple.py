#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[n ** 2 for n in row] for row in matrix]
    return new_matrix
