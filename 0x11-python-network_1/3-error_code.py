#!/usr/bin/python3
"""request to a given URL and displays the response body."""
from sys import argv
import urllib.error
import urllib.request


if __name__ == "__main__":
    link = argv[1]

    ask = urllib.request.Request(link)
    try:
        with urllib.request.urlopen(ask) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
