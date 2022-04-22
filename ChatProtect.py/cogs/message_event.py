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




from discord.ext import tasks








class Message_Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot











    @commands.Cog.listener()
    async def on_message(self, message):

        client = MongoClient("")
        db = client.dbname
        collection = db.dbname
        
        
        

        if message.author != self.bot.user:
            
            

            if bypassuserscollection.find_one({"guild_id": message.guild.id, "member_id": message.author.id}):
                return
            

            if bypasschannelscollection.find_one({"guild_id": message.guild.id, "channel_id": message.channel.id}):
                return
            

            for role in message.author.roles:
                if bypassrolescollection.find_one({"guild_id": message.guild.id, "role_id": role.id}):
                    return
                
                
                message.content = discord.utils.remove_markdown(message.content)
                message.content = re.sub(r'[^\w\s]', '', message.content)
                message.content = re.sub(r'\s+', '', message.content)
                message.content = message.content.lower()


                message.content = re.sub(r'[àáâäæãåā]', 'a', message.content)
                message.content = re.sub(r'[èéêëēėę]', 'e', message.content)
                message.content = re.sub(r'[îïíīįì]', 'i', message.content)
                message.content = re.sub(r'[ôöòóœøōõ]', 'o', message.content)
                message.content = re.sub(r'[ûüùúū]', 'u', message.content)
                message.content = re.sub(r'[ýÿ]', 'y', message.content)
                message.content = re.sub(r'[çćč]', 'c', message.content)
                message.content = re.sub(r'[ñń]', 'n', message.content)
                message.content = re.sub(r'[śšşŝ]', 's', message.content)
                message.content = re.sub(r'[žżź]', 'z', message.content)
                message.content = re.sub(r'[ł]', 'l', message.content)


        
            for word in collection.find({"guild_id": message.guild.id}):
                if word["word"] in message.content:
                    strikescollection.update_one({"guild_id": message.guild.id, "user_id": message.author.id}, {"$inc": {"strikes": 1}}, upsert=True)
                    await message.delete()

                    if enableembedscollection.find_one({"guild_id": message.guild.id, "embeds": "1"}):

                        embed = discord.Embed(title="Message Deleted", description=f"Your message has been deleted {message.author.mention}", color=0x00ff00)
                        embed.add_field(name="Strikes", value=strikescollection.find_one({"guild_id": message.guild.id, "user_id": message.author.id})["strikes"])
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                        await message.channel.send(embed=embed)

                        

                    try:
                        logchannel = logchannelcollection.find_one({"guild_id": message.guild.id})

                        if logchannel:
                        
                            if len(message.content) > 1200:

                                    embed = discord.Embed(title="Message Censored", description=f"{message.author.mention} sent a message found in the censor-list", color=0x00ff00)
                                    embed.add_field(name="Blocked Message", value=f"System message: Message is too big to display..", inline=False)
                                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                                    embed.add_field(name="Strikes", value=strikescollection.find_one({"guild_id": message.guild.id, "user_id": message.author.id})["strikes"])
                                    embed.set_thumbnail(url=message.author.avatar.url)
                                    embed.timestamp = discord.utils.utcnow()
                                    await self.bot.get_channel(logchannel["channel_id"]).send(embed=embed)

                                            



                            else:

                                    embed = discord.Embed(title="Message Censored", description=f"{message.author.mention} sent a message found in the censor-list", color=0x00ff00)
                                    embed.add_field(name="Blocked Message", value=f"{word}", inline=False)
                                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                                    embed.add_field(name="Strikes", value=strikescollection.find_one({"guild_id": message.guild.id, "user_id": message.author.id})["strikes"])
                                    embed.set_thumbnail(url=message.author.avatar.url)
                                    embed.timestamp = discord.utils.utcnow()
                                    await self.bot.get_channel(logchannel["channel_id"]).send(embed=embed)
                                        
                    except:
                        pass



         
         

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        client = MongoClient("")
        db = client.ChatProtect
        collection = db.blacklist
        strikescollection = db.strikes
        bypassuserscollection = db.bypass_users
        bypasschannelscollection = db.bypass_channels
        bypassrolescollection = db.bypass_roles
        enableembedscollection = db.disable_enable
        logchannelcollection = db.logchannel


        if after.author != self.bot.user:
            if bypassuserscollection.find_one({"guild_id": after.guild.id, "member_id": after.author.id}):
                return
            

            if bypasschannelscollection.find_one({"guild_id": after.guild.id, "channel_id": after.channel.id}):
                return
            

            for role in after.author.roles:
                if bypassrolescollection.find_one({"guild_id": after.guild.id, "role_id": role.id}):
                    return
                    
                    
                after.content = discord.utils.remove_markdown(after.content)
                after.content = re.sub(r'[^\w\s]', '', after.content)
                after.content = re.sub(r'\s+', '', after.content)
                
                after.content = after.content.lower()


                after.content = re.sub(r'[àáâäæãåā]', 'a', after.content)
                after.content = re.sub(r'[èéêëēėę]', 'e', after.content)
                after.content = re.sub(r'[îïíīįì]', 'i', after.content)
                after.content = re.sub(r'[ôöòóœøōõ]', 'o', after.content)
                after.content = re.sub(r'[ûüùúū]', 'u', after.content)
                after.content = re.sub(r'[ýÿ]', 'y', after.content)
                after.content = re.sub(r'[çćč]', 'c', after.content)
                after.content = re.sub(r'[ñń]', 'n', after.content)
                after.content = re.sub(r'[śšşŝ]', 's', after.content)
                after.content = re.sub(r'[žżź]', 'z', after.content)
                after.content = re.sub(r'[ł]', 'l', after.content)


        
            for word in collection.find({"guild_id": after.guild.id}):
                if word["word"] in after.content:

                    strikescollection.update_one({"guild_id": after.guild.id, "user_id": after.author.id}, {"$inc": {"strikes": 1}}, upsert=True)
                    await after.delete()
                    
                    if enableembedscollection.find_one({"guild_id": after.guild.id, "embeds": "1"}):
                    
                        
                        embed = discord.Embed(title="Message Deleted", description=f"Your message has been deleted {after.author.mention}", color=0x00ff00)
                        embed.add_field(name="Strikes", value=strikescollection.find_one({"guild_id": after.guild.id, "user_id": after.author.id})["strikes"])
                        embed.set_author(name=after.author.name, icon_url=after.author.avatar.url)
                        await after.channel.send(embed=embed)
            

                        try:
                            logchannel = logchannelcollection.find_one({"guild_id": after.guild.id})
                            if logchannel:
                        
                                if len(after.content) > 1200:

                                        embed = discord.Embed(title="Message Censored", description=f"{after.author.mention} sent a message found in the censor-list", color=0x00ff00)
                                        embed.add_field(name="Blocked Message", value=f"System message: Message is too big to display..", inline=False)
                                        embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                                        embed.add_field(name="Strikes", value=strikescollection.find_one({"guild_id": after.guild.id, "user_id": after.author.id})["strikes"])
                                        embed.set_thumbnail(url=after.author.avatar.url)
                                        embed.timestamp = discord.utils.utcnow()
                                        await self.bot.get_channel(logchannel["channel_id"]).send(embed=embed)

                                            



                                else:

                                        embed = discord.Embed(title="Message Censored", description=f"{after.author.mention} sent a message found in the censor-list", color=0x00ff00)
                                        embed.add_field(name="Blocked Message", value=f"{word}", inline=False)
                                        embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                                        embed.add_field(name="Strikes", value=strikescollection.find_one({"guild_id": after.guild.id, "user_id": after.author.id})["strikes"])
                                        embed.set_thumbnail(url=after.author.avatar.url)
                                        embed.timestamp = discord.utils.utcnow()
                                        await self.bot.get_channel(logchannel["channel_id"]).send(embed=embed)
                                        
                        except:
                            pass


                    


                
                                

    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Message_Events" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Message_Events(bot))
