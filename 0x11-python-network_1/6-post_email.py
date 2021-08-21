#!/usr/bin/python3
"""
Takes in an URL and an email address
and sends a POST request to the passed URL
using the email and displays the body of the
response.
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
