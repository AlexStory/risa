import random
import discord

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
            num = random.choice(range(100)) + 1
            await message.channel.send(f'{num}')
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


client = Risa()
client.run('NzE5NzE2ODM2NDkyNDQzNjY4.Xt7gsg.sRLA7LCIW3iIo6-EHTfK0Sv8vL8')