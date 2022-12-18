from nextcord import Colour, Embed, Interaction
from . import buttons as b
from . import views as v
from . import modals as m
from main_bot_logic import bot
from nextcord.ext import commands
from nextcord.ext.commands import Cog
import nextcord

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)

class AdminCommands(Cog):
    def __init__(self, bot, pass_msg: Interaction):
        self.bot = bot
        self.msg = pass_msg

    @bot.slash_command(description="Open the lottery application.")
    async def main_menu(self, message: Interaction):
        member = message.user
        name = member.display_name
        pfp = member.display_avatar
        view = v.MainMenu()
        buttons = {
        b.OpenShopButton(pass_row=0, pass_view=view, pass_msg=message),
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

        msg = await message.send(embed=embed, view=view)
        res = await view.wait()
        if res:
            await msg.delete()
            
    @bot.command(hidden=True)
    async def shop(self, message: Interaction):
        member = message.user
        name = member.display_name
        pfp = member.display_avatar
        view = v.ShopMenu(pass_msg=message)
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
        msg = await message.send(embed=embed, view=view)
        res = await view.wait()
        if res:
            msg.edit(embed=None, view=None)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(AdminCommands(bot, None)) # add the cog to the bot