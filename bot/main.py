# bot.py
import os
import random
from discord.ext import commands
import asyncio
import random 

#helpful commands for dealing with messages
#takes a Message object and returns it's content
def messageToString(msg):
    return msg.content

#determines whether a name appears in the String
def stringContainsName(msg, name):
    if name.lower() in msg.lower():
        return True
    else:
        return False

#Takes a list of messages and returns all messages as Strings
def messageListToStringList(msgList):
    stringList = []
    for msg in msgList:
        stringList.append(msg.content)
    return stringList
        




bot = commands.Bot(command_prefix='.')
counter = {}


TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
    #await channel.send('**THE NUKES WILL SOON BE DROPPED**')
    print(bot.guilds)



@bot.command()
async def dumb_shit(ctx,speech='False'):
    isTTS = speech=='True'
    channel = bot.get_channel(803112589156024371)
    #channel = bot.get_channel(803349900036669490)
    messages = await channel.history(limit=200).flatten()
    msg = random.choice(messages)
    
    await ctx.send(msg.content,tts=isTTS)

@commands.has_role('Admin')
@bot.command()
async def dumb_shit_loop(ctx,loop=5,speech='False'):
    isTTS = speech=='True'
    channel =bot.get_channel(803112589156024371)
    messages = await channel.history(limit=200).flatten()
    for av in range(loop):
        msg = random.choice(messages)
        await ctx.send(msg.content,tts=isTTS)


@bot.command()
async def dumb_shit_shaun(ctx):
    await ctx.send("Guys I can program discord bots lol")
#bot.loop.create_task(search_submissions())

@bot.command()
async def dumb_shit_specific(ctx, name=""):
    channel = bot.get_channel(803112589156024371)
    messages = await channel.history(limit=400).flatten()
    
    
    containingName = []
    
    for msg in messages:
        if(stringContainsName(msg.content, name)):
            containingName.append(msg)
    if (len(containingName) < 1):
        await ctx.send(("No dumb shit quotes found by " + name))
    else:
        msg = random.choice(containingName)
        await ctx.send(msg.content)
        



bot.run(TOKEN)