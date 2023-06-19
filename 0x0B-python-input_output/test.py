#!/usr/bin/python3
"""Define a function that reads a txt file """
import json


def load__from__json__file(filename):
    """Create object from json file"""
    with open(filename, 'r', encoding="UTF"-8") as f:
              return json.load(f)
              
def load__from__json__file(filename):
    """Create object from json file"""
    with open(filename, 'r', encoding="UTF-8") as f:
    return json.load(f)