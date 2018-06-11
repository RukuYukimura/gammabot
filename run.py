import discord
import os
from gamma import moderation, fun, websearch, logging, misc

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('hey 8 ball'):
        await client.send_message(message.channel,await fun.magic8ball())
    if message.content.startswith('roll a d'):
        await client.send_message(message.channel,"You rolled a... {}".format(await str(fun.roll(int(message.content.replace('roll a d',''))))))
    pass

client.run(os.environ['TOKEN'])
