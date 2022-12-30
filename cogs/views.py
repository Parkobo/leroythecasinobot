from nextcord import Interaction
from nextcord.ui import View

class MainMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class ShopMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class StatsMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class SettingsMenu(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class AlertWindow(View): # Create a MainMenu View, serves as player main menu with the bot.
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True