import discord
from discord.ext import commands
from datetime import datetime
import logging

#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents,)

global testingchannel; testingchannel=1338821320200425544
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    #im forced to do this cause "await can only be used in async functions"
    global outputchannel; outputchannel=(bot.get_channel(1339062070804742198) or await bot.fetch_channel(1339062070804742198))

@bot.event
async def on_message(message):
    if message.channel.id==testingchannel:
        timestamp=message.created_at.strftime('%H:%M')
        nickname=message.author.display_name
        username=message.author.name
        await outputchannel.send(f"`[{timestamp}] {nickname} ({username}):` {message.content}")

bot.run(
        open("discordtoken.txt").read(), 
        reconnect=True, 
        #log_handler=handler, 
        #log_level=logging.DEBUG
        )