#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    rep_list = my_list[:]
    for i in range(len(rep_list)):
        if rep_list[i] == search:
            rep_list[i] = replace
    return (rep_list)
