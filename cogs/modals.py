import nextcord
from nextcord.ui import TextInput as TxtBx, Modal
import data_methods as db
import math

class BuyModal(Modal):
    def __init__(self, *args, player: dict, cog, max, **kwargs):
        self.title = "<*> I T E M - S H O P <*>"
        self.player = player
        self.cog = cog
        self.max = max
        super().__init__(*args, title=self.title, **kwargs)

        self.tickets = TxtBx(label="Ticket Amount To Buy", placeholder=f"You can purchase {self.max} tickets or powerups", required=True)
        self.add_item(self.tickets)
        self.powerups = TxtBx(label="Powerup Amount To Buy", placeholder=f"You can purchase {self.max} tickets or powerups", required=True)
        self.add_item(self.powerups)

    async def callback(self, interaction: nextcord.Interaction):
        try:
            t = int(self.tickets.value)
            p = int(self.powerups.value)
            sum = t + p
            if (t > 0 or p > 0):
                if ((t <= self.max and p <= self.max) and sum <= self.max):
                    await db.update_player(player=self.player, tickets=t, powerups=p)
                    if t > 0 and p > 0:
                        await interaction.send(f"{t} tickets and {p} powerups added to your account for {sum*500}!", ephemeral=True)
                    elif t <= 0 and p > 0:
                        await interaction.send(f"{p} powerups added to your account for {sum*500}!", ephemeral=True)
                    else:
                        await interaction.send(f"{t} tickets added to your account for {sum*500}!", ephemeral=True)
                else:
                    await interaction.send("You do not have the necessary funds to make this purchase.", ephemeral=True)
                    await self.cog.main_window()
            else:
                await interaction.send("No items were in your cart during your purchase.", ephemeral=True)
                await self.cog.main_window()

        except ValueError:
            await interaction.send("Please enter a proper **INTEGER** amount of items to purchase", ephemeral=True)

class CashOutModal(Modal):
    def __init__(self, *args, player: dict, cog, funds, **kwargs):
        self.title = "<*> C A S H - O U T <*>"
        self.player = player
        self.cog = cog
        self.funds = funds
        self.min = math.trunc(funds / 2)
        super().__init__(*args, title=self.title, **kwargs)

        self.cash = TxtBx(label="Amount to cash out of the game", placeholder=f"You can cash out a minimum of ${self.min} up to ${self.funds}", required=True)
        self.add_item(self.cash)

    async def callback(self, interaction: nextcord.Interaction):
        c = int(self.cash.value)
        try:
            if (c >= self.min and c <= self.funds):
                await db.update_player_cash(player=self.player, funds=c)
                await interaction.send(f"You requested to cashed out ${c} successfully!", ephemeral=True)
                await self.cog.main_window()
            elif (c <= self.min):
                await interaction.send("Your cash out request is too low, you must withdraw half or more of your total funding!", ephemeral=True)
            else:
                await interaction.send("Your request exceeds the funds in your wallet!", ephemeral=True)
        except ValueError:
            await interaction.send("Please enter a proper **INTEGER** whole values for cash withdrawl!", ephemeral=True)

class ChangeNameModal(Modal):
    def __init__(self, *args, player: dict, cog, **kwargs):
        self.title = "<*> C H A N G E - N A M E <*>"
        self.player = player
        self.cog = cog
        super().__init__(*args, title=self.title, **kwargs)

        self.name = TxtBx(label="What would you like your name to be?", placeholder=f"Names can only have letters, no spaces, and be 20 or less characters!", required=True)
        self.add_item(self.name)

    async def callback(self, interaction: nextcord.Interaction):
        c = str(self.name.value)
        try:
            if (c.isalpha() and len(c) < 20):
                await db.update_player_name(player=self.player, name=c)
                await interaction.send(f"You have changed your account name to {c} successfully!", ephemeral=True)
                await self.cog.main_window()
            else:
                await interaction.send(f"The given name is incorrect. Your name should ONLY contain letters and be 20 characters or less!", ephemeral=True)
        except ValueError:
            await interaction.send("Please enter **LETTERS** for a name, and no other characters!", ephemeral=True)