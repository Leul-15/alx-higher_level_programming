#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    data = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    num = 0
    prev = 0
    for i in range(len(roman_string) - 1, -1, -1):
        current = data.get(roman_string[i], 0)
        if current >= prev:
            num += current
        else:
            num -= current
        prev = current
    return num
