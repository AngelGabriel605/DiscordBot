# En "main.py"
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.command(name='hey!')
async def hey(ctx):
    await ctx.send(f'Hey!, {ctx.author.name}!')

# Cuando reemplaze TOKEN por su token, NO elimine las comillas('')
client.run('TOKEN')
