#token = ODQzODIyMzg4MTIyMzUzNjk1.YKJc1g.Ng8imBF5SbeAybZubX_k6f71Sto
import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

client = commands.Bot(command_prefix="'")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def ban(ctx, name, *, reason=None):
    await name.ban(reason=reason)
    ctx.send("baned")


@client.command(pass_context=True)
async def kick(ctx, userName: discord.User):
    await client.kick(userName)
    ctx.send("kicked")


@client.command()
@commands.has_role('mod')
async def createRole(ctx, name):
    guild = ctx.guild
    await guild.create_role(name=name)

client.run('ODQzODIyMzg4MTIyMzUzNjk1.YKJc1g.Ng8imBF5SbeAybZubX_k6f71Sto')
