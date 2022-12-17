bot = discord.Bot()

# we need to limit the guilds for testing purposes
# so other users wouldn't see the command that we're testing

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

bot.run("TOKEN")


###############################

config_file = 'bot_cfg.ini'
record_file = 'player_records.json'

config = bot_utilities.load_config(config_file)
bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    description=config.get('bot','description')
)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#Just using sleep for these does NOT seem right.
#Should probably be using a cronjob
async def auto_update_records(filename):
    """Updates player records json file every 3 hours"""
    await bot.wait_until_ready()
    while not bot.is_closed:
        await asyncio.sleep(10800.0)
        bot_utilities.update_records(filename)

async def auto_give_points():
    """Gives points every 24 hours."""
    await bot.wait_until_ready()
    while not bot.is_closed:
        #Adjust point giving period as needed
        await asyncio.sleep(86400.0)
        bot_utilities.give_points()

#name these for the dc command. Probably a nicer way to do this than naming.
update_task = bot.loop.create_task(auto_update_records(record_file))
give_task = bot.loop.create_task(auto_give_points())

@bot.command(hidden=True, pass_context=True)
async def dc(ctx):
    """Updates records before disconnecting bot"""
    #May want to add in a way to shut down any games
    #in progress
    if ctx.message.author.id == config.get('bot','admin'):
        bot_utilities.update_records(record_file)
        update_task.cancel()
        give_task.cancel()
        await bot.logout()
        print('Disconnecting bot...')

bot_utilities.load_records(bot, record_file)
bot.add_cog(Blackjack(bot))

try:
    bot.run(config.get('bot','token'))
except:
    print('Login error or invalid token in bot config file.')
    exit()
bot_utilities.update_records(record_file)





##########################

    def add_new_player(self, p_uid):
        if not tps.get(p_uid):
            tps[p_uid] = Player(p_uid)
            tps[p_uid].lotto_small_tickets = 0
            tps[p_uid].lotto_large_tickets = 0
            tps[p_uid].high_material_tokens = 0
            tps[p_uid].low_material_tokens = 0
            tps[p_uid].currency_tokens = 10
            tps[p_uid].winnings_cash = 0
            # Meta data on a player
            tps[p_uid].meta_highest_prize_won = 0
            tps[p_uid].meta_lotto_wins = 0
            tps[p_uid].meta_player_searches = 0

    @commands.cooldown(rate=1, per=10)
    @commands.command(pass_context=True)
    async def player_stats(self,ctx):
        """Gets personal player information.
        Gets the player's game history, value, token count, and so on.
        Use the `help Blackjack` command for general Blackjack information.
        """
        if ctx.message.author.id in tps:
            view = View()
            view.add_item(butt)

        #     msg = ("""__**{0}**__\n
        #     *Your player information*\n
            
            
        #     """.format(📚
        #         ctx.message.author.display_name,
        #         tps[ctx.message.author.id].score,
        #         tps[ctx.message.author.id].wins))
            await self.bot.say(msg, view=view)
        await ctx.message.delete()









######################################################################
    @commands.cooldown(rate=1, per=10)
    @commands.command(pass_context=True)
    async def join(self, ctx):
        """Join a blackjack game queue.
        Attempts to add user to queue blackjack of a blackjack game in
        progress. Command has a 10 second cooldown.
        Use the `help Blackjack` command for general Blackjack information.
        """
        #Nested ifs since it's a long messy condition
        #Check if game in progress in user channel, then
        #check if user is not already in that game queue or ingame
        #If pass attempt add_to_tracked and add user to existing
        #game queue
        global ingame_channels
        if ctx.message.channel.is_private:
            return
        if ctx.message.channel.id in ingame_channels:
            self.add_to_tracked(ctx.message.author.id)
            player = tps.get(ctx.message.author.id)
            if player.playing:
                return
            channel_game = ingame_channels[ctx.message.channel.id]
            if not (player in channel_game.queue
                    and player in channel_game.ingame):
                channel_game.queue.append(player)
                player.playing = True

    @commands.cooldown(rate=1, per=5)
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        """Leave blackjack game.
        Removes user from the game at the end of a blackjack round.
        Use the `help Blackjack` command for general Blackjack information.
        """
        if ctx.message.channel.id in ingame_channels:
            player = tps.get(ctx.message.author.id)
            if player:
                player.request_leave = True
                await self.bot.send_message(
                    destination = ctx.message.author,
                    content = ('You will be removed from the game '
                                'at the end of the round.')
                )

        

    @commands.cooldown(rate=1, per=10)
    @commands.command(pass_context=True)
    async def start(self, ctx):
        """Start a blackjack game.
        Starts a new game of blackjack if there is not already a game in
        progress in the user's current channel. Automatically adds  user to
        game queue. Command has a 15 second cooldown.
        Use the `help Blackjack` command for general Blackjack information.
        """
        global tps
        global ingame_channels
        if ctx.message.channel.is_private:
            return
        #Check for game in channel
        if ctx.message.channel.id in ingame_channels:
            return
        self.add_to_tracked(ctx.message.author.id)
        player = tps[ctx.message.author.id]
        if player.playing:
            return
        #Add channel to ingame_channels list as a new Game() object
        ingame_channels[ctx.message.channel.id]  = (
            Lottery(self.bot, ctx.message.server)
        )
        ingame_channels[ctx.message.channel.id].queue.append(player)
        player.playing = True
        await ingame_channels[ctx.message.channel.id].game_loop(ctx)
        await self.bot.say('Thanks for playing!')
        del ingame_channels[ctx.message.channel.id]


        ######################## Buttons old
        # ( + ) Lottery Shop Buttons ( + ) #
class BuyTicketMenu(Select):
    def __init__(self, *args, _row, _label, _custom_id, **kwargs):
        label =_label
        emoji ="🎟️"
        row =_row
        style = discord.ButtonStyle.green
        custom_id=_custom_id
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass
        # Functionality for subtracting money and adding a ticket to p_db_object

class BuyPowerUpMenu(Select):
    def __init__(self, *args, _row, _label, _custom_id, **kwargs):
        label=_label
        emoji="🧧"
        row =_row
        style=discord.ButtonStyle.blurple
        custom_id=_custom_id
        
        super().__init__(*args, label=label, emoji=emoji, style=style, row=row, custom_id=custom_id, **kwargs)

    async def callback(self, interaction: discord.Interaction):
        pass
        # Functionality for subtracting money and adding a powerup token to p_db_object