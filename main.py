# In "main.py"
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.command(name='hey!')
async def hey(ctx):
    await ctx.send(f'Hey!, {ctx.author.name}!')

# When you paste your token, don't forget to remove the quotes
client.run('TOKEN')
