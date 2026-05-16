@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$emodji'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$moneda'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$cont'):
        await message.channel.send(contraseña(10))
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")
