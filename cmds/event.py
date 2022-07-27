import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(selF, member):
        channel = selF.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} join!') 
   
    @commands.Cog.listener()
    async def on_member_remove(selF, member):
        channel = selF.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} leave!')
 
    @commands.Cog.listener()
    async def on_message(selF, msg):
         if msg.content == 'hello':
             await msg.channel.send('安安')
            
    @commands.Cog.listener()
    async def on_message(selF, msg):
         if msg.content == 'sleeping':
             await msg.channel.send('再讓我睡會,我很快起來zzz')

    @commands.Cog.listener()
    async def on_message(selF, msg):
         if '放火' in msg.content:
             await msg.channel.send('ㄐㄐ')
   
def setup(bot):
    bot.add_cog(Event(bot))