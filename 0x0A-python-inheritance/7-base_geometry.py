#!/usr/bin/python
# """Define an  empty Class BaseGeometry"""



class BaseGeometry:
    """BaseGeometry class"""
    
    def area(self):
        """Raise an exceptiom if the area is not implmented"""
        raise NotImplementedError("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates the value as an integer"""
        self.name = name
        self.value = value
        
    if not isinstance(value, int):
        raise TypeError("<name> must be an integer")
    if value <= 0:
        raise ValueError("name must be >= 0")
   