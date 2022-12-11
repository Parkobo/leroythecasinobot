import discord
from discord.ext.commands import Bot
from discord import Cog, Interaction, ButtonStyle as style
from discord.ui import View, button, Button
import components as c

bot = Bot(intents=discord.Intents.all())

class AdminCommands(Cog): # create a class for our cog that inherits from commands.Cog -- Admin Commands
    def __init__(self, bot): # This is a special method that is called when the cog is loaded
        self.bot = bot

    @bot.slash_command(pass_context=True)
    async def main_menu(self, ctx):
        member = ctx.author
        name = member.display_name
        pfp = member.display_avatar
        view = MainMenu(ctx=ctx)
        buttons = {
        c.OpenShopButton(_row=0),
        c.OpenStatsButton(_row=0), 
        c.OpenSettingsButton(_row=0),
        c.BuyTicketButton(_row=1, _label="Quick Buy 1"),
        c.QuitButton(_row=1)
        }

        embed = discord.Embed(color=discord.Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
        embed.set_author(name=f"Good to see you {name}", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{pfp}")

        for button in buttons:
            view.add_item(button)
        await ctx.send(embed=embed, view=view)
        res = await view.wait()
        if res:
            # timed out
            pass
        
    @bot.command(hidden=True, pass_context=True)
    async def shop(self, ctx):
        member = ctx.author
        name = member.display_name
        pfp = member.display_avatar
        view = ShopMenu()
        buttons = {
        c.BuyTicketButton(_row=0, _label="Buy 1"),
        c.BuyTicketButton(_row=0, _label="Buy 5"),
        c.BuyTicketButton(_row=0, _label="Buy 20"),
        c.BuyTicketButton(_row=0, _label="Buy 50"),
        c.BuyTicketButton(_row=0, _label="Custom Amount"),
        c.BuyPowerUpButton(_row=1, _label="Buy 1"),
        c.BuyPowerUpButton(_row=1, _label="Buy 5"),
        c.BuyPowerUpButton(_row=1, _label="Buy 20"),
        c.BuyPowerUpButton(_row=1, _label="Buy 50"),
        c.BuyPowerUpButton(_row=1, _label="Custom Amount"),
        c.OpenMainMenuButton(_row=3),
        }

        embed = discord.Embed(color=discord.Colour.random(), title="What can I do for you?", type='rich', url=None, description="500 💵 => 🎟️\n250 💵 => 🧧")
        embed.set_author(name=f"You could win {name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{pfp}")

        for button in buttons:
            view.add_item(button)
        await ctx.send(embed=embed, view=view)
        res = await view.wait()
        if res:
            # timed out
            pass

class MainMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self, ctx):
        super().__init__()
        self.ctx=ctx

    async def interaction_check(self, interaction: Interaction) -> bool:
        if interaction.user :
            await interaction.response.send_message("This isn't your application window!", ephemeral=True)
            return False
        if interaction.user == self.ctx.author:
            for children in self.children:
                if children.custom_id == "open-shop":
                    await AdminCommands.shop()
                elif children.custom_id == "open-stats":
                    pass
                elif children.custom_id == "open-settings":
                    pass
                elif children.custom_id == "buy-ticket":
                    pass
                elif children.custom_id == "quit":
                    pass
                else:
                    raise Exception("The interface has found a button error in interaction_check().")
                    
            await self.stop()
        return True

class ShopMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self):
        super().__init__()

    async def interaction_check(self, interaction: Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("This isn't your application window!", ephemeral=True)
            return False
        if interaction.user == self.ctx.author:
            for children in self.children:
                if children.custom_id == "open-shop":
                    shop_view = ShopMenu()
                    await interaction.response.edit_message(view=shop_view)
                elif children.custom_id == "open-stats":
                    pass
                elif children.custom_id == "open-settings":
                    pass
                elif children.custom_id == "buy-ticket":
                    pass
                elif children.custom_id == "quit":
                    pass
                else:
                    raise Exception("The interface has found a button error in interaction_check().")
                    
            await self.stop()
        return True


        
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(AdminCommands(bot)) # add the cog to the bot