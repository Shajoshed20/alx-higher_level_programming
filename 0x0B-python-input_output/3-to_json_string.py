#!/usr/bin/python3

"""Function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """
    Returns:
        The JSON representation of an object (string)
    """

    return json.dumps(my_obj)
