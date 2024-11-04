import socket

import requests

def is_connected(hostname):
    url = "http://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        return False

REMOTE_SERVER = "one.one.one.one"

print(is_connected(REMOTE_SERVER))

