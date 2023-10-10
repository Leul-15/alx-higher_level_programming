#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """"append write"""
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
