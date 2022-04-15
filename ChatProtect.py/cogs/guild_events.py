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
import datetime

from discord import Message

import aiohttp



import os  
import discord  
from discord.ext import commands







class guild_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





 
 
 



            



 
 
 
 
 



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
            
        async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add, limit = 1):
            channel = self.bot.get_channel(958769243422339102)


            
            total_users = len(guild.members)
            total_bots = len([member for member in guild.members if member.bot == True])
            total_humans = total_users - total_bots

            e = discord.Embed(title="I've joined a server.", color= 3447003)
            e.add_field(name="Server Name:", value=guild.name, inline=False)
            e.add_field(name="Guild ID", value=guild.id, inline=False)
            e.add_field(name="Guild Owner", value=str(guild.owner), inline=False) 
            e.add_field(name="Bot Inviter", value=f"({entry.user})\n({entry.user.id})\n{entry.user.mention}")
            e.add_field(name="Guild Users", value="{}".format(total_users))
            e.add_field(name="Humans", value=total_humans)
            e.add_field(name="Bots", value=total_bots)
            try:
                e.set_thumbnail(url=guild.icon.url)

            except:
                pass

                    
            e.timestamp = datetime.datetime.utcnow()

            await channel.send(embed=e)

 
 
 




    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        
        
            
            channel = self.bot.get_channel(958769308350152714)

            total_users = len(guild.members)
            total_bots = len([member for member in guild.members if member.bot == True])
            total_humans = total_users - total_bots

            e = discord.Embed(title="I've left a server.", color=15158332)
            e.add_field(name="Server Name:", value=guild.name, inline=False)
            e.add_field(name="Guild ID", value=guild.id, inline=False)
            e.add_field(name="Guild Owner", value=str(guild.owner), inline=False)
            e.add_field(name="Guild Users", value="{}".format(total_users))
            e.add_field(name="Humans", value=total_humans)
            e.add_field(name="Bots", value=total_bots)
            try:
                e.set_thumbnail(url=guild.icon.url)

            except:
                pass

            e.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=e)
    



    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "guild_events" has been loaded!')
        print(f'---------------------------------------')            
                    

    
def setup(bot):
    bot.add_cog(guild_events(bot))