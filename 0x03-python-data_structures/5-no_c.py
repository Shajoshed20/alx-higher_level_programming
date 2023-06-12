#!/usr/bin/python3

def no_c(my_string):
    """removes all character c and C fron string"""
    copy_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            copy_string += ch
    return (copy_string)
