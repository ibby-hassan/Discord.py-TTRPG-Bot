import discord
from discord.ext import commands
from game.player import Player
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

@client.event
async def on_member_join(member:discord.User):
    await member.send(f'{member.mention} has joined the lobby.')

# Command to let users roll the dice
@client.tree.command(name="roll", description="Roll a dice in NdN format")
async def roll(interaction:discord.Interaction, dice_input:str):
    try:
        result:list = dice.roll(dice_input)
        await interaction.response.send_message(f"{interaction.user.mention} rolled: " + str(result))
        return
    except Exception as e:
        await interaction.response.send_message("Format has to be in NdN!", ephemeral=True)
        return
    
# Command to create affiliated player
@client.tree.command(name="create_character", description="Create a player")
async def create_character(interaction:discord.Interaction):
    player = Player(interaction.user)
    await interaction.response.send_message(f"{interaction.user.mention} has created a character.", ephemeral=True)
    await interaction.followup.send(player)
    return

# Running the bot, keep at the end of the file
try:
    client.run(os.getenv('BOT_TOKEN'))
except Exception as e:
    print("Couldn't resolve token", e)