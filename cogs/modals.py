import nextcord
import data_methods as crud
from nextcord.ui import TextInput, Modal

# class BuyModal(Modal, title='<*> I T E M - S H O P <*>'):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         tickets = TxtBx(label="How many tickets would you like to purchase?", placeholder=f"You can purchase {max_items} tickets")
#         powerups = TxtBx(label="How many powerup tokens would you like to purhcase?")

#     async def callback(self, interaction: discord.Interaction):
#         embed = discord.Embed(title="Modal Results")
#         embed.add_field(name="Short Input", value=self.children[0].value)
#         await interaction.response.send_message(embeds=[embed])





# class Pet(nextcord.ui.Modal):
#     def __init__(self):
#         super().__init__("Your pet")  # Modal title

#         # Create a text input and add it to the modal
#         self.name = nextcord.ui.TextInput(
#             label="Your pet's name",
#             min_length=2,
#             max_length=50,
#         )
#         self.add_item(self.name)

#         # Create a long text input and add it to the modal
#         self.description = nextcord.ui.TextInput(
#             label="Description",
#             style=nextcord.TextInputStyle.paragraph,
#             placeholder="Information that can help us recognise your pet",
#             required=False,
#             max_length=1800,
#         )
#         self.add_item(self.description)

#     async def callback(self, interaction: nextcord.Interaction) -> None:
#         """This is the function that gets called when the submit button is pressed"""
#         response = f"{interaction.user.mention}'s favourite pet's name is {self.name.value}."
#         if self.description.value != "":
#             response += f"\nTheir pet can be recognized by this information:\n{self.description.value}"
#         await interaction.send(response)