from nextcord import Interaction
from nextcord.ui import View

class MainMenu(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class ShopMenu(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class StatsMenu(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class SettingsMenu(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class AlertWindow(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class AlertCashOutWindow(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

class Inventory(View):
    def __init__(self: View):
        super().__init__()
        self.value = None

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True