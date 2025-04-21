import speech_recognition as sr
import pyttsx3

# Inicializar el motor de voz una sola vez
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar_microfono():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language="es-ES")
        print("Escuchado:", texto)
        return texto
    except sr.UnknownValueError:
        print("No entendí lo que dijiste.")
        return ""

