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

# Función para obtener emoji dependiendo de la respuesta (estilo clásico)
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
    elif "adiós" in respuesta or "hasta luego" in respuesta:
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
    await bot.add_cog(Moderacion(bot))
    try:
        synced = await bot.tree.sync()
        print(f"✅ Comando slash sincronizado: {len(synced)} comandos.")
    except Exception as e:
        print(f"[ERROR al sincronizar comandos slash] {e}")

# Comando clásico !marky
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

# Comando slash /marky
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

# Comando clásico !emojis
@bot.command(name="emojis")
async def mostrar_emojis(ctx):
    emojis = {
        "Alegre": "<:alegre:1371286103411392543>",
        "Feliz": "<:feliz:1371286488293183558>",
        "Sorprendido": "<:sorprendido:1372299120575910021>",
        "Molesto": "<:molesto:1372299232568152165>",
        "Triste": "<:triste:1372299333311139840>",
        "Sonrojado": "<:sonrrojado:1372299436784353432>",
        "Confundido": "<:confundido:1372299712757104670>",
        "Durmiendo": "<:Durmiendo:1373047869594140813>",
        "Enamorado": "<:Enamorado:1373049156175921152>",
        "Riendo": "<:Riendo:1373049753600004196>",
        "Travieso": "<:Travieso:1373051289306529892>",
        "Cansado": "<:Cansado:1373051370784952361>",
        "Analizando": "<:Analizando:1373051437055086682>",
        "Asustado": "<:Asustado:1373051504373530645>",
        "Batería baja": "<:Bateriabaja:1373051667628560515>",
        "Temeroso": "<:Temeroso:1373051895807217764>",
    }

    mensaje = "**📌 Emojis disponibles de MarkyBot:**\n\n"
    for nombre, emoji in emojis.items():
        mensaje += f"{emoji} **{nombre}**: {emoji}\n"

    await ctx.send(mensaje)

# Comando slash /emojis
@bot.tree.command(name="emojis", description="Muestra los emojis personalizados de MarkyBot")
async def slash_emojis(interaction: discord.Interaction):
    emojis = {
        "Alegre": "<:alegre:1371286103411392543>",
        "Feliz": "<:feliz:1371286488293183558>",
        "Sorprendido": "<:sorprendido:1372299120575910021>",
        "Molesto": "<:molesto:1372299232568152165>",
        "Triste": "<:triste:1372299333311139840>",
        "Sonrojado": "<:sonrrojado:1372299436784353432>",
        "Confundido": "<:confundido:1372299712757104670>",
        "Durmiendo": "<:Durmiendo:1373047869594140813>",
        "Enamorado": "<:Enamorado:1373049156175921152>",
        "Riendo": "<:Riendo:1373049753600004196>",
        "Travieso": "<:Travieso:1373051289306529892>",
        "Cansado": "<:Cansado:1373051370784952361>",
        "Analizando": "<:Analizando:1373051437055086682>",
        "Asustado": "<:Asustado:1373051504373530645>",
        "Batería baja": "<:Bateriabaja:1373051667628560515>",
        "Temeroso": "<:Temeroso:1373051895807217764>",
    }

    mensaje = "**📌 Emojis disponibles de MarkyBot:**\n\n"
    for nombre, emoji in emojis.items():
        mensaje += f"{emoji} **{nombre}**: {emoji}\n"

    await interaction.response.send_message(mensaje)

# Ejecutar el bot
if __name__ == "__main__":
    bot.run(TOKEN)

