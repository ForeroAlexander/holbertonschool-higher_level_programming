#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    response = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(owner, repo))

    commit = response.json()
    for i in range(10):
        print("{}: {}".format(
            commit[i].get("sha"),
            commit[i].get("commit").get("author").get("name")))
