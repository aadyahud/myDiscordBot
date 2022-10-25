import discord
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event#hgjhgj
async def on_connect():
  print("Your bot is online!")

@bot.command()
async def aadya(ctx):
  await ctx.reply("Hello from AadyaBot!")

bot.run('bot token here')

async def Time(ctx, time1, time2)
  resp="yo"
  if "am" in time2.lower():
    resp="Good morning!"
  elif "pm" in time2.lower():
    if int(time1)<5:
      resp="Good afternoon!"
    else:
      resp="Good evening!"
  else:
    resp=""