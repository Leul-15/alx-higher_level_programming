#!/usr/bin/python3
"""
class Rectangle that inherits BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle"""
    def __init__(self, width, height):
        """ Intialize a new Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return the print() and str() representation of a Rectangle """
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
