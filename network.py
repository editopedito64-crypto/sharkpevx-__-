import socket
import os

def resolver(host):
    try:
        return socket.gethostbyname(host)
    except:
        return None

def ping(host):
    comando = "ping -n 4 " + host if os.name == "nt" else "ping -c 4 " + host
    os.system(comando)