import json
import os

def generar_id():
    archivo = "savefiles/posts.json"
    if not os.path.exists(archivo):
        return 1
    with open(archivo, "r") as f:
        publicaciones = json.load(f)
    if not publicaciones:
        return 1
    return max(p["id"] for p in publicaciones) + 1
