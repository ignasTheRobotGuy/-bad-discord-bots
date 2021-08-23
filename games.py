from math import trunc
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import check
from discord.ext.commands.errors import MissingRequiredArgument
import time
import random
client = commands.Bot(command_prefix="!",
                      description="type !help games for help")


@client.event
async def on_ready():
    print('the bot is ready and named - {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith("!help games"):
        # simp meter command stolen from dank memer
        await message.channel.send("games - !8ball, !blackJack, !simp_meter and !guess_the_number")


@client.command()
async def _8ball(ctx, *, request):
    aws = [
        "YES of course",
        "aha yep yep",
        "wel of course (what did you think)",
        "yes it will",
        "idk idk try again :/",
        "NO NO NO NO never!",
        "nope it will not",
        "no it will not",
        "sorrybut not"
    ]
    ctx.send(request)
    ctx.send(random.choice(aws))


@client.commands
async def simp_meter(ctx):
    number = random.randint(0, 101)
    ctx.send(f"you are %{number} simp!")


@client.commands
async def blackjack(ctx, inp):  # the moves are: hit stand or go back. and inp is for input
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 2,
        "Q": 3,
        "K": 4,
        "A": 10
    }
    p1_hand = ""  # player
    p1_score = 0
    p2_hand = ""  # "algo" robot, im gonna use a simple alg to make the 'best' choice
    p2_score = 0
    # alg
    risk = 30  # this is a precentage of the alg risk taking. so for 30% precent of the time if its 14 or 15 it will hit
    p2_card_1 = random.choice(cards)
    p2_card_2 = random.choice(cards)
    p2_hand += p2_card_1 + p2_card_2
    ctx.send(f"algo's hand-{p2_hand}")
    p1_card_1 = random.choice(cards)
    p1_card_2 = random.choice(cards)
    p1_hand += p1_card_1 + p1_card_2
    ctx.send(f"your hard is-{p1_hand}")
    prec = random.randint(0, 100)
    for i in p2_hand:
        ans = card_values[i]  # this will get the value of every card on hand
        p2_score += ans  # we wont do it for p1 yet. since we only need it now bec of the alg
    if prec > risk:  # non risk
        while p2_score < 14:
            NewCard = random.choice(card_values)
            p2_score += NewCard
    if prec <= risk:  # risk
        while p2_score <= 16:
            NewCard = random.choice(card_values)
            p2_score += NewCard

    # alg done
    running = True
    while running:
        text = await client.wait_for("message", check=None)
        if text == "go back":
            ctx.send("you quited")
            running = False
        if text == "hit":
            new_card = random.choice(cards)
            ctx.send(new_card)
            new_card_value = card_values[new_card]
            p1_score += new_card_value
            ctx.send(p1_score)
        if text == "stand":
            ctx.send(f"youre value:{p1_score} algo's value:{p2_score}")
            if p1_score > p2_score:
                ctx.send("you won! congrats :smile:")
            if p1_score < p2_score:
                ctx.send("sorry you lost :(")
            if p1_score == p2_score:
                ctx.send("DRAW! try again :/")
        else:
            ctx.send("try again. its hit, stand or go back ")


@client.command()
async def guess_the_number(ctx):
    try:
        # pick a random number from 1 - 1000
        random_number = random.randint(1, 1000)
        running = True
        wrong = 0  # we will use this to count how many times user guesses wrong. kinda like a score
        while running == True:
            message = await client.wait_for('message', check=None)
            message = int(message)
            if message < random_number:
                wrong += 1
                ctx.send("to high. try again")
            if message > random_number:
                wrong += 1
                ctx.send("to low. try again")
            if message == random_number:
                ctx.send("congrats!! you got it")
                ctx.send(f"your score is : {wrong}")
                running = False  # this will stop the loop
    except SyntaxError:
        ctx.send("its a number....")
