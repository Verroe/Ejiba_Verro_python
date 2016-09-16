# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:25:15 2016

@author: verroejiba
"""
#Solution to number 1

import os, string
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

'''Solution to number 1
A function to open and read the file to read to be checked for palindrome'''

    

def is_palindrome(word):
       
    reverse = word[::-1] #write the word backward where word is a string
    if word == reverse:  #check if the forward and backward versions 
        return True #are the same return true if yes
    
#Input your file name
filename = input("Enter text file name: ")
#Opens the file then reads its lines
file = open(filename)
line = file.readline()
while line: #makes sure there are no empty string in line
    emptystr = '' 
    lowcaseline = line.lower() #converts capital letters to lowercase
    for a in lowcaseline:
        if a in string.ascii_letters: # checks that strings are letters
            emptystr = emptystr + a   # then add them to emptystr
            
    if is_palindrome(emptystr) == True :
        print(line, 'is a palindrome') #Prints the word to the screen
    else:
        print(line, 'is not a palindrome')
        
    line = file.readline() #reads the next line
        
file.close()

#Solution to number 2
import string 

#problem number 2
'''Write a semordnilap recogniser that accepts a file name (pointing to a list
 of words) from the user and finds and prints all pairs of words that are 
 semordnilaps to the screen.'''

#Prompts user to enter the file name then open the file
filename = input('Enter your text file name: ')
file = open(filename)

def semordinlap(filename):   
    with file as text: # opens the file from the user
    #read text, remove punctuation by replacing with empty string, 
    #convert to lowercase, and split words into a list        
        wordlist = text.read().translate(str.maketrans(string.punctuation,'{0: ^32}'.format(''))).lower().split()
        for word in wordlist:   
            for drow in wordlist:
                if word == drow[::-1]: #check if the 1st word is the same with the 2nd written backward
                    print(word + " " + drow) #prints palindromes to the console
                    
semordinlap(filename)

#Solution to problem 3
import string
from tabulate import tabulate

#Problem 3
'''Write a procedure char_freq_table()that, when run in a terminal, 
accepts a file name from the user, builds a frequency listing of the characters 
contained in the file, and prints a sorted and nicely formatted character 
frequency table to the screen.'''
filename = (input("Enter text file name: "))
def char_freq_table(filename):
    with open(filename) as text: #open the file entered by user as text
        words = text.read() # read text
        headers = ["Char", "Freq"]     #a list to hold characters and its frequency
        table = []    #new list to hold character frequencies
        for i in range(len(string.printable)): # add the character at position i and its frequency to the list
            table.append([string.printable[i], words.count(string.printable[i])])      
        print(tabulate(table, headers, tablefmt="fancy_grid"))  #print table             
char_freq_table(filename)

#Solution to problem 4
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

#Problem 5
import os, string
#import re 
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory


#Input filename by useer then open it
filename = (input("Enter file name: "))
file = open(filename)
#Number 5
'''Solution to number 5: Print all hapaxes in a given file name text
    A function that find all the hapaxes
    given the following text check for the word that appears once '''
    
newset = set() #A new set to store words that appear one time
rset = set() #A set to store all the words that have been removed

def hapax(filename):
    with file as text: 
        #Changes all capital letters to lowercase and
        #Separates the sentence in words
        wlist = text.read().remove(string.punction).lower().split()
        for word in wlist: 
            if word not in newset:
                newset.add(word) #Add nonrepeated words to the new set
            else:
                rset.add(word) #Add all duplicate to remove set
            if word in rset:
                newset.remove(word) #Remove words that appear in the 2 sets
print(newset)
hapax(filename)

#Problem 6

import os, string
print(os.getcwd()) #Check the working directory 
chdir = os.chdir(input('Enter new directory: ')) #Change to the desired directory

'''Solution to number 6:  Write a program that given a text file will create a 
new text file in which all the lines from the original file are numbered from 
1 to n (where n is the number of lines)
'''


filename = input("Enter file name: ")
def enum_line(filename):
    nfile = "enumtext.txt"
    with open(nfile, 'w') as create: #open new file to write in 
        with open(filename) as text: #open file provided by user
            line = text.readline()  #Read line from the original file
            n=1                     #assign the number line starting with 1
            while line:
                create.write(str(n) + "." + line) #write in the new file adding number line followed by '.' with line from original text
                n += 1 #increment by 1 for number line 
                line = text.readline() #read next line in original text
            
enum_line(filename) #call the function above for testing

#Problem 7

import os 
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

'''Solution to number 7: A program that calculates the average word length of 
        a text stored in a file '''

filename = input('Enter file name: ')
#sep = avgFile.split()#splits the words in order to ignore spaces

def avgFile(filename):
    newset = set() #Created set that will take all the non repeated words not
    total = len(filename) #Count the total number of words 
    count = 0
    with open(filename) as text:
        for word in text: 
            if word not in newset: #counts and adds the word not in the new set
                count += len(word)
                newset.add(word)
            else: #counts the repeated words
                count += len(word)
                
        avg = (count)/total # calculates the average word length
        
    print(count, total, avg)
avgFile(filename)

#Problem 8

        
    
    
    



