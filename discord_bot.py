import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

# Cargar token de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuración de intents y bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Historial por usuario
conversaciones = {}

# Función para obtener emoji dependiendo de la respuesta
def obtener_emoji(respuesta):
    if "gracias" in respuesta.lower() or "de nada" in respuesta.lower():
        return "🙏"
    elif "broma" in respuesta.lower() or "chiste" in respuesta.lower() or "jaj" in respuesta.lower():
        return "😂"
    elif "error" in respuesta.lower() or "problema" in respuesta.lower():
        return "⚠️"
    elif "hola" in respuesta.lower() or "bienvenido" in respuesta.lower():
        return "👋"
    elif "adiós" in respuesta.lower() or "hasta luego" in respuesta.lower():
        return "👋"
    elif "ayuda" in respuesta.lower():
        return "🆘"
    else:
        return "🤖"

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f"✅ MarkyBot está conectado como {bot.user}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="¡pregúntame algo!"))

# Comando !marky para interactuar con la IA
@bot.command(name='marky')
async def preguntar_ia(ctx, *, pregunta: str):
    try:
        usuario_id = str(ctx.author.id)
        mensaje_pensando = await ctx.send("💬 Estoy pensando...")

        historial = conversaciones.get(usuario_id, [])
        historial.append({"role": "user", "content": pregunta})

        respuesta = requests.post(
            "http://127.0.0.1:5000/responder",
            json={"mensaje": pregunta, "historial": historial}
        )

        if respuesta.status_code == 200:
            data = respuesta.json()
            respuesta_ia = data["respuesta"]

            historial.append({"role": "assistant", "content": respuesta_ia})
            conversaciones[usuario_id] = historial[-10:]

            emoji = obtener_emoji(respuesta_ia)
            await mensaje_pensando.edit(content=f"{respuesta_ia} {emoji}")
        else:
            await mensaje_pensando.edit(content="⚠️ Hubo un problema con la IA.")
    except Exception as e:
        print(f"[ERROR] {e}")
        await ctx.send("⚠️ Error al conectarse con la IA.")

# Ejecutar el bot
bot.run(TOKEN)


