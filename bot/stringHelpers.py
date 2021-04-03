# -*- coding: utf-8 -*-
"""
String Handlers
@author: Shaun
"""

# def takes a string and converts it into a list of characters
def stringToCharList(string):
    charList = []
    
    for char in string:
        charList.append(char)
    return charList
        
# Takes a list of chars and concatenates all indices left to right
def charListToString(charList):
    finalString =  ''
    
    for char in charList:
        finalString += char
    return finalString
    
# Takes a string and removes all instances of the specified character
def removeChar(targetChar, string):
    stringToChars = stringToCharList(string)
    
    cleanCharList = []
    
    for char in stringToChars:
        if(not(char == targetChar)):
            cleanCharList.append(char)
    return charListToString(cleanCharList)

# Takes a string and replaces every instance of the target character with the
# replacement character
def replaceCharIn(targetChar, replacementChar, msg):
    stringToChars = stringToCharList(msg)
    
    cleanCharList = []
    
    for char in stringToChars:
        if(char == targetChar):
            cleanCharList.append(replacementChar)
        else:
            cleanCharList.append(char)
    return charListToString(cleanCharList)

# goes through a list of chars and replaces all of them with the replacement 
# char
def replaceCharsIn(targetChars, replacementChar, string):
    finalString = string
    
    for char in targetChars:
        finalString = replaceCharIn(char, replacementChar, finalString)
    return finalString

def isValidLink(stringToCheck):
    return True
