import json

def guardar(resultados):
    with open("resultados.json", "w") as f:
        json.dump(resultados, f, indent=4)