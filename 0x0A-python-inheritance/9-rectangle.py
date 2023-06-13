#!/usr/bin/python3
"""A module that defines a class Rectangle that inherits from Class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def ___init___(self,width,height):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            """

        self.integer_validator("width",width)
        self.integer_validator("height",height)
        self.___width = width
        self.___height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__ (self):
        """Print string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
