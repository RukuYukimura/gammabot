import discord
import os
from gamma import moderation, fun, websearch, logging, misc

client = discord.Client()

@client.event
async def on_message(message):
    pass

client.run(os.environ['TOKEN'])
