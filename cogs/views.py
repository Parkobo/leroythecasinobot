from nextcord import Interaction
from nextcord.ui import View
from . import buttons as b

class MainMenu(View):
    def __init__(self: View, cog, timeout, disabled_flag, interaction):
        super().__init__(timeout=timeout)
        self.value = None
        self.cog = cog
        self.disabled_flag = disabled_flag
        self.interaction = interaction
        buttons = {
            b.OpenShopButton(cog=self.cog, pass_row=0, disabled_flag=self.disabled_flag, interaction=self.interaction),
            b.BuyTicketButton(cog=self.cog, pass_row=0, disabled_flag=self.disabled_flag, interaction=self.interaction),
            b.OpenInventoryButton(cog=self.cog, pass_row=1, interaction=self.interaction),
            b.OpenStatsButton(cog=self.cog, pass_row=1, interaction=self.interaction),
            b.OpenSettingsButton(cog=self.cog, pass_row=1, interaction=self.interaction),
            b.QuitButton(cog=self.cog, pass_row=2, interaction=self.interaction)
            }
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class ShopMenu(View):
    def __init__(self: View, cog, interaction):
        super().__init__(timeout=None)
        self.value = None
        self.cog = cog
        self.interaction = interaction
        buttons = {
            b.CheckerButton(cog=self.cog, pass_row=0, interaction=self.interaction),
            b.OpenMainMenuButton(cog=self.cog, pass_row=2, interaction=self.interaction),
            b.QuitButton(cog=self.cog, pass_row=3, interaction=self.interaction)
            }
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class StatsMenu(View):
    def __init__(self: View, cog, interaction):
        super().__init__(timeout=None)
        self.value = None
        self.cog = cog
        self.interaction = interaction
        buttons = {
            b.OpenMainMenuButton(cog=self.cog, pass_row=1, interaction=self.interaction),
            b.QuitButton(cog=self.cog, pass_row=2, interaction=self.interaction)
            }
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class SettingsMenu(View):
    def __init__(self: View, cog, interaction):
        super().__init__(timeout=None)
        self.value = None
        self.cog = cog
        self.interaction = interaction
        buttons = {
            b.EditPlayerNameButton(cog=self.cog, pass_row=0, interaction=self.interaction),
            b.OpenMainMenuButton(cog=self.cog, pass_row=1, interaction=self.interaction),
            b.QuitButton(cog=self.cog, pass_row=2, interaction=self.interaction)
            }
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class AlertWindow(View):
    def __init__(self: View, cog, interaction):
        super().__init__(timeout = None)
        self.value = None
        self.cog = cog
        self.interaction = interaction
        self.add_item(
            b.OkayButton(
                cog = self.cog,
                pass_row = 0, 
                interaction = self.interaction
                ))
    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class Inventory(View):
    def __init__(self: View, cog, interaction):
        super().__init__(timeout = None)
        self.value = None
        self.cog = cog
        self.interaction = interaction
        buttons = {
            b.CashOut(cog=self.cog, pass_row=0, interaction=self.interaction),
            b.DonateTickets(cog=self.cog, pass_row=0, interaction=self.interaction),
            b.OpenMainMenuButton(cog=self.cog, pass_row=1, interaction=self.interaction),
            b.QuitButton(cog=self.cog, pass_row=2, interaction=self.interaction)
            }
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class Arrows(View):
    def __init__(self: View):
        super().__init__(timeout=None)
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True