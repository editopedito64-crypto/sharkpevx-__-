import socket
import threading

def banner_grab(host, puerto):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, puerto))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode(errors="ignore")
        s.close()
        return banner.strip().split("\n")[0]
    except:
        return None

def escanear_puerto(host, puerto, resultados, timeout, sem):
    with sem:
        try:
            s = socket.socket()
            s.settimeout(timeout)

            if s.connect_ex((host, puerto)) == 0:
                banner = banner_grab(host, puerto)
                resultados.append({
                    "puerto": puerto,
                    "estado": "abierto",
                    "banner": banner if banner else "sin banner"
                })

            s.close()
        except:
            pass

def scan(host, puertos, timeout=1, max_threads=100):
    resultados = []
    hilos = []
    sem = threading.Semaphore(max_threads)

    for p in puertos:
        t = threading.Thread(target=escanear_puerto,
                             args=(host, p, resultados, timeout, sem))
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    return resultados