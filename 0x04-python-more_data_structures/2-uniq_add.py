#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    value = 0
    for uniq in set(my_list):
        value += uniq
    return (value)
