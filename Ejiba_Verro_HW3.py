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
#import matplotlib.pyplot as plt
#import numpy as np

abalone = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
abalone.columns =[]
income = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
income.colummns = []
diamond = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
diamond.columns=['Number','Carat','Colour','Clarity','Certification','Price']

def optbin(file):
    ''' a function that calculate the optimal bin size using the Freedman Diaconis rule
    bin size = 2(iqr(x)/(n^1/3))
    parameters:
    file = the data to compute the bin size of
    '''
    loc_stat = file.describe() #gets the stat summary of the data
    n = loc_stat.loc[['count']] #from summary get the size of the sample
    Q1 = file.quantile(.25) #get the first quantile
    Q3 = file.quantile(.75) #get the third quantile
    IQR = Q3 - Q1  #compute the IQR range #not giving the right output, how can this be fixed?
    bin_size = 2*(IQR/(n**(1/3))) #freedman rule 
    return bin_size
optbin(diamond)

def dist(file):
    '''A function that takes data as input, calculates the optimal bin size, 
    separate the outliers and print plots for histograms 
    file = data to work on 
    '''
    #gets the simple location statistics
    for c in file.columns.values :
        
        bins = optbin(file)
        Q1 = file.quantile(.25)
        Q3 = file.quantile(.75)
            
        lower = file[c].where(Q1 - (1.5*(Q3 - Q1))) #this line needs review
        upper = file[c].where(Q3 + (1.5*(Q3 - Q1)))#this line needs review
        
        outliers = (file[c] < lower) | (file[c] > upper)
        
        if outliers.empty == False :
            outliers.hist(file[c],bins) #plot the segment of data with outliers
        else:
            outliers.hist() #plot the segment of data wherever there is no outliers
        #file[c].boxplot() #plot the boxplot of the values of each column with numerical inputs'''

dist(diamond)
        
        
        
        
    