import discord
from discord import ButtonStyle as style
from discord.ext.commands import Bot
from discord.ui import Button

bot = Bot(intents=discord.Intents.all())
# await interaction.response.edit_message(content="hello there", view=None)
# await interaction.followup.send("Hi!")


# ( + ) Lottery Shop Buttons ( + ) #
class BuyTicketButton(Button):
    def __init__(self, *args, _row, _label, **kwargs):
        label =_label
        emoji ="🎟️"
        row =_row
        style = discord.ButtonStyle.green
        custom_id="buy-ticket"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass
        # Functionality for subtracting money and adding a ticket to p_db_object

class BuyPowerUpButton(Button):
    def __init__(self, *args, c_label, **kwargs):
        label=c_label
        emoji="🧧"
        style=discord.ButtonStyle.blurple
        custom_id="buy-power"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=0, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass
        # Functionality for subtracting money and adding a powerup token to p_db_object

# ( + ) Main Menu Buttons ( + ) # 
class OpenStatsButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="My Stats"
        emoji="📚"
        style=discord.ButtonStyle.blurple
        custom_id="open-stats"
        row=_row

        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(view=None)

class OpenShopButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="Ticket Shop"
        emoji="🏪"
        style=discord.ButtonStyle.green
        custom_id="open-shop"
        row=_row
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(view=None)

class OpenSettingsButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="Settings"
        emoji="⚙️"
        style=discord.ButtonStyle.gray
        row=_row
        custom_id="open-settings"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass

class OpenMainMenuButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="Main Menu"
        emoji="💻"
        style=discord.ButtonStyle.primary
        row=_row
        custom_id="open-main"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass

class QuitButton(Button):
    def __init__(self, *args, _row, **kwargs):
        label="QUIT"
        emoji="🛑"
        style=discord.ButtonStyle.danger
        row=_row
        custom_id="quit"
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass

# ( + ) Player Settings Buttons ( + ) #
class EditPlayerNameButton(Button):
    def __init__(self, row):
        super().__init__(label="Edit Profile Name", row=row, style=style.green, emoji="✏️")

    async def callback(self, interaction: discord.Interaction):
        pass
        # Functionality for player editing their name in the db

# ( + ) Player Stats Button ( + ) #
class DownloadPlayerStats(Button):
    pass
    # Functionality for allowing players to get a file downloaded for them with their stats