# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:30:15 2016

@author: verroejiba
"""
''' The crux of your challenge is to find a way to calculate a reasonable bin size 
or number of bins given the scale of each numeric column and plot the distribution 
using that optimal bin. In your code, you will need to test for severe outliers 
that could hide the true shape of the distribution, separate that part of the data,
 and plot histograms for both segments of the distribution. You will also need 
 to plot a boxplot of the entire distribution.'''
#Homework3
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

abalone = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
income = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
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
        #print(file[c])
            
        Q1 = loc_stat.loc[['25%']]
        Q3 = loc_stat.loc[['75%']]
            
        lower = file[c].transform(Q1 - (1.5*(Q3 - Q1))) #this line needs review
        upper = file[c].transform(Q3 + (1.5*(Q3 - Q1)))#this line needs review
        
        outliers = (file[c] < lower) | (file[c] > upper)
        
        if outliers == True:
            outliers.hist() #plot the segment of data with outliers
        else:
            outliers.hist() #plot the segment of data wherever there is no outliers
        file[c].boxplot() #plot the boxplot of the values of each column with numerical inputs'''

dist(diamond)
        
        
        
        
    