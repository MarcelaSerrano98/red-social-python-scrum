
from jsons.json_utils import leer_json
ruta= "savefiles/users.json"

def lista():
    usuarios= leer_json(ruta)
    print ("Haz seleccionado ver la lista de usuarios")
    print ("Lista de usuarios")                                                                
    print ("-----------------------------------------")
    for usuario in usuarios:
        print (f"Usuario: {usuario['Nombre']}")
        print(f"Codigo: {usuario['ID']}")
        print(f"Edad: {usuario['Anhos']}") 
        print ("-" *50)
    
    
