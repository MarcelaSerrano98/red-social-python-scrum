from logica.crearPublicaciones import crear_publicacion
from logica.registro import agregrar_datos
from jsons.json_utils import leer_json
from logica.login import iniciar_sesion

def menu_inicial():
    while True:
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_login()
        elif opcion == "3":
            print("👋 Gracias por usar la red social. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.") 


DATA_FILE = "savefiles/users.json"

def menu_registro():
    while True:
        print("\n===== MENÚ DE REGISTRO DE USUARIO =====")
        print("1. Registrar nuevo usuario")
        print("2. Ver todos los usuarios")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregrar_datos()
        elif opcion == "2":
            usuarios = leer_json(DATA_FILE)
            print("\nUsuarios registrados:")
            for usuario in usuarios:
                print(f"ID: {usuario['ID']}, Nombre: {usuario['Nombre']}, Edad: {usuario['Anhos']}")
        elif opcion == "3":
            print("👋 Saliendo del menú de registro...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

def menu_login():
    while True:
        print("\n===== MENÚ DE LOGIN =====")
        print("1. Iniciar sesión")
        print("2. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = iniciar_sesion()
            menu_principal(usuario)      
        elif opcion == "2":
            print("👋 Regresando...")
            break
        else:
            print("❌ Opción inválida.")

def menu_principal(usuario):
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Crear publicación")
        print("2. Ver publicaciones")
        print("3. Ver usuarios registrados")
        print("4. Buscar usuarios")
        print("5. Cerrar sesión")
    
    

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_publicacion(usuario["Nombre"])
        elif opcion == "2":
            print("👋 Regresando...")
            break
        