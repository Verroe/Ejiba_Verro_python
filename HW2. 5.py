# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:04:40 2016

@author: verroejiba
"""

#Number 5
''' In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Write a function that calculates how many different ways £2 can be made using any number of coins?
 '''

def factorial(n):
     if n == 1:
        return 1
     else:
        return n* factorial(n-1)
        
def combination(n, r):
    
    if r == 0:
        return 1
    elif r <= n:
        num =factorial(n)
        den = factorial(r) * factorial(n-r)
        result = num/den
    print("There are {0} different ways for {1} choice(s) in {2}".format(result, r, n))
        
def combinatorics(total): 
    n = [1, 2, 5, 10, 20, 50, 100, 200]
    for r in range(1, len(n)):
        choice = list()
        if r == 0:
            return 1
        else:
            lset= len(combination(n,r))
            while lset <= lset:            
                newset = set(
            for s in new:
                for i in range(1, total): #picks the coefficient i 
                    if total == i * s:
                        print(total, i, s)
            combination(n, r)

            
            
            
        
    #print("There are {0} different ways to make 2£", c)
    


combinatorics()
    