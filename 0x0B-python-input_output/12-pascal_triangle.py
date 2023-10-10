#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n=4500):
    """print pascal"""
    p = [[0]*i for i in range(1, n+1)]
    cmpt = 0
    for i in range(n):
        p[i][0] = 1
        p[i][-1] = 1
        for j in range(0, i//2):
            p[i][j+1] = p[i-1][j] + p[i-1][j+1]
            p[i][i-j-1] = p[i-1][j] + p[i-1][j+1]

    return p
