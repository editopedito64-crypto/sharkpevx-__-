from scanner import scan
from network import resolver, reverse, ping, ip_local
from network_scan import escanear_red
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
        inicio, fin = map(int, p.split("-"))
        return list(range(inicio, fin + 1))
    return [int(x) for x in p.split(",") if x.strip()]

def main():
    resultados = []

    while True:
        banner()

        print("[1] Escaneo de puertos")
        print("[2] Escaneo de red")
        print("[3] Resolver dominio")
        print("[4] Reverse DNS")
        print("[5] Ping")
        print("[6] Info HTTP")
        print("[7] IP local")
        print("[8] Guardar resultados")
        print("[0] Salir")

        opcion = input("\nOpción: ")

        if opcion == "1":
            host = input("Host: ")
            puertos = input("Puertos (80,443 o 1-1000): ")
            puertos = parsear_puertos(puertos)
            resultados = scan(host, puertos)

            print("\nResultados:\n")
            for r in resultados:
                print(f"{r['puerto']} abierto | {r['banner']}")

            input("\nEnter...")

        elif opcion == "2":
            base = input("Red base (ej: 192.168.0): ")
            activos = escanear_red(base)

            print("\nHosts activos:\n")
            for ip in activos:
                print(ip)

            input("\nEnter...")

        elif opcion == "3":
            host = input("Dominio: ")
            print(resolver(host))
            input("\nEnter...")

        elif opcion == "4":
            ip = input("IP: ")
            print(reverse(ip))
            input("\nEnter...")

        elif opcion == "5":
            host = input("Host: ")
            ping(host)
            input("\nEnter...")

        elif opcion == "6":
            host = input("Host: ")
            resultados = scan(host, [80, 443])

            print("\nInfo HTTP:\n")
            for r in resultados:
                print(f"{r['puerto']} -> {r['banner']}")

            input("\nEnter...")

        elif opcion == "7":
            print("IP local:", ip_local())
            input("\nEnter...")

        elif opcion == "8":
            guardar(resultados)
            print("Guardado en resultados.json")
            input("\nEnter...")

        elif opcion == "0":
            break

        else:
            print("Opción inválida")
            input("\nEnter...")

if __name__ == "__main__":
    main()