# -*- coding: utf-8 -*-
"""
Methods for handling txt files
Author: Shaun Seward
"""
import os

def fileToStringList(fileName):
    listOfStrings = []    
    file = open((fileName), 'r')
    for line in file:
        listOfStrings.append(line.strip("\n"))
    file.close()
    return listOfStrings
        

def addString(fileName, stringToAdd):
    file = open((fileName), 'a+')
    file.write(('\n' + stringToAdd))
    file.close()
        
    
def getFilePath():
    cwd = os.getcwd()
    return ("Current working directory: " + cwd)