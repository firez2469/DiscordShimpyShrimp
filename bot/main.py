# bot.py
import os
import discord
import random
from discord.ext import commands
import asyncio
import random 
import time
import stringHelpers as sh
import listHelpers as lh
import textFileHelpers as txtHelp
import youtube_dl


#helpful commands for dealing with messages
#takes a Message object and returns it's content
def messageToString(msg):
    return msg.content

TARGET_CHARS = sh.stringToCharList("-?.,;:!")

#determines whether a name appears in the String
def stringContainsName(msg, name):
    if name.lower() in sh.replaceCharsIn(TARGET_CHARS," ", msg.lower()).split():
        return True
    else:
        return False



#Takes a list of messages and returns all messages as Strings
def messageListToStringList(msgList):
    stringList = []
    for msg in msgList:
        stringList.append(msg.content)
    return stringList
        

def findRole(listOfRoles, roleName):
    for role in listOfRoles:
        if(role.name == roleName):
            return True
    return False

MAX_MSGS = 600
MSG_LENGTH = 2000
bot = commands.Bot(command_prefix='.')
counter = {}


TOKEN = os.getenv('DISCORD_TOKEN')

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
    #await channel.send('**THE NUKES WILL SOON BE DROPPED**')
    print(bot.guilds)

@bot.command(pass_context=True)
async def help(ctx):
    
    if(findRole(ctx.message.author.roles, "Admin")):
        embedAdmin = discord.Embed(
            title="Admin Help",
            description="Shrimpy Shrimp Admin Commands",
            color = 0x808080)
        embedAdmin.set_footer(text="Developed by D.J.~Sheep")
        embedAdmin.add_field(name=".dumb_shit_loop",
                             value="Returns n amount of dumb shit quotes.",
                             inline=False)
        embedAdmin.add_field(name=".dumb_shit_shaun",
                             value="Dumb Shaun command lol",
                             inline=False)
        embedAdmin.add_field(name=".dumb_shit_compare_to",
                             value="Takes a name and a username and determines how many of the users sent quotes contains their own name.",
                             inline=False)
        embedAdmin.add_field(name=".add_hug",
                             value="Adds a hug to the hug directory",
                             inline=False)
        embedAdmin.add_field(name=".get_directory",
                             value="Command for determining the file directory.",
                             inline=False)
        embedAdmin.add_field(name=".leaderboards",
                             value="Generates a leaderboard for all dumb shit quotes.",
                             inline=False)
        await ctx.message.author.send(embed=embedAdmin)
        
    embed = discord.Embed(
        title="Help",
        description="Shrimpy Shrimp Commands",
        color = 0x808080
        )
    embed.set_footer(text="Developed by D.J.~Sheep")
    embed.add_field(name=".dumb_shit",
                    value="Returns a random dumb shit quote",
                    inline=False)
    embed.add_field(name=".dumb_shit_specific",
                    value="Takes a name and returns a random dumb shit quote from that person",
                    inline=False)
    embed.add_field(name=".dumb_shit_count",
                    value="Takes a name and returns how many dumb shit quotes this person has",
                    inline=False)
    embed.add_field(name=".dumb_shit_percent",
                    value="Takes a name and determines the percent of all dumb shit quotes they have contributed.",
                    inline=False)
    embed.add_field(name=".dumb_shit_getall",
                    value="Takes a name and returns all of their dumb shit quotes",
                    inline=False)
    embed.add_field(name=".be_a_man",
                    value="Returns a random be a man quote",
                    inline=False)
    embed.add_field(name=".be_a_man_count",
                    value="Returns the total amount of be a man quotes",
                    inline=False)
    embed.add_field(name=".ask_shrimp",
                    value="Ask Shrimpy Shrimp a question",
                    inline=False)
    embed.add_field(name=".prayer",
                    value="Sends a daily prayer",
                    inline=False)
    embed.add_field(name=".hug",
                    value="Takes a name and hugs the given target",
                    inline=False)
    embed.add_field(name=".punch",
                    value="Takes a name and punches the given target",
                    inline=False)
    embed.add_field(name=".cuddle",
                    value="Takes a name and cuddles the given target",
                    inline=False)
    embed.add_field(name=".die",
                    value="Dies",
                    inline=False)
    embed.add_field(name=".discombobulate",
                    value="Takes a name and discombobulates the given target.",
                    inline=False)
    await ctx.send(embed=embed)


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
  
