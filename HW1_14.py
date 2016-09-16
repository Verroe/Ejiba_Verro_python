# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:46:18 2016

@author: verroejiba
"""

#Number 14

''' An alternade is a word in which its letters, taken alternatively in a strict 
sequence, and used in the same order as the original word, make up at least two 
other words. All letters must be used, but the smaller words are not necessarily 
of the same length. For example, a word with seven letters where every second 
letter is used will produce a four-letter word and a three-letter word.'''

filename = input('Enter file name: ')

def alternade(filename):
    
    with open(filename) as file: 
        wordbank = file.read().split() #read the filea nd separate line into words
        
        for word in wordbank:
            smallword_1 = '' #create an empty string to store the first new word
            smallword_2 = '' #create an empty string to store the 2nd word
            word_1 = ''
            word_2 = ''
    
        if len(word) == 1: #case with word of 1 character can't make a word
            print('"' + word + '": makes no word.')
        elif(len(word)>1): #for words with more than 1 character
            for i in range(len(word)):
                if i%2==0: #get character in an even # position
                    smallword_1 = smallword_1 + word[i] #add word at that position to the first small word
                elif i%2 ==1: #get character in an odd # position
                    smallword_2 = smallword_2 + word[i] #add word at that position to the second small word
        for j in range (len(wordbank)):
            if(smallword_1 == wordbank[j]): #check if the 1st small word is in the word list
                word_1 = wordbank[j]        #assign it to word_1
            elif smallword_2 == wordbank[j]:#do the same for the 2nd small word
                word_2 = wordbank[j];       #assign it to word_2
    
        if word_1 != '' and word_2 !='':  #two new small words are made when word1 is not the same as word2
            print(word + ' makes ' + word_1 +' and ' + word_2 +'\n')

alternade(filename)