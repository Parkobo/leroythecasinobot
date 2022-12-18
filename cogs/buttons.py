import nextcord
from nextcord import Interaction
from . import modals as m
from nextcord.ui import Button, View
from . import admin as a
from nextcord.ext.commands import Cog

# ( + ) Lottery Shop Modal Stuff ( + ) #
class CheckerButton(Button):
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(m.BuyModal(title="Buy Items"))
        
# ( + ) Main Menu Buttons ( + ) # 
class OpenStatsButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="My Stats"
        emoji="📚"
        style=nextcord.ButtonStyle.blurple
        custom_id="open-stats"
        row=_row

        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def button_callback(self, interaction: Interaction):
        pass

class OpenShopButton(Button):
    def __init__(self: Button, *args, cog, pass_row, pass_interaction: Interaction, **kwargs):
        label="Ticket Shop"
        emoji="🏪"
        style=nextcord.ButtonStyle.green
        custom_id="open-shop"
        row=pass_row
        self.cog=cog
        self.interact = pass_interaction

        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: Interaction):
        await self.cog.shop()

class OpenSettingsButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="Settings"
        emoji="⚙️"
        style=nextcord.ButtonStyle.gray
        row=_row
        custom_id="open-settings"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def button_callback(self, interaction: Interaction):
        pass

class OpenMainMenuButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="Main Menu"
        emoji="💻"
        style=nextcord.ButtonStyle.primary
        row=_row
        custom_id="open-main"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def button_callback(self, interaction: Interaction):
        await interaction.response.defer()

class QuitButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="QUIT"
        emoji="🛑"
        style=nextcord.ButtonStyle.danger
        row=_row
        custom_id="quit"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def button_callback(self, interaction: Interaction):
        pass

class BuyTicketButton(Button):
    def __init__(self, *args, _row, _label, _custom_id, **kwargs):
        label =_label
        emoji ="🎟️"
        row =_row
        style = nextcord.ButtonStyle.green
        custom_id=_custom_id
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: Interaction):
        pass

# ( + ) Player Settings Buttons ( + ) #
class EditPlayerNameButton(Button):
    def __init__(self, row):
        super().__init__(label="Edit Profile Name", row=row, style=nextcord.ButtonStyle.green, emoji="✏️")

    async def callback(self, interaction: nextcord.Interaction):
        pass
        # Functionality for player editing their name in the db

# ( + ) Player Stats Button ( + ) #
class DownloadPlayerStats(Button):
    pass
    # Functionality for allowing players to get a file downloaded for them with their stats