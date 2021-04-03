# -*- coding: utf-8 -*-
"""
Methods for handling txt files
Author: Shaun Seward
"""

def fileToStringList(fileName):
    listOfStrings = []    
    file = open(fileName, 'r')
    for line in file:
        listOfStrings.append(line.strip("\n"))
    file.close()
    return listOfStrings
        

def addString(fileName, stringToAdd):
    file = open(fileName, 'a+')
    file.write(stringToAdd)
    file.close()
        
    
    
            

