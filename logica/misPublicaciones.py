from jsons.json_utils import leer_json

def ver_perfil(usuario):
    print("\n===== MI PERFIL =====")
    print(f"👤 Nombre: {usuario['Nombre']}")
    print(f"🎂 Edad: {usuario['Anhos']} años")

    # Mostrar publicaciones del usuario
    publicaciones = leer_json("savefiles/posts.json")
    publicaciones_usuario = [p for p in publicaciones if p["usuario"] == usuario["Nombre"]]

    print("\n📚 Tus publicaciones:\n")
    if not publicaciones_usuario:
        print("❌ No has publicado nada aún.")
    else:
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
            print("-" * 50)
