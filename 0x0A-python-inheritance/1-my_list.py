#!/usr/bin/python3

"""A class MyList that inherits from list"""


class MyList(list):
    """Beginning of class to inherit."""

    def print_sorted(self):
        """Prints list in sorted order."""
        print(sorted(self))
