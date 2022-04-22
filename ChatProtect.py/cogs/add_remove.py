import discord
from discord.ext import commands
from discord.commands import Option
import re
from discord.commands import slash_command
from pymongo import MongoClient










class Add_Remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




            

                
                

    @slash_command(name="add", description="Add a word to the censor list.")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def add(self, ctx, word: Option(str, "Enter the word to censor.")):

        client = MongoClient("")
        db = client.dbname
        collection = db.dbname
        
        #if any letter is uppercase
        if any(c.isupper() for c in word):
            embed=discord.Embed(title="Error", color=0x00ff00, description = "You can only add words in lowercase.")
            return await ctx.respond(embed=embed)
        

        if re.search(r"[^a-zA-Z0-9]", word):
            embed=discord.Embed(title="Error", color=0x00ff00, description = "You can only add words with letters and numbers. Please remove any symbols as the bot will automaticly detect & remove them.")
            return await ctx.respond(embed=embed)
        


        if collection.find_one({"guild_id": ctx.guild.id, "word": word}):

            embed=discord.Embed(title="Error", color=0x00ff00, description = "This word is already in the censor list.")
            await ctx.respond(embed=embed)
        else:

            collection.insert_one({"guild_id": ctx.guild.id, "word": word})

            embed=discord.Embed(title="Success", color=0x00ff00, description = "This word has successfully been added to the censor list.")
            await ctx.respond(embed=embed)
            
            
            
            
            
            
            

    @slash_command(name="remove", description="Remove a word from the censor list.")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def remove(self, ctx, word: Option(str, "Enter the word to uncensor.")):

        #if any letter is uppercase
        if any(c.isupper() for c in word):
            embed=discord.Embed(title="Error", color=0x00ff00, description = "You can only remove words in lowercase.")
            return await ctx.respond(embed=embed)
        

        if re.search(r"[^a-zA-Z0-9]", word):
            embed=discord.Embed(title="Error", color=0x00ff00, description = "You can only add words with letters and numbers. Please remove any symbols as the bot will automaticly detect & remove them.")
            return await ctx.respond(embed=embed)
            
        client = MongoClient("")
        db = client.dbname
        collection = db.dbname

        if collection.find_one({"guild_id": ctx.guild.id, "word": word}):

            collection.delete_one({"guild_id": ctx.guild.id, "word": word})

            embed=discord.Embed(title="Success", color=0x00ff00, description = "This word has successfully been removed from the censor list")
            await ctx.respond(embed=embed)
            

        else:

            embed=discord.Embed(title="Error", color=0x00ff00, description = "This word is currently not in the censor list")
            await ctx.respond(embed=embed)
                    
            

                    
                    
                    
    

    
    @slash_command(name="clear_list", description="Clear the censor list.")
    @commands.cooldown(1, 5, commands.BucketType.member)
    @commands.has_guild_permissions(manage_messages=True)
    async def clear_list(self, ctx):

        client = MongoClient("")
        db = client.dbname
        collection = db.dbname
        
        #if there are no words in the collection, return a message that the list is already empty
        if collection.find_one({"guild_id": ctx.guild.id}):
            collection.delete_many({"guild_id": ctx.guild.id})

            embed=discord.Embed(title="Success", color=0x00ff00, description = "The censor list has been cleared")
            await ctx.respond(embed=embed)
            

        else:
            embed=discord.Embed(title="Error", color=0x00ff00, description = "The censor list is empty and can not be cleared.")
            await ctx.respond(embed=embed)

                 
                    
                    


    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Add_Remove" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Add_Remove(bot))
