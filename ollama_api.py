from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/responder', methods=['POST'])
def responder():
    data = request.get_json()
    mensaje = data.get('mensaje', '')

    # Enviar el mensaje al modelo de IA en Ollama
    try:
        respuesta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": mensaje,
                "stream": False
            }
        )
        respuesta.raise_for_status()
        respuesta_json = respuesta.json()
        return jsonify({"respuesta": respuesta_json.get("response", "Sin respuesta de la IA")})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error al conectar con Ollama: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False)
