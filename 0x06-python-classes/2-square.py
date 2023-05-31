#!/usr/bin/python3
"""create Class Square"""


class Square:
    """create instance of a Class"""
    def __init__(self, size=0):
        self.__size = size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
