import socket

def escanear_ip(ip):
    puertos = [80, 443]
    abiertos = []

    for p in puertos:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((ip, p)) == 0:
                abiertos.append(p)
            s.close()
        except:
            pass

    return abiertos

def escanear_red(base):
    activos = []

    for i in range(1, 255):
        ip = f"{base}.{i}"
        abiertos = escanear_ip(ip)

        if abiertos:
            activos.append((ip, abiertos))

    return activos