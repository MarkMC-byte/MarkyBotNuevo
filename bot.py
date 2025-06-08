import os
from dotenv import load_dotenv
from modulos.memoria import cargar_historial as cargar_memoria, guardar_historial as guardar_en_memoria
from modulos.ia import responder_ia as responder
from modulos.voz import hablar, escuchar_microfono
from modulos.emociones import detectar_emocion
from modulos.usuario import obtener_nombre_usuario
from modulos.rostro import ejecutar_reconocimiento_facial
import datetime

# Cargar configuración
load_dotenv()
NOMBRE_BOT = "MarkyBot"
modo_path = "datos/modo.txt"
log_path = "datos/logs.txt"

# Función para guardar logs por usuario
def guardar_log(nombre_usuario, mensaje_usuario, respuesta_bot):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {nombre_usuario}: {mensaje_usuario} => {respuesta_bot}\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)

# Función para mostrar menú interactivo
def mostrar_menu():
    print("\n=== MENÚ DE OPCIONES ===")
    print("1. Reconocimiento facial (escribe 'rostro')")
    print("2. Cambiar modo de interacción (escribe 'modo')")
    print("3. Salir del bot (escribe 'salir')\n")

# Función principal
def main():
    os.makedirs("datos", exist_ok=True)
    if not os.path.exists(modo_path):
        with open(modo_path, "w") as f:
            f.write("teclado")

    with open(modo_path, "r") as f:
        modo = f.read().strip()

    nombre_usuario = obtener_nombre_usuario()

    print(f"=== {NOMBRE_BOT.upper()} ===")
    print(f"Hola de nuevo, {nombre_usuario}!")

    print(f"Modo actual: {modo}")
    nuevo_modo = input("¿Quieres cambiar el modo? ('voz' o 'teclado', enter para mantener): ").strip().lower()
    if nuevo_modo in ["voz", "teclado"]:
        modo = nuevo_modo
        with open(modo_path, "w") as f:
            f.write(modo)
        print(f"Modo actualizado a: {modo}")

    memoria = cargar_memoria()

    while True:
        if modo == "voz":
            texto = escuchar_microfono()
        else:
            texto = input("Tú: ")

        if not texto:
            print("No se entendió el mensaje.")
            continue

        if texto.lower() in ["salir", "adiós", "exit"]:
            print("Hasta luego.")
            break

        if texto.lower() == "menu":
            mostrar_menu()
            continue

        if texto.lower() == "modo":
            nuevo_modo = input("Nuevo modo ('voz' o 'teclado'): ").strip().lower()
            if nuevo_modo in ["voz", "teclado"]:
                modo = nuevo_modo
                with open(modo_path, "w") as f:
                    f.write(modo)
                print(f"Modo cambiado a: {modo}")
            continue

        if texto.lower() == "rostro":
            reconocido = ejecutar_reconocimiento_facial()
            if reconocido:
                nombre_usuario = reconocido
                print(f"Rostro reconocido: {nombre_usuario}")
            continue

        emocion = detectar_emocion(texto)
        respuesta = responder(texto)
        print(f"{NOMBRE_BOT} ({emocion}): {respuesta}")

        hablar(respuesta)
        guardar_en_memoria(texto, respuesta)
        guardar_log(nombre_usuario, texto, respuesta)

if __name__ == "__main__":
    main()
