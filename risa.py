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

def _roll(n):
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
async def noob(ctx):
    if len(ctx.message.mentions) < 1:
        await ctx.send(f'{ctx.author.mention} is a huge noob')
    else:
        for mention in ctx.message.mentions:
            template = random.choice(noob_options)
            await ctx.send(template.format(mention.mention))

@risa.command()
async def roll(ctx, *, n='100'):
    try: 
        num = int(n)
        await ctx.send(f'{_roll(num)}')
    except:
        try:
            logging.log(logging.INFO, f'arg: {n}')
            if 'd' in n:
                [count, size] = n.split('d')
                logging.info(f'initial count and size: {count} {size}')
                count = int(count)
                mod = 0
                if '+' in size:
                    [size, mod] = size.split('+')
                    size = int(size)
                    mod = int(mod)
                else:
                    size = int(size)
                rolls = [_roll(size) for item in range(count)]
                logging.info(f'rolls: {rolls}')
                logging.info(f'count: {count}')
                logging.info(f'size: {size}')
                logging.info(f'mod: {mod}')
                await ctx.send(f'{sum(rolls) + mod} ({",".join(rolls)}')
        except:
            await ctx.send('Bad input try like one of the following: `roll` `roll 6` `roll 2d6+3`')


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