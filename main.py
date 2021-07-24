from hashlib import new
from typing import List
import discord
import os
from discord import user
from discord.user import User
import mnemonic
from pytezos import pytezos

client = discord.Client()

token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$create'):
        new_account = pytezos.key.generate()
        secretKey = new_account.secret_key()
        publicKey = new_account.public_key()
        publicHash = new_account.public_key_hash()
        keyList = {"SecretKey" : secretKey, "PublicKey" : publicKey, "PublicHash" : publicHash}
        await message.channel.send(keyList)

    if msg.startswith('$import'):
        mnemonics = msg[8:]
        account = pytezos.key.from_mnemonic(mnemonic= mnemonics)
        secretKey = account.secret_key()
        publicKey = account.public_key()
        publicHash = account.public_key_hash()
        keyList = {"SecretKey" : secretKey, "PublicKey" : publicKey, "PublicHash" : publicHash}
        await message.channel.send(mnemonics)
        await message.channel.send(keyList)

client.run(token)