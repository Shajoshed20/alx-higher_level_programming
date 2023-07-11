#!/usr/bin/python3

"""Funtion to write sting to text"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
