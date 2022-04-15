import discord

from discord.ext import commands

from discord import activity

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
from datetime import datetime


import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
from discord.commands import slash_command


import psutil

import uuid

from discord.commands import slash_command

from pymongo import MongoClient










class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




            

                
                

    @slash_command(name="list", description="View the bad word list.")
    @commands.has_guild_permissions(manage_messages=True)
    async def list(self, ctx):

        client = MongoClient("")
        db = client.ChatProtect
        collection = db.blacklist
        #create a list of all the words in the collection
        words = [word["word"] for word in collection.find({"guild_id": ctx.guild.id})]

        if not words:

            embed=discord.Embed(title="Error", color=0x00ff00, description = "There are currently no words in the censor list.")
            await ctx.respond(embed=embed)

        else:
            

            embed=discord.Embed(title="Censor List", color=0x00ff00, description = "The words in the censor list are: \n" + "\n".join(words))
            await ctx.respond(embed=embed)
            

                    
                    


    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "List" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(List(bot))