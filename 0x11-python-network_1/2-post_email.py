#!/usr/bin/python3
"""POST request to a given URL with a given email."""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    link = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    ask = urllib.request.Request(link, data)
    with urllib.request.urlopen(ask) as response:
        print(response.read().decode("utf-8"))
