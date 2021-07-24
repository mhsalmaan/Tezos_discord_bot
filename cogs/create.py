import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only
from pytezos import pytezos
import os

class Create(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @dm_only()
    async def create(self, ctx):
        new_account = pytezos.key.generate()
        secretKey = new_account.secret_key()
        publicKey = new_account.public_key()
        publicHash = new_account.public_key_hash()
        keyList = {"SecretKey" : secretKey, "PublicKey" : publicKey, "PublicHash" : publicHash}
        await ctx.send(keyList)

def setup(client):
    client.add_cog(Create(client=client))