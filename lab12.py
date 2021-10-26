import numpy as np


def question1():
    arr = np.random.randint(low=1, high=100, size=100)

    arr2 = arr % 2 == 1
    arr[arr2] = -1
    print(arr)
    # print(arr[arr2])

    arr[arr % 2 == 0] = arr[arr % 2 == 0] +1

    print(arr)


def question2():
    arr = np.array([1,3,4,5], dtype=int)
    arr2 = np.array([4,8,2,9], dtype=int)
    arr3 = np.intersect1d(arr, arr2)
    arr4 = np.setdiff1d(arr, arr2)
    print(arr3)
    print(arr4)


def question3():
    a = np.array([1,3,4,5,6,7,5,9,3,2,5,3])
    b = np.array([4,8,2,9,2,3,5,7,8,8,6,4])
    c = a == b
    b[c] = -1
    print(b)
    

def question4():
    a = np.array([1,3,4,5,6,7,5,9,3,2,5,3])
    b = np.where((a >= 5) & (a <=10))
    print(a[b])


def question5():
    print(np.__version__)


def question6():
    x = np.ones((3,3))
    print("Original array:")
    print(x)
    print("0 on the border and 1 inside in the array")
    x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
    print(x)
 

def question7():
    arr = np.array([[1, 3],[4, 5],[3, 4]])
    print(np.unique(arr))




question7()