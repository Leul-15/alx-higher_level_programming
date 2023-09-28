#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each '.', '?', ':'
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each '.', '?', ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delm in ".:?":
        text = (delm + "\n\n").join(
            [ln.strip(" ") for ln in text.split(delm)])
        print("{}".format(text), end="")
