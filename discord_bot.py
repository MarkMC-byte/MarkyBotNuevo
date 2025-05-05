import discord
from discord.ext import commands
from discord import app_commands
import requests
import os
from dotenv import load_dotenv
from moderacion import Moderacion  # Importa directamente la clase Moderacion

# Cargar token de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuración de intents y bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Necesario para moderación
bot = commands.Bot(command_prefix='!', intents=intents)

# Historial por usuario
conversaciones = {}

# Función para obtener emoji dependiendo de la respuesta
def obtener_emoji(respuesta):
    respuesta = respuesta.lower()
    if any(palabra in respuesta for palabra in ["gracias", "de nada"]):
        return "🙏"
    elif any(palabra in respuesta for palabra in ["broma", "chiste", "jaj"]):
        return "😂"
    elif any(palabra in respuesta for palabra in ["error", "problema"]):
        return "⚠️"
    elif any(palabra in respuesta for palabra in ["hola", "bienvenido"]):
        return "👋"
    elif any(palabra in respuesta for palabra in ["adiós", "hasta luego"]):
        return "👋"
    elif "ayuda" in respuesta:
        return "🆘"
    else:
        return "🤖"

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f"✅ MarkyBot está conectado como {bot.user}")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name="¡pregúntame algo!")
    )

# Hook para añadir cogs y sincronizar comandos slash
@bot.event
async def setup_hook():
    await bot.add_cog(Moderacion(bot))  # ← Aquí agregamos la clase Moderacion correctamente
    try:
        synced = await bot.tree.sync()
        print(f"✅ Comando slash sincronizado: {len(synced)} comandos.")
    except Exception as e:
        print(f"[ERROR al sincronizar comandos slash] {e}")

# Comando !marky
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

# Comando /marky
@bot.tree.command(name="marky", description="Hazle una pregunta a Marky (IA)")
@app_commands.describe(pregunta="Tu pregunta para Marky")
async def slash_marky(interaction: discord.Interaction, pregunta: str):
    await interaction.response.defer()
    try:
        usuario_id = str(interaction.user.id)
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
            await interaction.followup.send(f"{respuesta_ia} {emoji}")
        else:
            await interaction.followup.send("⚠️ Hubo un problema con la IA.")
    except Exception as e:
        print(f"[ERROR /marky] {e}")
        await interaction.followup.send("⚠️ Error al conectarse con la IA.")

# Ejecutar el bot
if __name__ == "__main__":
    bot.run(TOKEN)

