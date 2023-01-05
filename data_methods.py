from datetime import datetime as dt
from pymongo import MongoClient
import nextcord
from nextcord import Interaction
import dotenv
import os

# Load the credentials from the local .env file
dotenv.load_dotenv("secrets.env")

# Grab the cluster connection key for connecting to a cloud MongoDB
cluster = str(os.getenv("DATABASE"))

# Create a new db_client object using the MongoClient type (which serves as a driver for interacting with data in the cloud database)
db_client = MongoClient(cluster)

# Select a specific database from the MongoDB cloud database, in this case the lottery_bot database with a size of variable length
db = db_client.lottery_bot

# Set the database collections to their respective variables
player_data = db.player_data
admin_data = db.admin_data

# Create. Read. Update. Delete. #
async def create_player(pass_msg: Interaction):
    d_id = pass_msg.user.id
    check_d_id = player_data.find_one( { "Discord ID": d_id } )
    if check_d_id is None:
        p_na = pass_msg.user.display_name
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
                # Total amount of money withdrawn successfully by the player
                "Total Cashed Out": 0,
                # Total cash out requests made in the last day
                "Cashout Requests Made Today": 0,
                # Total amount of money paid in fees by the player in their lifetime
                "Total Fees Paid": 0,
                # Number of times a player has participated in the lottery -- participation is using at least > 0 tickets.
                "Attempts": 0,
                # Total number of tickets bought by the player in their lifetime
                "Tickets Bought": 0,
                # Total number of tickets redeemed for participating in lotteries. This should always be <= tickets bought
                "Tickets Used": 0,
                # Total number of tickets gifted from this player to other players
                "Tickets Gifted": 0,
                # Items donated in the current 24 hour window starting from the first donation
                "Items Donated Today": 0,
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
                # Time since the last cash out of the first series of cash outs was made -- applies to cash out fees
                "Cash Out Period": date,
                # 24 hour donation period starting from the first donation in a period
                "Donation Period": date,
                # The exact date and time of the player registering their account -- in case they leave or need records for something like logging
                "Joined": date,
        })
        await pass_msg.send(f"You have registered your account named *{p_na}* successfully, <@{d_id}>!")
        return True
    else:
        await pass_msg.send(f'**You already have an account <@{d_id}> !**')
    return False

async def read_player(pass_msg: Interaction):
    pd = player_data.find_one( { "Discord ID": pass_msg.user.id } )
    if pd is not None:
        return pd
    return pd
    
async def update_player(player: dict, tickets, powerups):
    d_id = player.get('Discord ID')
    cost = (tickets + powerups)*500
    player_data.update_one(
    { "Discord ID": d_id },
    { "$inc": 
        {
        "Funds": -abs(cost),
        "Tickets Bought": tickets,
        "Current Tickets Count": tickets,
        "Powerups Bought": powerups,
        "Current Powerups Count": powerups
        }
    })
    
async def update_player_cash(player: dict, funds):
    d_id = player.get('Discord ID')
    player_data.update_one(
    { "Discord ID": d_id },
    { "$inc":
        {
        "Funds": -abs(funds)
        }
    })

async def update_player_name(player: dict, name):
    d_id = player.get('Discord ID')
    player_data.update_one(
    { "Discord ID": d_id },
    { "$set":
        {
        "Player Name": name
        }
    })
