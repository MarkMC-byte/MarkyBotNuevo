import json
import os

RUTA_MEMORIA = "datos/memoria.json"

def cargar_memoria():
    if os.path.exists(RUTA_MEMORIA):
        with open(RUTA_MEMORIA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return {"conversaciones": []}

def guardar_en_memoria(pregunta, respuesta):
    memoria = cargar_memoria()
    memoria["conversaciones"].append({"pregunta": pregunta, "respuesta": respuesta})
    with open(RUTA_MEMORIA, "w", encoding="utf-8") as archivo:
        json.dump(memoria, archivo, ensure_ascii=False, indent=4)

def mostrar_memoria():
    memoria = cargar_memoria()
    if memoria["conversaciones"]:
        for i, conv in enumerate(memoria["conversaciones"], 1):
            print(f"{i}. Tú: {conv['pregunta']}")
            print(f"   Bot: {conv['respuesta']}")
    else:
        print("No hay memoria guardada todavía.")


