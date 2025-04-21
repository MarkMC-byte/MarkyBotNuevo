import os

RUTA_USUARIO = "datos/usuario.txt"

def obtener_nombre_usuario():
    if os.path.exists(RUTA_USUARIO):
        with open(RUTA_USUARIO, "r", encoding="utf-8") as archivo:
            return archivo.read().strip()
    return None

def guardar_nombre_usuario(nombre):
    os.makedirs(os.path.dirname(RUTA_USUARIO), exist_ok=True)
    with open(RUTA_USUARIO, "w", encoding="utf-8") as archivo:
        archivo.write(nombre)
