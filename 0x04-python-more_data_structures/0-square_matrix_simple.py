#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        newRow = list(map(lambda i: i ** 2, row))
        new.append(newRow)
    return(new)
