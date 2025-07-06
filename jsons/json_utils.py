import json
import os

def leer_json(ruta_archivo):
    """Lee y retorna datos desde un archivo JSON. Si no existe, retorna lista vacía."""
    if not os.path.exists(ruta_archivo):
        return []
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        return json.load(file)

def escribir_json(ruta_archivo, datos):
    """Escribe una lista de datos en un archivo JSON con formato indentado."""
    with open(ruta_archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        