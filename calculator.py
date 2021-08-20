
# token - NzU2ODI4MDk1NTExNTI3NDk0.X2XhFw.6yVwZwYXYplRFgY7d8xOhYqpslU

import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

client = commands.Bot(command_prefix="'")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith("help calculator"):
        await message.channel.send("example - 'calculator 36 / 6")


@client.command()
async def calculator(ctx, arg1, dec, arg2):
    try:
        ag1 = int(arg1)
        ag2 = int(arg2)
        if dec == "+":
            await ctx.send(ag1 + ag2)
        if dec == "-":
            await ctx.send(ag1 - ag2)
        if dec == "*":
            await ctx.send(ag1 * ag2)
        if dec == "/":
            await ctx.send(ag1 / ag2)
        else:
            await ctx.send("send - / + * or -")
    except ValueError:
        await ctx.send("dumbass its soposed to be a number")
client.run("TOKEN")
#ignas razmys's code