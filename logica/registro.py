from jsons.json_utils import leer_json, escribir_json

DATA_FILE = "savefiles/users.json"

def try_parse_int(s) -> int : 
    try:
        return int(s)
    except ValueError:
        return None

def agregrar_datos():
    """Crear datos en el archivo"""
    users = leer_json(DATA_FILE)
    users_id = try_parse_int(input("Ingresa tu ID: "))
    try:
        ##users_id = int(input("Ingresa tu ID: "))
        name = input("👤 Ingresa tu nombre: ")
        age = int(input("🎂 Ingresa tu edad (debes ser mayor de edad): "))
        password = input("🔒 Ingresa tu contraseña: ")

    except ValueError:
        print ("❌.....ERROR (Dato mal ingresado, intenta nuevamente).....")
        return
    
    if age < 18:
        print("🚫 Debes ser mayor de edad para registrarte.")
        return

    if any(user["ID"] == users_id for user in users):
        print("⚠️ El ID ya está registrado. Usa uno diferente.")
        return
    
    if len(str(users_id)) == 5 :
        print ("✅ID registrado 😄")
    else:
        print("❌ Tu ID debe tener unicamente 5 digitos")
        return

    users.append({
        "ID": users_id,
        "Nombre": name,
        "Anhos": age,
        "Contraseña": password
    })

    escribir_json(DATA_FILE, users)
    print("✅🎉 Usuario creado correctamente.")

def menu_registro_log():
    from menu.menus import menu_registro 
    while True:
        menu_registro()
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregrar_datos()
        elif opcion == "2":
            usuarios = leer_json(DATA_FILE)
            print("\n📋 Usuarios registrados:")
            for usuario in usuarios:
                print(f"ID: {usuario['ID']}, Nombre: {usuario['Nombre']}, Edad: {usuario['Anhos']}")
        elif opcion == "3":
            print("👋 Saliendo del menú de registro...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
