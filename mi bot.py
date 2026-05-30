from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def encendido():

    print(f'Tu bot {bot.user} esta en linea')
@bot.command()
async def comandos(ctx):
    await ctx.send("saludo:  medioabiente:   (preguntas: por que es importante?, que podemos hacer?, que se puede reciclar?)")

@bot.command()
async def saludos(ctx):
    await ctx.send("Hola bro!!")

@bot.command()
async def medioambiente(ctx):
    await ctx.send("Es el entorno donde vivimos y del que dependemos para obtener los recursos necesarios para la vida.")

@bot.command()
async def preguntas(ctx, *, mensaje:str):
    mensaje = mensaje.lower().strip()

    if mensaje in "por que es importante?":
        await ctx.send("El medioambiente es importante porque nos proporciona los recursos necesarios para vivir, como aire limpio, agua, alimentos y energía.  Además, mantiene el equilibrio de los ecosistemas y ayuda a proteger la salud y el bienestar de todos los seres vivos.")

    elif mensaje in "que podemos hacer?":
        await ctx.send("Para cuidar el medioambiente debemos reducir la contaminación, reciclar los residuos y ahorrar agua y energía.")

    elif mensaje in " que se puede reciclar?":
        await ctx.send("Algunos materiales que se pueden reciclar en casa son: 1:Papel y cartón (periódicos, cajas, revistas).  2:Plástico (botellas, envases y recipientes).  3:Vidrio (botellas y frascos).  4:Metal (latas de aluminio y conservas).  5:Envases de cartón para bebidas (como cajas de leche o jugo).")


token=""

bot.run(token)
