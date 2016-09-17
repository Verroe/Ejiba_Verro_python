# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:19:03 2016

@author: verroejiba
"""
"""
    This funtion takes in a wordbank of anagrams from a text file and prints to 
    the console the sets containing the most anagrams with matching letters.
"""

from collections import defaultdict
#import defaultdict which is a subclass of the dict class that locates missing words

filename = input('Enter file name with anagram dictionary: ')
def anagram_sets(filename): #parameter --  filename, a file with the list of words
    anagram_dict = defaultdict(set) #create an empty set to store the words
    with open(filename) as wordbank: #opens the file
        for word in wordbank:
            word = word.rstrip() #this removes trailing character(whitespaces) from word
            anagram_dict[''.join(sorted(word))].add(word)   #adds sorted word to the set
    
   
        m = max(anagram_dict, key = lambda x: len(anagram_dict[x])) #max to get the characters containing the most words
        maxlength = len(anagram_dict[m]) #assign maxlength to the length of the object in anagram_dict with most words 
        while len(anagram_dict[m]) == maxlength: 
            print(anagram_dict[m]) #print words with max length
            del anagram_dict[m] #deletes the current set to run the next one
            m = max(anagram_dict, key = lambda x: len(anagram_dict[x])) #run the next set of anagrams
        

anagram_sets(filename)
