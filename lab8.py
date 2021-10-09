import tools


# Question 1
def q1():
    num1 = tools.intInput('Enter the first number ')
    num2 = tools.intInput('Enter the second number ')
    average = (num1 + num2) / 2
    print(average)


# Question 2
def q2ER():
    try:
        fileContent = open("tes.txt", "r")
    except IOError as error:
        fileContent = open("tes.txt", "w")
        print("File \"tes.txt\" didn't exist creating a new one.")

    try:
        line = fileContent.readline()
        print(line)

        number = int(line)
        print(number)

    except IOError:
        print("no line to read")
    except ValueError:
        print("Invalid literal")

    fileContent.close()


q2ER()
