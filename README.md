# 🤖 MarkyBot v2

HEAD
MarkyBot es un asistente inteligente con dos modos de funcionamiento:

1. 🖥️ **Versión Desktop**: funciona en tu computadora usando micrófono, cámara, reconocimiento facial, emociones y texto.
2. 🛰️ **Versión Discord**: se integra en un servidor de Discord con comandos slash, moderación automática y respuestas con IA local.

---

## 📂 Estructura del repositorio

MarkyBot-v2/
├── Desktop/ # Versión clásica por consola (modo local, voz, rostro, emociones)
├── Discord/ # Versión bot de Discord con IA, comandos, emojis y moderación


---

# 🤖 MarkyBot (Versión completa)

MarkyBot es un bot inteligente con respuestas generadas por IA local (Ollama), comandos personalizados (¡incluyendo comandos Slash!), moderación automática y emojis personalizados con estilo anime cibernético.


## 🧠 Requisitos generales

- Python 3.11+
- [Ollama](https://ollama.com) para IA local (modelos como DeepSeek, LLaMA, Mistral)
- Flask para la API local
- Discord Developer Account (si usarás el bot de Discord)
- Micrófono y cámara (si usas la versión Desktop)

---

## 🚀 ¿Cómo ejecutar?

### ▶️ 1. Desktop (modo consola)

```bash
cd Desktop
pip install -r requirements.txt
python bot.py


Incluye:

Entrada por voz o teclado

Respuesta hablada

Reconocimiento facial

Detección de emociones

Memoria persistente


▶️ 2. Discord

cd Discord
pip install -r requirements.txt
python ollama_api.py    # Servidor de IA local
python discord_bot.py   # Inicia el bot de Discord


Incluye:

/marky o !marky → pregunta lo que quieras

/emojis → muestra todos los emojis de MarkyBot

Moderación automática

Memoria por usuario


📘 Documentación incluida
README.md en cada subcarpeta (Desktop/ y Discord/)

Manual_MarkyBot.txt con instrucciones detalladas

🛡️ Seguridad
El archivo .env no se incluye ni debe subirse al repositorio.

Usa .gitignore para proteger claves y archivos temporales.

✨ Créditos
Desarrollado por: MarkMC-byte
Asistencia técnica: ChatGPT
IA Local: Ollama + modelos open-source
Tecnologías: Discord API, OpenCV, Pyttsx3, SpeechRecognition, Flask

📌 Licencia
Este proyecto está bajo la licencia MIT

---

### ✅ ¿Qué hacer ahora?

1. Guarda este contenido como `README.md` dentro de tu carpeta `MarkyBotNuevo`
2. Luego ejecuta desde la terminal:

```bash
HEAD
cd "C:\Users\marco.pedroza\OneDrive - INEGI\Desktop\MarkyBotNuevo"
git add README.md
git commit -m "Agregado README general para MarkyBot-v2 (Desktop + Discord)"
git push

ollama run deepseek-coder  # o mistral/llama3 según el modelo que uses
```

---

## 📁 Estructura del proyecto

```
MarkyBotNuevo/
│
├── discord_bot.py          # Código principal del bot
├── moderacion.py           # Sistema de advertencias/moderación
├── .env                    # (no subir, contiene el token)
├── .env.example            # Ejemplo de archivo .env
├── requirements.txt        # Librerías necesarias
├── README.md               # Este archivo
```



## ☁️ Notas adicionales

- Este bot funciona **100% offline con Ollama** (sin necesidad de APIs de pago como OpenAI).
- Los emojis personalizados están integrados para respuestas y también accesibles por los usuarios.

---

## 🙌 Créditos

Desarrollado por [markurielMC] + ChatGPT  
IA integrada: `Deepseek`, `LLaMA3` o `Mistral` vía [Ollama](https://ollama.com)  
Diseño visual: Emojis de MarkyBot generados por IA (estilo anime cibernético)
