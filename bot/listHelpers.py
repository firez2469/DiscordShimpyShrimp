# -*- coding: utf-8 -*-
"""
List Helper methods

Author: Shaun Seward
"""

# Removes duplicates from the given string list and returns all the unique
# elements
def removeDuplicates(stringList):
    unique = []
    
    for element in stringList:
        if element.title() not in unique:
            unique.append(element.title())
    return unique

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

def isInList(target, listToSearch):
    for element in listToSearch:
        if (element == target):
            return True
    return False

def newLineString(listOfStrings):
    finalString = ""
    for string in listOfStrings:
        finalString += (string + "\n")
    return finalString