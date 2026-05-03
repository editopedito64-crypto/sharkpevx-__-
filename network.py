import socket
import os

def resolver(host):
    try:
        return socket.gethostbyname(host)
    except:
        return "No disponible"

def reverse(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "No disponible"

def ping(host):
    os.system(f"ping -n 1 {host}")

def ip_local():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "No disponible"