import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json



from discord.ext import *
from discord.ext.commands import *
from ctypes import *







class Error_Handler(commands.Cog):
	def __init__(self, bot):
		self.bot = bot





	@commands.Cog.listener()
	async def on_application_command_error(self, ctx, error):
		embed = discord.Embed(title="An Error Occured", color=0x00ff00, description=f"```{str(error)}```")      
		embed.timestamp = discord.utils.utcnow() 
		await ctx.respond(embed=embed, ephemeral=True)
  
  
  

    

	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Error_Handler" has been loaded!')
		print(f'---------------------------------------')


def setup(bot):
	bot.add_cog(Error_Handler(bot))






