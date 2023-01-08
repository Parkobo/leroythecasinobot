from nextcord.ext import commands, application_checks
import data_methods as db
import nextcord
from . import views as v
from . import buttons as b
from nextcord.ext.commands import Cog
from nextcord import Colour, Embed, Interaction
from emoji import emojize as e

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents=intents)

class UserActions(Cog): # Create a class for our cog that inherits from commands.Cog -- Admin Commands

    def __init__(self, bot, interaction: Interaction):
        self.bot = bot
        self.interaction = interaction

    @bot.slash_command()
    async def register(self, message: Interaction, uid: int):
        if uid <= 99999:
            await db.create_player(pass_msg=message, uid=uid)
        else:
            await message.response.send_message("The UID entered is too long, please enter a shorter UID value!")

    @bot.slash_command()
    # @application_checks.has_role('Admin') 
    async def clear_player_cashouts(self, message: Interaction):
        await db.clear_cash_out()

    @bot.slash_command()
    # @application_checks.has_role('Admin')
    async def get_player_cashouts(self, interaction: Interaction):
        players = await db.read_cash_out()
        self.interaction = interaction
        pages = [players[x:x+25] for x in range(0, len(players), 100)]
        embeds = []
        page_counter = 1
        if len(players) > 0:
            for page in pages:
                embed = Embed(color=Colour.random())
                embed.set_author(name=f"PAGE {page_counter}", icon_url='https://i.stack.imgur.com/022Fl.gif')
                embed.set_image(url="https://media.tenor.com/mL8DVhVViQcAAAAC/cyberpunk-cyberpunkedgerunners.gif")
                page_counter += 1

                # Embed contains up to 25 items which we check beforehand, adding the embed items here
                for requestor in page:
                    d_id = requestor.get("Discord ID")
                    uid = requestor.get("Player UID")
                    funds = requestor.get("Requested Funds")
                    date = requestor.get("First Request Date")
                    embed.add_field(
                        name=e(f":secret: UID -> {uid}"),
                        value=e(
                            f""":id: {d_id}
                            :dollar: {funds}
                            :date: {date}
                            :wavy_dash:"""),
                        inline=False)
                embeds.append(embed)

            view = v.Arrows()
            buttons = {
                b.DownArrow(cog=self),
                b.DMStats(cog=self),
                b.QuitButton(cog=self, pass_row=3)
            }

            for button in buttons:
                view.add_item(button)

            self.msg = await interaction.response.send_message(embed=embed, view=view)
        else:
            await interaction.response.send_message(f"There are no players awaiting a cash out at this time.")

    async def quit(self):
        await self.msg.delete()
        await self.interaction.send("Closed successfully!", ephemeral=True)

    async def dm_stats(self):
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

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(UserActions(bot, interaction=None)) # add the cog to the bot