#!/usr/bin/python3
"""Creates a Class Square with size and gets area of the square"""


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """Square constructor using size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method to get Square's area"""
        return (self.__size * self.__size)
