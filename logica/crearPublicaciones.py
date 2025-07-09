from datetime import datetime
from logica.generarId import generar_id
from jsons.json_utils import leer_json, escribir_json


def crear_publicacion(nombre_usuario):
    libro = input("📘 Título del libro: ")
    reseña = input("📝 Escribe tu micro reseña: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo = "savefiles/posts.json"

    publicaciones = leer_json(archivo)

    nueva_reseña = {
        "id": generar_id(),
        "usuario": nombre_usuario,
        "libro": libro,
        "reseña": reseña,
        "likes": 0,
        "comentarios": [],
        "fecha": fecha
    }

    publicaciones.append(nueva_reseña)
    escribir_json(archivo, publicaciones)

    print("✅ ¡Tu reseña fue publicada! 📝")


