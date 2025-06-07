import discord
from discord.ext import commands
from collections import defaultdict

# Diccionario para advertencias por usuario
advertencias = defaultdict(int)

# Lista de palabras prohibidas
PALABRAS_PROHIBIDAS = [
    "bastardo", "cabrón", "chinga", "chingar", "coño", "culero", "estupida", "estúpido",
    "gilipollas", "hdp", "hpta", "idiota", "imbecil", "imbécil", "inútil", "jodete",
    "maldito", "malnacido", "mamon", "marica", "maricón", "mierda", "pendejo", "perra",
    "puta", "tonto", "verga", "zorra"
]

# Registro de mensajes para detectar spam
spam_mensajes = defaultdict(list)

class Moderacion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return

        contenido = message.content.lower()
        user_id = message.author.id

        # Detección de malas palabras
        if any(palabra in contenido for palabra in PALABRAS_PROHIBIDAS):
            advertencias[user_id] += 1
            await message.delete()
            await message.channel.send(
                f"🚫 {message.author.mention}, tu mensaje fue eliminado por lenguaje inapropiado. Advertencia #{advertencias[user_id]}",
                delete_after=5
            )
            return

        # Detección de spam (3 mensajes en 5 segundos)
        ahora = message.created_at.timestamp()
        spam_mensajes[user_id].append(ahora)
        spam_mensajes[user_id] = [t for t in spam_mensajes[user_id] if ahora - t < 5]

        if len(spam_mensajes[user_id]) >= 3:
            advertencias[user_id] += 1
            await message.delete()
            await message.channel.send(
                f"⚠️ {message.author.mention}, tu mensaje fue eliminado por spam. Advertencia #{advertencias[user_id]}",
                delete_after=5
            )

    @commands.command()
    async def advertencias(self, ctx, miembro: discord.Member = None):
        miembro = miembro or ctx.author
        n = advertencias.get(miembro.id, 0)
        await ctx.send(f"📋 {miembro.mention} tiene **{n} advertencia(s)**.")

def setup_moderacion(bot):
    bot.add_cog(Moderacion(bot))
