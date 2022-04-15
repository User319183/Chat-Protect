import discord

from discord.ext import commands
from datetime import datetime
from discord.commands import slash_command
import datetime, time


global startTime
startTime = time.time()



class BasicCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




            

                
                
                    
                    


    @slash_command(name="info", description="General information about the bot.")
    @commands.cooldown(1, 20, commands.BucketType.guild)
    async def info(self, ctx):


        embed = discord.Embed(title="Info", description="This is general information about me.", color=0x00ff00)
        embed.add_field(name="Bot developers:", value="User319183#3149\nTheWizz1338#6367\nAnonymousDev#3773", inline=False)
        embed.add_field(name="Server Count:", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Users being watched:", value=len(self.bot.users), inline=False)
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed.add_field(name="Uptime:", value=uptime, inline=False)
        embed.add_field(name="Websocket ping:", value=f"{round(self.bot.latency * 1000)}")
        embed.add_field(name="Version:", value="1.0.1", inline=False)
        embed.add_field(name="Invite:", value=f"https://discord.com/oauth2/authorize?client_id=957668017079222303&permissions=8&scope=bot%20applications.commands", inline=False)
        embed.add_field(name="Support Server:", value="https://discord.gg/ecz2z36gkB", inline=False)     
        await ctx.respond(embed=embed, ephemeral=True)
        
        
        
        
        
        
    @slash_command(name="help", description="Default help panel")
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def help(self, ctx):
        embed=discord.Embed(title="Help Panel", color=0x00ff00, description = "The command you need for help.", url="https://discord.gg/ecz2z36gkB")
        embed.add_field(name = "Please visit our help page here", value = "https://github.com/User319183/Chat-Protect/blob/main/README.md", inline = False)
        await ctx.respond(embed=embed, ephemeral=True)

        
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Basic Commands" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(BasicCmds(bot))
