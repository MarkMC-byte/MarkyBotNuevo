# emojis.py

# Diccionario de emojis personalizados por emoción
emojis_personalizados = {
    "alegre": "<:alegre:1371286103411392543>",
    "feliz": "<:feliz:1371286488293183558>",
    "sorprendido": "<:sorprendido:1372299120575910021>",
    "molesto": "<:molesto:1372299232568152165>",
    "triste": "<:triste:1372299333311139840>",
    "sonrrojado": "<:sonrrojado:1372299436784353432>",
    "confundido": "<:confundido:1372299712757104670>",
    "durmiendo": "<:Durmiendo:1373047869594140813>",
    "enamorado": "<:Enamorado:1373049156175921152>",
    "riendo": "<:Riendo:1373049753600004196>",
    "travieso": "<:Travieso:1373051289306529892>",
    "cansado": "<:Cansado:1373051370784952361>",
    "analizando": "<:Analizando:1373051437055086682>",
    "asustado": "<:Asustado:1373051504373530645>",
    "bateriabaja": "<:Bateriabaja:1373051667628560515>",
    "temeroso": "<:Temeroso:1373051895807217764>"
}

# Función para obtener emoji por emoción
def obtener_emoji_por_emocion(emocion):
    return emojis_personalizados.get(emocion.lower(), "")
