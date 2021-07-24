import discord
from discord.ext import commands
from discord.ext.commands import ChannelNotFound, MissingRequiredArgument
import os

from discord.ext.commands.errors import CommandNotFound

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
    print(f"\n# Logged in as {client.user}", end="\n\n")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    error_to_skip = [CommandNotFound, MissingRequiredArgument]

    for error_type in error_to_skip:
        if isinstance(error, error_type):
            return

    raise error


client.run(os.getenv('DISCORD_TOKEN'))