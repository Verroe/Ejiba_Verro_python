# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:33:09 2016

@author: verroejiba
"""
import random
#Problem 8

   """
      This function is a "Guess the number"-game, where the number to be guessed 
      is randomly chosen between 1 and 20. Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) 
      This is how it should work when run in a terminal:  
      >>> import guess_number Hello! What is your name? Torbjörn Well, Torbjörn, 
      I am thinking of a number between 1 and 20. Take a guess.  10 Your guess 
      is too low. Take a guess. 15 Your guess is too low. Take a guess. 18 Good 
      job, Torbjörn! You guessed my number in 3 guesses!
     """
#No parameters needed     
def guess_number():
  
     print('Hello! What is your name? ')
     name = input() #user enter name
     print('\n') #new line
     print('Well, ',name,', ', 'I am thinking of a number between 1 and 20. Take a guess.')
     count = 0 #count the number of guesses starting at 0
     num = random.randint(1, 20) #stores a random number between 1 and 20 into num
     
     while True:
         guess = int(input()) #user input guessed number
         if guess < num: #check if the guessed number < the generated random num
             count += 1 #increment count by 1 for the guess
             print('Your guess is too low. Take a guess') #print this to the console
         elif guess > num: #check if the guessed num > the generated random num
             count += 1 
             print('Your guess is too high. Take a guess')
         elif guess == num: #case when the user guessed right 
             count += 1
             print('Good job,',name,'! You guessed my number in', count, 'guesses!')
             break
 
guess_number() 