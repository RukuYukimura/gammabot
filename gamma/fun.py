import discord
from random import randint
from datetime import date

async def magic8ball():
  reactions = {
    1: 'no',
    2: 'yes',
    3: 'try again'
  }
  return reactions[randint(1,len(reactions)-1)]

if __name__ == "__main__":
  import sys
  sys.exit(-1)
