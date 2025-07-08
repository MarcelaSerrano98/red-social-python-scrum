from logica.listado_de_usuarios import lista
from jsons.json_utils import leer_json, escribir_json


DATA_FILE = "savefiles/posts.json"
DATA_FILE2 = "savefiles/users.json"


def visualizar_perfil_usuarios():
    lista()
    print("Que perfil deseas ver?")
    publicaciones = leer_json(DATA_FILE)
    usuarios_perfil = leer_json(DATA_FILE2)

    perfil_nombre = input("Ingrese el nombre: ")

    encontrado = False
    for usuario in usuarios_perfil:
        if perfil_nombre == usuario['Nombre']:
            print("="*50)
            print("                  PERFIL               ")
            print("="*50)
            print(f"👤 Nombre: {usuario['Nombre']}")
            print(f"🎂 Edad: {usuario['Anhos']} años")
            print("="*50)
            encontrado = True
            break


    if not encontrado:
        print("❌ No se encontró un usuario con ese nombre.")
        return

    publicaciones_usuario = [p for p in publicaciones if p["usuario"] == perfil_nombre]

    if publicaciones_usuario:
        print(f"           PUBLICACIONES DE {perfil_nombre.upper()}   ")
        print("="*50)
        for pub in publicaciones_usuario:
            print(f"📘 Libro: {pub['libro']}")
            print(f"📝 Reseña: {pub['reseña']}")
            print(f"❤️ Likes: {pub['likes']}")
            print("💬 Comentarios:")
            if pub["comentarios"]:
                for c in pub["comentarios"]:
                    print(f"   - {c['usuario']}: {c['comentario']}")
            else:
                print("   (Ninguno)")
            print(f"🕒 Fecha: {pub['fecha']}")
            print("="*50)
    else:
        print(f"😢 {perfil_nombre} no tiene publicaciones aún.")