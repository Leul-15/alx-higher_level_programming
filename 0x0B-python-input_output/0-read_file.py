#!/usr/bin/python3

"""Program that prints a text file to stdout"""


def read_file(filename=""):
    """prints file contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
