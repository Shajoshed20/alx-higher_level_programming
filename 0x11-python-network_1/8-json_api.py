#!/usr/bin/python3
""" POST request to http://0.0.0.0:5000/search_user with a given letter."""
from sys import argv
import requests


if __name__ == "__main__":
    post = "" if len(argv) == 1 else argv[1]
    load = {"q": post}

    ask = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        response = ask.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
