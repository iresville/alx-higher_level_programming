#!/usr/bin/python3
""" Define a class MyList"""


class myList(list):
    """A subclass list that provides additional functionality for\
        printing the elements of the list in sorted order ."""
        
        
    def print_sorted(self):
        """ Prints the element of the list in sorted (ascending) order"""
       
        sorted_list = sorted(self)
        print(sorted_list)
    