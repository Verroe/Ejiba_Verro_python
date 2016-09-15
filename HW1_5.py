# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:50:12 2016

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

'''Solution to number 5: Print all hapaxes in a given file name text
    A function that find all the hapaxes
    given the following text check for the word that appears once '''
#Open desired file 
file = openFile(input('Enter file name: '))
#Changes all capital letters to lowercase and
#Separates the sentence in words
wlist = file.lower().split() 
newlist = set() #A new set to store unduplicated words
rlist = set() #A set to store all the words that have been removed
def hapax(file)
    for word in wlist: 
        if word not in newlist:
            newlist.add(word) #Add nonrepeated words to the new set
        else:
            rlist.add(word) #Add all duplicate to remove set
        if word in rlist:
            newlist.remove(word) #Remove words that appear in the 2 sets
    print(newlist)
