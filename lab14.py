import numpy as np

def question1():
    a = np.random.randint(low=1, high=100, size=10)
    b = np.random.randint(low=1, high=100, size=10)
    arr3 = np.intersect1d(a, b)
    arr4 = np.setdiff1d(a, b)
    print(arr3)
    print(arr4)


def question2():
    aug = np.arange('2019-08', '2019-09', dtype='datetime64[D]')
    evenDays = aug[1::2]
    print(evenDays)


def question3():
    tNow = np.datetime64('now', 'h')
    age = np.datetime64(input("Date of birth => "))
    print(tNow - age)

def question5():
    x = np.ones((3,3))
    print("Original array:")
    print(x)
    print("0 on the border and 1 inside in the array")
    x = np.pad(x, pad_width=2, mode='constant', constant_values=0)
    print(x)

    x = np.array([[1, 2],[3, 4],[5, 3],[2, 5]])
    print("Original array:")
    print(x)
    print("0 on the border and 1 inside in the array")
    x = np.pad(x, pad_width=1, mode='mean')
    print(x)
    

def question6():
    aug = np.arange('2019-08', '2019-09', dtype='datetime64[D]')
    evenDays = aug[1::2]
    for i in evenDays:

        print(i)
        

def question7():
    TNow = np.datetime64('now', 'h')
    bd = np.datetime64(input('When is your birthday!?'))
    print(TNow- bd)