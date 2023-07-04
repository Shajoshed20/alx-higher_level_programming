#!/usr/bin/python3

"""Defining funtion to print a name"""


def say_my_name(first_name, last_name=""):
    """Funtion to print name.

    Args:
        first_name (str): For first name printed.
        last_name (str): For last name printed.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
