from . import admin as a
from discord.commands import context 
from discord import Interaction, ApplicationContext as AppCtx
from discord.ui import View

class MainMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self, ctx: AppCtx):
        super().__init__()
        self.ctx=ctx

    async def interaction_check(self, interaction: Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("This isn't your application window!", ephemeral=True)
            return False
        if interaction.user == self.ctx.author:
            view_items = self.children
            for item in view_items:
                if interaction.custom_id == "open-shop":
                    self.disable_all_items()
                    await interaction.response.edit_message(content="** **", embed=None, view=None)
                    await a.AdminCommands.shop(context=self.ctx)
                elif item.custom_id == "open-stats":
                    pass
                elif item.custom_id == "open-settings":
                    pass
                elif item.custom_id == "buy-ticket":
                    pass
                elif item.custom_id == "quit":
                    pass
                else:
                    raise Exception("The interface has found a button error in interaction_check().")
            self.stop()
        return True

class ShopMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self, ctx):
        super().__init__()
        self.ctx=ctx

    async def interaction_check(self, interaction: Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("This isn't your application window!", ephemeral=True)
            return False
        if interaction.user == self.ctx.author:
            view_items = self.children
            for item in view_items:
                if interaction.custom_id == "open-main":
                    self.disable_all_items()
                    await interaction.response.edit_message(content="** **", embed=None, view=None)
                    await a.AdminCommands.main_menu(ctx=self.ctx)
                elif item.custom_id == "open-stats":
                    pass
                else:
                    raise Exception("The interface has found a button error in interaction_check().")
            self.stop()
        return True