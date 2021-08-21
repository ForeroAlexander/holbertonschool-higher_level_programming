#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            cont = response.read()
            utf8 = cont.decode('utf-8')
            print(utf8)
    except HTTPError as status:
        print("Error code: {}".format(status.code))
