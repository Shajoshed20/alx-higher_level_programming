#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""
from sys import argv
import requests


if __name__ == "__main__":
    link = argv[1]
    value = {"email": argv[2]}

    ask = requests.post(link, data=value)
    print(ask.text)
