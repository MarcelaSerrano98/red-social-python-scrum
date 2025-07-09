from jsons.json_utils import leer_json
from menu.menus import menu_principal, menu_login
from logica.registro import menu_registro_log
from logica.limpiarConsola import limpiarConsola



DATA_FILE = "savefiles/users.json"

def iniciar_sesion():
    print("\n===== INICIAR SESIÓN =====")
    username = input("👤 Nombre de usuario: ")
    password = input("🔒 Contraseña: ")

    usuarios = leer_json(DATA_FILE)

    for usuario in usuarios:
        if usuario["Nombre"] == username and usuario["Contraseña"] == password:
            print(f"✅ ¡Inicio exitoso {username}!") 
            return usuario

    print("❌ Usuario o contraseña incorrectos.")
    return

def menu_inicial_log():
    from menu.menus import menu_inicial, menu_registro, menu_login
    limpiarConsola()
    while True:
        print("✨=== BIENVENIDO A LA RED SOCIAL SNAPBOOK===✨")
        menu_inicial()
        opcion = input("📌 Selecciona una opción: ")
        if opcion == "1":
            limpiarConsola()
            menu_registro_log()
            
        elif opcion == "2":
            limpiarConsola()
            menu_login_log()
            
        elif opcion == "3":
            print("👋 Gracias por usar la red social. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.") 


def menu_login_log():
    limpiarConsola()
    while True:
        menu_login()
        opcion = input("📌 Selecciona una opción: ")

        if opcion == "1":
            limpiarConsola()
            usuario = iniciar_sesion()
            if usuario:
                limpiarConsola()
                menu_principal(usuario)
                """ Cuando menu_principal termina (porque se cerró sesión),"""
                """ rompemos el bucle del menú de login para volver al menú inicial. """
                break 
        elif opcion == "2":
            print("👋 Regresando...")
            limpiarConsola()
            break
        else:
            print("❌ Opción inválida.")

def cerrar_sesion():
    print("🔒 ===== MENÚ DE CIERRE DE SESIÓN =====")
    print("1. 🚪 Cerrar sesion")
    print("2. 🔁 Cancelar")
    opcion_cierre = input("📌 Ingresa la opcion que desees: ")

    if opcion_cierre == "1":
        print("\nQue regreses pronto 🚪")
        print("🔒✅ Sesión cerrada. Regresando al menú principal...\n")
        limpiarConsola()

        return True  # Devuelve True para indicar que se cerró la sesión
    elif opcion_cierre == "2":
        print("🔁 Cancelado. Sigues en sesión.")
        limpiarConsola()

        return False # Devuelve False para indicar que se canceló
    else:
        print("❌ Opción inválida. No se cerrará la sesión.")
        return False