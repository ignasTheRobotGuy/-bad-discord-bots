import discord
import os
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
messages = ("create_user 'name' 'password'",
            "check_messages 'name' 'password'", "send_message 'friendName' 'friendPassword' 'your message'")  # i will print this to the user so he knows the commands
client = commands.Bot(command_prefix=";")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith("help phoneBot"):
        for i in messages:
            await message.channel.send("command: " + i)


@client.command()
# with this we will check if file exists and if not creates one
async def create_user(ctx, name, password):
    try:
        path = "your path"
        # this makes a file and the "path" is where to put the systems file link
        os.mkdir(os.path.join(path, name+password))
        path = os.path.join("file/path", name+password)  # changes path
        messages = open(path, "x")
    except FileExistsError:
        await ctx.send("your profile already exists")


@client.command()
async def check_messages(ctx, name, password):
    try:
        # first we will check if account exists and if True check the password
        NewPath = os.path.join("cd:/system/path/" + name+password)
        file = open(NewPath, "r")
        await ctx.send(file.read())
        file.close()

    except FileNotFoundError:
        await ctx.send("this account doesnt exists or you put in the wrong password-. use ;create_user for an a account")
    except:
        await ctx.sendd("somethings wrong")


@client.command()
async def send_message(ctx, friendName, friendPassword, *, message):
    try:
        link = os.path.join("link/" + friendName+friendPassword)
        file = open(link, "w")
        file.write(message)
        await ctx.send("sucsesfully sent")

    except FileNotFoundError:
        await ctx.send("who is your friend? :blushed:")
    except:
        await ctx.send("something went wrong error 404")


client.run("TOKEN |:")
