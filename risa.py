import random
import os
import logging
import discord

logging.basicConfig(level=logging.INFO)


noob_options = [
    "{} is a huge noob",
    "{} is a big noob",
    "{} is the biggest noob",
    "{} is a noob",
    "{} is the noob lord",
    "{} isn't a noob dummy"
]


class Risa(discord.Client):
    async def on_ready(self):
        logging.log(logging.INFO, f"Logged in as {self.user}")
        print(f"Logged in as {self.user}!")

    
    async def on_message(self, message):
        if message.author == client.user:
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
            else:
                try:
                    high = int(tokens[1])
                    num = random.choice(range(high)) + 1
                    await messaeg.channel.send(f'{num}')
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
                await message.channeel.send('only one persone please')
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