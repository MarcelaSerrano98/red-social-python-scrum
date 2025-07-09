from jsons.json_utils import leer_json, escribir_json

def editar_publicacion(nombre_usuario):
    ruta = "savefiles/posts.json"
    publicaciones = leer_json(ruta)

    publicaciones_usuario = [p for p in publicaciones if p["usuario"] == nombre_usuario]

    if not publicaciones_usuario:
        print("❌ No tienes publicaciones para editar.")
        return

    print("\n📝 Tus publicaciones:")
    for i, pub in enumerate(publicaciones_usuario, 1):
        print(f"{i}. 📚 Libro: {pub['libro']}\n   📝 Reseña: {pub['reseña']}\n")

    try:
        seleccion = int(input("📌 Selecciona el número de la publicación que deseas editar: "))
        if seleccion < 1 or seleccion > len(publicaciones_usuario):
            print("❌ Selección inválida.")
            return
    except ValueError:
        print("❌ Entrada no válida.")
        return

    publicacion_objetivo = publicaciones_usuario[seleccion - 1]

    print("\n🛠️ ¿Qué deseas editar?")
    print("1. 📖 Título del libro")
    print("2. ✏️ Reseña")
    opcion = input("📌 Elige una opción: ")

    if opcion == "1":
        nuevo_libro = input("📖 Nuevo título del libro: ")
        publicacion_objetivo["libro"] = nuevo_libro
    elif opcion == "2":
        nueva_resena = input("✏️ Nueva reseña: ")
        publicacion_objetivo["reseña"] = nueva_resena
    else:
        print("❌ Opción no válida.")
        return

    # Reemplazar la publicación editada en la lista completa
    for i, pub in enumerate(publicaciones):
        if pub["id"] == publicacion_objetivo["id"]:
            publicaciones[i] = publicacion_objetivo
            break

    escribir_json(ruta, publicaciones)
    print("✅ Publicación actualizada con éxito.")
