#!/usr/bin/python3
"""Define an  empty Class BaseGeometry"""



class BaseGeometry:
    """Initializing BaseGeometry"""
    
    def area(self):
        """ Raise an exception if the area is not implemented"""
        raise Exception("area() is not implemented")
    