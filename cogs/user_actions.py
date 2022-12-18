from nextcord.ext import commands
import data_methods as db
import nextcord
from nextcord.ext.commands import Cog

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents=intents)

class UserActions(Cog): # Create a class for our cog that inherits from commands.Cog -- Admin Commands

    def __init__(self, bot): # This is a special method that is called when the cog is loaded
        self.bot = bot

    @bot.slash_command()
    async def register(self, message):
        await db.create_player(pass_msg=message)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(UserActions(bot)) # add the cog to the bot