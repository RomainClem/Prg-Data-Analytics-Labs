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


question3()
