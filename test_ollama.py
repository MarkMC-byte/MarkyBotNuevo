from modulos.ollama_integrador import responder_ollama

pregunta = input("Tú: ")
respuesta = responder_ollama(pregunta)
print("Bot:", respuesta)

