#!/usr/bin/python3

"""class BaseGeometry"""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """public instance method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validator
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
