# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:49:11 2016

@author: verroejiba
"""

#Verro Ejiba Group A Homework 1 Due 9/15/2016
import os, string
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

'''Solution to number 1
A function to open and read the file to read to be checked for palindrome'''

<<<<<<< HEAD
    

def is_palindrome(word):
       
    reverse = word[::-1] #write the word backward where word is a string
    if word == reverse:  #check if the forward and backward versions 
        return True #are the same return true if yes
    
#Input your file name
filename = input("Enter text file name: ")
#Opens the file then reads its lines
file = open(filename)
line = file.readline()
while line: #makes sure there are no empty string in line
    emptystr = '' 
    lowcaseline = line.lower() #converts capital letters to lowercase
    for a in lowcaseline:
        if a in string.ascii_letters: # checks that strings are letters
            emptystr = emptystr + a   # then add them to emptystr
            
    if is_palindrome(emptystr) == True :
        print(line, 'is a palindrome') #Prints the word to the screen
    else:
        print(line, 'is not a palindrome')
        
    line = file.readline() #reads the next line
        
file.close()
=======
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
>>>>>>> origin/master
