# sharkpevx-__-

Herramienta de reconocimiento de red en Python (CLI)

```
   ███████╗██╗  ██╗ █████╗ ██████╗ ██╗  ██╗██╗   ██╗
   ██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝╚██╗ ██╔╝
   ███████╗███████║███████║██████╔╝█████╔╝  ╚████╔╝ 
   ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗   ╚██╔╝  
   ███████║██║  ██║██║  ██║██║  ██║██║  ██╗   ██║   
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

              SHARKPEVX TOOL PRO+
```

---

## Descripción

sharkpevx-__ es una herramienta de línea de comandos (CLI) para reconocimiento de red, diseñada con fines educativos y pruebas en entornos controlados.

Incluye funcionalidades como:

* Escaneo de puertos
* Banner grabbing (detección de servicios)
* Resolución DNS
* Ping a hosts
* Escaneo básico de red

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/TU-USUARIO/sharkpevx-__.git
cd sharkpevx-__
```

2. Ejecutar:

```bash
python sharky.py
```

---

## Uso

### Escaneo de puertos

```bash
python sharky.py scan 127.0.0.1
```

### Escaneo de rango de puertos

```bash
python sharky.py scan 127.0.0.1 --ports 1-1000
```

### Banner Grabbing

```bash
python sharky.py scan 127.0.0.1 --ports 8000
```

### Escaneo de red

```bash
python sharky.py netscan 192.168.0
```

### Resolver dominio

```bash
python sharky.py resolve google.com
```

### Ping

```bash
python sharky.py ping google.com
```

---

## Estructura del proyecto

```
sharkpevx-__/
├── sharky.py
├── scanner.py
├── network.py
├── network_scan.py
├── utils.py
├── README.md
└── requirements.txt
```

---

## Salida

Los resultados se guardan automáticamente en:

```
resultados.json
```

---

## Disclaimer

Esta herramienta está destinada únicamente para:

* uso educativo
* pruebas en sistemas propios
* entornos con autorización explícita

El uso indebido de esta herramienta es responsabilidad del usuario.

---

## Tecnologías

* Python 3
* Sockets
* Multithreading

---

## Roadmap

* Detección de sistema operativo
* Mejoras en rendimiento
* Interfaz gráfica
* Exportación avanzada de resultados

---

## Autor

Desarrollado por sharkpevx

---

## Contribuciones

Las contribuciones son bienvenidas. Se pueden realizar forks y enviar pull requests.

---

## Licencia

MIT License
