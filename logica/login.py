from jsons.json_utils import leer_json
from menu.menus import menu_principal
from logica.registro import menu_registro_log

DATA_FILE = "savefiles/users.json"

def iniciar_sesion():
    print("\n===== INICIAR SESIÓN =====")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    usuarios = leer_json(DATA_FILE)

    for usuario in usuarios:
        if usuario["Nombre"] == username and usuario["Contraseña"] == password:
            print(f"✅ ¡Inicio exitoso {username}!")
            return usuario

    print("❌ Usuario o contraseña incorrectos.")
    return None

def menu_inicial_log():
    from menu.menus import menu_inicial, menu_registro, menu_login
    while True:
        menu_inicial()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            menu_registro_log()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("👋 Gracias por usar la red social. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.") 


def menu_login_log():
    while True:
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = iniciar_sesion()
            menu_principal(usuario)      
        elif opcion == "2":
            print("👋 Regresando...")
            break
        else:
            print("❌ Opción inválida.")
