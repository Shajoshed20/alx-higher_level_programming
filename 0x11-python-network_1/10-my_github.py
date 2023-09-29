#!/usr/bin/python3
"""GitHub API to display a GitHub ID based on given credentials."""

from requests.auth import HTTPBasicAuth
from sys import argv
import requests


if __name__ == "__main__":
    cred = HTTPBasicAuth(argv[1], argv[2])
    ask = requests.get("https://api.github.com/user", auth=cred)
    print(ask.json().get("id"))
