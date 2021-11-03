import numpy as np
import pandas as pd

df = pd.read_csv("attacks.csv", encoding="ISO-8859-1")

def question1i():
    freqAttacks = df['Location']

    print(freqAttacks.value_counts().head(1)) 

def question1ii():
    locs = df['Country'].value_counts()
    print(type(locs))
    print(locs.head(6))


def question1iii():
    fatalAttacks = df['Country'][df['Fatal'] == 'Y']
    print(fatalAttacks.value_counts().head(6)) 
    
def question1iv():
    surfing = len(df[df['Activity'] == 'Surfing'])
    scuba = len(df[df['Activity'] == 'Scuba diving'])
    print(surfing)
    print(scuba)

def question2i():
    fatal = len(df[df["Fatal"]=="Y"])
    total = len(df)
    print(f"Percentage of attacks that are fatal: {fatal*100/total:.2f}")


def question2ii():
    # grouped_by_country = df.groupby("Country")
    # total_by_country = grouped_by_country.size()
    # fatal_by_country = grouped_by_country["Fatal"].apply(lambda x: (x=="Y").sum())
    # print((fatal_by_country*100/total_by_country))

    # fatal_attacks = df['Country'][df['Fatal'] == 'Y'].value_counts()
    # total_attacks = df['Country'].value_counts()
    # print((fatal_attacks * 100) / total_attacks) 

    countries = pd.unique(df["Country"])

    for c in countries:
        country = df["Country"] == c
        fatal = df["Fatal"] == 'Y'
        non_fatal = df["Fatal"] == 'N'

        country_fatal = df[country & fatal]
        country_non_fatal = df[country & non_fatal]

        if len(country_fatal) > 0:
            print('The percentage of fatal attacks: ',c, len(country_fatal)*100/(len(country_fatal)+len(country_non_fatal))) 


def calculateYearlyAttacks(df):
    group_by_country_year = df.groupby(["Country","Year"])
    print(group_by_country_year.size().sort_values(ascending=True))


def yearlyAttack(c, df):
    countryBool = df["Country"] == c
    for yr in pd.unique(df['Year']):
        if yr >1924 and yr <2016:
            print("woof")
calculateYearlyAttacks(df) 
