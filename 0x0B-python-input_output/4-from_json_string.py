#!/usr/bin/python3

"""A function that returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """Return:
        An object (Python data structure) represented by a JSON string.
    """
    return json.loads(my_str)
