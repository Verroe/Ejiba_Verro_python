# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:48:35 2016

@author: verroejiba
"""
''' Write a function that accepts a list of strings and uses recursion to return a sorted list. Each
    step should modify at most two elements in the list
    Parameter =  a list of strings''' 
    
def srt(lst, offset = None):
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
    