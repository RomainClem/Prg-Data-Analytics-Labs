#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on a nice day / at least it's not raining

@author: Romain Clemencon

@ID: R00193006
"""
import numpy as np
#--------------------------------

"""
Beginning of task one
"""
def LineDetector():

    myImmutableCollection = []

    lineStart = ["\"", "\'"] 
    lineEnd = ["\"", "\'", "."]

    file = open('test.txt', 'r')
    fileContent = file.read()
    file.close()

    allWords = fileContent.split()

    ongoingSentence = False

    sentence = ""


    for word in allWords:
        if word[-1] in lineEnd and ongoingSentence:
            sentence += word + ' '
            myImmutableCollection.append(sentence)
            sentence = ""
            ongoingSentence = False
        elif word[0] in lineStart:
            ongoingSentence = True
            sentence += word + ' '
        elif ongoingSentence:
            sentence += word + ' '
    
    return myImmutableCollection # this is a collection of lines where each line has the aformentioned conditions.
    
"""
End of task one
"""
print(LineDetector())
#--------------------------------

"""
Beginning of task two
"""
def IntegerDetector(inputString):
    
    integerList = [] # this is a list that will keep the extracted substrings that can be converted into integer numbers from the input string (inputString)
    
    
    stringArray = inputString.split(" ")
    
    negative = False
    prevChar = False
    intConstructor = ""


    for str in stringArray:
        for char in str:
            if char == "-":
                if prevChar:
                    if len(intConstructor) > 0:
                        integerList.append(0 - int(intConstructor) if negative else int(intConstructor))
                        intConstructor = ""
                else:
                    negative = True
                    prevChar = True
            elif char.isnumeric():
                intConstructor += char
                prevChar = True
            elif len(intConstructor) > 0:
                integerList.append(0 - int(intConstructor) if negative else int(intConstructor))
                intConstructor = ""
                prevChar = False
                negative = False
    
    if len(intConstructor) > 0:
        integerList.append(0 - int(intConstructor) if negative else int(intConstructor))

    print(integerList)

"""
End of task two
"""

#--------------------------------


"""
Beginning of task three
"""
def CasualUsersAMPM():
    
    am = 0.0 # this is a variable that keeps the average number of casual users before midday
    pm = 0.0 # this is a variable that keeps the average number of casual users after midday
    
    data = np.genfromtxt('bikeSharing.csv', delimiter=",")
    
    #Sorry I'm not very familiar with am and pm, I assumed am is before 12 and pm 12 onwards 
    morning = data[data[:, 4] < 12]
    afternoon = data[data[:, 4] >= 12]
    
    am = np.mean(morning[:, 13])
    pm = np.mean(afternoon[:, 13])
    
    
    print("Average of Casual Users before midday is ", am)
    print("Average of Casual Users after midday is ", pm)


"""
End of task three
"""
    