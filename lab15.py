import numpy as np

data = np.genfromtxt('bikeSharing.csv', delimiter=",")

# Question 1
def compareHolidays(data, holiday):
    subset = data[data[:, 5] == holiday]
    print ("Number of entries ", len(subset))
    print ("Mean", np.mean(subset[:, 14]))



# compareHolidays(data, 0)
# compareHolidays(data, 1)

# Question 2
def normalizedValues(data):
    temp = np.copy(data[:,9])*41
    atemp = np.copy(data[:,10])*50
    hum = np.copy(data[:,11])*100
    windspeed = np.copy(data[:,12])*67
    print(temp)
    print(atemp)
    print(hum)
    print(windspeed)

# normalizedValues(data)

# Question 3
def question3():
    result = data[:, 13] > data[:, 14] # Boolean array 
    print ("Percentage of time where causal users > registered", (len(data[result])*100.0)/len(data) )


#Question 4

def averagePerCondition(data):
    conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}
    for key in conditions:
        subesetData = data[data[:,8] == key]
        print(f"{key}: ", np.mean(subesetData[:, 15]))


# averagePerCondition(data)

#Question 5

def analyseTemp(data, minvalue, maxvalue):
    hTemp = (data[: ,9]*41)>=minvalue
    lTemp = (data[: ,9]*41)<=maxvalue
    subset = data[hTemp & lTemp]
    meanVal = np.mean(subset[:, 13])
    print("for temp in range", minvalue, "to", maxvalue, "the mean val is", meanVal)


for temp in range(1, 40, 5):
    analyseTemp(data, temp, temp+4)
