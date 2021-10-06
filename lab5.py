import tools


# Question 1
def question1():
    area1 = tools.float_input("Rectangle #1 width => ") * tools.float_input("Rectangle #1 length => ")
    area2 = tools.float_input("Rectangle #2 width => ") * tools.float_input("Rectangle #2 length => ")

    width = area1 if (area1 > area2) else area2
    width = area1 if (area1 == area2) else width


# Question 2.ii
def question2ii():
    commercialYears = tools.int_input("How many years of commercial software development experience do you have: ") > 4
    microsoftCert = tools.binaryOption("Do you hold a Microsoft certification y/n:", "y", "n") == "y"
    firstClass = tools.binaryOption("Do you have a first class honours primary degree y/n:", "y", "n") == "y"

    eligibility = "" if (commercialYears and microsoftCert and firstClass) else "not"

    print(f"You are {eligibility} eligible for this position.")


# Question 3
def question3():
    quantity = tools.intInput("Enter quantity => ")

    while quantity < 1:
        print("Input a positive quantity")
        quantity = tools.intInput("Enter quantity => ")

    discount = 50 if quantity > 99 else 0;
    if 9 < quantity < 20:
        discount = 0.8
    elif 20 < quantity < 50:
        discount = 0.7
    elif 50 < quantity < 100:
        discount = 0.6


# Question 4.i
def limitMultiplication(num, limit):
    i = 0
    while i <= limit:
        print(f"{num}*{i} = {num * i}")
        i += 1


def question4i():
    number = tools.int_input("number => ")
    limitInput = tools.int_input("limit => ")

    limitMultiplication(number, limitInput)


# Question 4.ii
def tree(num, i=1):
    if i <= num:
        print(f"{i}" * i)
        tree(num, i + 1)


def question4ii():
    tree(5)


# Question 5
def question5():
    monthAmount = tools.intInput("How many months (min 1, max 12) => ")
    rainfall = []

    while monthAmount < 1 or monthAmount > 12:
        print("Min 1 and max 12")
        monthAmount = tools.intInput("How many months (min 1, max 12) => ")

    for x in range(monthAmount):
        rain = tools.floatInput(f"Please enter rainfall for month{x + 1} => ", "p")
        rainfall.append(rain)

    rainfall.sort()
    print("Highest rainfall value:", rainfall[monthAmount - 1])
    print("Lowest rainfall value:", rainfall[0])
    print("Average is:", (sum(rainfall) / monthAmount))


# Question 6
def question6():
    fib = [0, 1]
    for x in range(2, 40):
        fib.append(fib[x - 2] + fib[x - 1])

    fibIndex = tools.intInput("Number to Fibonacci (min 0, max 40)=> ")
    while fibIndex < 0 or fibIndex > 40:
        print("Min 0 and max 40")
        fibIndex = tools.intInput("Number to Fibonacci (min 0, max 40)=> ")

    print(f"Fib of {fibIndex} is {fib[fibIndex - 1]}")


# Question 7
def question7():
    i = tools.floatInput("Enter a number => ")
    o = tools.floatInput("Enter a number => ")

    operation = [(i + o), (i - o), (i * o), (i / o)]
    oType = ["Addition", "Subtraction", "Multiplication", "Division"]

    print(f"Would you like to perform:\n1.{oType[0]}\n2.{oType[1]}\n3.{oType[2]}\n4.{oType[3]}")
    choice = tools.rangeInt("=> ", 1, 4)

    print(f"{oType[choice - 1]} of {i} and {o} is {operation[choice - 1]}")


