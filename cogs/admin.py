from discord import Cog, ApplicationContext as AppCtx, Colour, Embed
from . import buttons as b
from . import views as v
from . import modals as m
from main_bot_logic import bot
from discord.ext.commands import Bot
import discord

bot = Bot(intents=discord.Intents.all())

class AdminCommands(Cog): # create a class for our cog that inherits from commands.Cog -- Admin Commands
    def __init__(self, bot): # This is a special method that is called when the cog is loaded
        self.bot = bot

    @bot.slash_command()
    async def main_menu(self, ctx: AppCtx):
        member = ctx.author
        name = member.display_name
        pfp = member.display_avatar
        view = v.MainMenu(ctx=ctx)
        buttons = {
        b.OpenShopButton(_row=0),
        b.OpenStatsButton(_row=0), 
        b.OpenSettingsButton(_row=0),
        b.BuyTicketButton(_row=1, _label="Quick Buy 1", _custom_id="buy-one-ticket"),
        b.QuitButton(_row=1)
        }

        embed = Embed(color=Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
        embed.set_author(name=f"Good to see you {name}", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{pfp}")

        for button in buttons:
            view.add_item(button)

        msg = await ctx.send_response(embed=embed, view=view)
        res = await view.wait()
        if res:
            await msg.delete_original_response()
            

    @bot.command(hidden=True)
    async def shop(self, ctx: AppCtx):
        member = ctx.author
        name = member.display_name
        pfp = member.display_avatar
        view = v.ShopMenu(ctx=ctx)
        buttons = {
        b.BuyTicketButton(_row=0, _label="Buy 1", _custom_id="buy-one-ticket"),
        b.OpenMainMenuButton(_row=2)
        }

        embed = Embed(color=Colour.random(), title="What can I do for you?", type='rich', url=None, description="500 for 1")
        embed.set_author(name=f"You could win {name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{pfp}")

        for button in buttons:
            view.add_item(button)
        msg = await ctx.send_response(embed=embed, view=view)
        res = await view.wait()
        if res:
            msg.edit(embed=None, view=None)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(AdminCommands(bot)) # add the cog to the bot