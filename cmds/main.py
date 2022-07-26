import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(selF, bot):
        selF.bot= bot
        
    @commands.command()
    async def ping(selF, ctx):
        await ctx.send(F'{round(selF.bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(Main(bot))