# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:25:31 2016

@author: verroejiba
"""

#number 6
import math

''' Use recursion to write a function that takes a positive integer and checks if it is prime
    parameter i = positive integer '''
def is_prime(i):
    
    if i <= 0: #checks if integer i is 0 or negative
        print("{0} is an invalid input. Choose a number larger than 0".format(i))
    elif i == 1: #if i = 1 is not prime
        return False
    else:
        if i == 2: #i = 2 is the first prime
            return True
        if i % 2 == 0: #ay factor of 2 is not prime
            return False
        for x in range(3, int(math.sqrt(i)) + 1, 2): #step by 2 to disregard the even number and compares the remain of that number to its sqrt rt 
            if i % x == 0:
                return is_prime(i) #recursion prime
        return print("{0} is a positive prime integer".format(i))
