import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    pass

client.run(os.environ['TOKEN'])
