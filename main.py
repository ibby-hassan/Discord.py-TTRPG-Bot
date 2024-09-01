import discord
from discord.ext import commands
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

try:
    client.run(os.getenv('BOT_TOKEN'))
except Exception as e:
    print("Couldn't resolve token", e)