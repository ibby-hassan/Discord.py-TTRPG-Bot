import discord
from discord.ext import commands
import os
import dice

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def roll(ctx:discord.Interaction, dice_str:str):
    result = dice.roll(dice_str)
    await ctx.send(result)

try:
    client.run(os.getenv('BOT_TOKEN'))
except Exception as e:
    print(e)