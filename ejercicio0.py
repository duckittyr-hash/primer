import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


bot.run("PUT YOUR TOKEN HERE")






meme_dict = {
    "cringe": "Algo raro ",
    "lol":"Respuesta a algo gracioso",
    "creepy": "Algo aterrador",
    "rolf": "Respuesta a algo gracioso",
    "sheesh": "ligera desaprobación"
}

print("Escribe en minúscula las palabras ")

for i in range (5): #bucle
    word = input("Escribe una palabra que no entiendas")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No tenemos la palabra")
