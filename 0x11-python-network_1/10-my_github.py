#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, password))
    print(response.json().get("id"))
