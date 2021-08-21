#!/usr/bin/python3
"""Sends a request to a URL passed as an
argument. Displays the value of the variable
X-Request-Id in response header.
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
