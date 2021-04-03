# -*- coding: utf-8 -*-
"""
Methods for handling txt files
Author: Shaun Seward
"""

def fileToStringList(fileName):
    listOfStrings = []    
    try:
        file = open(fileName, 'r')
    finally:
        file.close()
        
    for line in file:
        listOfStrings.append(line.strip("\n"))
    return listOfStrings


def addString(fileName, stringToAdd):
    try:
        file = open(fileName, 'a+')
    finally:
        file.close()
    
    file.write(stringToAdd)
    
    
    
            

