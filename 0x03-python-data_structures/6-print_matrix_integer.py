#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if x != len(matrix[i]) - 1:
                    e = ' '
                else:
                    e = ''
                print("{:d}".format(matrix[i][x]), end=e)
            print()
