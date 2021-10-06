import tools
from random import randrange
from math import hypot


##Question 2

# randomNumber = randrange(100)
# userInput = tools.int_input("Input number <100 => ")

## Question 3

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# print(recur_factorial(7))

## Question 5

x = tools.int_input("Enter X => ")
y = tools.int_input("Enter Y => ")

print(hypot(x, y))