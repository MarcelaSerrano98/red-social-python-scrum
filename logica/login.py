from jsons.json_utils import leer_json

DATA_FILE = "savefiles/users.json"

def iniciar_sesion():
    print("\n===== INICIAR SESIÓN =====")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    usuarios = leer_json(DATA_FILE)

    for usuario in usuarios:
        if usuario["Nombre"] == username and usuario["Contraseña"] == password:
            print(f"✅ ¡Inicio exitoso {username}!")
            return True

    print("❌ Usuario o contraseña incorrectos.")
    return False