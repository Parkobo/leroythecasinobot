from datetime import datetime as dt
from discord import ApplicationContext as AppCtx
from pymongo import MongoClient
import dotenv
import os

# Load the credentials from the local .env file
dotenv.load_dotenv("secrets.env")

# Grab the cluster connection key for connecting to a cloud MongoDB
cluster = str(os.getenv("cluster"))

# Create a new db_client object using the MongoClient type (which serves as a driver for interacting with data in the cloud database)
db_client = MongoClient(cluster)

# Select a specific database from the MongoDB cloud database, in this case the lottery_bot database with a size of variable length
db = db_client.lottery_bot

# Set the database collections to their respective variables
player_data = db.player_data
admin_data = db.admin_data

# Create. Read. Update. Delete. #
async def create_player(ctx: AppCtx):
    d_id = ctx.author.id
    check_d_id = player_data.find_one( { "Discord ID": d_id } )
    if check_d_id is None:
        p_na = ctx.author.name
        date = dt.now()
        player_data.insert_one(
            {
                # Their true discord ID to make sure the user is not being nefarious
                "Discord ID": d_id,
                # Name of the player given at registration
                "Player Name": p_na,
                # Current standing total funds a player has in their account
                "Funds": 1000,
                # Number of times a player has won the lottery in their lifetime
                "Lottery Win Count": 0,
                # Total amount of money won by the player in the lottery in their lifetime
                "Total Winnings": 0,
                # Total amount of money lost by the player in the lottery in their lifetime
                "Total Losses": 0,
                # Number of times a player has participated in the lottery -- participation is using at least > 0 tickets.
                "Attempts": 0,
                # Total number of tickets bought by the player in their lifetime
                "Tickets Bought": 0,
                # Total number of tickets redeemed for participating in lotteries. This should always be <= tickets bought
                "Tickets Used": 0,
                # Total number of tickets gifted from this player to other players
                "Tickets Gifted": 0,
                # Total number of tickets received from other players gifting them
                "Tickets Received": 0,
                # Current balance of tickets in the 'wallet' of the player
                "Current Tickets Count": 0,
                # Total number of powerups bought by the player in their lifetime
                "Powerups Bought": 0,
                # Total number of powerups redeemed for participating in lotteries. This should always be <= tickets bought
                "Powerups Used": 0,
                # Current balance of powerups in the 'wallet' of the player
                "Current Powerups Count": 0,
                # The exact date and time of the player registering their account -- in case they leave or need records for something like logging
                "Joined": date,
        })
        await ctx.send_response(f"You have been registered successfully, {ctx.author.name}!")
        return True
    else:
        await ctx.send_response(f'**You already have an account <@{ctx.author.id}> !**')
    return False

def read_player():
    pass

def update_player():
    pass

def delete_player():
    pass

# Non-Direct Database Helpers #
def get_max_tickets_player_can_buy():
    pass
