#!/usr/bin/python3
"""sends a POST request to the passed URL with the email
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urlencode(email)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        cont = response.read()
        utf8 = cont.decode('utf-8')
        print(utf8)
