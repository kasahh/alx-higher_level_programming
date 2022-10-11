#!/usr/bin/python3
"""Ceeates a Class Square with size, method area, getters and setters """


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """Square constructor with size"""
        self.size = size

    @property
    def size(self):
        """get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return square area"""

        return (self.__size * self.__size)
