
# import os
# import discord
# from discord.ext import commands

import os



import discord


intents = discord.Intents.all()

#client = discord.Client()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_connect():
    print('AadyaBot has connected to Discord!')

async def 
bot.run('MTAzNDIyNDY1MzI5Nzc3ODcxOQ.G-YBtg.bUzBBKv-hui0PC0jusqRQ_rT5mav4b15Vmcu-I')
  
my_secret = os.environ['TOKEN']
client.run(my_secret)

# intents = discord.Intents.all()

# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_connect():
#   print("Your bot is online!")

# @bot.command()
# async def aadya(ctx):
#   await ctx.reply("Hello from AadyaBot!")

# bot.run('MTAzNDIyNDY1MzI5Nzc3ODcxOQ.G-YBtg.bUzBBKv-hui0PC0jusqRQ_rT5mav4b15Vmcu-I')

# @client.event
# async def on_message(msg):
#   if msg.author==client.user:
#     return
#   if msg.content.startswith("!aadya"):
#     await msg.channel.send("Hello from AadyaBot!")

# my_secret = os.environ['TOKEN']
# client.run(my_secret)

