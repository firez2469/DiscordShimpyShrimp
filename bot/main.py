# bot.py
import os
import random
from discord.ext import commands
import asyncio
import random 


#def takes a string and converts it into a list of characters
def stringToCharList(string):
    charList = []
    
    for char in string:
        charList.append(char)
    return charList
        
#takes a list of chars and concatenates all indices left to right
def charListToString(charList):
    finalString =  ''
    
    for char in charList:
        finalString += char
    return finalString
    
#takes a string and removes all instances of the specified character
def removeChar(targetChar, string):
    stringToChars = stringToCharList(string)
    
    cleanCharList = []
    
    for char in stringToChars:
        if(not(char == targetChar)):
            cleanCharList.append(char)
    return charListToString(cleanCharList)

#Takes a string and replaces every instance of the target character with the
#replacement character
def replaceCharIn(targetChar, replacementChar, msg):
    stringToChars = stringToCharList(msg)
    
    cleanCharList = []
    
    for char in stringToChars:
        if(char == targetChar):
            cleanCharList.append(replacementChar)
        else:
            cleanCharList.append(char)
    return charListToString(cleanCharList)

#goes through a list of chars and replaces all of them with the replacement char
def replaceCharsIn(targetChars, replacementChar, string):
    finalString = string
    
    for char in targetChars:
        finalString = replaceCharIn(char, replacementChar, finalString)
    return finalString
            
#helpful commands for dealing with messages
#takes a Message object and returns it's content
def messageToString(msg):
    return msg.content

TARGET_CHARS = stringToCharList("-?.,;:!")

#determines whether a name appears in the String
def stringContainsName(msg, name):
    if name.lower() in replaceCharsIn(TARGET_CHARS," ", msg.lower()).split():
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
    await ctx.send("As Nick would say this is definitely not in my character archetype to do this.\nFuck you Nick lol")
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
        await ctx.send(("No dumb shit quotes found containing " + name.title()))
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
        
        outputMessage = name.title() + " has contributed " + str(count) + " dumb shit quotes... wow"
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
    
    percent = int((theirQuotes / totalQuotes) * 1000) / 10
    outputMessage = name.title() + " shares " + str(percent) + "%" + " of all dumb shit quotes."
    
    await ctx.send(outputMessage)
  

@bot.command()
async def dumb_shit_getall(ctx, name=""):
    channel = bot.get_channel(803112589156024371)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    theirQuotes = []
    outputMessage = ""
    for msg in messages:
        if(stringContainsName(msg.content, name)):
            theirQuotes.append(msg.content)
    
    for quote in theirQuotes:
        outputMessage = outputMessage + quote + "\n\n" 
    
    await ctx.send(outputMessage)
    
    
@bot.command()
async def be_a_man(ctx):
    channel = bot.get_channel(816486690982068234)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    msg = random.choice(messages)
    await ctx.send(msg.content)
    
    
    

@bot.command()
async def leaderboards(ctx):
    _leaderboards = {}
    channel = bot.get_channel(803112589156024371)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    authors = retrieveAuthors(messages)
    for author in authors:
        count = findAuthorCount(messages,author)
        _leaderboards[author] = count
    newLeaderboards = sortDict(_leaderboards)
    msg= "Dumb Shit Leaderboards: \n"
    for auth in newLeaderboards:
        msg+="{0}:{1} quotes \n".format(auth,newLeaderboards[auth])
    await ctx.send(msg)
    
def findAuthorCount(messages,author):
    count =0
    for msg in messages:
        if(stringContainsName(msg.content,author)):
            count+=1
    return count
    
dic = {"a":1,"b":9,"c":5}

def sortDict(dict1):
    maxVal = -1000
    maxKey = ""
    
    if len(dict1)>1:
        for k in dict1:
            if dict1[k]>maxVal:
                maxVal = dict1[k]
                maxKey = k
        dict1.pop(maxKey)
        newDict =dict1
        newVal= {maxKey:maxVal}
        newVal.update(sortDict(newDict))
        
        return newVal
    else:
        print(dict1)
        return dict1
    
#takes a 2 dimensional list and returns it as a single dimensional list
def flatten(list2d):
    flatList = []
    
    for element in list2d:
        if(type(element) is list):
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

def removeDuplicates(stringList):
    unique = []
    
    for element in stringList:
        if element.title() not in unique:
            unique.append(element.title())
    return unique     

# ASSUME: message input is a string
def lookForAuthor(message):
    messageList = message.split("\n")
    authorList = []
    
    for msg in messageList:
        splitMsg = msg.split("\"")
        if(splitMsg[0] == ''):
            authorList.append(splitMsg[len(splitMsg) - 1].strip(" :-"))
        elif(splitMsg[len(splitMsg) - 1] == ''):
            authorList.append(splitMsg[0].strip(" :-"))
    return authorList
        

def retrieveAuthors(messages):
    authors = []
    for msg in messages:
        authors.append(lookForAuthor(msg.content))
    return removeDuplicates(flatten(authors))


bot.run(TOKEN)
