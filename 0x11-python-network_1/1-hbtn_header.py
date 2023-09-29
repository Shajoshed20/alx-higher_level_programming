#!/usr/bin/python3
"""X-Request-Id header variable of a request to a given URL."""
import sys
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]

    ask = urllib.request.Request(link)
    with urllib.request.urlopen(ask) as response:
        print(dict(response.headers).get("X-Request-Id"))
