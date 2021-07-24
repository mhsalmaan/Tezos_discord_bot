import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only

from pytezos import pytezos

class Import(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['import', 'get'])
    @dm_only()
    async def _import(self, ctx, *, seedphrase):
        account = pytezos.key.from_mnemonic(mnemonic= seedphrase, passphrase='')
        secretKey = account.secret_key()
        publicKey = account.public_key()
        publicHash = account.public_key_hash()
        keyList = {"SecretKey" : secretKey, "PublicKey" : publicKey, "PublicHash" : publicHash}
        await ctx.send(keyList)
        await ctx.send(f'{ctx.author}')


def setup(client):
    client.add_cog(Import(client=client))