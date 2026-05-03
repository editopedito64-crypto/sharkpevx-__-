import argparse
from scanner import scan
from network import resolver, ping
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

              SHARKPEVX TOOL PRO+
""")

def parsear_puertos(p):
    if "-" in p:
        inicio, fin = map(int, p.split("-"))
        return list(range(inicio, fin + 1))
    else:
        return [int(x) for x in p.split(",")]

def main():
    banner()

    parser = argparse.ArgumentParser(description="sharkpevx-__ CLI tool")
    sub = parser.add_subparsers(dest="cmd")

    # scan
    scan_cmd = sub.add_parser("scan")
    scan_cmd.add_argument("host")
    scan_cmd.add_argument("--ports", default="80,443,8000")
    scan_cmd.add_argument("--timeout", type=float, default=1)

    # netscan
    net_cmd = sub.add_parser("netscan")
    net_cmd.add_argument("base", help="Ej: 192.168.0")

    # resolve
    res_cmd = sub.add_parser("resolve")
    res_cmd.add_argument("host")

    # ping
    ping_cmd = sub.add_parser("ping")
    ping_cmd.add_argument("host")

    args = parser.parse_args()

    if args.cmd == "scan":
        puertos = parsear_puertos(args.ports)
        resultados = scan(args.host, puertos, args.timeout)

        print("\nResultados:\n")
        if resultados:
            for r in resultados:
                print(f"{r['puerto']} abierto | {r['banner']}")
        else:
            print("No se encontraron puertos abiertos")

        guardar(resultados)

    elif args.cmd == "netscan":
        activos = escanear_red(args.base)

        print("\nHosts activos:\n")
        if activos:
            for ip, puertos in activos:
                print(f"{ip} -> {puertos}")
        else:
            print("No se encontraron hosts activos")

    elif args.cmd == "resolve":
        ip = resolver(args.host)
        print(ip if ip else "No se pudo resolver")

    elif args.cmd == "ping":
        ping(args.host)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()