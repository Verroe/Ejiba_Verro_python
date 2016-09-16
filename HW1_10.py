# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:39:59 2016

@author: verroejiba
"""
#Number 10 
''' In a game of Lingo, there is a hidden word, five characters long. The object 
of the game is to find this word by guessing, and in return receive two kinds 
of clues: 1) the characters that are fully correct, with respect to identity as 
well as to position, and 2) the characters that are indeed present in the word, 
but which are placed in the wrong position. Write a program with which one can 
play Lingo. Use square brackets to mark characters correct in the sense of 1), 
and ordinary parentheses to mark characters correct in the sense of 2). '''

def lingo_game():
    print('Welcome to Lingo! You will need to guess a letter in a word containing 5 characters')
    hidden = 'tiger' #hidden word
    while True:
        guess = input('Guess a letter: ') #prompts the user to enter a guess
        lhidden = list(hidden) #put the letters in hidden to a list
        lguess = list(guess) #put the letters in guess to a list
            
        if hidden == guess: #if all the letters in both hidden and guess are = print the word
            print('[t][i][g][e][r]')
            break
            
        for i in range(len(lguess)):
            if lguess[i] == lhidden[i]: #add then print the letter that are the same and the same position
                keep =('[',lguess[i],']')
                lguess[i]=''.join(keep)
                print(lguess[i])
            elif lguess in hidden: #put a () for a correct guessed letter that is in a wrong position
                nkeep =('(',lguess[i],')')
                lguess[i]=''.join(nkeep)
        clue = ''.join(lguess) #convert to string
        print('Clue: ', clue) #print the clue
            
lingo_game()

                