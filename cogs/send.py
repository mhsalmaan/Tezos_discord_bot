import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only
from pytezos import pytezos
from decimal import Decimal

class Send(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @dm_only()
    async def send(self, ctx, ownkey,shell,  destination, amount):
        pytezos.using(key=ownkey, shell= shell).transaction(destination=destination, amount=Decimal(amount)).autofill().sign().inject()
        await ctx.send('Sent')

def setup(client):
    client.add_cog(Send(client=client))