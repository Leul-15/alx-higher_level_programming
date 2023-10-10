#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n=4500):
    """print pascal"""
    pas = [[0]*i for i in range(1, n+1)]
    cmpt = 0
    for x in range(n):
        pas[x][0] = 1
        pas[x][-1] = 1
        for y in range(0, i//2):
            pas[x][y+1] = pas[x-1][y] + pas[x-1][y+1]
            pas[x][x-y-1] = pas[x-1][y] + pas[x-1][y+1]

    return pas
