#!/usr/bin/python3
"""create Class Square"""


class Square:
    """ A Class that defines a square"""

    def __init__(self, size=0):
        self.__size = 0
		self.size = None

		@property
		def size(self):
			return self.__size

		@size.setter
		def size(self, value):
			if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            return self.__size ** 2
