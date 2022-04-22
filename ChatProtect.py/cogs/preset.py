import discord
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command
from pymongo import MongoClient 



racisim_words = ["nigga", "nigger", "nigg", "niger", "retard", "returd", "uppity", "peanutgallery", "bugger", "bamboula", "balija"]

bad_words = ["fuc", "shit", "cock", "penis", "feck", "arse", "tit", "pussy", "dick"]

toxic_words = ["dumb", "cunt", "idiot", "looser", "dickhead", "kill", "suicide", "death", "dum", "stupid", "fag", "fatass"]

tenor = ["httpstenorcom"]
    


class Presets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

     

                
                

    @slash_command(name="preset", description="Create a pre-built censor list.")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def preset(self, ctx, filter: Option(str, "Enable a pre-built filter for the bot. All of the previous censored words will be removed. ", choices=["racisim", "badwords", "toxicity", "tenor"]),):

        client = MongoClient("")
        db = client.dbname
        collection = db.dbname
        
        if filter == "racisim":
            collection.delete_many({"guild_id": ctx.guild.id})

            for word in racisim_words:
                collection.insert_one({"guild_id": ctx.guild.id, "word": word})
            embed=discord.Embed(title="Success", color=0x00ff00, description = "Anti-racisim filter has been enabled.")
            await ctx.respond(embed=embed)

        elif filter == "badwords":
            collection.delete_many({"guild_id": ctx.guild.id})
            for word in bad_words:
                collection.insert_one({"guild_id": ctx.guild.id, "word": word})
            embed=discord.Embed(title="Success", color=0x00ff00, description = "Anti-bad-words filter has been enabled.")
            await ctx.respond(embed=embed)
        elif filter == "toxicity":
            collection.delete_many({"guild_id": ctx.guild.id})
            for word in toxic_words:
                collection.insert_one({"guild_id": ctx.guild.id, "word": word})
            embed=discord.Embed(title="Success", color=0x00ff00, description = "Anti-toxicity filter has been enabled.")
            await ctx.respond(embed=embed)
            

        elif filter == "tenor":
            collection.delete_many({"guild_id": ctx.guild.id})
            for word in tenor:
                collection.insert_one({"guild_id": ctx.guild.id, "word": word})
            embed=discord.Embed(title="Success", color=0x00ff00, description = "Anti-tenor filter has been enabled.")
            await ctx.respond(embed=embed)











    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Presets" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Presets(bot))