@commands.has_role('Admin')
@bot.command()
async def dumb_shit_compare_to(ctx, name, user):
    channel = bot.get_channel(803112589156024371)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    targetUser = user
    targetSeen = 0
    targetName = name
    lom = []
    
    for msg in messages:
        if(stringContainsName(msg.content, targetName)):
            lom.append(msg)
    
    for msg in lom:
        if(msg.author.name == targetUser):
            targetSeen += 1
    
    await ctx.send(str(int(targetSeen / len(lom) * 1000) / 10) + "% are from themselves")

    
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
        if(len(outputMessage + quote + "\n\n") > MSG_LENGTH):
            await ctx.send(outputMessage)
            outputMessage = ""
        outputMessage = outputMessage + quote + "\n\n" 
    
    await ctx.send(outputMessage)
    
    
@bot.command()
async def be_a_man(ctx):
    channel = bot.get_channel(816486690982068234)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    msg = random.choice(messages)
    
    #to find an image for embed
    beamanphotos = txtHelp.fileToStringList("./bot/beaman.txt")
    photo = random.choice(beamanphotos)
    
    embed = discord.Embed(
        title="Be a Man",
        description=msg.content,
        color = 0xff0000)
    embed.set_author(name="Be a Man Guy",
                     icon_url="https://yt3.ggpht.com/ytc/AAUvwnjoP97mMYHZDqiXHS11JO5Z0fvYZpXLnSZH4xUY=s900-c-k-c0x00ffffff-no-rj")
    embed.set_image(url=photo)
    await ctx.send(embed=embed)
    
@bot.command()
async def be_a_man_count (ctx):
    channel = bot.get_channel(816486690982068234)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    
    #to find an image for embed
    beamanphotos = txtHelp.fileToStringList("./bot/beaman.txt")
    photo = random.choice(beamanphotos)
    
    embed = discord.Embed(
        title="Be a Man",
        description=("We are " + str(len(messages)) + " tips closer to being a man."),
        color = 0xff0000)
    embed.set_author(name="Be a Man Guy",
                     icon_url="https://yt3.ggpht.com/ytc/AAUvwnjoP97mMYHZDqiXHS11JO5Z0fvYZpXLnSZH4xUY=s900-c-k-c0x00ffffff-no-rj")
    embed.set_image(url=photo)

    await ctx.send(embed=embed)
    
    
@bot.command()
async def ask_shrimp(ctx):
    ballResponses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidely so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes - definitely.", "You may rely on it."]
    msg = random.choice(ballResponses)    
    await ctx.send(msg)
    
