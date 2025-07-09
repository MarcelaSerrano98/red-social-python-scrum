from logica.crearPublicaciones import crear_publicacion
from logica.listado_de_usuarios import lista
from logica.verPublicaciones import ver_publicaciones
from logica.misPublicaciones import ver_perfil
from logica.visualizar_perfil_usuarios import visualizar_perfil_usuarios


def menu_inicial():
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")


DATA_FILE = "savefiles/users.json"

def menu_registro():
        print("\n===== MENÚ DE REGISTRO DE USUARIO =====")
        print("1. Registrar nuevo usuario")
        print("2. Ver todos los usuarios")
        print("3. Salir")

def menu_login():
         
         print("\n===== MENÚ DE LOGIN =====")
         print("1. Iniciar sesión")
         print("2. Volver al menú anterior")


def menu_principal(usuario):
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Mi perfil")
        print("2. Crear publicación")
        print("3. Ver publicaciones")
        print("4. Ver usuarios registrados")
        print("5. Interactuar en las publicaciones")
        print("6. Buscar usuarios")
        print("7. Cerrar sesión")
    
    

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_perfil(usuario)
            
        elif opcion == "2":
            crear_publicacion(usuario["Nombre"])
            
        elif opcion == "3": 
            ver_publicaciones()

        elif opcion == "4":
            lista()
        elif opcion == "5":
            from logica.interactuarPublicacion import interactuar_pub
            interactuar_pub()
        elif opcion == "6":
            visualizar_perfil_usuarios()
        elif opcion == "7":
            from logica.login import cerrar_sesion
            """" Si cerrar_sesion() devuelve True, rompemos el bucle del menu_principal """
            if cerrar_sesion():
                break
                               
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
            break
            
            

def menu_interactuar():
    print("\n===== INTERACTUAR CON PUBLICACIONES =====")
    print("1. Comentar")
    print("2. Dar like")
    print("3. Volver al menu anterior")
        
