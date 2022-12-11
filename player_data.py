from globals import tracked_players

class Player(object):
    def __init__(self):
        self.uid = ''
        self.status_text = ''
        self.anonymous = True

        # Tickets owned by player for the three variations on the lottery
        self.lotto_small_tickets = 0         #   $500
        self.lotto_large_tickets = 0        #   $2500 (x2 high coins + $1,500 || x4 low coins + $1,500)

        # Token currency for all purchases in the discord to the bot
        self.currency_tokens = 0            #   $500

        # High-end special tokens only purchased by rare materials in game
        self.high_material_tokens = 0   #   $500  (x1 titanium) || (x5 plastic) 

        # Low-end special tokens only purchased by common materials in game
        self.low_material_tokens = 0   #   $500  (x50 any mat(?))

        # Total cash that a player can pull out of the game if they wish to do so, can purchase tokens
        self.winnings_cash = 0

        # Meta data on a player
        self.meta_player_value = ((self.lotto_small_tickets + self.currency_tokens + self.high_material_tokens + self.low_material_tokens)*500) 
        + (self.lotto_large_tickets*2500) + self.winnings_cash
        self.meta_highest_prize_won = 0
        self.meta_lotto_wins = 0
        self.meta_player_searches = 0

        # Active game data
        self.no_response = 0
        self.request_leave = False
        self.playing = False