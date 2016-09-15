# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:25:15 2016

@author: verroejiba
"""
#Verro Ejiba Group A Homework 1 Due 9/15/2016
import os 
import io
import re 
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

#Solution to number 1
#A function to open and read the file to read to be checked for palindrome
def openFile(filename):
    file = open('filename.txt')
    file.read().split()

'''Solution to number 7: A program that calculates the average word length of 
        a text stored in a file '''
#Open the desired file
avgFile = openFile(input('Enter file name: '))
#sep = avgFile.split()#splits the words in order to ignore spaces
newset = set() #Created set that will take all the non repeated words not
total = len(avgFile) #Count the total number of words 
count = 0
def average(avgFile):
    for word in avgFile: 
        if word not in newset: #counts and adds the word not in the new set
            count += len(word)
            newset.add(word)
        else: #counts the repeated words
            count += len(word)
            
    avg = (count)/total # calculates the average word length
        
    print(count, total, avg)
        



