import json
import os

RUTA_MEMORIA = "memoria_conversaciones.json"

def cargar_historial():
    if os.path.exists(RUTA_MEMORIA):
        with open(RUTA_MEMORIA, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def guardar_historial(historial):
    with open(RUTA_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=2, ensure_ascii=False)



