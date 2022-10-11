#!/usr/bin/python3
"""creates class square with size propeerty, area and print_Square method getters and setters"""


class Square:

    def __init__(self, size):
        """Class Square"""

        self.size = size

    @property
    def size(self):
        """getter of size attribute"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """setter of size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method to get square's area"""

        return (self.__size * self.__size)

    def my_print(self):
        """method to print square"""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
