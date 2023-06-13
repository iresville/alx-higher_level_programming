#!/usr/bin/python3
"""Define a function that checks if an object is either an instance of a local \
    class or an inherited class"""

def is_kind_of_class(obj, a_class):
    """ Check is obj is an instance of a class or a subclass"""
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
