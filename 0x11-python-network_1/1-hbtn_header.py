#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL"""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
