# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:51:38 2016

@author: verroejiba
"""

import os, string
#import re 
print(os.getcwd()) #Check the working directory 
chdir = os.chdir(input('Enter new directory: ')) #Change to the desired directory

'''Solution to number 6:  Write a program that given a text file will create a 
new text file in which all the lines from the original file are numbered from 
1 to n (where n is the number of lines)
'''

<<<<<<< HEAD

filename = input("Enter file name: ")
def enum_line(filename):
    nfile = "enumtext.txt"
    with open(nfile, 'w') as create: #open new file to write in 
        with open(filename) as text: #open file provided by user
            line = text.readline()  #Read line from the original file
            n=1                     #assign the number line starting with 1
            while line:
                create.write(str(n) + "." + line) #write in the new file adding number line followed by '.' with line from original text
                n += 1 #increment by 1 for number line 
                line = text.readline() #read next line in original text
            
enum_line(filename) #call the function above for testing
        
=======
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
>>>>>>> origin/master
