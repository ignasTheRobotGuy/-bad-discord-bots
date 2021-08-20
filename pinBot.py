# NzU2ODI4MDk1NTExNTI3NDk0.X2XhFw.6yVwZwYXYplRFgY7d8xOhYqpslU
import time as t
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("help"):
        t.sleep(0.9)
        await message.channel.send("to use this bot type '-remind' then what you want to be reminded")
        t.sleep(0.9)
        await message.channel.send("then type the minutes you want to wait for the reminder. exemple -")
        t.sleep(0.9)
        await message.channel.send("-remind doHomework 15")


@client.command()
async def remind(ctx, reminder, timemin):
    slep = int(timemin)
    t.sleep(slep * 60)
    await ctx.send(reminder)

client.run("NzU2ODI4MDk1NTExNTI3NDk0.X2XhFw.6yVwZwYXYplRFgY7d8xOhYqpslU")
