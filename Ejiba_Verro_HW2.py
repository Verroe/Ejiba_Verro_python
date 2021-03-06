# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 07:37:42 2016

@author: verroejiba
"""
#==============================================================================
#Number 1
import math

def digit(d):
    ''' The 12th term is the first term to contain three digits. Write a function 
        that calculates the th term of the Fibonacci sequence. What is the index of the 
        first term in the Fibonacci sequence to contain 100 digits?
        
        Parameter:
        d - an interger of the desired number of digits
    '''
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

#==============================================================================
#Number 2
              

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
                  
    for x in range(len(triangle)-2, -1, -1):
        for y in range(0, x+1):
            triangle[x][y] += max(triangle[x+1][y], triangle[x+1][y+1])
    print("The maximum weighted path has sum {0}.".format(triangle[0][0]))
    
maxweight(triangle)

#==============================================================================
#Number 3

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
    i = 1 #will be used to count the number of terms in the chain with inital value of 1
    if n <1: #prompts user to enter an integer n
       print("Choose and integer greater than 1.")
       n = int(input())
       collatz(n)
    elif n ==1: # case for n = 1, 1->4->2->1 has 3 terms in the chain
        print("Your Collatz chain has 3 terms.")
        return(3)
    else: #Otherwise compute the numbers from the start n to deduce at 1
        while n > 1: 
            if n%2==0: # divides by 2 if n is even, then increment i at which operation
                n = n/2
                i += 1
            else: # times 3 plus 1 if n is odd then increment the number of chains
                n = 3*n+1
                i += 1
        print("Your Collatz chain has {0} terms.".format(i)) #prints the number of chains
        return(i)

def main(maxrange):
    """
    This function returns the maximum chain length and the chain's starting
    value of all chains between 1 and parameter maxrange.
    
    Parameters:
    maxrange - integer value for upper end of calculation range (non-inclusive)
    """
    terms = [(n, collatz(n)) for n in range(1, maxrange)] #returns the number of chains for a given int n
    tup = max(terms, key = lambda x: x[1]) #puts the terms into a list then return the max

    print("The Collatz chain has {1} terms with a starting value of {0}.".format(tup[0], tup[1]))


main(1000)

#Number 4

'''Write a function that calculates the length of the recurring cycle for a given 
integer. Use this function to find the value of d < 500 for which 1/d contains 
the longest recurring cycle in its decimal fraction part.

For this problem, it is sufficient to consider only denominators that are prime. All other numbers are either solely
made up of factors of 10 (meaning the decimal expansion is finite), or are made up of factors of 10 and smaller primes
(meaning that after some initial non-repetitive section, digits equal to the higher power of 2 or 5, repetend will be
equal to the length of some smaller prime's repetend). Andrew Stewart
'''

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
         #Function to take care of when the denomination is prime 
    if 10 < denominator:
        suborder = subgroup_order(10, denominator) 
        if denominator - 1 == suborder:
            return denominator - 1
        elif (denominator - 1) % suborder == 0:  # checks for even division between denominator -1 and suborder then return the its factr. Otherwise return denominator - 1
            return (denominator - 1) / suborder
        return denominator - 1   
    return denominator - 1   

def subgroup_order(element, modulus): #
    order = 1
    if modulus == 2: #the order is 1 for even numbers
        return order
    else:
        while (element ** order) % modulus != 1:  # 
            order += 1
    return order


def repetend_len(denominator): #Get the repeating number in the denominator
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

def count(S, m, n , ans) :
  
  	#case where the sum of the combination is 0
	if (n == 0) :
		# uncomment the below line to print all the combinations also
		# print(ans)
		return 1
	#For the case where the sum is < 0 return 0
	if (n < 0) :
		return 0
 
      #
	if (m <=0 and n >= 1) :
		return 0
  #Creat en empty string in which all the choices will be added and it stays the same if there is no answer
	temp = ''
	if(ans == '') :
		temp = ''
	else :
		temp = ans + "+"

	temp += str(S[m-1]) #increment temp by the number before last in the list

	# recursion step
	return count( S, m - 1, n ,ans) + count( S, m, n-S[m-1],temp)


arr = [1, 2, 5, 10, 20, 50, 100, 200]
m = len(arr)

print("TOTAL WAYS :: " + str(count(arr, m, 200, "")))

#Number 6
import math

def is_prime(i):
    ''' Use recursion to write a function that takes a positive integer and checks if it is prime
        
        Parameter:
        i = positive integer '''
    
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
def srt(lst, offset = None):
    ''' Write a function that accepts a list of strings and uses recursion to 
        return a sorted list. Each step should at most modify two elements of the list.
        
        Parameter: 
        lst - word list 
    '''
    #the case where sorting is insignificant
    if len(lst) <2 :
        print("There is not modification to make with the given input")
    else:
        #If there is no offset assigns the offset to the length of the list minus 1
        if (offset is None): 
            offset = len(lst) - 1
        #Loop ends when offset is 0    
        if (offset >= 0):
            
            lst = srt(lst, offset - 1)
            elt = offset #assigns offset to elt assuming that it is the smallest index in the list
            #Loop to search the element with the smallest index then change it
            for r in range(offset+1, len(lst)):
                if (lst[elt] > lst[r]):
                    elt = r
                    
            nelt = lst[offset] #assign the element at the index of the offset to nelt
            #swap the element at offset with the element at the smallest index
            lst[offset] = lst[elt] 
            lst[elt] = nelt
            #print the result
            print(str(offset+1))
            #print the result in a single list
            for r in range(0, len(lst)):
                print(lst[r])
        return lst
        
    
lst= [" I ","love", "God", "and", "my", "family"]
srt(lst)

#Number 8

def fun1(x,n):
    """
    the function calculates the value of f(x)=3.95*（x-x**2）with n times recursion
    
    Parameters:
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
    
    Parameters:
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