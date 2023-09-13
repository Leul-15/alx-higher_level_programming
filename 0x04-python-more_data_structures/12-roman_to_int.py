#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [rom_data[n] for n in roman_string] + [0]
    num = 0

    for n in range(len(numbers) - 1):
        if numbers[n] >= numbers[n+1]:
            num += numbers[n]
        else:
            num -= numbers[n]

    return num
