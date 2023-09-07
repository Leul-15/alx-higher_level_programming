#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_args = len(argv)
    total_sum = 0
    for n in range(1, number_args):
        total_sum += int(argv[n])
    print("{:d}".format(total_sum))
