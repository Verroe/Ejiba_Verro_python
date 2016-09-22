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
        if (offset is None):
            offset = len(lst) - 1
            
        if (offset >= 0):
            
            lst = srt(lst, offset - 1)
            elt = offset
            
            for r in range(offset+1, len(lst)):
                if (lst[1] > lst[r]):
                    elt = r
                    
            nelt = lst[offset]
            lst[offset] = lst[elt]
            lst[elt] = nelt
            print(str(offset+1))
            for r in range(0, len(lst)):
                print(lst[r])
        return lst
        
    
lst= [" I ","love", "God", "and", "my", "family"]
srt(lst)
    