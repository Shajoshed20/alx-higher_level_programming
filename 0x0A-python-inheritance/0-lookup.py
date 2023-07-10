#!/usr/bin/python3

"""
    function to return the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """Returns list of attributes for list."""
    return (dir(obj))
