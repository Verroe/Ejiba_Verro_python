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

#solution to problem 8

import random

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

#Problem 10
'''In a game of Lingo, there is a hidden word, five characters long. The object
 of the game is to find this word by guessing, and in return receive two kinds 
 of clues: 1) the characters that are fully correct, with respect to identity 
 as well as to position, and 2) the characters that are indeed present in the 
 word, but which are placed in the wrong position. Write a program with which 
 one can play Lingo. Use square brackets to mark characters correct in the 
 sense of 1), and ordinary parentheses to mark characters correct in the sense of 2).'''

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

#Problem 11    
''' A sentence splitter is a program capable of splitting a text into sentences. 
The standard set of heuristics for sentence splitting includes 
(but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that
a. Periods followed by whitespace followed by a lower case letter are not 
sentence boundaries.  
b. Periods followed by a digit with no intervening whitespace are not sentence boundaries.  
c. Periods followed by whitespace and then an upper case letter, but preceded 
by any of a short list of titles are  not sentence boundaries. Sample titles 
include Mr., Mrs., Dr., and so on.  
d. Periods internal to a sequence of letters with no adjacent whitespace are 
not sentence boundaries (for  example, www.aptex.com, or e.g).  
e. Periods followed by certain kinds of punctuation (notably comma and more periods) 
are probably not sentence boundaries.Your task here is to write a program that 
given the name of a text file is able to write its content with each sentence 
on a separate line.
 
Test your program with the following short text: 
Mr. Smith bought cheapsite.com for 1.5 
million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks 
he didn't. In any case, this isn't true... Well, with a probability of .9 it 
isn't. The result should be:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for
it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
  Well, with a probability of .9 it isn't. '''

import re

#Number 11
text = '"Droll?" said Mr. Newman, laughing too. "Did you ever hear of Christopher Columbus?"'
text2 = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
#splits the sentence following patterns in the parenteses
sep = re.split('(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s' , text)

#Prints the string following the pattern listed above in a new line
for i in sep :
    print(i + '\n')


#Problem 12

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
            del anagram_dict[m] #delets the current set to run the next one
            m = max(anagram_dict, key = lambda x: len(anagram_dict[x])) #run the set of anagrams
        

anagram_sets(filename)


#Problem 13

''' Your task in this exercise is as follows:  a. Generate a string with N 
opening brackets ("[") and N closing brackets ("]"), in some arbitrary order. 
b. Determine whether the generated string is balanced; that is, whether it 
consists entirely of pairs of  opening/closing brackets (in that order), none 
of which mis-nest'''
import random
#function that takes an integer n as a parameter
def string_gen(n):
    string = '' #create an empty string
    for i in range(2*n): #doubles the integer because the strings go in pairs               
        if random.randint(0,1) == 0:    #generates random number between 0 and 1 
            string += '[' #add [  to the string if the generated num = 0
        else: 
            string += ']' #add ] otherwise
    return(string)
#a function that checks if the generated string is balanced
def check(string):
    counter = 0 #
    for i in range (len(string)):     #loops through the length of string
        if string[i] == '[':          #the string at ith position is '[' 
            counter += 1              #increment counter by 1
        else:                         #decrease counter by 1 otherwise       
            counter -= 1 
            if counter < 0:            #counter < 0 is unbalanced therefore quit
                break
            
    if counter == 0:                  #string is balanced when counter = 0
        print(string, '\nOk')
    else:                               #unbalanced otherwise
        print(string, '\nNotOk')

check(string_gen(0))
check(string_gen(1))
check(string_gen(2))
check(string_gen(3))

#Pokemon

"""
    Given a list of possible names, this function generates the/a sequence with
    the highest possible number of Pokemon names where the subsequent name 
    starts with the final letter of the preceding name. No Pokemon name is to
    be repeated. 
    """
pokeList = ["audino","bagon","baltoy","banette","bidoof", "braviary", "bronzor", 
"carracosta","charmeleon","cresselia", "croagunk", "darmanitan", "deino", "emboar", 
"emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus", "heatmor", 
"heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan","kricketune", "landorus", 
"ledyba", "loudred", "lumineon", "lunatone", "machamp", "magnezone", "mamoswine",
"nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath", "poochyena", 
"porygon2", "porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye", 
"scolipede", "scrafty", "seaking", "sealeo", "silcoon", "simisear", "snivy", 
"snorlax", "spoink", "starly", "tirtouga", "trapinch", "treecko","tyrogue", 
"vigoroth", "vulpix", "wailord", "wartortle","whismur","wingull" ,"yamask"]

finalList = [] #create an empty list to store the element of final list

def main(): 
    global finalList

    solve([])

    print(len(finalList)) ##print the length of final list 
    print("The elements are :") 
    for name in finalList: ##search for the name in the final list then print them
        print(name)

def solve(newList): #newList is an empty list

    global finalList
    flag = 0    #hints to track if the conditions are met for the game
    for name in pokeList:   #loop through the names  in the pokemon list
        if((len(newList) == 0) or (name not in newList and (name[0] == newList[-1][-1]))): #check if the newList is empty or if the name is not one of its elments(to avoid repeats) and the first element is = to the last
            flag =1 #set to 1 if the above conditions are met
            newList.append(name) #add the name to the newlist
            solve(newList)
            newList.pop() #pops the name for backtracking
    

    if(flag == 0): #means that none of the element met the condition
        if (len(newList) > len(finalList)): #check to compare the size of new and final list. IF yes, then the newlist becomes the final list
            finalList = list(newList)


main();

#Problem 14
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

    



