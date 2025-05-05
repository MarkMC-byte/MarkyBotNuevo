import discord
from discord.ext import commands
from collections import defaultdict
import asyncio

# Diccionario para advertencias por usuario
advertencias = defaultdict(int)

# Tabla de sanciones (escalada)
sanciones = [
    (3, 120),        # 2 minutos
    (5, 420),        # 7 minutos
    (10, 900),       # 15 minutos
    (15, 1800),      # 30 minutos
    (20, 3600),      # 1 hora
    (25, 43200),     # 12 horas
    (35, 86400),     # 1 día
    (50, 604800),    # 1 semana
    (75, "kick"),
    (100, "ban"),
]

# Lista extendida de palabras prohibidas
PALABRAS_PROHIBIDAS = [
    "bastardo", "cabrón", "chinga", "chingar", "coño", "culero", "estupida", "estúpido",
    "gilipollas", "hdp", "hpta", "idiota", "imbecil", "imbécil", "inútil", "jodete",
    "maldito", "malnacido", "mamon", "marica", "maricón", "mierda", "pendejo", "perra",
    "puta", "tonto", "verga", "zorra"
]

# Registro de spam por usuario
spam_mensajes = defaultdict(list)

def obtener_sancion(n):
    for limite, accion in sanciones:
        if n < limite:
            return accion
    return "ban"

async def aplicar_sancion(usuario, canal):
    n = advertencias[usuario.id]
    sancion = obtener_sancion(n)

    if isinstance(sancion, int):
        mute_rol = discord.utils.get(usuario.guild.roles, name="Muted")
        if mute_rol:
            await usuario.add_roles(mute_rol)
            await canal.send(f"🔇 {usuario.mention} ha sido silenciado por {sancion // 60} minuto(s).")
            await asyncio.sleep(sancion)
            await usuario.remove_roles(mute_rol)
            await canal.send(f"🔊 {usuario.mention} ya puede hablar de nuevo.")
    elif sancion == "kick":
        await canal.send(f"👢 {usuario.mention} ha sido **expulsado** por acumular {n} advertencias.")
        await usuario.kick(reason="Demasiadas advertencias.")
    elif sancion == "ban":
        await canal.send(f"⛔ {usuario.mention} ha sido **baneado** por acumular {n} advertencias.")
        await usuario.ban(reason="Demasiadas advertencias.", delete_message_days=1)

class Moderacion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return

        ahora = message.created_at.timestamp()
        user_id = message.author.id
        spam_mensajes[user_id].append(ahora)
        spam_mensajes[user_id] = [t for t in spam_mensajes[user_id] if ahora - t < 5]

        # Detección de spam
        if len(spam_mensajes[user_id]) >= 3:
            advertencias[user_id] += 1
            await message.channel.send(
                f"⚠️ {message.author.mention}, ¡no hagas spam! Recibes una advertencia ({advertencias[user_id]})"
            )
            await aplicar_sancion(message.author, message.channel)
            return

        # Detección de malas palabras
        contenido = message.content.lower()
        if any(palabra in contenido for palabra in PALABRAS_PROHIBIDAS):
            advertencias[user_id] += 1
            await message.delete()
            await message.channel.send(
                f"🚫 {message.author.mention}, ese lenguaje no está permitido. Advertencia {advertencias[user_id]}"
            )
            await aplicar_sancion(message.author, message.channel)

    @commands.command()
    async def advertencias(self, ctx, miembro: discord.Member = None):
        miembro = miembro or ctx.author
        n = advertencias.get(miembro.id, 0)
        await ctx.send(f"📋 {miembro.mention} tiene **{n} advertencia(s)**.")

def setup_moderacion(bot):
    bot.add_cog(Moderacion(bot))
