from discord import ApplicationContext as AppCtx, Bot
from discord.ext import commands
import data_methods as db
import discord

bot = Bot(intents=discord.Intents.all())

class UserActions(commands.Cog): # Create a class for our cog that inherits from commands.Cog -- Admin Commands

    def __init__(self, bot): # This is a special method that is called when the cog is loaded
        self.bot = bot

    @bot.slash_command()
    async def register(self, ctx: AppCtx):
        await db.create_player(ctx=ctx)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(UserActions(bot)) # add the cog to the bot