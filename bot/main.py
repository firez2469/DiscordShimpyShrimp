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
    if name.lower() in msg.lower().split():
        return True
    else:
        return False

#Takes a list of messages and returns all messages as Strings
def messageListToStringList(msgList):
    stringList = []
    for msg in msgList:
        stringList.append(msg.content)
    return stringList
        



MAX_MSGS = 400
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
    messages = await channel.history(limit=MAX_MSGS).flatten()
    msg = random.choice(messages)
    
    await ctx.send(msg.content,tts=isTTS)

@commands.has_role('Admin')
@bot.command()
async def dumb_shit_loop(ctx,loop=5,speech='False'):
    isTTS = speech=='True'
    channel =bot.get_channel(803112589156024371)
    messages = await channel.history(limit=MAX_MSGS).flatten()
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
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    
    containingName = []
    
    for msg in messages:
        if(stringContainsName(msg.content, name)):
            containingName.append(msg)
    if (len(containingName) < 1):
        await ctx.send(("No dumb shit quotes found by " + name))
    else:
        msg = random.choice(containingName)
        await ctx.send(msg.content)
        
@bot.command()
async def contributors(ctx):
    await ctx.send('Bot was developed by firez2469 \n Contributed to by DjSheep')

@bot.command()
async def dumb_shit_count(ctx, name=""):
    channel = bot.get_channel(803112589156024371)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    count = 0
    outputMessage = ""
    if(name == ""):
        outputMessage = "As a server we have " + str(len(messages)) + " dumb shit quotes. I am sorry everyone."
    else: 
        for msg in messages:
            if(stringContainsName(msg.content, name)):
                count += 1
        
        outputMessage = name + " has contributed " + str(count) + " dumb shit quotes... wow"
    await ctx.send(outputMessage)
    
@bot.command()
async def dumb_shit_percent(ctx, name=""):
    channel = bot.get_channel(803112589156024371)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    totalQuotes = len(messages)
    theirQuotes = 0
    
    for msg in messages:
        if(stringContainsName(msg.content, name)):
            theirQuotes += 1
    
    percent = int((theirQuotes / totalQuotes) * 1000)
    outputMessage = name + " shares " + str(percent) + "%" + " of all dumb shit quotes."
    
    await ctx.send(outputMessage)
    

bot.run(TOKEN)
