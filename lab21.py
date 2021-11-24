from sklearn import datasets
from sklearn import tree

import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import math 
from sklearn.model_selection import train_test_split
from pandas import read_csv
import numpy as np
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from io import StringIO
from sklearn import linear_model
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import KBinsDiscretizer


def Q1():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
    flt = df [['Activity', 'Sex ', 'Fatal']].copy()
    
    HighFreq = max(flt['Sex '].value_counts())
    AllFreq = flt['Sex '].value_counts()
    IndHighFreq = AllFreq[AllFreq == HighFreq ].index[0]
    flt['Sex '] = flt['Sex '].fillna(IndHighFreq)
    
    flt = flt [['Activity', 'Sex ', 'Fatal']].dropna()
   
  
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
    
    allFatals = np.unique(flt['Fatal'])
    
    dict1 = {}
    c = 1 
    for ac in allFatals:
        dict1[ac] = c
        c = c+1
    
    flt['Fatal'] = flt['Fatal'] .map(dict1)
    #print(dict1)
    
    
    allgenders = np.unique(flt['Sex '])
    
    dict1 = {}
    c = 1 
    for ac in allgenders:
        dict1[ac] = c
        c = c+1
    
    flt['Sex '] = flt['Sex '] .map(dict1)
    
    

    X = (flt[['Activity', 'Sex ']])
    
    y = flt[['Fatal']]
    
    
    tree_clf = tree.DecisionTreeClassifier()
    
    cv_results = cross_validate(tree_clf,  X, y, cv=3, scoring='accuracy', return_train_score=True)
   
    print('Training  ',cv_results['train_score'].mean())
    
    #clf.fit(X_test, y_test)
   
    print('Testing ....  ',cv_results['test_score'].mean())
    

    

def Q2():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
    flt = df [['Activity', 'Country', 'Fatal']].copy()
    
    
    flt = flt [['Activity', 'Country', 'Fatal']].dropna()
    
   
    
    allActivities = np.unique(flt['Activity'].astype(str))
    
    dict2 = {}
    c = 1 
    for ac in allActivities:
        dict2[ac] = c
        c = c+1
    
    flt['Activity'] = flt['Activity'] .map(dict2)
    
    #print(dict2)
    
    allCountries = np.unique(flt['Country'].astype(str))
    
    dict2 = {}
    c = 1 
    for ac in allCountries:
        dict2[ac] = c
        c = c+1
    
    flt['Country'] = flt['Country'] .map(dict2)
    
    
    
    allFatals = np.unique(flt['Fatal'].astype(str))
    
    dict1 = {}
    c = 1 
    for ac in allFatals:
        dict1[ac] = c
        c = c+1
    
    flt['Fatal'] = flt['Fatal'] .map(dict1)
    #print(dict1)
    

    X = (flt[['Activity', 'Country']])
    
    y = flt[['Fatal']]
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=42)
    
    #tree_clf = tree.DecisionTreeClassifier( random_state=42)
    
    tree_clf =  DecisionTreeClassifier()
    
    tree_clf.fit(X_train, y_train)
   
    print('Training  ',tree_clf.score(X_train, y_train))
    
    
   
    print('Testing  ',tree_clf.score(X_test, y_test))

    

 

def Q3():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
    flt = df [['Activity','Age', 'Fatal']].copy()
    
    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    flt['Age'] = flt['Age'].fillna(flt['Age'].mean())
    
    flt.loc[flt['Activity'].str.lower().str.contains('surf', na=False), 'Activity'] = 0
    flt.loc[flt['Activity'].str.lower().str.contains('swimm', na=False), 'Activity'] = 1
    flt.loc[flt['Activity'].str.lower().str.contains('shark', na=False), 'Activity'] = 2
    
    flt['Activity'] = flt['Activity'].apply(pd.to_numeric, errors='coerce')
    
    
    flt = flt.dropna()
    
    
    allFatals = np.unique(flt['Fatal'])
    
    dict1 = {}
    c = 1 
    for ac in allFatals:
        dict1[ac] = c
        c = c+1
    
    flt['Fatal'] = flt['Fatal'] .map(dict1)
    
    
    X = (flt[['Activity', 'Age']])
    
    y = flt[['Fatal']]
    
    
    models = []
   
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('DTC', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(kernel='linear')))
    models.append(('RFS',RandomForestClassifier()))
    # evaluate each model in turn
    names = []
    results = {}
    for name, model in models:
        
        cv_results = cross_validate(model, X, y, cv=5, scoring='accuracy', return_train_score=True)
       
        results[name] = cv_results
        #print(cv_results)
    for models in results:
        print(models)
        print('Training  ',results[models]['train_score'].mean())
        print('Test  ',results[models]['test_score'].mean())
        




def Q4():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    dict = {'female': 1, 'male':2}
    df['Sex'] = df['Sex'] .map(dict)
    
    flt = df [['Survived', 'Pclass', 'Age', 'Sex']]
    
   
  
    flt = flt.dropna()
    


    X = (flt[['Sex', 'Pclass', 'Age']])
    
    y = flt[['Survived']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    c=1
    mylistTr =[]
    mylistTs =[]
    
    index = range(1, 51)
    for n in range(50):
        clf =  tree.DecisionTreeClassifier(max_depth=c, random_state=42)
        c = c+1
        clf.fit(X_train, y_train)
        
        #print(clf.score(X_train, y_train))
       
        mylistTr.append(clf.score(X_train, y_train))
        mylistTs.append(clf.score(X_test, y_test))
        
    plt.plot(index, mylistTr)
    plt.plot(index, mylistTs)
    plt.legend(['Train', 'Test'])
    plt.show()

 

def Q5():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    dict = {'female': 1, 'male':2}
    df['Sex'] = df['Sex'] .map(dict)
    
    flt = df [['Survived', 'Pclass', 'Fare', 'Sex']]
    
   
  
    flt = flt.dropna()
    


    X = (flt[['Sex', 'Pclass', 'Survived']])
    
    y = flt[['Fare']]
    
    
    
    y = y.dropna()
    y = y.values.reshape(-1,1)
    enc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
        #print(X)
    enc.fit(y)
    y = enc.transform(y)
    #print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    
    
    clf =  tree.DecisionTreeClassifier(max_depth=5, random_state=42)

    clf.fit(X_train, y_train)
        
        #print(clf.score(X_train, y_train))
       
    print(clf.score(X_train, y_train))
    print(clf.score(X_test, y_test))
    
    
Q5()