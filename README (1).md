
# 🤖 MarkyBot (Versión Discord)

MarkyBot es un bot de Discord inteligente con respuestas generadas por IA local (Ollama), comandos personalizados (¡incluyendo comandos Slash!), moderación automática y emojis personalizados con estilo anime cibernético.

---

## 🚀 Funcionalidades principales

- 💬 Interacción con IA local usando `/marky` o `!marky`
- 🧠 Respuestas inteligentes usando modelos locales vía Flask (ej: Deepseek o LLaMA3)
- ❗ Moderación automática de mensajes ofensivos (con advertencias y eliminación)
- 🎭 Emojis personalizados de MarkyBot con emociones anime
- 💡 Comando `/emojis` y `!emojis` para ver todos los emojis disponibles
- 🔧 Sistema de historial de conversación por usuario

---

## ⚙️ Requisitos del sistema

### 📦 Programas necesarios:
- Python 3.11 o superior
- [Ollama](https://ollama.com) (para ejecutar el modelo de IA local)
- Git (opcional, para clonar el repositorio)

### 🐍 Instalación de dependencias:
```bash
pip install -r requirements.txt
```

Asegúrate de tener el modelo en Ollama ejecutando:

```bash
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

---

## 🧪 Comandos disponibles

### 🤖 Comandos IA
- `!marky <pregunta>` → Interactúa con la IA (vía Flask)
- `/marky` → Comando Slash para preguntar

### 🎭 Emojis personalizados
- `!emojis` o `/emojis` → Muestra todos los emojis de MarkyBot listos para copiar

---

## 🛠 Cómo ejecutar MarkyBot

1. Asegúrate de que tu archivo `.env` contenga tu token de Discord:
```
DISCORD_TOKEN=tu_token_aqui
```

2. Inicia tu API Flask (si usas IA local):
```bash
python ollama_api.py
```

3. Inicia el bot:
```bash
python discord_bot.py
```

---

## ☁️ Notas adicionales

- Este bot funciona **100% offline con Ollama** (sin necesidad de APIs de pago como OpenAI).
- Los emojis personalizados están integrados para respuestas y también accesibles por los usuarios.

---

## 🙌 Créditos

Desarrollado por [markurielMC] + ChatGPT  
IA integrada: `Deepseek`, `LLaMA3` o `Mistral` vía [Ollama](https://ollama.com)  
Diseño visual: Emojis de MarkyBot generados por IA (estilo anime cibernético)
