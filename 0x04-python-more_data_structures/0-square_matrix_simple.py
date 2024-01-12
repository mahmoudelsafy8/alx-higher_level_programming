#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    for row in matrix:
        s.append([c**2 for c in row])
        return s
