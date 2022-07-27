import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


Intents = discord.Intents.default()
Intents.members = True

bot=commands.Bot(command_prefix='[', intents = Intents)

@bot.event
async def on_ready():
    print("bot is online")
 


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'已加載 {extension}')
    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension}')
    
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'已重新加載加載 {extension}')
    
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
       bot.load_extension(F'cmds.{Filename[:-3]}')


if __name__ == "__main__":

#need to set up a json file call setting.json and import your TOKEN like mine
 bot.run(jdata['TOKEN'])