#!/usr/bin/python3
# def print_matrix_integer(matrix=[[]]):
#     for row in matrix:
#         for i in range(len(row)):
#             if i == len(row) - 1:
#                 print("{:d}".format(row[i]))
#             else:
#                 print("{:d}".format(row[i]), end=" ")


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" " if column != row[-1] else "")
        print()
