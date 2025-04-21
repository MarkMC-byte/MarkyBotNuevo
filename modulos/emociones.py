# modulos/emociones.py

def detectar_emocion(texto):
    texto = texto.lower()

    emociones = {
        "felicidad": ["feliz", "contento", "alegre", "genial", "excelente", "maravilloso"],
        "tristeza": ["triste", "deprimido", "llorar", "solo", "sola", "desanimado"],
        "enojo": ["enojado", "molesto", "furioso", "fastidiado", "ira", "rabia"],
        "miedo": ["miedo", "asustado", "nervioso", "preocupado", "temor"],
        "amor": ["amor", "te quiero", "te amo", "querido", "cariño"],
        "sorpresa": ["sorprendido", "wow", "no esperaba", "impresionante", "increíble"]
    }

    for emocion, palabras_clave in emociones.items():
        for palabra in palabras_clave:
            if palabra in texto:
                return emocion

    return "neutral"

