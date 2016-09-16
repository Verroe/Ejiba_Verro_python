# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:36:51 2016

@author: verroejiba
"""
#Number 13

''' Your task in this exercise is as follows:  a. Generate a string with N 
opening brackets ("[") and N closing brackets ("]"), in some arbitrary order. 
b. Determine whether the generated string is balanced; that is, whether it 
consists entirely of pairs of  opening/closing brackets (in that order), none 
of which mis-nest'''
import random
#function that takes an integer n as a parameter
def string_gen(n):
    string = '' #create an empty string
    for i in range(2*n): #doubles the integer because the strings go in pairs               
        if random.randint(0,1) == 0:    #generates random number between 0 and 1 
            string += '[' #add [  to the string if the generated num = 0
        else: 
            string += ']' #add ] otherwise
    return(string)
#a function that checks if the generated string is balanced
def check(string):
    counter = 0 #
    for i in range (len(string)):     #loops through the length of string
        if string[i] == '[':          #the string at ith position is '[' 
            counter += 1              #increment counter by 1
        else:                         #decrease counter by 1 otherwise       
            counter -= 1 
            if counter < 0:            #counter < 0 is unbalanced therefore quit
                break
            
    if counter == 0:                  #string is balanced when counter = 0
        print(string, '\nOk')
    else:                               #unbalanced otherwise
        print(string, '\nNotOk')

check(string_gen(0))
check(string_gen(1))
check(string_gen(2))
check(string_gen(3))

