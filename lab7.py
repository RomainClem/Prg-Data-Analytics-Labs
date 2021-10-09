import tools
from random import randrange
from math import hypot, log


# Question 1i
def powerV1(base, power_num):
    print(f"The value {base} raised to the power of {power_num} is: {base ** power_num}")


def powerV2(power_num, result):
    print(f"The logarithm of {result} with base {power_num} is: {log(result, power_num)}")


def question1i():
    powerV1(tools.intInput("base number => ", "p"), tools.intInput("power number => ", "p"))


def question1ii():
    powerV2(tools.intInput("Power number => ", "p"), tools.intInput("Result number => ", "p"))


# Question 2
def generateRandomNumber(range_num):
    return randrange(range_num)


def askUser():
    return tools.rangeInt("Please enter your guess: ", 0, 100)


def checkGuess(num, guess):
    if num > guess:
        print("Too low")
        return False
    elif num < guess:
        print("Too high")
        return False
    else:
        return True


def question2():
    randomNumber = generateRandomNumber(100)
    userInput = tools.intInput("Input number => ")
    guessAmount = 1

    while not checkGuess(randomNumber, userInput):
        guessAmount += 1
        userInput = tools.intInput("Please guess another number => ")

    print(f"Correct. You made a total of {guessAmount} guesses.")


#  Question 3
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


# Question 4
def average(a, b, c, d, e):
    return (a+b+c+d+e) / 5


def maxNumber(a, b, c, d, e):
    return max([a, b, c, d, e])


def minNumber(a, b, c, d, e):
    return min([a, b, c, d, e])


def sortNumber(a, b, c, d, e):
    return [a, b, c, d, e].sort(reverse=True)


def sumNumber(a, b, c, d, e):
    return a+b+c+d+e


#  Question 5

# x = tools.intInput("Enter X => ")
# y = tools.intInput("Enter Y => ")
#
# print(hypot(x, y))
