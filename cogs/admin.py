from nextcord import Colour, Embed, Interaction
from . import buttons as b
from . import views as v
from . import modals as m
from main_bot_logic import bot
from nextcord.ext import commands
from nextcord.ext.commands import Cog
import data_methods as db
import nextcord
from emoji import emojize as e

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents=intents)

class AdminCommands(Cog):
    def __init__(self, bot, interaction: Interaction):
        self.bot = bot
        self.interaction = interaction
        self.member = None
        self.name = None
        self.pfp = None

    @bot.slash_command(description="Open the lottery application.")
    async def main_menu(self, interaction: Interaction):
        player = await db.read_player(pass_msg=interaction)
        if player is not None:
            self.interaction = interaction
            self.member = interaction.user
            self.name = interaction.user.display_name
            self.pfp = interaction.user.display_avatar
            
            funds = player.get('Funds')
            self.max_items = funds // 500
            self.disabled = False

            if self.max_items <= 0:
                self.disabled = True

            view = v.MainMenu()
            buttons = {
                b.OpenShopButton(cog=self, pass_row=0, disabled_flag=self.disabled),
                b.BuyTicketButton(cog=self, pass_row=0, disabled_flag=self.disabled),
                b.OpenInventoryButton(cog=self, pass_row=1),
                b.OpenStatsButton(cog=self, pass_row=1),
                b.OpenSettingsButton(cog=self, pass_row=1),
                b.QuitButton(cog=self, pass_row=2)
            }

            for button in buttons:
                view.add_item(button)

            embed = Embed(color=Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
            embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
            embed.set_thumbnail(url=f"{self.pfp}")

            self.msg = await interaction.response.send_message(embed=embed, view=view)
            res = await view.wait()
            if res:
                await self.msg.delete()
        else:
            await interaction.response.send_message(f"You are not registered <@{interaction.user.id}>! Please use the **/register** command to get registered for the lottery!")

    async def shop(self):
        player = await db.read_player(pass_msg=self.interaction)
        name=player.get("Player Name")
        view = v.ShopMenu()
        buttons = {
        b.CheckerButton(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=2),
        b.QuitButton(cog=self, pass_row=3)
        }

        for button in buttons:
            view.add_item(button)

        embed = Embed(color=Colour.random(), title=e(":package: ITEMS"), type='rich', url=None, description=e(":ticket: Ticket = $500\n:secret: Powerup = $500\n:wavy_dash:"))
        embed.set_author(name=f"How can I be of assistance {name}?", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12cbe8a4-f55c-4b40-85bb-d8e1405e7b84/d98qb8z-56df9d2f-1a24-41d4-ad7d-e4244cc189be.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyY2JlOGE0LWY1NWMtNGI0MC04NWJiLWQ4ZTE0MDVlN2I4NFwvZDk4cWI4ei01NmRmOWQyZi0xYTI0LTQxZDQtYWQ3ZC1lNDI0NGNjMTg5YmUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Nd7Pghx-n6PtcGxt3q1iXKcSmh0AlSH0jkMzXViaWqE")
        embed.set_thumbnail(url=f"{self.pfp}")
        embed.add_field(
            name=e(":1234: ODDS:"),
            value=e(
                f""":secret: 1 in 8\n
                :white_flower::secret: 1 in 20\n
                :white_flower::white_flower::secret: 1 in 200\n
                :white_flower::white_flower::white_flower: 1 in 500\n
                :white_flower::white_flower::white_flower::secret: 1 in 4,000\n
                :white_flower::white_flower::white_flower::white_flower: 1 in 10,000\n
                :white_flower::white_flower::white_flower::white_flower::secret: 1 in 80,000"""),
            inline=False)
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def stats(self):
        player = await db.read_player(pass_msg=self.interaction)
        total_revenue = int(player.get("Total Winnings")) - int(player.get("Total Losses"))
        ticket_money_spent = int(player.get("Tickets Bought")*500)
        powerup_money_spent = int(player.get("Powerups Bought")*500)
        view = v.StatsMenu()
        buttons = {
        b.DownloadPlayerStatsButton(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=2)
        }

        for button in buttons:
            view.add_item(button)
        
        embed = Embed(color=Colour.random())
        embed.set_author(name="If you have any questions, use the /help command!", icon_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3ce212da-22a2-4830-85cc-f5e5affc5cd6/dcxehfe-dd22d80d-4cff-49bf-be56-bb51f5ea0a78.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNjZTIxMmRhLTIyYTItNDgzMC04NWNjLWY1ZTVhZmZjNWNkNlwvZGN4ZWhmZS1kZDIyZDgwZC00Y2ZmLTQ5YmYtYmU1Ni1iYjUxZjVlYTBhNzguZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.FPZzigXwn6ZWFixDogw4z5uQbIfnJSzyq8TDI9K_3o8')
        embed.set_image(url="https://www.icegif.com/wp-content/uploads/2022/03/icegif-83.gif")
        embed.set_thumbnail(url=f"{self.pfp}")
        embed.add_field(name=e(":bust_in_silhouette: NAME:"), value=player.get("Player Name"))
        embed.add_field(name=e(":moneybag: FUNDS:"), value=player.get("Funds"))
        embed.add_field(
            name=e(":green_book: MONETARY DATA:"),
            value=e(
                f""":accept::chart_with_upwards_trend: Lifetime Winnings -> ${player.get('Total Winnings')}\n
                :accept::chart_with_downwards_trend: Lifetime Losses -> ${player.get('Total Winnings')}\n
                :accept::file_folder: Lifetime Revenue -> ${total_revenue}\n
                :accept::dollar: Total Spent On Tickets -> ${ticket_money_spent}\n
                :accept::pound: Total Spent On Powerups -> ${powerup_money_spent}
                :wavy_dash:"""),
            inline=False)
        embed.add_field(
            name=e(":closed_book: TICKET DATA:"),
            value=e(
                f""":ticket::one: Tickets Bought -> {player.get('Tickets Bought')}\n
                :ticket::two: Tickets Used -> {player.get('Tickets Used')}\n
                :ticket::three: Tickets Gifted -> {player.get('Tickets Gifted')}\n
                :ticket::four: Tickets Received -> {player.get('Tickets Received')}\n
                :ticket::five: Current Tickets Count -> {player.get('Current Tickets Count')}
                :wavy_dash:"""),
            inline=False)
        embed.add_field(
            name=e(":orange_book: POWERUP DATA:"),
            value=e(
                f""":secret::one: Powerups Bought -> {player.get('Powerups Bought')}\n
                :secret::two: Powerups Used -> {player.get('Powerups Used')}\n
                :secret::five: Current Powerups Count -> {player.get('Current Powerups Count')}
                :wavy_dash:"""),
            inline=False)
        embed.add_field(
            name=e(":blue_book: LOTTERY DATA:"),
            value=e(
                f""":slot_machine::one: Win Count -> {player.get('Lottery Win Count')}\n
                :slot_machine::two: Lotteries Attempted -> {player.get('Attempts')}:wavy_dash:"""),
            inline=False)
        embed.set_footer(text=e(f"Joined on {player.get('Joined')}"))
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def settings(self):
        player = await db.read_player(pass_msg=self.interaction)
        name=player.get("Player Name")
        view = v.SettingsMenu()
        buttons = {
        b.EditPlayerNameButton(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=2)
        }

        for button in buttons:
            view.add_item(button)

        embed = Embed(color=Colour.random(), title="SETTINGS", type='rich', url=None, description="500 for 1")
        embed.set_author(name=f"You could win {name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://64.media.tumblr.com/0be6dd3b9a8624c8b0ed47deec5f39fd/tumblr_o9w9bfjRiY1vyuxeno1_1280.gif")
        embed.set_thumbnail(url=f"{self.pfp}")

        await self.interaction.edit_original_message(embed=embed, view=view)

    async def main_window(self):
        player = await db.read_player(pass_msg=self.interaction)
        name=player.get("Player Name")
        funds = player.get('Funds')
        self.max_items = funds // 500
        self.disabled = False
        
        if self.max_items <= 0:
            self.disabled = True

        view = v.MainMenu()
        buttons = {
            b.OpenShopButton(cog=self, pass_row=0, disabled_flag=self.disabled),
            b.BuyTicketButton(cog=self, pass_row=0, disabled_flag=self.disabled),
            b.OpenInventoryButton(cog=self, pass_row=1),
            b.OpenStatsButton(cog=self, pass_row=1),
            b.OpenSettingsButton(cog=self, pass_row=1),
            b.QuitButton(cog=self, pass_row=2)
        }

        for button in buttons:
            view.add_item(button)

        embed = Embed(color=Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
        embed.set_author(name=f"Good to see you {name}", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
        embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
        embed.set_thumbnail(url=f"{self.pfp}")

        await self.interaction.edit_original_message(embed=embed, view=view)

    async def inventory(self):
        player = await db.read_player(pass_msg=self.interaction)
        funds = int(player.get("Funds"))
        tickets = int(player.get("Current Tickets Count"))
        powerups = int(player.get("Current Powerups Count"))
        total_worth = funds + ((tickets + powerups)*500)
        donations = int(player.get("Tickets Gifted"))
        cash_out_total = int(player.get("Total Cashed Out"))
        fees = int(player.get("Total Fees Paid"))
        view = v.Inventory()
        buttons = {
        b.CashOut(cog=self, pass_row=0),
        b.DonateTickets(cog=self, pass_row=0),
        b.OpenMainMenuButton(cog=self, pass_row=1),
        b.QuitButton(cog=self, pass_row=2)
        }

        for button in buttons:
            view.add_item(button)

        embed = Embed(color=Colour.random())
        embed.set_author(name=f"Your Assets Total Worth : ${total_worth}", icon_url='https://media.tenor.com/k-PfH9O4EpcAAAAj/money-cash.gif')
        embed.set_image(url="https://www.icegif.com/wp-content/uploads/2022/03/icegif-83.gif")
        embed.set_thumbnail(url=f"{self.pfp}")
        embed.add_field(
            name=e("🏦 CASH OUT INFORMATION:"),
            value=e(
                f"""+ You can cash out 50% -> 100% of your wallet per request\n
                + Cash outs are completed in city in bulk, check for related announcements\n
                + Funds are delivered via wire transfer in city\n
                + Funds are returned to your account NOT INCLUDING fees paid if funds are not collected in city within a week of the first request\n
                + You have unlimited cash out requests, however, a fee applies after the first cash out within 24 hours:\n
                + Fees only apply to the amount requested for that specific withdrawl, and not the total requested of all combined cash outs\n
                :arrow_right:1st Time -> Free\n
                :arrow_right:2nd Time -> 15% Fee On Amount\n
                :arrow_right:3rd Time -> 35% Fee On Amount\n
                :arrow_right:4th Time -> 55% Fee On Amount\n
                :arrow_right:5+ Times -> 70% Fee On Amount\n
                :wavy_dash:"""),
            inline=False)
        embed.add_field(
            name=e("💝 DONATION INFORMATION:"),
            value=e(
                f"""+ You can donate 5,000 items a day to other users\n
                + Donations of items come at a small fee of 20% of the item's total value\n
                + Donation fees are non-refundable\n
                + Donation milestones in the form of discord roles are available\n
                :arrow_right:100 Donations -> Gifter\n
                :arrow_right:500 Donations -> Charitable\n
                :arrow_right:1,000 Donations -> Benevolent\n
                :arrow_right:4,000 Donations -> Donation Jockey\n
                :arrow_right:10,000 -> Donation Chief\n
                :arrow_right:75,000 -> Golden Caretaker\n
                :arrow_right:150,000 -> Philanthropist\n
                :arrow_right:250,000+ -> Miracle Worker"""),
            inline=False)
        embed.set_footer(text=e(f"Total donated items: {donations}\nTotal cash withdrawn successfully: ${cash_out_total}\nTotal fees paid: ${fees}"))
        await self.interaction.edit_original_message(embed=embed, view=view)

    async def buy_ticket(self):
        player = await db.read_player(pass_msg=self.interaction)
        funds = player.get('Funds')
        self.max_items = funds // 500
        if self.max_items > 0:
            await db.update_player(player=player, tickets=1, powerups=0)
            await self.interaction.send("One ticket purchased!", ephemeral=True)
        else:
            await self.alert()

    async def quit(self):
        await self.msg.delete()
        await self.interaction.send("Thanks for stopping by!", ephemeral=True)

    async def edit_name(self, interaction: Interaction, cog):
        self.cog = cog
        player = await db.read_player(pass_msg=self.interaction)
        name_modal = m.ChangeNameModal(player=player, cog=self.cog)
        await interaction.response.send_modal(modal=name_modal)

    async def cash_out(self, interaction: Interaction, cog):
        self.cog = cog
        player = await db.read_player(pass_msg=self.interaction)
        funds = int(player.get('Funds'))
        if funds > 0 and funds < 500:
            await self.quick_cash_out(interaction, player, funds)
        elif funds > 0:
            cash = m.CashOutModal(player=player, cog=self.cog, funds=funds)
            await interaction.response.send_modal(modal=cash)
        else:
            await self.alert_cash_out()
    
    async def quick_cash_out(self, interaction: Interaction, player, funds):
        await db.update_player_cash(player=player, funds=funds)
        await interaction.response.send_message(f"You have successfully cashed out ${funds}!", ephemeral=True)

    async def donate(self):
        pass

    async def alert(self):
        view = v.AlertWindow()
        view.add_item(b.OkayButton(cog=self, pass_row=0))

        embed = Embed(color=Colour.random(), title="ALERT", type='rich', url=None, description="You do not have enough funds to purchase any items from the shop at this time.")
        embed.set_image(url="https://64.media.tumblr.com/8d0620c4919bc5b9fa8b36dd9106a0ab/tumblr_n0zrp2SNo61rpfk7eo1_500.gif")
        embed.set_thumbnail(url=f"{self.pfp}")

        await self.interaction.edit_original_message(embed=embed, view=view)

    async def alert_cash_out(self):
        view = v.AlertCashOutWindow()
        view.add_item(b.OkayButton(cog=self, pass_row=0))

        embed = Embed(color=Colour.random(), title="ALERT", type='rich', url=None, description="You have no funds to withdraw at this time!")
        embed.set_image(url="https://64.media.tumblr.com/8d0620c4919bc5b9fa8b36dd9106a0ab/tumblr_n0zrp2SNo61rpfk7eo1_500.gif")
        embed.set_thumbnail(url=f"{self.pfp}")

        await self.interaction.edit_original_message(embed=embed, view=view)

    async def purchase(self, interaction: Interaction, cog):
        self.cog = cog
        player = await db.read_player(pass_msg=self.interaction)
        funds = player.get('Funds')
        self.max_items = funds // 500
        if self.max_items > 0:
            buy = m.BuyModal(player=player, cog=self.cog, max=self.max_items)
            await interaction.response.send_modal(modal=buy)
        else:
            await self.alert()

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(AdminCommands(bot, interaction=None)) # add the cog to the bot