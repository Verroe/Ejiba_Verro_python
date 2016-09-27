# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:30:15 2016

@author: verroejiba
"""

#Homework3
import pandas as pd
#import matplotlib.pyplot as plt

data = 'https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv'
file = pd.read_csv(data)
file.columns=['Number','Carat','Colour','Clarity','Certification','Price']
file.describe() #print the simple location statistics
carat = file[['Carat']] #only print the "carat "column
carat.hist()
price = file[['Price']] #only print the "price" column
price.hist()
