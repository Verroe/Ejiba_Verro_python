# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:28:23 2016

@author: verroejiba
"""
import string, os, time

#Problem 4
''' Your task in this exercise is to write a procedure speak_ICAO()able to 
translate any text (i.e. any string) into spoken ICAO words.'''

icao = {'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta',
            'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
            'i':'india', 'j':'juliette', 'k':'kilo', 'l':'lee-ma',
            'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
            'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
            'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
            'y':'yankee', 'z':'zulu', '0': 'zero', '1': 'one',
            '2': 'two', '3': 'three', '4': 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
            
def speak_ICAO(text, letterpause = .25, wordpause = .5):
 
  os.system("'say' " + text ) #plays the words in text   
  wordlist = text.lower().split() #changes uppercase to lowercase and separate the word into a list
  for word in wordlist:
      for letter in word:
          if letter not in string.punctuation: #ignores punction in the words
              os.system("'say' " + icao[letter])  #plays the letter in icao
              time.sleep(letterpause) # pause between spoken letters
          time.sleep(wordpause)   # pause between spoken words

speak_ICAO("My mom is a nice lady.")        
speak_ICAO("Hip-hop anonymous")        