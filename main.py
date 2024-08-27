import os
import discord
from botcommands import tree

# Setting the permissions for the bot, 
# In this case, allowing the bot to read full contents of all messages.
intents = discord.Intents.default()
intents.message_content = True
# Creation of the client.
client = discord.Client(intents=intents)
    
# This is the event that is called when the bot is ready.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    try:
        await tree.sync()
    except Exception as e:
        print (e)


# This is the event that is called when a message is sent.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
