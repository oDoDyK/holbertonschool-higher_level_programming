#!/usr/bin/python3
"""
Module defines a class square with a private instance attribute size
"""


class Square:
    """
    class Square that defines a square by: (based on 3-square.py)
    """
    def __init__(self, size=0):

        self.__size = size
        """
        Initialize a square with size.
        """
    @property
    def size(self):
        """
        Retrieve the size to the square.
        Returns:
            int: the size to the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method.
        Returns:
            int: The current square area
        """
        return self.__size * self.__size
