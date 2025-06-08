
# 🤖 MarkyBot (Versión completa)

MarkyBot es un bot inteligente con respuestas generadas por IA local (Ollama), comandos personalizados (¡incluyendo comandos Slash!), moderación automática y emojis personalizados con estilo anime cibernético.


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



## ☁️ Notas adicionales

- Este bot funciona **100% offline con Ollama** (sin necesidad de APIs de pago como OpenAI).
- Los emojis personalizados están integrados para respuestas y también accesibles por los usuarios.

---

## 🙌 Créditos

Desarrollado por [markurielMC] + ChatGPT  
IA integrada: `Deepseek`, `LLaMA3` o `Mistral` vía [Ollama](https://ollama.com)  
Diseño visual: Emojis de MarkyBot generados por IA (estilo anime cibernético)
