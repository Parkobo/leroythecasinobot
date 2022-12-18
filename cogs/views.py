from . import admin as a
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ui import View, Button, Item

class MainMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, local_msg: Interaction) -> bool:
        # if local_msg.user != self.msg.user:
        #     await local_msg.response.send_message("This isn't your application window!", ephemeral=True)
        #     return False
        # if local_msg.user == self.ctx.author:
        #     view_items = self.children
        #     for item in view_items:
        #         if local_msg.custom_id == "open-shop":
        #             self.disable_all_items()
        #             await local_msg.response.edit_message(content="** **", embed=None, view=None)
        #             await a.AdminCommands.shop(context=self.ctx)
        #         elif item.custom_id == "open-stats":
        #             pass
        #         elif item.custom_id == "open-settings":
        #             pass
        #         elif item.custom_id == "buy-ticket":
        #             pass
        #         elif item.custom_id == "quit":
        #             pass
        #         else:
        #             raise Exception("The interface has found a button error in interaction_check().")
        #     self.stop()
        return True

class ShopMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None