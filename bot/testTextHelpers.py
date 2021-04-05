# -*- coding: utf-8 -*-
"""
textFiletesterclass
@author: Shaun
"""
import textFileHelpers as txtHelp

def testFileToStringList():
    listOfContents = txtHelp.fileToStringList('killMePlease.txt')
    print(listOfContents)


def testAppendSomething():
    stringToAdd = 'hello nick'
    txtHelp.addString('killMePlease.txt', stringToAdd)
    
    print(txtHelp.fileToStringList('killMePlease.txt'))
    
testFileToStringList()
testAppendSomething()
