#!/usr/bin/python3
""" Define a function that checks if an object exactly matches \
    a specified class"""

def is_same_class(obj, a_class):
    """
    Function that validate if object is exact instance of specified class
    
    Args: (obj) is the object to be validated is matched\
        against an exact class name
        
    Returns: 
    True if obj is an exact instance of class
    False otherwise
    
    """
    if type(obj) == a_class:
        return True
    else:
        return False
