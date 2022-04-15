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










class Strikes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




            

                
                

    @slash_command(name="update_strikes", description="Update a member's strikes.")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def update_strikes(self, ctx, member: Option(discord.Member, "The member to update strikes."), amount: Option(int, "The amount of strikes to give.")):
        

        if member not in ctx.guild.members:
            embed=discord.Embed(title="Error", color=0x00ff00, description = "That user is not in this server.")
            await ctx.respond(embed=embed)
            

        else:


            client = MongoClient("")
            db = client.ChatProtect
            collection = db.strikes

            collection.update_one({"guild_id": ctx.guild.id, "user_id": member.id}, {"$set": {"strikes": amount}}, upsert=True)
            
            embed=discord.Embed(title="Success", color=0x00ff00, description = "{} now has {} strikes.".format(member.mention, amount))
            await ctx.respond(embed=embed)
        



    @slash_command(name="view_strikes", description="View a member's strikes.")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def view_strikes(self, ctx, member: Option(discord.Member, "The member to view strikes.")):
        

        if member not in ctx.guild.members:
            embed=discord.Embed(title="Error", color=0x00ff00, description = "That user is not in this server.")
            await ctx.respond(embed=embed)
            

        else:

            client = MongoClient("")
            db = client.ChatProtect
            collection = db.strikes

            strikes = collection.find_one({"guild_id": ctx.guild.id, "user_id": member.id})

            embed=discord.Embed(title="Strike Count", color=0x00ff00, description = "{} has {} strikes.".format(member.mention, strikes["strikes"]))
            await ctx.respond(embed=embed)




            

            
            
            

    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Strikes" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Strikes(bot))