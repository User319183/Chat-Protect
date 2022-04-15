import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv



intents = discord.Intents.all()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix="cp-", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=f"for blocked messages"))

bot.remove_command('help')


for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is running on version {discord.__version__}')
    print(f'---------------------------------------')
        

load_dotenv()
token = os.getenv('TOKEN')

bot.run(token)
