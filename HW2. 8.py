# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:42:29 2016

@author: verroejiba
"""
''' Write functions for each that takes as input 
a value x in and an integer . The function should then calculate the solution to 
each and then feed that back into the function (going through the function a total of times).

'''


def fun1(x,n):
    """
    the function calculates the value of f(x)=3.95*（x-x**2）with n times recursion
    parameters:
    x: a number in [0,1] 
    n: numbers of recursion 
    """
    
    if n == 1:        #return the value for the function f_x = 3.95*(x-x**2)
        return 3.95*(x-x**2) 
    else:
        return fun1(fun1(x,1),n-1) #otherwise set the previous solution to x into the function and do this n times

def fun2(x,n):
    """
    the function calculuates the value function f(x)=3.95*x*(1-x）through n times recursion
    
    parameters:
    x: a number in [0,1] 
    n: number of recursion 
    """
    if n==1:     #Initial case 
        return 3.95*x*(1-x) 
    else:
        return fun2(fun2(x,1),n-1) #otherwise set the previous solution to x into the function and do this n times


def fun3(x,n):
    """
    the function calculates the value of f(x)=3.95*x-3.95*(x**2) through n times recursion
    
    parameters:
    x: a number in [0,1] 
    n: number of recursion 
    """
    if n==1:
        return 3.95*x-3.95*(x**2) #Intial case 
    else:
        return fun3(fun3(x,1),n-1) #otherwise set the previous solution to x into the function and do this n times

#Test Case: n=1, n = 10, n = 50, n = 100
print("When x = 0.5 , n = 1")
print("the answers return: ", fun1(0.5, 1), fun2(0.5, 1), fun3(0.5,1) )
print("When x = 0.5 , n = 2")
print("the answers return: ", fun1(0.5, 2), fun2(0.5, 2), fun3(0.5,2) )
print("When x = 0.5 , n = 10")
print("the answers return: ", fun1(0.5, 10), fun2(0.5, 10), fun3(0.5,10) )
print("When x = 0.5 , n = 50")
print("the answers return: ", fun1(0.5, 50), fun2(0.5, 50), fun3(0.5,50) )
print("When x = 0.5 , n = 100")
print("the answers return: ", fun1(0.5, 100), fun2(0.5, 100), fun3(0.5,100))
print("When x = 0.9 , n = 100")
print("the answers return: ", fun1(0.9, 100), fun2(0.9, 100), fun3(0.9,100))

'''
Comments:
We noticed that the functions do not yield the same answer. When the value of x 
gets closer to 1 and when n is large there is a difference in their results.
Fun1 decreease with increasing x and n , Fun2 decrease when 0<= x<= .5 and increase 
otherwise with n increasing in both cases, and Fun3 decrease when x<= .5, increase 
then decrease by the time x= .9 with increasing n for all cases ''' 