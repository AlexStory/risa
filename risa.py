import random
import os
import logging
import math

import requests
import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)


noob_options = [
    "{} is a huge noob",
    "{} is a big noob",
    "{} is the biggest noob",
    "{} is a noob",
    "{} is the noob lord",
    "{} isn't a noob dummy"
]

def roll(n):
    num = math.floor(random.random() * n) + 1
    return num

noobs = [
    'lexan',
    'anqwah',
    'drago'
]


risa = commands.Bot('$')

@risa.event
async def on_ready():
    logging.log(logging.INFO, f"Loggid in as {risa.user.name}")


@risa.command()
async def whisper(ctx):
    emoji = '\U00002705'
    await ctx.message.add_reaction(emoji)
    await ctx.author.send('hi')

@risa.command()
async def joke(ctx):
    n = random.random()
    if n < .1:
        noob = random.choice(noobs)
        await ctx.send(f'{noob}')
    else:
        headers = {
            'Accept': 'application/json'
        }
        r = requests.get('https://icanhazdadjoke.com/', headers=headers)
        await ctx.send(f'{r.json()["joke"]}')

@risa.command()
async def hello(ctx):
    logging.log(logging.INFO, f'hi')
    await ctx.send('Hi!')

@risa.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@risa.command()
async def roll(ctx, *, arg):
    tokens = ctx.message.content.split(' ')
    tokens = [item for item in tokens if item != ' ']
    if len(tokens) == 1:
        num = random.choice(range(100)) + 1
        await ctx.send(f'{num}')
    elif len(tokens) == 2:
        try:
            if 'd' in tokens[1]:
                mod = 0
                [dice, size] = tokens[1].split('d')
                if '+' in size:
                    [size, mod] = size.split('+')
                    size = size.strip() 
                    mod = mod.strip()
                rolls = [roll(int(size)) for r in range(int(dice))]
                n = sum(rolls)
                if int(mod):
                    n += int(mod)
                await ctx.send(f'{n} ({", ".join([str(r) for r in rolls])})')
            else:
                n = int(tokens[1])
                num = math.floor(random.random() * n) + 1
                await ctx.send(f'{num}')
        except:
            await ctx.send('Enter the command as `$roll` or with a number like `$roll 6`')


@risa.command()
async def noob(ctx):
    if len(ctx.message.mentions) < 1:
        await ctx.channel.send('mention someone')
    elif len(ctx.message.mentions) > 1:
        await ctx.send('only one persone please')
    else:
        template = random.choice(noob_options)
        await ctx.send(template.format(ctx.message.mentions[0].mention))

@risa.event
async def on_message(message):
    if message.author == risa.user:
        return

    if message.content == 'cool':
        await message.channel.send('cool cool cool')
    
    if not message.content.startswith('$noob') and 'noob' in message.content:
        if random.random() < 0.2:
            await message.channel.send('no u')

    await risa.process_commands(message)


token = os.getenv('DISCORD_TOKEN')
risa.run(token)