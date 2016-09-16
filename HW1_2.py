# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:34:53 2016

@author: verroejiba
"""
import string 

#problem number 2
'''Write a semordnilap recogniser that accepts a file name (pointing to a list
 of words) from the user and finds and prints all pairs of words that are 
 semordnilaps to the screen.'''

#Prompts user to enter the file name then open the file
filename = input('Enter your text file name: ')
file = open(filename)

def semordinlap(filename):   
    with file as text: # opens the file from the user
    #read text, remove punctuation by replacing with empty string, 
    #convert to lowercase, and split words into a list        
        wordlist = text.read().translate(str.maketrans(string.punctuation,'{0: ^32}'.format(''))).lower().split()
        for word in wordlist:   
            for drow in wordlist:
                if word == drow[::-1]: #check if the 1st word is the same with the 2nd written backward
                    print(word + " " + drow) #prints palindromes to the console
                    
semordinlap(filename)



