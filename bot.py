import discord
from discord.ext import commands
from hikari import Intents


Intents = discord.Intents.default()
Intents.members = True

bot=commands.Bot(command_prefix='[', intents = Intents)

@bot.event
async def on_ready():
    print("bot is online")
 
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1000666712506650627)
    await channel.send(f'{member} join!') 
   
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1000666712506650627)
    await channel.send(f'{member} leave!')
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('TOKEN')
