#!/usr/bin/env python3

"""
Invocations:
    url-expand.py http://tinyurl.com/2g9mqh
    echo http://tinyurl.com/2g9mqh | url-expand.py

Output:
    If the URL supplied has an HTTP redirect, displays the target URL.
    Otherwise, displays "None".
"""

import sys
from http.client import HTTPConnection, HTTPSConnection
from urllib.parse import urlparse

def get_url():
	if len(sys.argv) > 1:
		return sys.argv[1]
	else:
		return input()

def request(url):
	parsed = urlparse(url)
	conn = connect(parsed.scheme, parsed.netloc)
	conn.request("GET", parsed.path)
	return conn.getresponse()

def connect(scheme, host):
	if scheme == "http":
		return HTTPConnection(host)
	elif scheme == "https":
		return HTTPSConnection(host)

def show_redirect(response):
	print(response.getheader("Location"))

show_redirect(request(get_url()))

