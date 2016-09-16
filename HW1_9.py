# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:38:47 2016

@author: verroejiba
"""
#Problem 9 

'''An anagram is a type of word play, the result of rearranging the letters of 
a word or phrase to produce a new word or phrase, using
all the original letters exactly once; e.g., orchestra = carthorse, A decimal 
point = I'm a dot in place. Write a Python program that, when started 1) 
randomly picks a word w from given list of words, 2) randomly permutes w 
(thus creating an anagram of w), 3) presents the anagram to the user, and 4) 
enters an interactive loop in which the user is invited to guess the original 
word'''

import numpy, random

color = ['orange', 'yellow', 'blue', 'red', 'brown'] #list of word choices
num = random.randint(0, len(color)-1) #select a random number from the length of a word from the list "color"
word = color[num] #hids the word that it at the position num -- from random selection


def anagramgenerator(choice):
    order = numpy.random.choice(len(choice), len(choice), replace = False) #permutes the order of a given word
    print(order)
    anagram = ''
    for i in range(len(order)):
        anagram = anagram + choice[order[i]] #add the word from permutation to make anagram
    return(anagram)
    

anagram = anagramgenerator(word)

def anagramGame():
    print('***Anagram***\n')
    print('Color word anagram: ',anagram,'\n') #prints the permutated word 
    while True:    
        guess = input('Guess the color word: ')#prompts user to enter guess
        if guess != word:
            print('Incorrect, guess again.')
        elif guess == word:
            print('Correct!')
            break
            
anagramGame()