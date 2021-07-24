import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @dm_only()
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Example(client=client))