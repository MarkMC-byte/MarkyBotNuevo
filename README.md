
# 🤖 MarkyBot

MarkyBot es un asistente conversacional inteligente con capacidades de voz, reconocimiento facial y memoria de conversación. Puede responder preguntas, reconocer usuarios mediante la cámara, registrar emociones básicas, y recordar interacciones anteriores.

---

## 🧠 Funcionalidades

- 💬 Interacción por **voz** o **teclado**
- 🎤 Reconocimiento de voz con `SpeechRecognition` y `PyAudio`
- 🧠 Memoria conversacional almacenada en JSON
- 🤗 Respuestas generadas por **IA local** (Mistral 7B Instruct con Ollama)
- 😊 Detección de emociones basada en texto
- 👤 Reconocimiento facial con `face_recognition` y `OpenCV`
- 📝 Registro de actividad (logs)

---

## 🚀 Requisitos del sistema

### 🔧 Programas necesarios:

- Python 3.11 o superior
- Git (opcional para clonar repositorio)
- [Ollama](https://ollama.com/) con el modelo **mistral** descargado (`ollama run mistral`)

### 🐍 Librerías de Python:

Instalar todas las dependencias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si `face_recognition` falla por problemas de compilación, instala `dlib-bin` primero:

```bash
pip install dlib-bin
pip install --no-deps face_recognition
```

---

## 📁 Estructura del proyecto

```
BotInteractivo/
│
├── bot.py
├── .env
├── requirements.txt
├── README.md
├── Manual_MarkyBot.pdf
│
├── datos/
│   ├── memoria.json
│   ├── modo.txt
│   ├── rostros/
│   └── audios/
│
├── logs/
│   └── actividad.log
│
├── modulos/
│   ├── __init__.py
│   ├── emociones.py
│   ├── ia.py
│   ├── memoria.py
│   ├── ollama_integrador.py
│   ├── rostro.py
│   ├── usuario.py
│   └── voz.py
```

---

## 🕹 Uso del Bot

1. Ejecuta el bot:

```bash
python bot.py
```

2. Elige el **modo de interacción** (voz o teclado).
3. Escribe o habla con el bot normalmente.
4. Escribe `menu` para abrir el menú de opciones:
   - `rostro` → reconocimiento facial
   - `modo` → cambiar de voz a teclado
   - `salir` → finalizar conversación

---

## ✅ Estado del desarrollo

- 🟢 Funcional
- 🛠 Mejoras en progreso:
  - Soporte para múltiples usuarios reconocidos
  - Mejoras en comprensión emocional
  - Interfaz gráfica futura (GUI)

---

## 🙌 Créditos

Desarrollado junto a **ChatGPT + [markurielMC]**  
IA integrada: `deepseek` con `Ollama`
