from sklearn import datasets
from sklearn import tree

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import math 

 

def q1():
    feature1 = (np.random.rand(200)+1)*10
   
    feature1 = np.append(feature1, (np.random.rand(200)+1.5)*10)
    
    
    feature2 = (np.random.rand(200)*100)+100
   
    feature2 = np.append(feature2, (np.random.rand(200)*100)+150)
    
    claz = np.ones(200)
    claz = np.append(claz, np.ones(200)+1)
    #print(feature2)
    
    clf = tree.DecisionTreeClassifier()
    allFeatures = pd.DataFrame({'feature1':feature1, 'feature2':feature2})
    
    clf.fit(allFeatures, claz)
    print (clf.predict([[14, 245]]))

 

def q2():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    """ 
    Apprach 1 how to deal with categorical data when the number of
    unique categorical values is small and known to us ...
    
    """
    """
    dict = {'female': 1, 'male':2}
    df['Sex'] = df['Sex'] .map(dict)
    df['Sex'] = df['Sex'].astype(int)
    """
    
    """ 
    Apprach 2 how to deal with categorical data . where we can 
    use conditionas e.g., only chanege cells with values 'male' 
    from column 'Sex' to 2: df.loc[df['Sex']=='male', 'Sex'] = 2
    
    """
    
    df.loc[df['Sex']=='male', 'Sex'] = 2
    df.loc[df['Sex']=='female', 'Sex'] = 1
    
    
    
    flt = df [['Survived', 'Pclass',  'Sex']]

    print(flt.mean())
    flt = flt.fillna(flt.mean())
    
    
    X = (flt[['Pclass',  'Sex']])
    
    y = flt[['Survived']]
    tree_clf = tree.DecisionTreeClassifier()
    
    
    tree_clf.fit(X, y)   
    
    print (tree_clf.predict([[2.0, 20.0]]))

 

def Q3():
    df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")
    dict = {'female': 1, 'male':2}
    df['Sex'] = df['Sex'] .map(dict)
    
    flt = df [['Survived', 'Pclass', 'Age', 'Sex']]
  
    """
    filling the empty cells with the average of the exisiting values in each column.
    """
    flt = flt.fillna(flt.mean())
    
    X = (flt[['Pclass', 'Age']])
    
    y = flt[['Survived']]
    tree_clf = tree.DecisionTreeClassifier( random_state=42)
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))
    
    
    X = (flt[['Pclass', 'Age', 'Sex']])
    
    y = flt[['Survived']]
    tree_clf = tree.DecisionTreeClassifier(random_state=42)
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))
    

   


def Q4():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
    flt = df [['Activity', 'Age', 'Fatal']]
    
    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    
    flt = flt [['Activity', 'Age', 'Fatal']].dropna()
   
  
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
    

    X = (flt[['Activity', 'Age']])
    
    y = flt[['Fatal']]
    #print(np.shape(X), np.shape(y))
    
    tree_clf = tree.DecisionTreeClassifier( )
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))
    

    
def Q5_1():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
   
    
    flt = df [['Activity', 'Age', 'Fatal']].copy()
    
    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    
    flt = flt [['Activity', 'Age', 'Fatal']].dropna()
    flt = flt[flt['Age']<50]
    #print(np.shape(flt))
   
    
    allActivities = np.unique(flt['Activity'].astype(str))
    
    dict2 = {}
    c = 1 
    for ac in allActivities:
        dict2[ac] = c
        c = c+1
    
    flt['Activity'] = flt['Activity'] .map(dict2)
    
    #print(dict2)
    
    allFatals = np.unique(flt['Fatal'].astype(str))
    
    dict1 = {}
    c = 1 
    for ac in allFatals:
        dict1[ac] = c
        c = c+1
    
    flt['Fatal'] = flt['Fatal'] .map(dict1)
    #print(dict1)
    

    X = (flt[['Activity', 'Age']])
    
    y = flt[['Fatal']]
    #print(np.shape(X), np.shape(y))
    
    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    return tree_clf.score(X, y)

 

def Q5_2():
    df = pd.read_csv("attacks.csv",encoding = "ISO-8859-1")
    
    flt = df [['Injury', 'Age', 'Fatal']].copy()
    
    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    
    flt = flt [['Injury', 'Age', 'Fatal']].dropna()
    flt = flt[flt['Age']<50]
    #print(np.shape(flt))
   
    
    allActivities = np.unique(flt['Injury'].astype(str))
    
    dict2 = {}
    c = 1 
    for ac in allActivities:
        dict2[ac] = c
        c = c+1
    
    flt['Injury'] = flt['Injury'] .map(dict2)
    
    #print(dict2)
    
    allFatals = np.unique(flt['Fatal'].astype(str))
    
    dict1 = {}
    c = 1 
    for ac in allFatals:
        dict1[ac] = c
        c = c+1
    
    flt['Fatal'] = flt['Fatal'] .map(dict1)
    #print(dict1)
    

    X = (flt[['Injury', 'Age']])
    
    y = flt[['Fatal']]
    #print(np.shape(X), np.shape(y))
    
    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    return tree_clf.score(X, y)

 

def Q5():
    print(Q5_1())
    print(Q5_2())
 
Q5()