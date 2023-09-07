#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    n = len(argv)

    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    number1 = int(argv[1])
    number2 = int(argv[3])
    optn = argv[2]

    def unknown_operator():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def add_function():
        answer = add(number1, number2)
        print("{:d} + {:d} = {:d}".format(number1, number2, answer))
        return answer

    def sub_function():
        answer = sub(number1, number2)
        print("{:d} - {:d} = {:d}".format(number1, number2, answer))
        return answer

    def mul_function():
        answer = mul(number1, number2)
        print("{:d} * {:d} = {:d}".format(number1, number2, answer))
        return answer

    def div_function():
        answer = div(number1, number2)
        print("{:d} / {:d} = {:d}".format(number1, number2, answer))
        return answer

    options = {
        "+": add_function,
        "-": sub_function,
        "*": mul_function,
        "/": div_function
    }
    options.get(optn, unknown_operator)()
