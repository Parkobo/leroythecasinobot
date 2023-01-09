import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext.commands import Cog
import data_methods as db
from main_bot_logic import bot
from . import embeds as em
from . import modals as m
from . import views as v
from . import buttons as b

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents = intents)

class BaseCommands(Cog):
    def __init__(self, bot, interaction: Interaction):
        self.bot = bot
        self.interaction = interaction
        self.pfp = None
        self.timeout = 180.0
        self.main_view = None

    def is_me(self, m):
        return m.author == self.bot.user

    @bot.slash_command(description = "Create a personal channel for the lottery menu.")
    async def lottery(self, interaction: Interaction, shop_time: int):
        if shop_time <= 10 and shop_time > 0:
            self.timeout = shop_time * 60
            unique_channel_name = interaction.user.name.lower() + 's-menu'
            channel = nextcord.utils.get(interaction.guild.text_channels, name=unique_channel_name)
            if interaction.channel.name != 'bot_commands':
                await interaction.response.send_message(f"You must use this command in #bot_commands", ephemeral = True)
            elif channel is not None:
                await interaction.response.send_message(f"A channel called **{channel.name}** already exists for you!", ephemeral = True)
                await channel.send(f"Here is your channel <@{interaction.user.id}>! Use the **/main_menu** command to call the menu!")
            else:
                category = nextcord.utils.get(interaction.guild.categories, name = 'lottery')
                overwrites = {
                    interaction.guild.default_role: nextcord.PermissionOverwrite(read_messages = False),
                    interaction.guild.get_member(interaction.user.id): nextcord.PermissionOverwrite(read_messages = True)
                    }
                channel = await interaction.guild.create_text_channel(
                    unique_channel_name, 
                    overwrites = overwrites,
                    category = category
                    )
                await interaction.response.send_message(f"A channel called **{channel.name}** was created for you!", ephemeral = True)
                await channel.send(f"Here is your channel <@{interaction.user.id}>! Use the **/main_menu** command to call the menu!")
        else:
            await interaction.response.send_message("The time given must be 10 minutes or less and non-negative, please try the **/lottery** command again!", ephemeral = True)

    @bot.slash_command(description = "Open the lottery main menu.")
    async def main_menu(self, interaction: Interaction):
        player_channel = interaction.user.name.lower() + 's-menu'
        if interaction.channel.name != player_channel:
            await interaction.response.send_message(f"You must use this command in a personal lottery channel. Please first use the **/lottery** command to create your channel!", ephemeral = True)
        else:
            await interaction.channel.purge(check = self.is_me)
            player = await db.read_player(pass_msg = interaction)
            if player is not None:
                self.interaction = interaction
                self.pfp = interaction.user.display_avatar
                max_items = player.get('Funds') // 500
                disabled = True if max_items <= 0 else False
                self.main_view = v.MainMenu(
                    cog = self,
                    timeout = self.timeout,
                    disabled_flag = disabled,
                    interaction = self.interaction
                    )
                self.msg = await interaction.response.send_message(
                    embed = await em.main_embed(self.pfp), 
                    view = self.main_view
                    )
                res = await self.main_view.wait()
                if res:
                    try:
                        await self.quit()
                    except Exception:
                        await interaction.channel.purge(check = self.is_me)
            else:
                await interaction.response.send_message(f"You are not registered <@{interaction.user.id}>! Please use the **/register** command to get registered for the lottery!", ephemeral = True)
    
    async def main_window(self):
        player = await db.read_player(pass_msg = self.interaction)
        self.main_view.clear_items()
        max_items = player.get('Funds') // 500
        if max_items <= 0:
            buttons = await self.apply_main_buttons(True)
            for button in buttons:
                self.main_view.add_item(button)
        else:
            buttons = await self.apply_main_buttons(False)
            for button in buttons:
                self.main_view.add_item(button)

        await self.interaction.edit_original_message(
            embed = await em.main_embed(self.pfp), 
            view = self.main_view
            )

    async def apply_main_buttons(self, disabled):
        buttons = {
            b.OpenShopButton(cog=self, pass_row=0, disabled_flag=disabled, interaction=self.interaction),
            b.BuyTicketButton(cog=self, pass_row=0, disabled_flag=disabled, interaction=self.interaction),
            b.OpenInventoryButton(cog=self, pass_row=1, interaction=self.interaction),
            b.OpenStatsButton(cog=self, pass_row=1, interaction=self.interaction),
            b.OpenSettingsButton(cog=self, pass_row=1, interaction=self.interaction),
            b.QuitButton(cog=self, pass_row=2, interaction=self.interaction)
            }
        return buttons

    async def shop(self):
        player_name = (await db.read_player(pass_msg = self.interaction)).get("Player Name")
        shop_view = v.ShopMenu(
            cog = self,
            interaction = self.interaction
            )
        await self.interaction.edit_original_message(
            embed = await em.shop_embed(self.pfp, player_name), 
            view = shop_view
            )

    async def stats(self):
        player = await db.read_player(pass_msg = self.interaction)
        view = v.StatsMenu(
            cog = self,
            interaction = self.interaction       
            )
        await self.interaction.edit_original_message(
            embed = await em.stats_embed(self.pfp, player), 
            view = view
            )

    async def settings(self):
        player_name = (await db.read_player(pass_msg = self.interaction)).get("Player Name")
        view = v.SettingsMenu(
            cog = self,
            interaction = self.interaction     
            )
        await self.interaction.edit_original_message(
            embed = await em.settings_embed(self.pfp, player_name), 
            view = view
            )

    async def inventory(self):
        player = await db.read_player(pass_msg = self.interaction)
        view = v.Inventory(
            cog = self,
            interaction = self.interaction
            )
        await self.interaction.edit_original_message(
            embed = await em.inventory_embed(self.pfp, player), 
            view = view
            )

    async def buy_ticket(self):
        player = await db.read_player(pass_msg = self.interaction)
        max_items = player.get('Funds') // 500
        if max_items > 0:
            await db.update_player(player = player, tickets = 1, powerups = 0)
            await self.interaction.send("One ticket purchased!", ephemeral = True)
        else:
            await self.alert()

    async def quit(self):
        await self.msg.delete()
        await self.interaction.send("Thanks for stopping by!", ephemeral = True)

    async def edit_name(self, interaction: Interaction, cog):
        player = await db.read_player(pass_msg = self.interaction)
        await interaction.response.send_modal(
            modal = m.ChangeNameModal(
                player = player,
                cog = cog
                ))

    async def cash_out(self, interaction: Interaction, cog):
        player = await db.read_player(pass_msg = self.interaction)
        funds = int(player.get('Funds'))
        if funds > 0 and funds < 500:
            await self.quick_cash_out(interaction, player, funds)
            await self.cog.main_window()
        elif funds > 0:
            await interaction.response.send_modal(
                modal = m.CashOutModal(
                    player = player,
                    cog = cog,
                    funds = funds
                    ))
        else:
            await self.alert_cash_out()
    
    async def quick_cash_out(self, interaction: Interaction, player, funds):
        await db.update_player_cash(player = player, funds = funds)
        await interaction.response.send_message(f"You have successfully cashed out ${funds}!", ephemeral = True)
        
    async def donate(self):
        pass

    async def alert(self):
        view = v.AlertWindow(
            cog = self,
            interaction = self.interaction
            )
        await self.interaction.edit_original_message(
            embed = await em.alert_embed(self.pfp), 
            view = view
            )

    async def alert_cash_out(self):
        view = v.AlertWindow(
            cog = self,
            interaction = self.interaction
            )
        await self.interaction.edit_original_message(
            embed = await em.alert_cash_out_embed(self.pfp), 
            view = view
            )

    async def purchase(self, interaction: Interaction, cog):
        player = await db.read_player(pass_msg = self.interaction)
        max_items = player.get('Funds') // 500
        if max_items > 0:
            await interaction.response.send_modal(
                modal = m.BuyModal(
                    player = player,
                    cog = cog,
                    max = max_items
                    ))
        else:
            await self.alert()

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(BaseCommands(bot, interaction=None)) # add the cog to the bot