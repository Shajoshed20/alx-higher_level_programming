#!/usr/bin/python3
"""X-Request-Id header variable of a request to a given URL."""
import requests
import sys


if __name__ == "__main__":
    link = sys.argv[1]

    ask = requests.get(link)
    print(ask.headers.get("X-Request-Id"))
