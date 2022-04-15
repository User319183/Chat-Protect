import discord

from discord.ext import commands

from discord import DMChannel, activity


import discord
from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

import re
import string


from discord.ext import *
from discord.ext.commands import *
from ctypes import *
import datetime

from pymongo import MongoClient

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





load_dotenv()
token = os.getenv('TOKEN')
    


        
        
    

bot.run(token)