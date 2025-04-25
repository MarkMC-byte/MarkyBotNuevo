import requests

# Llama a la API local de Ollama usando el modelo llama3
def obtener_respuesta(mensaje):
    try:
        respuesta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": mensaje,
                "stream": False
            }
        )
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos.get("response", "Lo siento, no recibí respuesta de la IA.")
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error al conectar con la IA: {str(e)}"
def responder_ia(mensaje, historial=None):
    return obtener_respuesta(mensaje)



