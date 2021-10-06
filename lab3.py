salary  = float(input("salary > ")) > 40
age = float(input("age > "))
work = float(input("work > "))
kid = bool(input("kid > "))

if ((salary and age > 25) or (work >= 25 and kid)):
    print("Question 1")

if ((salary or age > 35) and (work >= 10 or kid)):
    print("Question 2")