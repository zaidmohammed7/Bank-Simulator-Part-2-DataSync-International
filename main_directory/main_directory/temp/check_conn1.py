import socket
REMOTE_SERVER = "one.one.one.one"


def is_connected(hostname):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        print('[ INFO ] Connection [ Connection  ] : Connection SUCCESSFUL')
        return True
    except:
        print('[ INFO ] Connection [ Connection  ] : Connection NOT SUCCESSFUL')
        pass
    return False


value = is_connected(REMOTE_SERVER)
print(value)
