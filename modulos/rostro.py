import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime

RUTA_ROSTROS = "datos/rostros"
RUTA_LOGS = "datos/logs"

os.makedirs(RUTA_ROSTROS, exist_ok=True)
os.makedirs(RUTA_LOGS, exist_ok=True)

def registrar_log(texto):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(RUTA_LOGS, "actividad.log"), "a", encoding="utf-8") as f:
        f.write(f"[{ahora}] {texto}\n")

def registrar_rostro(nombre):
    cap = cv2.VideoCapture(0)
    print("[INFO] Mostrando cámara. Presiona 's' para guardar, 'q' para salir sin guardar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] No se pudo acceder a la cámara.")
            break

        cv2.imshow("Registro de rostro", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ubicaciones = face_recognition.face_locations(rgb_frame)
            if ubicaciones:
                codificacion = face_recognition.face_encodings(rgb_frame, ubicaciones)[0]
                np.save(os.path.join(RUTA_ROSTROS, f"{nombre}.npy"), codificacion)
                print(f"[INFO] Rostro de {nombre} guardado.")
                registrar_log(f"Rostro registrado: {nombre}")
            else:
                print("[ADVERTENCIA] No se detectó ningún rostro. Intenta de nuevo.")
            break
        elif key == ord("q"):
            print("[INFO] Cancelado por el usuario.")
            break

    cap.release()
    cv2.destroyAllWindows()

def reconocer_rostro():
    rostros_codificados = []
    nombres = []

    for archivo in os.listdir(RUTA_ROSTROS):
        if archivo.endswith(".npy"):
            nombre = archivo.replace(".npy", "")
            ruta = os.path.join(RUTA_ROSTROS, archivo)
            codificacion = np.load(ruta)
            rostros_codificados.append(codificacion)
            nombres.append(nombre)

    if not rostros_codificados:
        print("[ERROR] No hay rostros registrados.")
        return None

    cap = cv2.VideoCapture(0)
    print("[INFO] Mostrando cámara. Presiona 'q' para salir.")

    nombre_reconocido = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        ubicaciones = face_recognition.face_locations(rgb_frame)

        for ubicacion in ubicaciones:
            codificacion = face_recognition.face_encodings(rgb_frame, [ubicacion])[0]
            coincidencias = face_recognition.compare_faces(rostros_codificados, codificacion)
            distancias = face_recognition.face_distance(rostros_codificados, codificacion)

            if len(distancias) > 0:
                mejor_match = np.argmin(distancias)
                if coincidencias[mejor_match]:
                    nombre_reconocido = nombres[mejor_match]
                    registrar_log(f"Rostro reconocido: {nombre_reconocido}")
                    print(f"[INFO] Reconocido: {nombre_reconocido}")
                    break

        cv2.imshow("Reconocimiento Facial", frame)
        if cv2.waitKey(1) & 0xFF == ord("q") or nombre_reconocido:
            break

    cap.release()
    cv2.destroyAllWindows()
    return nombre_reconocido

def ejecutar_reconocimiento_facial():
    print("=== RECONOCIMIENTO FACIAL ===")
    print("1. Registrar un nuevo rostro")
    print("2. Reconocer rostro")
    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        nombre = input("Ingresa tu nombre: ")
        registrar_rostro(nombre)
    elif opcion == "2":
        resultado = reconocer_rostro()
        if resultado:
            print(f"Rostro reconocido: {resultado}")
        else:
            print("No se reconoció ningún rostro.")
    else:
        print("Opción inválida.")
