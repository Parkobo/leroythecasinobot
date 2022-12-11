import discord
from discord.ext import commands

class UserActions(commands.Cog): # Create a class for our cog that inherits from commands.Cog -- Admin Commands

    def __init__(self, bot): # This is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.slash_command()
    async def goodbye(self, ctx):
        await ctx.respond('Test')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(UserActions(bot)) # add the cog to the bot