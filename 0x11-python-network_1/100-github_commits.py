#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
from sys import argv
import requests


if __name__ == "__main__":
    link = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    ask = requests.get(link)
    commits = ask.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                commits[j].get("sha"),
                commits[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
