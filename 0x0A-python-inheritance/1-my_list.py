#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
