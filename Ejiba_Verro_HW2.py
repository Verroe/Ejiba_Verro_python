# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 07:37:42 2016

@author: verroejiba
"""

#Number 1
import math
''' The 12th term is the first term to contain three digits. Write a function 
that calculates the th term of the Fibonacci sequence. What is the index of the 
first term in the Fibonacci sequence to contain 100 digits?
    Parameter = d -- an interger of the desired number of digits'''
def digit(d):
    f1 = 1
    f2 = 1
    n=3     #Start at n = 3 
    while True:
        fn = f1 + f2  #computes the Fib number  
        if d == (int(math.log10(fn))+1): #print the index of the number if the length of the digits is d
            print("The index of the first Fib number with {0} digits is {1}".format(d, n))#print the number of digit and the index of the fib #
            print("The Fibonacci number of {0} digits is {1}".format(d, fn)) #prints the number of digits and  its fib number
            break
        else: #loops through the next number if the first condition is not met
            f1 = f2
            f2 = fn
            n += 1
        
digit(3)
digit(10)
digit(100)

#Number 2

triangle= [   [75],
              [95, 64],
              [17, 47, 82],
              [18, 35, 87, 10],
              [20, 4, 82, 47, 65],
              [19, 1, 23, 75, 3, 34],
              [88, 2, 77, 73, 7, 63, 67],
              [99, 65, 4, 28, 6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
              [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
              [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
              [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
              [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
              [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
              [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
              

def maxweight(triangle):
    """
    This function finds the weight of the path with the highest sum through
    a triangle representing an acyclic digraph. Instead of evaluating every
    possible path, this function breaks the larger problem down into many
    sub-problems. 
    For any row except the bottom row, we have n sub-problems, where n is the
    number of nodes in the row. We begin at the next to last row at the bottom.
    Each vertex node has two options. thus we take the sum of the vertex and 
    the maximum of it's two option nodes. This value replaces the vertex node
    and we continue along the row repeating this same procedure for each vertex
    node. Once a row is complete, we move up a row and repeat. Eventually, at 
    the vertex of the triangle, we are left with a single number. This is the 
    value of the maximum weighted path through the triangle.
    
    Parameters:
    triangle - a list of lists containing node weights.
        Example: [[1], [2,3], [4,5,6], [7,8,9,10]]
    """
    for x in range(len(triangle)-2, -1, -1):
        for y in range(0, x+1):
            triangle[x][y] += max(triangle[x+1][y], triangle[x+1][y+1])
    print("The maximum weighted path has sum {0}.".format(triangle[0][0]))
    
maxweight(triangle)

#Number 3

"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even) n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and
finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all
starting numbers finish at 1.
Write a program that calculates the length of the Collatz chain for a given integer. Which starting number,
under one thousand, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one thousand.
"""

def collatz(n):
    """
    This function is an implementation of the Collatz chain for starting value
    n, following this rule:
    if n is even, n → n/2
    if n is odd, n → 3n + 1.
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and
    finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all
    starting numbers finish at 1.
    
    Parameters:
    n - integer starting value (n >= 1)
    """
    i = 1 #
    if n <1: # 
       print("Choose and integer greater than 1.")
       n = int(input())
       collatz(n)
    elif n ==1: # r
        print("Your Collatz chain has 3 terms.")
        return(3)
    else:
        while n > 1: 
            if n%2==0: # 
                n = n/2
                i += 1
            else: # 
                n = 3*n+1
                i += 1
        print("Your Collatz chain has {0} terms.".format(i))
        return(i)

def main(maxrange):
    """
    This function returns the maximum chain length and the chain's starting
    value of all chains between 1 and parameter maxrange.
    
    Parameters:
    maxrange - integer value for upper end of calculation range (non-inclusive)
    """
    terms = [(n, collatz(n)) for n in range(1, maxrange)] #
    tup = max(terms, key = lambda x: x[1]) #

    print("The Collatz chain has {1} terms with a starting value of {0}.".format(tup[0], tup[1]))


main(1000)

#Number 4

def is_prime(n):
    """
    This function checks to see if a number is prime.
    Returns TRUE if the number is prime.

    Parameters:
    n - integer to be tested for primality
    """
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False


def prime_denom(denominator):
         # 
    if 10 < denominator:
        suborder = subgroup_order(10, denominator)
        if denominator - 1 == suborder:
            return denominator - 1
        elif (denominator - 1) % suborder == 0:  # 
            return (denominator - 1) / suborder
        return denominator - 1  # 
    return denominator - 1  # 

def subgroup_order(element, modulus):
    order = 1
    if modulus == 2:
        return order
    else:
        while (element ** order) % modulus != 1:  # 
            order += 1
    return order


def repetend_len(denominator):
    if denominator == 1:
        return int(0)
    elif is_prime(denominator):
        return prime_denom(denominator)


def main():
    repetends = set()
    for i in range(1,500):
        if is_prime(i):
            repetends.add((i, repetend_len(i)))
    print(max(repetends, key = lambda x: x[1]))

main()

#Number 5

#Number 6
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

#Number 7