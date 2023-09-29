#!/usr/bin/python3
"""request to a given URL and displays the response body."""

from sys import argv
import requests


if __name__ == "__main__":
    link = argv[1]

    ask = requests.get(link)
    if ask.status_code >= 400:
        print("Error code: {}".format(ask.status_code))
    else:
        print(ask.text)
