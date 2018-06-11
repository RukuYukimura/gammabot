import discord
from random import randint
from datetime import date

async def magic8ball():
  reactions = {
    1: 'It is certain.',
    2: 'Most likely.',
    3: 'Without a doubt.',
    4: 'Signs point to yes.',
    5: 'You may rely on it.',
    6: 'Reply hazy try again.',
    7: 'Ask again later.',
    8:'Better not tell you now.',
    9: 'Cannot predict now.',
    10: 'Concentrate and ask again.',
    11: 'Don\'t count on it.',
    12: 'My reply is no.',
    13: 'My sources say no.',
    14: 'Outlook not so good.',
    15: 'Very doubtful.',
    16: 'No u.',
    17: 'No me.'
  }
  return reactions[randint(1,len(reactions)-1)]

if __name__ == "__main__":
  import sys
  sys.exit(-1)
