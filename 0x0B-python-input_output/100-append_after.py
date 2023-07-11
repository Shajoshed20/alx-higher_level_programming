#!/usr/bin/python3

"""A function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
        specific string

    Args:
        filename: File's name in string form.
        search_string: Search string.
        new_string (str): New string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
