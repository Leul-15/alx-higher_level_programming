#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = len(sys.argv)
    if number <= 1:
        print("0 arguments.")
    else:
        if number == 2:
            print("{:d} argument:".format(number - 1))
        else:
            print("{:d} arguments:".format(number - 1))
        for n in range(1, number):
            print("{:d}: {}".format(n, sys.argv[n]))
