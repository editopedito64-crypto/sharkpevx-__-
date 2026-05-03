import socket
from concurrent.futures import ThreadPoolExecutor

def obtener_banner(sock):
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        return sock.recv(1024).decode(errors="ignore").split("\n")[0]
    except:
        return "sin banner"

def escanear_puerto(host, puerto, timeout):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((host, puerto))
        banner = obtener_banner(sock)
        sock.close()
        return {"puerto": puerto, "estado": "abierto", "banner": banner}
    except:
        return None

def scan(host, puertos, timeout=1):
    resultados = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(escanear_puerto, host, p, timeout) for p in puertos]
        for f in futures:
            r = f.result()
            if r:
                resultados.append(r)
    return resultados