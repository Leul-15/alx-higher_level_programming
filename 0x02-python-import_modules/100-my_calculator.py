#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    options = ["+", "-", "*", "/"]
    from calculator_1 import *
    functions = [add, sub, mul, div]
    for i, n in enumerate(options):
        if argv[2] == n:
            print("{} {} {} = {}".format(num1, n, num2, functions[i](num1, num2)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
