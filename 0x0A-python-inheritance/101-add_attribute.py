#!/usr/bin/python3

"""A function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Beginning of funtion to add attribute.

    Args:
        obj (any): The object.
        att (str): The name of the attribute.
        value (any): The value of att.
    Raises:
        TypeError: When the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