@bot.command()
async def prayer(ctx):
    embed = discord.Embed(
        title="Daily Prayer", 
        description="Namu Amida butsu!",
        color=0x00ff00)
    embed.set_image(url='https://static.wikia.nocookie.net/real-life-heroes/images/9/94/Gautama-buddha-1.jpg/revision/latest/top-crop/width/360/height/450?cb=20180205063148')
    embed.set_author(name='Buddha',
                     icon_url='https://static.wikia.nocookie.net/real-life-heroes/images/9/94/Gautama-buddha-1.jpg/revision/latest/top-crop/width/360/height/450?cb=20180205063148')
    embed.add_field(name=ctx.message.author.name,
                       value="has called for our daily prayer.", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def random_song(ctx):
    channel = bot.get_channel(820143026525175818)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    msg = random.choice(messages)
    await ctx.send(";;play " + msg.content)
    
    if(not(stringContainsName("http"))):
        time.sleep(2)
        await ctx.send(";;play 1")

"""
INTERACTION COMMANDS:

    hug(ctx, string)     -- hugs the target
    punch(ctx, string)   -- punches the target
    cuddle(ctx, string)  -- cuddles the target

"""    
@bot.command()
async def hug(ctx, target):
    
    dadId = 181213007597142017
    lucyId = 406162486220423168
    cooperId = 755919229248602164
    
    channel = bot.get_channel(831305587525419018)
    hugGifs = await channel.history(limit=MAX_MSGS).flatten()
    gif = random.choice(hugGifs)
    
    if((target.lower() == "shaun" or target.lower() == "lucy") and (ctx.author.id == lucyId or ctx.author.id == dadId)):
        await ctx.send("Oh my godd eww cooties!!")
    elif((target.lower() == "lucy" or target.lower() == "cooper") and (ctx.author.id == cooperId or ctx.author.id == lucyId)):
        await ctx.send("GINGER moment")
    elif((target.lower() == "shaun" or target.lower() == "cooper") and (ctx.author.id == cooperId or ctx.author.id == dadId)):
        await ctx.send("Lady killers")
    elif(target.lower() == "shrimpy" or target.lower() == "shrimpy shrimp"):
        if(ctx.author.id == dadId):
            await ctx.send("My dad gave me a hug!!")
        else: 
            await ctx.send(ctx.author.mention + " gave me a hug thank you!")
    elif(ctx.author.id == 690402649555861524):
        await ctx.send("Zoey hugging " + target.title() + "'s mom lmao.")
    else:
        await ctx.send(ctx.author.mention + " gave " + target.title() + " a hug!")
    await ctx.send(gif.content)


@commands.has_role('Admin')
@bot.command()
async def add_hug(ctx, link):
    channel = bot.get_channel(831305587525419018)
    await channel.send(link)
    await ctx.message.delete()
    await ctx.send("Link added successfully")
        
@bot.command()
async def punch(ctx, target):
    punchGifs = txtHelp.fileToStringList("./bot/punchGifs.txt")
    gif = random.choice(punchGifs)
    
    if (target.lower() == "shrimpy" or target.lower() == "shrimpy shrimp"):
        await ctx.send("How dare you...")
    else:
        await ctx.send(ctx.author.mention + " punched " + target.title())
        await ctx.send(gif)
  

@bot.command()
async def cuddle(ctx, target):
    cuddleGifs = txtHelp.fileToStringList("./bot/cuddleGifs.txt")
    gif = random.choice(cuddleGifs)
    
    await ctx.send(ctx.author.mention + " is cuddling " + target.title())
    await ctx.send(gif)
    
@bot.command()
async def die(ctx):
    hugGifs = txtHelp.fileToStringList("./bot/hugGifs.txt")
    gif = random.choice(hugGifs)
    
    await ctx.send("Nope you can't do that sorry, have a hug instead.")
    await ctx.send("Shrimpy Shrimp hugged " + ctx.author.mention + "!")
    await ctx.send(gif)
    
@bot.command()
async def discombobulate(ctx, target):
    discombobulateGif = "https://thumbs.gfycat.com/IncredibleUglyAnophelesmosquito-max-1mb.gif"
    
    await ctx.send("This mustn't register on an emotional level, " + target)
    time.sleep(2)
    await ctx.send("First, distract target. ")
    time.sleep(1)
    await ctx.send("Then block his blind jab.")
    time.sleep(1)
    await ctx.send("Discombobulate")
    await ctx.send(discombobulateGif)
    time.sleep(3)
    await ctx.send("Dazed, he'll attempt a wild hay maker. Employ the elbow block.")
    time.sleep(1)
    await ctx.send("Discombobulate")    
    await ctx.send(discombobulateGif)
    time.sleep(2)
    await ctx.send("Block thorough left.")
    time.sleep(2)
    await ctx.send("Weaken right jaw.")
    time.sleep(1)
    await ctx.send("Discombobulate")    
    await ctx.send(discombobulateGif)
    time.sleep(3)
    await ctx.send("In summary:")
    time.sleep(2)
    await ctx.send("Discombobulate")    
    await ctx.send(discombobulateGif)
    

"""
WIP CODE

"""
def membersListToString(lom):
    newList = []
    for member in lom:
        newList.append(member.name)
    return newList

def userFind(ctx, targetUsername):
    listOfMembers = ctx.guild.members
    
    print(membersListToString(listOfMembers))
    
    for member in listOfMembers:
        if (member.name == targetUsername or member.nick == targetUsername):
            return member.mention()
        
    return targetUsername
@commands.has_role('Admin')    
@bot.command()
async def get_directory(ctx):
    await ctx.send(os.path.abspath('hugGifs.txt'))
    #await ctx.send(txtHelp.getFilePath())
    await ctx.send(str(open('./bot/hugGifs.txt').read().split(' ')[0]))

@commands.has_role('Admin')    
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
    
@commands.has_role('Admin')
@bot.command()
async def mentionTarget(ctx, target):
    target = userFind(ctx, target)
    await ctx.send(target)
    
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
    return lh.removeDuplicates(lh.flatten(authors))

"""
AUDIO SHIT
"""

bot.run(TOKEN)
