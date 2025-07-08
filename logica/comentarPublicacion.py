from jsons.json_utils import leer_json

ruta_posts= "savefiles/posts.json"

def leer_json_posts():
    posts= leer_json(ruta_posts)
    for i,post in enumerate(posts):
        print(f"{i+1}.")
        print(f"post: {post['libro']}")

def Interactuar_publicaciones():
    leer_json_posts()
    print ("Escoja el # de la publicación con la que desea interactuar")
    