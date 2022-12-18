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
bot = commands.Bot(intents=intents)

class AdminCommands(Cog):
    def __init__(self, bot, interaction: Interaction):
        self.bot = bot
        self.interaction = interaction
        self.member = None
        self.name = None
        self.pfp = None

    @bot.slash_command(description="Open the lottery application.")
    async def main_menu(self, interaction: Interaction):
        self.interaction = interaction
        self.member = interaction.user
        self.name = interaction.user.display_name
        self.pfp = interaction.user.display_avatar

        view = v.MainMenu()
        buttons = {
        b.OpenShopButton(cog=self, pass_row=0),
        b.OpenStatsButton(cog=self, pass_row=0),
        b.OpenSettingsButton(cog=self, pass_row=0),
        b.BuyTicketButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=1)
        }

        embed = Embed(color=Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
        embed.set_author(name=f"Good to see you {self.name}", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{self.pfp}")

        for button in buttons:
            view.add_item(button)

        msg = await interaction.response.send_message(embed=embed, view=view)
        res = await view.wait()
        if res:
            await msg.delete()

    async def shop(self):
        view = v.ShopMenu()
        buttons = {
        b.CheckerButton(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=2)
        }

        embed = Embed(color=Colour.random(), title="What can I do for you?", type='rich', url=None, description="500 for 1")
        embed.set_author(name=f"You could win {self.name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{self.pfp}")

        for button in buttons:
            view.add_item(button)
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def stats(self):
        view = v.StatsMenu()
        buttons = {
        b.DownloadPlayerStatsButton(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=2)
        }

        embed = Embed(color=Colour.random(), title="STATS", type='rich', url=None, description="500 for 1")
        embed.set_author(name=f"You could win {self.name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{self.pfp}")

        for button in buttons:
            view.add_item(button)
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def settings(self):
        view = v.SettingsMenu()
        buttons = {
        b.EditPlayerNameButton(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=2)
        }

        embed = Embed(color=Colour.random(), title="SETTINGS", type='rich', url=None, description="500 for 1")
        embed.set_author(name=f"You could win {self.name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{self.pfp}")

        for button in buttons:
            view.add_item(button)
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def main_window(self):
        view = v.MainMenu()
        buttons = {
        b.OpenShopButton(cog=self, pass_row=0),
        b.OpenStatsButton(cog=self, pass_row=0),
        b.OpenSettingsButton(cog=self, pass_row=0),
        b.BuyTicketButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=1)
        }

        embed = Embed(color=Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
        embed.set_author(name=f"Good to see you {self.name}", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{self.pfp}")

        for button in buttons:
            view.add_item(button)
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def buy_ticket(self):
        pass

    async def quit(self):
        pass

    async def buy_ticket(self):
        pass

    async def edit_name(self):
        pass

    async def download(self):
        pass

    async def purchase(self):
        pass

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(AdminCommands(bot, interaction=None)) # add the cog to the bot