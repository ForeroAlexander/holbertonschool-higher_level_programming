#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the
letter as a parameter
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, data={'q': sys.argv[1]})
    except IndexError:
        r = requests.post(url, data={'q': ""})
    try:
        r = r.json()
        if not r:
            print('No result')
        else:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
    except ValueError:
        print('Not a valid JSON')
