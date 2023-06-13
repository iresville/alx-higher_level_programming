#!/usr/bin/python3
"""A module that defines a class Rectangle that inherits from Class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectange"""
    
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
    
    