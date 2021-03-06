# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:30:15 2016

@author: verroejiba
"""

#Homework3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

abalone = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
income = pd.read_csv()
diamond = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
diamond.columns=['Number','Carat','Colour','Clarity','Certification','Price']
diamond.describe() #print the simple location statistics
carat = diamond[['Carat']] #only print the "carat "column
carat.hist()
price = diamond[['Price']] #only print the "price" column
price.hist()
diamond.describe().loc[['count']]

#a function that takes data as input, calculates the optimal bin size, separate the outliers and print plots for histograms  
def dist(file):
    #gets the simple location statistics
    loc_stat = file.describe()
    for c in file.columns.values :
        Q1 = loc_stat.loc[['25%']]
        Q3 = loc_stat.loc[['75%']]
        lower = c.transform(Q1 - (1.5*(Q3 - Q1)))
        upper = c.transform(Q3 + (1.5*(Q3-Q1)))
        outliers = (c < lower) | (c > upper)
        
        if outliers == True:
            outliers.hist()
        else:
            outliers.hist()
        c.boxplot()
        
        
        
        
    