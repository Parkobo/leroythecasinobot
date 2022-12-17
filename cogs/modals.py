import discord
import data_methods as crud
from discord.ui import Modal, InputText as TxtBx

# class BuyModal(Modal, title='<*> I T E M - S H O P <*>'):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         max_items = crud()

#         tickets = TxtBx(label="How many tickets would you like to purchase?", placeholder=f"You can purchase {max_items} tickets")
#         powerups = TxtBx(label="How many powerup tokens would you like to purhcase?")

#     async def callback(self, interaction: discord.Interaction):
#         embed = discord.Embed(title="Modal Results")
#         embed.add_field(name="Short Input", value=self.children[0].value)
#         await interaction.response.send_message(embeds=[embed])