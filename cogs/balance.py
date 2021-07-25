import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only
from pytezos import pytezos

class Balance(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @dm_only()
    async def balance(self, ctx, ownkey):
        await ctx.send(pytezos.using(key=ownkey).account())

def setup(client):
    client.add_cog(Balance(client=client))