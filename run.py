import discord
import os
from gamma import moderation, fun, websearch, logging, misc

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('hey 8 ball'):
        await client.send_message(message.channel,fun.magic8ball())
    pass

client.run(os.environ['TOKEN'])
