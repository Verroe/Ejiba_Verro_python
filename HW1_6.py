# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:51:38 2016

@author: verroejiba
"""

import os 
import io
import re 
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

#A function to open and read the file 
def openFile(filename):
    file = open('filename.txt')
    file.read().split()

#Solution to number 6: Number lines on the copied version of a specific file
example = '''Love your neighbor as you love yourself \n 
            This is the command from the Lord of Israel \n 
            Put your trust and whole heart in it '''

#open the desired file
#file = openFile(input('Enter file name: ')) 
#nlines = len(io.readline(example))  #Get the number of lines
for word in example:
    word
    for index in range(1, n):
        line = example.next()
        enumerate(line)
print(example)