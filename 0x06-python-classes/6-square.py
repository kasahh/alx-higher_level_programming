#!/usr/bin/python3
"""creates square class with size, property, setters and getters"""


class Square:
    """Class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor using size and position"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """getter of size attribute"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter of position"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """setter of position"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method to get the square's area"""
        return (self.__size * self.__size)

    def my_print(self):
        """method that prints square with spaces"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
