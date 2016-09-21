# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:34:23 2016

@author: verroejiba
"""

import math
#Number 1
''' The 12th term is the first term to contain three digits. Write a function 
that calculates the th term of the Fibonacci sequence. What is the index of the 
first term in the Fibonacci sequence to contain 100 digits?
    Parameter = d -- an interger of the desired number of digits'''
def digit(d):
    term = list() #empty list to store the value of Fib number
    f1 = 1
    f2 = 1
    n=3     #Start at n = 3 
    while True:
        fn = f1 + f2  #computes the Fib number  
        if fn not in term: #adds the computed fib number to the list
            term.append(fn)
            if d == (int(math.log10(fn))+1) in term: #print the index of the first term if the length of the digits in the list is d
                print("The index of the first Fib number with {0} digit is {1}".format(d, n))#print the number of digit and the index of the fib #
                print("The Fibonacci number of {0} digits is {1}".format(d, fn)) #prints the number of digits and  its fib number
                break
            else: #loops through the next number if the first condition is not met
                f1 = f2
                f2 = fn
                n += 1
        
digit(2)
digit(3)
digit(10)
        