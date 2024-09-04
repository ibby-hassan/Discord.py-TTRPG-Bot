import discord
from discord import app_commands
from discord.ext import commands
import os
import dice

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

# When the bot is initialised, sync command tree
@client.event
async def on_ready():
    print('Bot is ready.')
    try:
        await client.tree.sync()
    except Exception as e:
        print("Couldn't sync commands", e)

# Slash commands
@client.tree.command(name="roll", description="Roll a dice in NdN format")
async def roll(interaction:discord.Interaction, dice_input:str):
    try:
        result:list = dice.roll(dice_input)
        await interaction.response.send_message("You rolled: " + str(result))
        return
    except Exception as e:
        await interaction.response.send_message("Format has to be in NdN!", ephemeral=True)
        return

# Running the bot, keep at the end of the file
try:
    client.run(os.getenv('BOT_TOKEN'))
except Exception as e:
    print("Couldn't resolve token", e)