#!/usr/bin/python3
"""
Define a class that represents a square.
"""


class Square:
    '''
    A simple class that represents a square.
    It initializes the square with a validated size value.
    '''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
