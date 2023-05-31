#!/usr/bin/python3
"""Define class Square"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
		self.__size = size

    @property
    def size(self):
        """Get size of square matrix"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square matrix"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of square matrix"""
        return self.__size ** 2

    def my_print(self):
        """print the sqaure matrix using '#' notation"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
