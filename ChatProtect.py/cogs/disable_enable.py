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

import datetime, time






class Disable_Enable(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




            

                
                
                    
                    


    @slash_command(name="embeds", description="Enable or disable the embeds on the warn message.")
    @commands.cooldown(1, 5, commands.BucketType.member)
    @commands.has_guild_permissions(manage_messages=True)
    async def embeds(self, ctx, set: Option(str, "Set if you want the censor list embeds enabled or disabled ", choices=["enabled", "disabled"]),):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.disable_enable
        if set == "disabled":

                collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"embeds": "0"}}, upsert=True)
                embed=discord.Embed(title="Success", color=0x00ff00, description = "Embeds are now disabled.")
                await ctx.respond(embed=embed)
        elif set == "enabled":
                collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"embeds": "1"}}, upsert=True)
                
                embed=discord.Embed(title="Success", color=0x00ff00, description = "Embeds are now enabled.")
                await ctx.respond(embed=embed)

            


        

        
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Disable_Enable" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Disable_Enable(bot))