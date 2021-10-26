import numpy as np

def question1():
    arr = np.array([[1, 3, 4, 2, 3, 5],[4,6, 4, 5, 1, 5],[3,3, 41, 25, 1, 4]
        ,[3,3, 4, -5, 1, 4],[3,3, 4, 5, 1, 4],[3,3, 4, 5, 1, 4]])
    a = int(len(arr)/3)
    res = arr[a:a*2, a:a*2]
    print(arr)
    print(res)


def question2():
    arr = np.array([[1, 3, 4, 2, 3, 5],[4,6, 4, 5, 1, 5],[3,3, 41, 25, 1, 4]              
        ,[3,3, 4, -5, 1, 4],[3,3, 4, 5, 1, 4],[3,3, 4, 5, 1, 4]])
    a = int(len(arr[0])/2)
    print(arr[1:: 2, a:]) # rows with indexes: 1,3,5,7,9,…
    print(arr[:: 2, a:]) # rows with indexes: 0,2,4,6,8,…


def question3():
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')
    arr = np.unique(data[:,1])
    print(arr)


def question4():
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')
    resultMaxArr = np.amax(data[:, 9], axis=0)
    resultMinArr = np.amin(data[:, 9], axis=0)
    resultMeanArr = np.mean(data[:, 9], axis=0)

    print ("\t Max temp", resultMaxArr * 41)
    print ("\t Min temp", resultMinArr * 41)
    print ("\t Mean temp", resultMeanArr * 41)


question4()
    
        