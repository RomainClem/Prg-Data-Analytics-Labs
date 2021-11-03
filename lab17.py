import numpy as np
import pandas as pd

df = pd.read_csv("attacks.csv", encoding="ISO-8859-1")


def question1():
    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    grs =  df.groupby('Country')['Age'].mean()
    print(grs)


def question2():
    countryArea = pd.unique(df['Country'])
    for c in countryArea:
        cn1 = df['Country'] == c
        cn = df[cn1]
        areas = pd.unique(cn['Area'])
        print(c, len(areas))


def question3():
    countryArea = pd.unique(df['Country'])
    for c in countryArea:
        cn1 = df['Country'] == c
        cn = df[cn1]
        cn = cn.dropna(subset=['Area'])
        areas = pd.unique(cn['Area'])
        print(c, len(areas))


def question4():
    fatals = df[df['Fatal']=='Y']
    grs = fatals.groupby('Country')['Fatal'].size()
    print(grs)


def question5(df):
    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=['Age'])

    yrs = df.groupby('Year')
    averg = yrs['Age'].mean()

    print(averg.sort_values().tail(10))


question5(df)