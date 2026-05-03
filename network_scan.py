import socket

def escanear_red(base):
    activos = []
    for i in range(1, 50):
        ip = f"{base}.{i}"
        try:
            socket.gethostbyaddr(ip)
            activos.append(ip)
        except:
            pass
    return activos