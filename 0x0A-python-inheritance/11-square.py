#!/usr/bin/python3

""" square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        """ Constructor """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Calculator area """
        return super().area()

    def __str__(self):
        """ str """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
