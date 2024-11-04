import socket
import requests

REMOTE_SERVER = "one.one.one.one"


def is_connected(hostname):
    url = "http://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False


# value = is_connected(REMOTE_SERVER)
# print(value)
