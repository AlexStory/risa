import random
import os
import logging
import discord
import math
import requests

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


class Risa(discord.Client):
    async def on_ready(self):
        logging.log(logging.INFO, f"Logged in as {self.user}")
    
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$whisper'):
            emoji = '\U00002705'
            await message.add_reaction(emoji)
            await message.author.send('hi')
            return


        if message.content == '$joke':
            n = random.random()
            if n < .1:
                noob = random.choice(noobs)
                await message.channel.send(f'{noob}')
            else:
                headers = {
                    'Accept': 'application/json'
                }
                r = requests.get('https://icanhazdadjoke.com/', headers=headers)
                await message.channel.send(f'{r.json()["joke"]}')
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hi!')
            return

        if message.content.startswith('$say '):
            await message.channel.send(message.content[4:])
            return

        if message.content.startswith('$roll'):
            tokens = message.content.split(' ')
            tokens = [item for item in tokens if item != ' ']
            if len(tokens) == 1:
                num = random.choice(range(100)) + 1
                await message.channel.send(f'{num}')
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
                        await message.channel.send(f'{n} ({", ".join([str(r) for r in rolls])})')
                    else:
                        n = int(tokens[1])
                        num = math.floor(random.random() * n) + 1
                        await message.channel.send(f'{num}')
                except:
                    await message.channel.send('Enter the command as `$roll` or with a number like `$roll 6`')
            return

        if message.content == 'cool':
            await message.channel.send('cool cool cool')
            return

        if message.content.startswith('$noob '):
            if len(message.mentions) < 1:
                await message.channel.send('mention someone')
            elif len(message.mentions) > 1:
                await message.channel.send('only one persone please')
            else:
                template = random.choice(noob_options)
                await message.channel.send(template.format(message.mentions[0].mention))
            return

        if 'noob' in message.content:
            if random.random() < 0.2:
                await message.channel.send('no u')
            return


token = os.getenv('DISCORD_TOKEN')
client = Risa()

client.run(token)