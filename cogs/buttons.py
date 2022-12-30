import nextcord
from nextcord import Interaction
from . import modals as m
from nextcord.ui import Button
from . import admin as a

# ( + ) Lottery Shop Modal Stuff ( + ) #
class CheckerButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Purchase Items"
        emoji = "🛒"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.purchase(interaction, self.cog)
        
# ( + ) Main Menu Buttons ( + ) # 
class OpenShopButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Ticket Shop"
        emoji = "🏪"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog

        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.shop()

class OpenStatsButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "My Stats"
        emoji = "📚"
        style = nextcord.ButtonStyle.blurple
        row = pass_row
        self.cog = cog

        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.stats()

class OpenSettingsButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Settings"
        emoji = "⚙️"
        style = nextcord.ButtonStyle.gray
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.settings()

class OpenMainMenuButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Main Menu"
        emoji = "💻"
        style = nextcord.ButtonStyle.primary
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.main_window()

class QuitButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "QUIT"
        emoji = "🛑"
        style = nextcord.ButtonStyle.danger
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.quit()

class OkayButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "OK"
        emoji = "✔️"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.main_window()

class BuyTicketButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Quick Buy 1"
        emoji = "🎟️"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.buy_ticket()

# ( + ) Player Settings Buttons ( + ) #
class EditPlayerNameButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Edit Name"
        emoji = "📋"
        style = nextcord.ButtonStyle.gray
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.edit_name()

# ( + ) Player Stats Button ( + ) #
class DownloadPlayerStatsButton(Button):
    def __init__(self: Button, *args, cog, pass_row, **kwargs):
        label = "Download"
        emoji = "📋"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.download()