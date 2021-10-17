from typing import Mapping
import tools
from random import randrange


# Question 1
def question1():
    studentDict = {}

    while True:
        if tools.binaryOption("Add a student y/n => ", "y", "n") == "n":
            break
        studentName = tools.readNonemptyString("Student name => ")
        studentId = tools.intInput("Student ID => ", "p")
        if studentId in studentDict:
            print("Student ID already exist in dictionary, discarding data.")
        else:
            print(f"Adding {studentName} with {studentId} in the dictionary.")
            studentDict[studentId] = studentName

    print(studentDict)


# Question2
def question2():
    listConversion = [1, 2, 3, 2, 1, 5, 6, 2, 1]
    dictRepeat = {}

    for x in listConversion:
        if x in dictRepeat:
            dictRepeat[x] = dictRepeat[x] + 1
        else:
            dictRepeat[x] = 1

    print(dictRepeat)


# Question 3
def question3():
    dict1 = {"dog": "woof", "cat": "meow", "fox": "???", 3: 14}
    dict2 = {1: "one", 2: "two", 3: "three"}

    if len(dict1) <= len(dict2):
        shortestDict = dict1
        dictMerged = dict2
    else:
        shortestDict = dict2
        dictMerged = dict1

    print(f"Merging: \n- {shortestDict} \ninto \n- {dictMerged}.\n")

    for x in shortestDict:
        if x in dictMerged:
            choice = tools.binaryOption(f"Key '{x}' with value '{shortestDict[x]}' already exist with value '{dictMerged[x]}'."
                                        f"\nWhich would you like to keep: "
                                        f"\n1. {shortestDict[x]}"
                                        f"\n2. {dictMerged[x]}\n=> ", "1", "2")
            if choice == "1":
                dictMerged[x] = shortestDict[x]
        else:
            dictMerged[x] = shortestDict[x]

    print(f"Merging complete, new dictionary: \n- {dictMerged}")




# Question 4
def question4(first, second):
    return dict(zip(first, second))


# Question 5
def question5():
    dict = {}
    
    for x in range(10):
        dict[x+1] = randrange(1, 20)
    
    first = list(dict.keys())
    second = list(dict.values())
    
    print(first, second)
    
    
question5()