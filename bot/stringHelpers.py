# -*- coding: utf-8 -*-
"""
String Handlers
@author: Shaun
"""
import listHelpers as lh

def listToStringList(stringList):
    output = ""
    if (len(stringList) == 2):
        return (stringList[0] + " and " + stringList[1])
    else:
        for i in range(len(stringList)):
            if (i != (len(stringList) - 1)):
                output += (stringList[i] + ", ")
            else:
                output += ("and " + stringList[i])
    return output    
def charInString(charToFind, string):
    for char in string:
        if char == charToFind:
            return True
    return False

def findIndexOfChar(targetChar, string):
    indexAt = -1
    for i in range(len(string)):
        if string[i] == targetChar:
            indexAt = i
    return indexAt

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

def findMultipleAuthors(stringToFindAuthors):
    uniqueAuthors = []
    
    splitMessage = stringToFindAuthors.split("\n")
    for quote in splitMessage:
        authorName = ""
        for char in quote:
            if (char == ":"):
                if (not(lh.isInList(authorName, uniqueAuthors))):
                    uniqueAuthors.append(authorName)
                    break
            authorName += char
    return listToStringList(uniqueAuthors)

def findAuthor(stringToFindAuthor):
    indexOfDash = findIndexOfChar("-", stringToFindAuthor)
    indexOfColon = findIndexOfChar(":", stringToFindAuthor)
    
    if(indexOfColon != -1):
        return findMultipleAuthors(stringToFindAuthor)
    elif(indexOfDash != -1):
        return stringToFindAuthor[indexOfDash + 2:]
    
def extractQuote(dumbShitMessage):
    quote = ""
    seenQuote = False
    if(charInString(":", dumbShitMessage)):
        return dumbShitMessage

    for char in dumbShitMessage:
        if (char == "\""):
            quote += char
            seenQuote = not(seenQuote)
        elif (seenQuote):
            quote += char
    return quote
            
        
def isValidLink(stringToCheck):
    return True

print(extractQuote("\"I feel like playing cards with God.\" - Lucy proceeding to eat 5 jelly beans"))
print(extractQuote("Shaun: \"Testing\"\nNick: \"Yes sir!\"\nShaun: \"Hellooooo\"\nLucy: \"derp\""))