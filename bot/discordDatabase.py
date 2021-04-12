"""
DISCORD CHANNEL DATABASE CODE
"""

import discord

MAX_MSGS = 600

def discordChannelToStringList(bot, channelId):
    finalListOfStrings = []
    
    channel = bot.get_channel(channelId)
    messages = await channel.history(limit=MAX_MSGS).flatten()
    
    for msg in messages:
        finalListOfStrings.append(msg.content)
        
    return finalListOfStrings