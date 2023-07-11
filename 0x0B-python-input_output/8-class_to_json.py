#!/usr/bin/python3

"""A function that returns the dictionary description"""


def class_to_json(obj):
    """Return:
        The dictionary represntation of a simple data structure.
    """
    return obj.__dict__
