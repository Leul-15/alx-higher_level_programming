#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    mul = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)

    return (mul)
