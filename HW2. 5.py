# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:04:40 2016

@author: verroejiba
"""

#Number 5
''' In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Write a function that calculates how many different ways £2 can be made using any number of coins?

parameters: S -- list of available choices, m -- length of S, n -- the sum of 
differnet combination, ans -- answer for the different choices of coins 
 '''

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
    