from logica.crearPublicaciones import crear_publicacion
from logica.editarMisPublicaciones import editar_publicacion
from logica.listado_de_usuarios import lista
from logica.verPublicaciones import ver_publicaciones
from logica.misPublicaciones import ver_perfil
from logica.visualizar_perfil_usuarios import visualizar_perfil_usuarios
from logica.editarMisPublicaciones import editar_publicacion


def menu_inicial():
        print("="*50)
        print("1. 📝 Registrarse")
        print("2. 🔐 Iniciar sesión")
        print("3. 🚪 Salir")
        print("="*50)



DATA_FILE = "savefiles/users.json"

def menu_registro():
        print("\n===== MENÚ DE REGISTRO DE USUARIO =====")
        print("1. 👤 Registrar nuevo usuario")
        print("2. 📋 Ver todos los usuarios")
        print("3. 🔙 Volver menú anterior")

def menu_login():
         
         print("\n🔐===== MENÚ DE LOGIN =====🔐")
         print("1. 🔑 Iniciar sesión")
         print("2. 🔙 Volver al menú anterior")


def menu_principal(usuario):
    while True:
        print("\n===== 📱 MENÚ PRINCIPAL 📱 =====")
        print("1. 👤 Mi perfil")
        print("2. ✍️  Crear publicación")
        print("3. 📰 Ver publicaciones")
        print("4. 🛠️  Editar mis publicaciones")
        print("5. 📋 Ver usuarios registrados")
        print("6. 💬 Interactuar en las publicaciones")
        print("7. 🔍 Buscar usuarios")
        print("8. 🚪 Cerrar sesión")
    
    

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_perfil(usuario)
            input("👉 Pulsa ENTER para continuar")
            
        elif opcion == "2":
            crear_publicacion(usuario["Nombre"])
            input("👉 Pulsa ENTER para continuar")

            
        elif opcion == "3": 
            ver_publicaciones()
            input("👉 Pulsa ENTER para continuar")

        elif opcion == "4": 
            editar_publicacion(usuario["Nombre"])
            input("👉 Pulsa ENTER para continuar")

        elif opcion == "5":
            lista()
            input("👉 Pulsa ENTER para continuar")

        elif opcion == "6":
            from logica.interactuarPublicacion import interactuar_pub
            interactuar_pub()
            input("👉 Pulsa ENTER para continuar")

        elif opcion == "7":
            visualizar_perfil_usuarios()
            input("👉 Pulsa ENTER para continuar")

        elif opcion == "8":
            print("Que vuelvas pronto🚪")
            break
        else:
            print("🚫 Opcion invañida: Debe ser un numero del 1 al 8")
            input("👉 Pulsa ENTER para continuar")

            
            

def menu_interactuar():
    print("\n===== INTERACTUAR CON PUBLICACIONES =====")
    print("1. ✏️  Comentar")
    print("2. 👍 Dar like")
    print("3. 🔙 Volver al menu anterior")
        
        
    
def menu_cerrar_sesion():
    print()
           
