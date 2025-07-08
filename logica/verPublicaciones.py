from jsons.json_utils import leer_json

def ver_publicaciones():
    archivo = "savefiles/posts.json"
    publicaciones = leer_json(archivo)

    if not publicaciones:
        print("❌ No hay publicaciones aún.")
        return

    print("\n===== HISTORIAS PUBLICADAS =====\n")

    for pub in publicaciones:
        print(f"👤 Usuario: {pub['usuario']}")
        print(f"📘 Libro: {pub['libro']}")
        print(f"📝 Reseña: {pub['reseña']}")
        print(f"❤️ Likes: {pub['likes']}")

        if pub["comentarios"]:
            print("💬 Comentarios:")
            for c in pub["comentarios"]:
                print(f"   - {c['usuario']}: {c['comentario']}")
        else:
            print("💬 Comentarios: (ninguno)")

        print(f"🕒 Fecha: {pub['fecha']}")
        print("-" * 50)