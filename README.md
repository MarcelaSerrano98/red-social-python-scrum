# 📚 SnapBook - Red Social para Lectores

¡Bienvenido a **SNAPBOOK**!  
Una pequeña red social en Python (consola) pensada para **amantes de los libros**. Aquí podrás compartir tus lecturas, comentar publicaciones de otros lectores y conectar con una comunidad que disfruta el placer de leer tanto como tú.

---

## 🚀 Características principales

- ✅ Registro e inicio de sesión con credenciales.
- ✍️ Crear publicaciones para compartir tus pensamientos o reseñas.
- 👀 Ver publicaciones de toda la comunidad.
- ❤️ Dar "Me gusta" a los posts que te interesen.
- 💬 Comentar publicaciones para iniciar conversaciones.
- 📋 Listar todos los usuarios registrados.
- 🖥️ Menús claros en consola para una navegación sencilla.
- ⚠️ Mensajes de error amigables y flujo intuitivo.

---

## 🛠 Instalación y ejecución

### ✅ Requisitos
- Python 3.9 o superior

### 🔥 Cómo ejecutar el proyecto
1. Clona este repositorio:
    ```bash
    git clone https://github.com/MarcelaSerrano98/red-social-python-scrum.git
    ```

2. Accede a la carpeta del proyecto y ejecuta el programa con:
    ```bash
    cd red-social-python-scrum
    python -m app.main
    ```

✅ ¡Y listo! Ya puedes registrarte o iniciar sesión y comenzar a usar **LectoRed**.

---

## 📂 Estructura del proyecto

├── app/
│ └── main.py # Punto de entrada principal
├── jsons/
│ └── json_utils.py # Funciones para leer y escribir JSON
├── logica/
│ ├── crearPublicacion.py
│ ├── interactuarPublicacion.py
│ └── ... # Otras funciones de lógica del negocio
├── menu/
│ └── menus.py # Todos los menús de interacción en consola
├── savefiles/
│ ├── users.json # Datos de usuarios
│ └── posts.json # Publicaciones
└── README.md


### 📌 Breve descripción de carpetas
- **`jsons/`**: Funciones utilitarias para manipular archivos JSON (leer, escribir).
- **`logica/`**: Toda la lógica del negocio (crear posts, dar likes, comentar, etc.).
- **`menu/`**: Funciones para mostrar y controlar los menús.
- **`savefiles/`**: Archivos JSON donde se guardan usuarios y publicaciones.

---

## 👥 Equipo del proyecto

- **Owner**: Marcela Albarracín
- **Scrum Master**: Sara Balaguera
- **Developers**: Juan David y Sebastián Jaimes

---

✨ ¡Disfruta el proyecto y sigue compartiendo tus lecturas con el mundo!
