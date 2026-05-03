import socket
import subprocess
from scanner import scan
from utils import guardar


def banner():
    print(r"""
 ███████╗██╗  ██╗ █████╗ ██████╗ ██╗  ██╗██╗   ██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝╚██╗ ██╔╝
 ███████╗███████║███████║██████╔╝█████╔╝  ╚████╔╝
 ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗   ╚██╔╝
 ███████║██║  ██║██║  ██║██║  ██║██║  ██╗   ██║
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝

        SHARKPEVX TOOL v2
""")


def parsear_puertos(p):
    if not p.strip():
        return [80, 443, 8000]

    if "-" in p:
        inicio, fin = p.split("-")
        return list(range(int(inicio), int(fin) + 1))

    return [int(x.strip()) for x in p.split(",")]


def escaneo_puertos():
    host = input("Host: ")
    puertos = input("Puertos (80,443 o 1-1000): ")
    puertos = parsear_puertos(puertos)

    resultados = scan(host, puertos)

    print("\nResultados:\n")

    if not resultados:
        print("No se encontraron puertos abiertos")
    else:
        for r in resultados:
            print(f"{r['puerto']} abierto | {r['banner']}")

    return resultados


def resolver_dominio():
    dominio = input("Dominio: ")
    try:
        ip = socket.gethostbyname(dominio)
        print(f"IP: {ip}")
    except:
        print("Error al resolver dominio")


def reverse_dns():
    ip = input("IP: ")
    try:
        dominio = socket.gethostbyaddr(ip)
        print(f"Dominio: {dominio[0]}")
    except:
        print("No se pudo resolver")


def ping():
    host = input("Host: ")
    try:
        subprocess.run(["ping", host])
    except:
        print("Error en ping")


def info_http():
    host = input("Host: ")
    try:
        with socket.socket() as s:
            s.settimeout(3)
            s.connect((host, 80))
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            data = s.recv(1024).decode(errors="ignore")
            print(data)
    except:
        print("No se pudo obtener info HTTP")


def ip_local():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"IP local: {ip}")
    except:
        print("Error al obtener IP")


def menu():
    print("""
[1] Escaneo de puertos
[2] Resolver dominio
[3] Reverse DNS
[4] Ping
[5] Info HTTP
[6] IP local
[7] Guardar resultados
[0] Salir
""")


def main():
    resultados_guardados = []

    while True:
        banner()
        menu()

        opcion = input("Opción: ")

        if opcion == "1":
            resultados_guardados = escaneo_puertos()
            input("\nEnter...")

        elif opcion == "2":
            resolver_dominio()
            input("\nEnter...")

        elif opcion == "3":
            reverse_dns()
            input("\nEnter...")

        elif opcion == "4":
            ping()
            input("\nEnter...")

        elif opcion == "5":
            info_http()
            input("\nEnter...")

        elif opcion == "6":
            ip_local()
            input("\nEnter...")

        elif opcion == "7":
            guardar(resultados_guardados)
            print("Resultados guardados en resultados.json")
            input("\nEnter...")

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()