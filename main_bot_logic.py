import os
import discord
from discord.ext.commands import Bot
import logging
import dotenv
from pymongo import MongoClient

# Make a new bot called bot, all permissions allowed
bot = Bot(intents=discord.Intents.all())

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

# Get the connection token for the bot and add logging for the bot to a local fi le 
token = str(os.getenv("TOKEN")) 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='leroyDiscord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Get all cogs into the bot for use of categorized commands
cogs_list = [
    'cogs.admin',
    'cogs.passives',
    'cogs.user_actions',
]

# Add them to the bot
for cog in cogs_list:
    bot.load_extension(cog)

# Print in console lets us know the bot has successfully made it alive to our server
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Start the bot 
bot.run(token)