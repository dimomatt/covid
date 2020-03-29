import sklearn
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv("train.csv")
countries = {}
for country in train["Country_Region"]:
    try:
        if countries[country]:
            continue
    except KeyError:
        countries[country] = 0

#note on nomenclature- infected vs. unifected can also be attributed to testing rate- better datasets might include all 
infected = {}
uninfected = {}

for country in countries:
    countries[country] = train.loc[train['Country_Region'] == country]
    if countries[country]["ConfirmedCases"].iloc[-1] == 0:
        uninfected[country] = countries[country]
    else:
        infected[country] = countries[country]


