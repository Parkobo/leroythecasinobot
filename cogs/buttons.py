import nextcord
from nextcord import Interaction
from . import modals as m
from nextcord.ui import Button
from . import admin as a
from emoji import emojize as e

# ( + ) Lottery Shop Modal Stuff ( + ) #
class CheckerButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Purchase Items"
        emoji = "🛒"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.purchase(interaction, self.cog)
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

# ( + ) Main Menu Buttons ( + ) # 
class OpenShopButton(Button):
    def __init__(self: Button, *args, cog, pass_row, disabled_flag, interaction: Interaction, **kwargs):
        label = "Ticket Shop"
        emoji = "🏪"
        style = nextcord.ButtonStyle.green
        row = pass_row
        disabled = disabled_flag
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, disabled=disabled, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.shop()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class OpenStatsButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "My Stats"
        emoji = "📚"
        style = nextcord.ButtonStyle.blurple
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.stats()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class OpenSettingsButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Settings"
        emoji = "⚙️"
        style = nextcord.ButtonStyle.gray
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.settings()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class OpenMainMenuButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Main Menu"
        emoji = "💻"
        style = nextcord.ButtonStyle.primary
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.main_window()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class OpenInventoryButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Inventory Actions"
        emoji = "🎒"
        style = nextcord.ButtonStyle.gray
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.inventory()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class QuitButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "QUIT"
        emoji = "🛑"
        style = nextcord.ButtonStyle.danger
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.quit()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class OkayButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "OK"
        emoji = "✔️"
        style = nextcord.ButtonStyle.green
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.main_window()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class BuyTicketButton(Button):
    def __init__(self: Button, *args, cog, pass_row, disabled_flag, interaction: Interaction, **kwargs):
        label = "Quick Buy 1"
        emoji = "🎟️"
        style = nextcord.ButtonStyle.primary
        row = pass_row
        disabled = disabled_flag
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, disabled=disabled, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.buy_ticket()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

# ( + ) Player Settings Buttons ( + ) #
class EditPlayerNameButton(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Edit Name"
        emoji = "📋"
        style = nextcord.ButtonStyle.gray
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.edit_name(interaction, self.cog)
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class CashOut(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Cash Out"
        emoji = "💰"
        style = nextcord.ButtonStyle.gray
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.cash_out(interaction, self.cog)
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class DonateTickets(Button):
    def __init__(self: Button, *args, cog, pass_row, interaction: Interaction, **kwargs):
        label = "Donate"
        emoji = "🎁"
        style = nextcord.ButtonStyle.blurple
        row = pass_row
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, **kwargs)

    async def callback(self, interaction: Interaction):
        if interaction.user == self.context.user:
            await self.cog.donate()
        else:    
            await interaction.response.send_message("This is not your menu! Please create your own private channel using the **/lottery** command!", ephemeral=True)

class UpArrow(Button):
    def __init__(self: Button, *args, cog, interaction: Interaction, **kwargs):
        label = "PREVIOUS PAGE"
        emoji = "⬆️"
        style = nextcord.ButtonStyle.blurple
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=0, **kwargs)

    async def callback(self, interaction: Interaction):
        pass

class DownArrow(Button):
    def __init__(self: Button, *args, cog, interaction: Interaction, **kwargs):
        label = "NEXT PAGE"
        emoji = "⬇️"
        style = nextcord.ButtonStyle.blurple
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=1, **kwargs)

    async def callback(self, interaction: Interaction):
        pass

class DMStats(Button):
    def __init__(self: Button, *args, cog, interaction: Interaction, **kwargs):
        label = "Send Page"
        emoji = "📟"
        style = nextcord.ButtonStyle.blurple
        self.cog = cog
        self.context = interaction
        super().__init__(*args, label=label, emoji=emoji, style=style, row=2, **kwargs)

    async def callback(self, interaction: Interaction):
        pass