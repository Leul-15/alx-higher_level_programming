#!/usr/bin/python3
#!/usr/bin/python3
"""
This module defines a Square class
"""
class Square:

    def __init__(self, size=0):
        """Initialize a new data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
