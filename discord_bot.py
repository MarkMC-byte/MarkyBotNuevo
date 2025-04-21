import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar el token desde el archivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Historial de conversación por usuario
conversaciones = {}

# Analiza la respuesta para elegir un emoji
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

@bot.event
async def on_ready():
    print(f"✅ MarkyBot está conectado como {bot.user}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="¡pregúntame algo!"))

# 🔹 Comando principal con IA
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

# 🔸 Comando personalizado: saludo
@bot.command(name='saludo')
async def saludo(ctx):
    await ctx.send(f"👋 ¡Hola {ctx.author.mention}! ¿En qué puedo ayudarte hoy?")

# 🔸 Comando personalizado: info
@bot.command(name='info')
async def info(ctx):
    await ctx.send("🤖 Soy MarkyBot, un asistente inteligente con IA. Pídeme lo que necesites usando `!marky`.")

# 🔸 Comando personalizado: ayuda
@bot.command(name='ayuda')
async def ayuda(ctx):
    await ctx.send("🆘 **Comandos disponibles:**\n"
                   "- `!marky [pregunta]` → Pregúntale a la IA\n"
                   "- `!saludo` → Saludo personalizado\n"
                   "- `!info` → Información sobre el bot\n"
                   "- `!ayuda` → Ver este mensaje\n"
                   "- `!hora` → Ver la hora actual\n"
                   "- `!clima` → Saber el clima en Ciudad de México")

# 🔸 Comando personalizado: hora
@bot.command(name='hora')
async def hora(ctx):
    ahora = datetime.now().strftime("%H:%M:%S")
    await ctx.send(f"🕒 La hora actual es: `{ahora}`")

# 🔸 Comando personalizado: clima (versión básica para Ciudad de México)
@bot.command(name='clima')
async def clima(ctx):
    await ctx.send("🌤️ El clima en Ciudad de México está mayormente soleado con 25°C (ejemplo estático).")

# Ejecutar el bot
bot.run(TOKEN)



