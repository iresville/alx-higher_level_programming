#!/usr/bin/python3
"""A module that defines a class Square that inherits from Class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Represents a Square"""
    
    def ___init___(self,width,height):
        """Initializes a new instance of the square class.
        
        Args:
            width (int): The width of the square.
            height (int): The height of the square.
            """
            
        self.integer_validator("width",width)
        self.integer_validator("height",height)
        self.___width = width
        self.___height = height
    
    def area(self):
        """Returns the area of the square"""
        return self.__width * self.__height
    
    def __str__ (self):
        """Print string representation of the square"""
        return f"[square] {self.__width}/{self.__height}"