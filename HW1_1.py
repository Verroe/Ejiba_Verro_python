# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:49:11 2016

@author: verroejiba
"""

#Verro Ejiba Group A Homework 1 Due 9/15/2016
import os 
import io
import re 
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

'''Solution to number 1
A function to open and read the file to read to be checked for palindrome'''

def openFile(filename):
    file = open('filename.txt')
    file.read().split()
#Palindrome function
def is_palindrome: 
    for word in openFile(input('Enter file name: ')):
            reverse = word[::-1] #write the words backward
            if word == reverse:  #check for palindrome
                print(word, 'is a palindrome') #Prints the word to the screen
            else:
                print(word, 'is not a palidrome')
