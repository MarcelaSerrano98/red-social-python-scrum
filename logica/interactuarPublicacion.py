from jsons.json_utils import leer_json, escribir_json
from menu.menus import menu_interactuar
from logica.verPublicaciones import ver_publicaciones



ruta_posts= "savefiles/posts.json"

def comentar_publicacion(id_pub):
    comentarios_posts = leer_json(ruta_posts)
    print("Escogiste comentar Publicacion")
    for post in comentarios_posts:
        if post['id'] == id_pub:
            usuario = input("¿Cuál es tu nombre de usuario? ")
            comentario = input("Escribe tu comentario: ")
            
            # Agregar el comentario como diccionario
            post['comentarios'].append({
                "usuario": usuario,
                "comentario": comentario
            })
            escribir_json(ruta_posts, comentarios_posts)
            print("Comentario agregado exitosamente")
            break

def dar_like_publicacion(id_pub):
    like_posts = leer_json(ruta_posts)
    for post in like_posts:
        if post['id'] == id_pub:
            post['likes'] += 1
            print(f"¡Le diste like a la publicación de {post['usuario']}! Ahora tiene {post['likes']} ❤️")
            break

    escribir_json(ruta_posts, like_posts)


def interactuar_pub():
    ver_publicaciones()
    num_pub= int(input("Seleccione el número de la publicación con la que desea interactuar: "))

    posts = leer_json(ruta_posts)
    for post in posts:
        if num_pub == post['id']:
            print (f"---Publicacion de {post['usuario']}---")
            print(f"📘 Libro: {post['libro']}")
            print(f"📝 Reseña: {post['reseña']}")
            print(f"❤️ Likes: {post['likes']}")

            if post["comentarios"]:
                print("💬 Comentarios:")
                for c in post["comentarios"]:
                    print(f"   - {c['usuario']}: {c['comentario']}")
            else:
                print("💬 Comentarios: (ninguno)")
            menu_interactuar()
            
            opcion = input( "Elija una opción: ")
            if opcion == "1":
                comentar_publicacion(num_pub)
            elif opcion == "2":
                dar_like_publicacion(num_pub)
            elif opcion == "3":
                break
    
            




   


    