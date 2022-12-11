import discord
from discord.ext import commands

class Passives(commands.Cog): # create a class for our cog that inherits from commands.Cog -- Admin Commands

    def __init__(self, bot): # This is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.Cog.listener() # we can add event listeners to our cog
    async def on_member_join(self, member): # this is called when a member joins the server
    # you must enable the proper intents
    # to access this event.
    # See the Popular-Topics/Intents page for more info
        await member.send('Welcome to the server!')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Passives(bot)) # add the cog to the bot