#!/usr/bin/python3
"""
Returns True if the obj. is an inst
"""


def inherits_from(obj, a_class):
    """ return True if the obj is an instance of a class that inherited"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
