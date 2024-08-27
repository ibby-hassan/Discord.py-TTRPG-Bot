import discord
from discord import app_commands
from main import client
import dice

tree = app_commands.CommandTree(client)

@tree.command(name="roll", description="Rolls a dice in NdN format.")
async def roll(interaction: discord.Interaction, roll: str):
    await interaction.response.send_message(f"Roll results: *{dice.roll(roll)}*")

