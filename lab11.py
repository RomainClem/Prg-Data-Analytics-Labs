import tools
from os import name


def question1():
    students = {}
    studentFile = open("DataSet StudentDetails.txt", "r")
    for line in studentFile:
        data = line.split(' ')
        students[data[0]] = (int(data[1]) + int(data[2]) + int(data[3])) / 3
    
    while True:
        name = tools.readNonemptyString("Enter name => ")
        if name in students:
            print(f"{name}: {students[name]}")
        else:
            print(f"{name} not in database.")
        if tools.binaryOption("Do you wish to continue y/n =>", "y", "n") == "n":
            break


def question2():
    print("WIP")
    


def formatWord(word):
    itemToDelete = [",", ".", "?", "(", ")", ":", ";", "'s", "\"", "%", "&", "-"]
    
    for item in itemToDelete:
        if item in word:
            word = word.replace(item , "")
            
    return word

def question3():
    upperFreq = 10
    charLength = 10
    
    fileObj = open('SherlockHolmes.txt', 'r')
    fileContents = fileObj.read()
    fileObj.close()
    
    allWords = fileContents.split()
    
    dict = {}
    
    for word in allWords:
        
        alteredWord = formatWord(word)
        
        if alteredWord in dict:
            dict[alteredWord] = dict[alteredWord] +1
        else:
            dict[alteredWord] = 1
    
    for word in dict:
        if len(dict[word]) >= upperFreq:
            print(word, " -- ", dict[word])
    

question3()