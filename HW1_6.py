# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:51:38 2016

@author: verroejiba
"""

import os 
#import io
#import re 
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

#A function to open and read the file 
def openFile(filename):
    file = open('filename.txt')
    file.read().split()

'''Solution to number 6: Number lines on the copied version of a specific file'''
#Open the desired file
example = openFile(input('Enter file name: ')

#open the desired file
sep = example.splitlines()
if ' ' in sep :
    sep.remove(' ')
n = len(sep)
print(n, "is the total number of lines")

for (num, line) in enumerate(sep):
    print('%d %s' % (num + 1, line))
