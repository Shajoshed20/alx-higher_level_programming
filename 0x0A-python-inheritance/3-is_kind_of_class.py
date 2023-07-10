#!/usr/bin/python3

""" Function to check for whether an object is
    an instance of a class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns: if the object is an instance of - True, or
        if the object is an instance of a class that
        inherited from, the specified class; otherwise False.
    """
    return (isinstance(obj, a_class))
