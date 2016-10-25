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
import numpy as np

abalone = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
abalone.columns =['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight'
                    ,'Shell weight','Rings']
                    
income = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
income.colummns = ['AAGE','ACLSWKR','ADTIND','ADTOCC', 'AGI','AHGA','AHRSPAY','AHSCOL','AMARITL', 'AMJIND'
                    ,'AMJOCC','ARACE', 'AREORGN', 'ASEX', 'AUNMEM','AUNTYPE','AWKSTAT', 'CAPGAIN','CAPLOSS',
                    'DIVVAL','FEDTAX','FILESTAT','GRINREG','GRINST', 'HHDFMX','MARSUPWT', 'MIGMTR1','MIGMTR3',
                    'MIGMTR4','MIGSAME','MIGSUN','NOEMP','PARENT', 'PEARNVAL','PEFNTVTY', 'PEMNTVTY', 'PENATVTY',
                    'PRCITSHP','PTOTVAL','SEOTR','TAXINC','VETQVA','VETYN','WKSWORK']
                    
diamond = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
diamond.columns=['Number','Carat','Colour','Clarity','Certification','Price']

def optbin(file):
    ''' a function that calculate the optimal bin size using the Freedman Diaconis rule
    bin size = 2(iqr(x)/(n^1/3))
    
    Parameters:
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
    separate the outliers and print plots for histograms.
    
    Parameter:
    file - data  
    '''
    #Only takes numerical values in the dataframe
    file = file.select_dtypes(include=[np.number])
    
    for c in file.columns.values :
        
        bin_size = optbin(file)
        Q1 = file.quantile(.25)
        Q3 = file.quantile(.75)
                    
        lower = file[c].where(file[c]<(Q1 - (1.5*(Q3 - Q1)))).dropna() #gets the lower bounds dropping the missing data
        upper = file[c].where(file[c]>(Q3 + (1.5*(Q3 - Q1)))).dropna() #gets upper bound dropping the missing data
            
        loweroutliers = file[c] < lower
        upperoutliers = file[c] > upper
            
        if loweroutliers.empty == False :
            plt.hist(loweroutliers,bin = bin_size) #plot the segment of data with outliers
            plt.title("Lower Outlier Histogram")
            
        if upperoutliers.empty == False :
            plt.hist(upperoutliers, bin = bin_size) #plot the segment of data wherever there is no outliers
            plt.title("Upper Outlier Histogram")
            
        plt.boxplot(file[c]) #plot the boxplot of the values of each column with numerical inputs'''
        #plt.show()

dist(diamond)
        
        
        
        
    