#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({key: a_dictionary[key] * 2 for key in a_dictionary})
