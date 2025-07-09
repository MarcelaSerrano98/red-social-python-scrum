
from jsons.json_utils import leer_json
ruta= "savefiles/users.json"

def lista():
    usuarios= leer_json(ruta)
    print("📋 Has seleccionado ver la lista de usuarios")
    print("👥 Lista de usuarios")
    print("=========================================")
    for usuario in usuarios:
        print(f"👤 Usuario: {usuario['Nombre']}")
        print(f"🆔 Código: {usuario['ID']}")
        print(f"🎂 Edad: {usuario['Anhos']} años")
        print("-" * 50)
    
    
