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










class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @slash_command(name="logchannel", description="When the user says a censored word, send it specified channel.")
    @commands.has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def log_channel(self, ctx, channel: Option(discord.TextChannel, "Select a channel")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.logchannel


        collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"channel_id": channel.id}}, upsert=True)
        embed=discord.Embed(title="Success", color=0x00ff00, description = "Log channel has been set to {}".format(channel.mention))
        await ctx.respond(embed=embed)

                    
                    


    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Logging" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Logging(bot))