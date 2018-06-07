import discord
import sys
import random
import urllib.request
import urllib.parse
import re
import os
import traceback
client = discord.Client()

prefix = '!'

customCommands = {}

errorSendingChannel = "NUFING"

eightballreactions = {
    1: 'It is certain.',
    2: 'It is decidedly so.',
    3: 'Without a doubt.',
    4: 'Yes definitely.',
    5: 'You may rely on it.',
    6: 'As I see it, yes.',
    7: 'Most likely.',
    8: 'Outlook good.',
    9: 'Yes.',
    10: 'Sign points to yes.',
    11: 'Reply hazy try again.',
    12: 'Ask again later.',
    13: 'Better not tell you now.',
    14: 'No u',
    15: 'No me',
    16: 'Cannot predict now.',
    17: 'Concentrate and ask again.',
    18: 'Don\'t count on it.',
    19: 'My reply is no.',
    20: 'My sources say no.',
    21: 'Outlook not so good.',
    22: 'Very doubtful.',
    23: 'I deter to the last 8 ball user.',
    24: 'I am like 75% of americans, indecisive.',
    25: 'Ask <@285915453094756362>.'
}

async def try_command(message):
    command = message.content.replace(prefix,'')
    channel = message.channel
    if command.startswith('kick'):
        if message.author.permissions_in(channel).kick_members:
            command = command.split(' ')
            if len(command) > 2:
                for a in range(3,99):
                    try:
                        command[2] = '{} {}'.format(command[2],command[a])
                    except:
                        break
            reason = command[2]
            tokick = command[1]
            tokick = await resolve_user(command[1], message.channel.server)
            await try_kick(tokick,reason,message)
    elif command.startswith('ban'):
        if message.author.permissions_in(channel).ban_members:
            command = command.split(' ')
            if len(command) > 2:
                for a in range(3,99):
                    try:
                        command[2] = '{} {}'.format(command[2],command[a])
                    except:
                        break
            reason = command[2]
            tokick = command[1]
            await try_ban(tokick,reason,message)
    elif command.startswith('softban'):
        if message.author.permissions_in(channel).kick_members:
            command = command.split(' ')
            if len(command) > 2:
                for a in range(3,99):
                    try:
                        command[2] = command[a]
                    except:
                        break
            reason = command[2]
            tokick = command[1]
            await try_softban(tokick,reason,message)
    elif command.startswith('mute'):
        if message.author.permissions_in(channel).mute_members:
            command = command.split(' ')
            if len(command) > 2:
                for a in range(3,99):
                    try:
                        command[2] = '{} {}'.format(command[2],command[a])
                    except:
                        break
            reason = command[2]
            tomute = command[1]
            await try_mute(tomute,reason,channel)
    elif command.startswith('unmute'):
        if user.permissions_in(channel).mute_members:
            command = command.split(' ')
            tounmute = command[1]
            await try_unmute(tounmute,channel)
    elif command.startswith('cc'):
        if command == 'cc view':
            if len(customCommands.keys()) > 0:
                embed=discord.Embed(title="Custom Commands",description="Here is a list of specified custom commands.",color=0xa3d114)
                for key in customCommands.keys():
                    embed.add_field(name="{}".format(key),value="{}".format(customCommands[key]),inline=False)
                await client.send_message(channel,embed=embed)
            else:
                await client.send_message(channel,"There are no custom commands specified.")
        else:
            if message.author.permissions_in(channel).manage_messages:
                command = command.split(' ')
                if len(command) == 1:
                    embed=discord.Embed(title="Custom Command", description="View/Edit custom commands", color=0xa3d114)
                    embed.add_field(name='{}cc view'.format(prefix), value='Views the current custom commands.'.format(prefix), inline=False)
                    embed.add_field(name='{}cc edit (command name) (command reply)'.format(prefix), value='Edit an already made custom command.', inline=False)
                    embed.add_field(name='{}cc add (command name) (command reply)'.format(prefix), value='Create a custom command.', inline=False)
                    embed.add_field(name='{}cc delete (command name)'.format(prefix), value='Delete a custom command.', inline=True)
                    embed.set_footer(text="Used by {}".format(message.author.name))
                    await client.send_message(channel,embed=embed)
                else:
                    c = command[0]
                    choice = command[1]
                    if choice == 'add':
                        try:
                            alpha = command[2]
                            if len(command) > 3:
                                for a in range(4,99):
                                    try:
                                        command[3] = '{} {}'.format(command[3],command[a])
                                    except:
                                        break
                            beta = command[3]
                            if alpha in customCommands.keys():
                                raise KeyError
                            customCommands.setdefault(alpha,beta)
                            await client.send_message(channel,"Command '{0}' created.".format(alpha))
                        except IndexError:
                            await client.send_message(channel,"You must specify a Command Name and a Command Reply.")
                            return
                        except KeyError:
                            await client.send_message(channel,"This command already exists.")
                    elif choice == 'edit':
                        try:
                            alpha = command[2]
                            if len(command) > 3:
                                for a in range(4,99):
                                    try:
                                        command[3] = '{} {}'.format(command[3],command[a])
                                    except:
                                        break
                            beta = command[3]
                            if alpha in customCommands.keys():
                                customCommands[alpha] = beta
                                await client.send_message(channel,"Command '{}' successfully edited.".format(alpha))
                        except:
                            return
                    elif choice == 'delete':
                        try:
                            alpha = command[2]
                            customCommands.pop(alpha)
                            await client.send_message(channel,"Command '{}' successfully deleted.".format(alpha))
                        except Exception as e:
                            await client.send_message(channel,e)
    elif command.startswith('choose'):
        command = command.replace('choose ','')
        command = command.split(',')
        choice = random.randint(1,len(command)-1)
        await client.send_message(channel,"I choose '{}'!".format(command[choice]))
    elif command.startswith('yt'):
        query = command.replace('youtube ','')
        query_string = urllib.parse.urlencode({'search_query': query})
        html_content = urllib.request.urlopen('https://www.youtube.com/results?'+query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        await client.send_message(channel,"https://www.youtube.com/watch?v="+search_results[0])
    elif command.startswith('help'):
        embed=discord.Embed(title="Gamma Commands", description="This is a list of available commands.", color=0xa3d114)
        embed.add_field(name='Commands anyone can use:', value='--------------------------------', inline=False)
        embed.add_field(name='help', value='Shows a list of commands', inline=False)
        embed.add_field(name='cc view', value='Shows a list of custom commands', inline=False)
        embed.add_field(name='yt (query)', value='Searches youtube for a video based on your query.', inline=False)
        embed.add_field(name='choose (a[,b,c,...])', value='Chooses an option from the listed.', inline=True)
        await client.send_message(channel,embed=embed)
        embed=discord.Embed(title="Gamma Commands", description="This is a list of available commands.", color=0xa3d114)
        embed.add_field(name='Commands moderators can use:', value='-------------------------------------', inline=True)
        embed.add_field(name='kick (user) (reason)', value='Kicks a user from the server.', inline=False)
        embed.add_field(name='ban (user) (reason)', value='Bans a user from the server.', inline=False)
        embed.add_field(name='softban (user) (reason)', value='Kicks a user from the server, and deletes their messages.', inline=False)
        embed.add_field(name='unban (user)', value='Unbans a user from this server.', inline=False)
        embed.add_field(name='mute (user) (reason)', value='Mutes a user from typing in chat.', inline=False)
        embed.add_field(name='unmute (user)', value='Unmutes a user to allow typing in chat.', inline=False)
        embed.add_field(name='cc add (command) (response)', value='Creates a custom command and response.', inline=False)
        embed.add_field(name='cc edit (command) (response)', value='Edits a custom command and response.', inline=False)
        embed.add_field(name='cc delete (command)', value='Deletes a custom command.', inline=False)
        await client.send_message(channel,embed=embed)
    else:
        for key in customCommands.keys():
            if command == key:
                await client.send_message(channel,"{}".format(customCommands[key]))
    pass

async def try_mute(user,reason,message):
    mutee = message.channel.server.get_member(user)
    await client.send_message(mutee,"You were muted for the following reason: {}".format(reason))
    roles = message.channel.server.roles
    for role in roles:
        if role.name == 'Muted':
            mutedrole = role
            break
    await client.add_roles(mutee,mutedrole)
    pass

async def try_unmute(user,message):
    unmutee = message.channel.server.get_member(user)
    await client.send_message(unmutee,"You were unmuted.")
    roles = message.channel.server.roles
    for role in roles:
        if role.name == 'Muted':
            mutedrole = role
            break
    await client.remove_roles(unmutee,mutedrole)
    pass

async def try_softban(user,reason,message):
    kickee = message.channel.server.get_member(user)
    if kickee.permissions_in(message.channel).administrator:
        await client.send_message(message.channel,"I can't do that, they are an administrator!")
        return
    else:
        try:
            await client.send_message(kickee,"You were kicked for the following reason: {}".format(reason))
            await client.ban(kickee,7)
            await client.unban(message.channel.server,kickee)
        except:
            await client.send_message(message.channel,"They have DM's disabled, but were kicked.")
            await client.ban(kickee,7)
            await client.unban(message.channel,server,kickee)

async def try_ban(user,reason,message):
    banee = message.channel.server.get_member(user)
    if banee.permissions_in(channel).administrator:
        await client.send_message(channel,"I can't do that, they are an administrator!")
        return
    else:
        await client.send_message(banee,"You were banned for the following reason: {}".format(reason))
        await client.ban(banee,0)

async def try_kick(user,reason,message):
    kickee = message.channel.server.get_member(user)
    if kickee.permissions_in(channel).administrator:
        await client.send_message(channel,"I can't do that, they are an administrator!")
        return
    await client.send_message(kickee,"You were kicked for the following reason: {}".format(reason))
    await client.kick(kickee)

async def try_warn(user,reason,message):
    warnee = message.channel.server.get_member(user)
    await client.send_message(channel,"**<@{}>, you have been warned: {}.**".format(user,reason))

async def resolve_user(u_resolvable, server):
    if (u_resolvable.startswith("<@") or u_resolvable.startswith("<@!")) and u_resolvable.startswith(">"): #Covers Case of @
        return await server.get_member(u_resolvable.strip('<@!>'))
    elif u_resolvable.isdigit(): #Covers ID Case
        return await server.get_member(u_resolvable)
    else: #Covers Name Case
        mems = server.members
        for x in mems:
            if not u_resolvable.lower() in x.display_name.lower():
                continue
            return x
        return None

@client.event
async def on_message(message):
    if message.channel.is_private:
        return
    if message.channel.server.get_member(message.author.id).bot:
        return
    if message.content.startswith(prefix):
        await try_command(message)
        return
    if 'hello gamma' in message.content.lower():
        await client.send_message(message.channel,"Hello!")
    elif 'good bot' in message.content.lower():
        await client.send_message(message.channel,":heartpulse:")
    elif 'bad bot' in message.content.lower():
        await try_warn(message.author.id,"I AM THE BEST BOT",message.channel)
    elif message.content.lower() == 'epsilon':
        await client.send_message(message.channel,':facepalm: This is in no relation to Epsilon whatsoever.')
    elif message.content.lower().startswith('hey 8 ball'):
        await client.send_message(message.channel,"{}".format(eightballreactions[random.randint(1,len(eightballreactions)-1)]))
    elif message.content.lower().startswith('roll a d'):
        try:
            randonum = random.randint(1,int(message.content[8:]))
        except:
            await client.send_message(message.channel,"dude you gotta give me a number like come on mate")
            return
        await client.send_message(message.channel,"you rolled a... {}".format(randonum))
        if randonum < 5:
            await client.send_message(message.channel,"well that sucks")
        elif randonum == 20:
            await client.send_message(message.channel,"NATURAL 20 BOIS")
    elif message.content.lower() == 'i love you gamma':
        if message.author.id == '285915453094756362':
            await client.send_message(message.channel,"you cant do that, you love kill :(")
        elif message.author.id == '377495235309207552':
            await client.send_message(message.channel,"but xua will be sad if he finds out :(")
        else:
            await client.send_message(message.channel,"aww :heartpulse:")
    elif message.content.lower().startswith('set error channel'):
        if message.author.permissions_in(message.channel).manage_channels:
            errorSendingChannel = message.channel
            await client.send_message(message.channel,"Success!")

@client.event
async def on_error(event,*args,**kwargs):
    error = traceback.format_exc()
    message = args[0]
    await client.send_message(message.channel,":exclamation: An error has occured in {}:\n```{}```".format(event,error))

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,game=discord.Game(name="FUCK"))
    print('Bot loaded.')
    print('Connected to user: {}'.format(client.user.name))
    print('Connected servers:')
    for a in client.servers:
        print('* {0} ({1})'.format(a.name,a.me.nick))

token = os.environ['TOKEN']
client.run(token)
