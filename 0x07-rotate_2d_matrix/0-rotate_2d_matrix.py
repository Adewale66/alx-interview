#!/usr/bin/python3
"""Rotate matrix
"""


def rotate_2d_matrix(mtx):
    """rotate 2d matrix

    Args:
        mtx (_type_): _description_
    """
    n = len(mtx)
    for i in range(n):
        for j in range(i+1, n):
            mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    for i in range(n):
        for j in range(n // 2):
            mtx[i][j], mtx[i][n - j - 1] = mtx[i][n - j - 1], mtx[i][j]
