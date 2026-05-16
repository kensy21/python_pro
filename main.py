from discord.ext import commands
from bot_logic import *
import discord
import random


intents = discord.Intents.default()
intents.message_content = True

#$
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def encendido():

    print(f'Tu bot {bot.user} esta en linea')

@bot.command()
async def saludo(ctx):

    await ctx.send('Hola que mas manitooooo')

@bot.command()
async def comandos(ctx):
    await ctx.send("Estos son los comandos que tengo"
                   "$saludo:"
                    "$despedida: aqui tienes que poener un mensaje como chao"
                    "$hola"
                    "$emodji"
                    "$moneda"
                    "$cont")

@bot.command()
async def despedida (ctx, *, mensaje:str):

    #novemo

    mensaje = mensaje.lower().strip()

    if mensaje in 'chao':

        await ctx.send('Chao se me cuida')
    
    elif mensaje in 'bye':

        await ctx.send('Goodbye')

    elif mensaje in 'novemo':

        await ctx.send('nosrevimos')

@bot.command()
async def operacion(ctx, left: int, mensaje:str, right: int):
    if mensaje == "*" or mensaje == "x":
        await ctx.send( left * right)
    elif mensaje == "+":
        await ctx.send( left + right)
    elif mensaje == "-":
        await ctx.send( left - right)
    elif mensaje == "/":
        await ctx.send( left / right)
        

token=""

bot.run(token)

