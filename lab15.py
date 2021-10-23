import numpy as np


# # Question 2
# temp = np.copy(data[:,9])*41
# array[:, 9] *= 41


#Question 3
# result = data[:, 13] > data[:, 14] # Boolean array 

#Question 4

def averagePerCondition(data):
    conditions = {1:"C", 2:"L", 3:"M", 4:"H"}
    for key in conditions:
        subesetData = data[data[:,8] == key]
        print(np.mean(subesetData[:, 15]))

data = np.genfromtxt('bikeSharing.csv', delimiter=",")

#Question 5


def analyseTemp(data, minvalue, maxvalue):
    hTemp = (data[: ,9]*41)>=minvalue
    lTemp = (data[: ,9]*41)<=maxvalue
    subset = data[hTemp & lTemp]
    meanVal = np.mean(subset[:, 13])
    print("for temp in range", minvalue, "to", maxvalue, "the mean val is", meanVal)


for temp in range(1, 40, 5):
    analyseTemp(data, temp, temp+4)    
