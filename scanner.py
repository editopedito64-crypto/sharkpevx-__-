import socket
from concurrent.futures import ThreadPoolExecutor

def escanear_puerto(host, puerto):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(3)
            sock.connect((host, puerto))  # usamos connect directo

            try:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").split("\n")[0]
            except:
                banner = "sin banner"

            return {
                "puerto": puerto,
                "estado": "abierto",
                "banner": banner
            }

    except Exception as e:
        return None


def scan(host, puertos):
    resultados = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(escanear_puerto, host, p) for p in puertos]

        for f in futures:
            r = f.result()
            if r:
                resultados.append(r)

    return resultados
