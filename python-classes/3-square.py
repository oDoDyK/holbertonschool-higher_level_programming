#!/usr/bin/python3
"""
Module defines a class square with a private instance attribute size
"""


class Square:
    """
    Class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):
        """
        Initialize a square with size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance method.
        Returns:
            int: the current square area.
        """
        return self.__size * self.__size
