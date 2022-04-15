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










class Bypass_Unbypass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot














    @slash_command(name="bypass_channel", description="Bypass a specific channel.")
    @commands.has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def bypass_channel(self, ctx, channel: Option(discord.TextChannel, "Select a channel")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_channels

        if collection.find_one({"guild_id": ctx.guild.id, "channel_id": channel.id}):
            
            embed=discord.Embed(title="Error", color=0x00ff00, description = "This channel has already been bypassed.")
            await ctx.respond(embed=embed)
        else:
            collection.insert_one({"guild_id": ctx.guild.id, "channel_id": channel.id})
            embed=discord.Embed(title="Success", color=0x00ff00, description = f"Channel {channel.mention} has been added to the bypass list.")
            await ctx.respond(embed=embed)
            
            
            

    @slash_command(name="unbypass_channel", description="Unbypass a specific channel.")
    @commands.has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def unbypass_channel(self, ctx, channel: Option(discord.TextChannel, "Select a channel")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_channels

        if collection.find_one({"guild_id": ctx.guild.id, "channel_id": channel.id}):

                collection.delete_one({"guild_id": ctx.guild.id, "channel_id": channel.id})
                
                embed=discord.Embed(title="Success", color=0x00ff00, description = f"Channel {channel.mention} has been removed from the bypass list.")
                await ctx.respond(embed=embed)
        else:
                embed=discord.Embed(title="Error", color=0x00ff00, description = "This channel is not in the bypass list.")
                await ctx.respond(embed=embed)
                

        
            
            
            

            
            
            

    @slash_command(name="bypass_user", description="Bypass a specific user.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def bypass_user(self, ctx, member: Option(discord.Member, "Select a member to bypass")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_users
        
        if collection.find_one({"guild_id": ctx.guild.id, "member_id": member.id}):
            embed=discord.Embed(title="Error", color=0x00ff00, description = "This user has already been bypassed.")
            await ctx.respond(embed=embed)
            
            await ctx.respond("This user has already been bypassed.")
        else:
            collection.insert_one({"guild_id": ctx.guild.id, "member_id": member.id})
            
            embed=discord.Embed(title="Success", color=0x00ff00, description = f"member {member.mention} has been added to the bypass list.")
            await ctx.respond(embed=embed)


                    
      #create a slash cmd called "unbypass_user" which takes self, ctx and user:discord.Member as arguments
    @slash_command(name="unbypass_user", description="Unbypass a specific user.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def unbypass_user(self, ctx, member: Option(discord.Member, "Select a member to unbypass")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_users
        if collection.find_one({"guild_id": ctx.guild.id, "member_id": member.id}):
                collection.delete_one({"guild_id": ctx.guild.id, "member_id": member.id})
                embed=discord.Embed(title="Success", color=0x00ff00, description = f"Member {member.mention} has been removed from the bypass list.")
                await ctx.respond(embed=embed)
                
        else:
                embed=discord.Embed(title="Error", color=0x00ff00, description = "This user is not in the bypass list.")
                await ctx.respond(embed=embed)


                    



    @slash_command(name="bypass_role", description="Bypass a specific role.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def bypass_role(self, ctx, role: Option(discord.Role, "Select a role to bypass")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_roles
        if collection.find_one({"guild_id": ctx.guild.id, "role_id": role.id}):
            embed=discord.Embed(title="Error", color=0x00ff00, description = "This role has already been bypassed.")
            await ctx.respond(embed=embed)
            
        else:
                collection.insert_one({"guild_id": ctx.guild.id, "role_id": role.id})
                embed=discord.Embed(title="Success", color=0x00ff00, description = f"Role * {role.name} * has been added to the bypass list.")
                await ctx.respond(embed=embed)






    @slash_command(name="unbypass_role", description="Unbypass a specific role.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def unbypass_role(self, ctx, role: Option(discord.Role, "Select a role to unbypass")):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_roles
        if collection.find_one({"guild_id": ctx.guild.id, "role_id": role.id}):
                collection.delete_one({"guild_id": ctx.guild.id, "role_id": role.id})
                
                embed=discord.Embed(title="Success", color=0x00ff00, description = f"Role {role.name} has been removed from the bypass list.")
                await ctx.respond(embed=embed)
        else:
                embed=discord.Embed(title="Error", color=0x00ff00, description = f"This role has not yet been bypassed.")
                await ctx.respond(embed=embed)
                            





    @slash_command(name="view_bypass", description="View all bypassed roles, users, and channels.")
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def view_bypass(self, ctx):
        client = MongoClient("")
        db = client.ChatProtect
        collection = db.bypass_channels
        collection2 = db.bypass_users
        collection3 = db.bypass_roles
        
        #create a list of all channels in the bypass_channels collection
        bypass_channels = []
        for channel in collection.find({"guild_id": ctx.guild.id}):
            bypass_channels.append(channel)
        #create a list of all users in the bypass_users collection
        bypass_users = []
        for user in collection2.find({"guild_id": ctx.guild.id}):
            bypass_users.append(user)
        #create a list of all roles in the bypass_roles collection
        bypass_roles = []
        for role in collection3.find({"guild_id": ctx.guild.id}):
            bypass_roles.append(role)


        #send an embed with all the bypassed channels, users, and roles
        embed = discord.Embed(title="Bypassed items", description="View the list of bypassed guild items" , color=0x00ff00)
        #create a feild for each item in the list
        
        #if channels bypassed is empty, add a field saying so
        if bypass_channels == []:
            embed.add_field(name="Channels", value="No channels have been bypassed.")
        else:
            embed.add_field(name="Channels", value="\n".join([f"<#{channel['channel_id']}>" for channel in bypass_channels]))
            
            #if users bypassed is empty, add a field saying so
        if bypass_users == []:
            embed.add_field(name="User", value="No users have been bypassed.")
        else:
            embed.add_field(name="User IDs", value="\n".join([f"{user['member_id']}" for user in bypass_users]))
            
            #if roles bypassed is empty, add a field saying so
        if bypass_roles == []:
            embed.add_field(name="Roles", value="No roles have been bypassed.")
        else:
            embed.add_field(name="Role IDs", value="\n".join([f"{role['role_id']}" for role in bypass_roles]))
        await ctx.respond(embed=embed)
            
                
                
                
                
                
                
                
                

    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Bypass_Unbypass" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Bypass_Unbypass(bot))