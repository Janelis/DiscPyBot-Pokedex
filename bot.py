# bot.py
import funcsBot
import discord
import os
from dotenv import load_dotenv
import re
from libgen_api import LibgenSearch
import pokebase as pkb

load_dotenv()
TOKEN = os.getenv('TOKEN')
srch = LibgenSearch()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        #HELLO
        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

        #LIBGEN SEARCH
        if message.content.startswith('!search '):
            msg = re.sub('!search ','',message.content)
            results = srch.search_title(msg)
            resAmmount = len(results)
            fullReply = str(resAmmount) + ' Results Found!\n\n'
            
            for idx, i in enumerate(results):
                segment = '{} - {}\n'.format(i['Author'].partition(',')[0], i['Title'])
                if len(fullReply) + len(segment) < 2000:
                    fullReply += segment
                else:
                    break

            await message.reply(funcsBot.codeBlock(fullReply))

        #POKEMON SEARCH
        if message.content.startswith('!pokemon '):
            msg = re.sub('!pokemon ','', message.content)
            pkm = pkb.pokemon(msg)
            await message.reply('Looking for {}'.format(pkm))
            channel = message.channel
            await channel.send(file = discord.File(pkb.sprite('pokemon',pkm.id).path))
            await channel.send(funcsBot.codeBlock(funcsBot.blockfy(pkm)))
            




























intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)