import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount : int = 0):
        await ctx.channel.purge(limit= amount)

def setup(client):
    client.add_cog(Clear(client=client))