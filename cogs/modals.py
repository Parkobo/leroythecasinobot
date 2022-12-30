import nextcord
import data_methods as crud
from nextcord.ui import TextInput as TxtBx, Modal
import data_methods as db

class BuyModal(Modal):
    def __init__(self, *args, player: dict, cog, **kwargs):
        self.title = "<*> I T E M - S H O P <*>"
        self.player = player
        self.cog = cog
        super().__init__(*args, title=self.title, **kwargs)

        self.tickets = TxtBx(label="Ticket Amount To Buy", placeholder=f"You can purchase {self.max_items} tickets", required=True)
        self.add_item(self.tickets)
        self.powerups = TxtBx(label="Powerup Amount To Buy", placeholder=f"You can purchase {self.max_items} powerups", required=True)
        self.add_item(self.powerups)

    async def callback(self, interaction: nextcord.Interaction):
        t = int(self.tickets.value)
        p = int(self.powerups.value)
        sum = t + p
        if (t > 0 or p > 0):
            if ((t <= self.max_items and p <= self.max_items) and sum <= self.max_items):
                await db.update_player(player=self.player, tickets=t, powerups=p)
                if t > 0 and p > 0:
                    await interaction.send(f"{t} tickets and {p} powerups added to your account for {sum*500}!", ephemeral=True)
                    await self.cog.shop()
                elif t <= 0 and p > 0:
                    await interaction.send(f"{p} powerups added to your account for {sum*500}!", ephemeral=True)
                    await self.cog.shop()
                else:
                    await interaction.send(f"{t} tickets added to your account for {sum*500}!", ephemeral=True)
                    await self.cog.shop()
            else:
                await interaction.send("You do not have the necessary funds to make this purchase.", ephemeral=True)
                await self.cog.main_window()
        else:
            await interaction.send("No items were in your cart during your purchase.", ephemeral=True)
            await self.cog.main_window()