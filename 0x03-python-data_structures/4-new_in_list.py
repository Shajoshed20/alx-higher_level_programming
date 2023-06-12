#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace the elment on the copied version of a list"""
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    copy_list = my_list.copy()
    copy_list[idx] = element
    return (copy_list)
