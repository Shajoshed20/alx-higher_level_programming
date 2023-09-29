#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""

import requests


if __name__ == "__main__":
    ask = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(ask.text)))
    print("\t- content: {}".format(ask.text))
