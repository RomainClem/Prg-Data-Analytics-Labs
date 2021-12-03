from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import math 
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.preprocessing import KBinsDiscretizer

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVR
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier


from sklearn.cluster import KMeans

from sklearn import datasets

 

def Q1():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    flt = df [['Survived', 'Pclass', 'Age']]


    flt = flt.fillna(flt.mean())
    scalingObj = preprocessing.MinMaxScaler()
    newFLT = scalingObj.fit_transform(flt)
    kmeans = KMeans(n_clusters=2).fit(newFLT)   
    
    print(kmeans.inertia_) # this line returns cost
    #print(kmeans.predict([[0,3,55]]))
    
#Q1()    

def Q2():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    flt1 = df [['Survived', 'Sex', 'Age']].copy()
    
    
    allgenders = np.unique(flt1['Sex'])
    
    dict1 = {}
    c = 1 
    for ac in allgenders:
        dict1[ac] = c
        c = c+1
    
    flt1['Sex'] = flt1['Sex'] .map(dict1)


    flt1 = flt1.fillna(flt1.mean())
    
    scalingObj = preprocessing.MinMaxScaler()
    newFLT1 = scalingObj.fit_transform(flt1)
    
    kmeans = KMeans(n_clusters=2).fit(newFLT1)   
    
    print('3 attrs: ',kmeans.inertia_) # this line returns cost
    
    flt2 = flt1[['Survived',  'Age']]
    
    flt2 = flt2.fillna(flt2.mean())
    
    scalingObj = preprocessing.MinMaxScaler()
    newFLT2 = scalingObj.fit_transform(flt2)
    
    kmeans = KMeans(n_clusters=2).fit(newFLT2)   
    
    print('2 attrs"  ',kmeans.inertia_) # this line returns cost
    
#Q2()
    
def Q3():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    flt = df [['Pclass', 'Age']]


    flt = flt.fillna(flt.mean())
    
    scalingObj = preprocessing.MinMaxScaler() 
    newFLT = scalingObj.fit_transform(flt) #with scaling
    #newFLT = flt # without scaling
    costs = []
    for i in range(8):
    
        kmeans = KMeans(n_clusters=i+1).fit(newFLT)   
        costs.append(kmeans.inertia_)
        print(kmeans.inertia_) # this line returns cost
    indexs = np.arange(1, 9)
    plt.plot(indexs, costs)
    
# Q3()

def Q4():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
    flt = df [['Activity',  'Age']].copy()
    
    
    flt = flt [['Activity',  'Age']].dropna()
   
  
    
    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    flt['Age'] = flt['Age'].fillna(flt['Age'].mean())
    
    
    """
    Use .astype(str) to make sure all values are treated as string for converstion.
    """
    allActivities = np.unique(flt['Activity'].astype(str))
    
    dict2 = {}
    c = 1 
    for ac in allActivities:
        dict2[ac] = c
        c = c+1
    
    flt['Activity'] = flt['Activity'] .map(dict2)
    
    #print(dict2)
    
   
    
    
    

    X = (flt[['Activity', 'Age']])
    
    scalingObj = preprocessing.MinMaxScaler()
    newFLT = scalingObj.fit_transform(X)
    
    index = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    cost = []
    for i in range(10):
        kmeans = KMeans(n_clusters=i+2).fit(newFLT)   
        cost.append(kmeans.inertia_)
        i = i+1
    plt.plot(index, cost)
    # 3, 7
    
    kmeans = KMeans(n_clusters=7).fit(newFLT)  
    Y = kmeans.labels_
    X_train, X_test, y_train, y_test = train_test_split(newFLT, Y, test_size=0.3, random_state=42)
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    print(clf.score(X_train, y_train))
    print(clf.score(X_test, y_test))

# Q4()