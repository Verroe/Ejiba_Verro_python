# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:25:15 2016

@author: verroejiba
"""
#Verro Ejiba Group A Homework 1 Due 9/15/2016
import os 
import io
print(os.getcwd()) #Check the working directory 
os.chdir(input('Enter new directory: ')) #Change to the desired directory

#Solution to number 1
#A function to open and read the file to read to be checked for palindrome
def openFile(filename):
    file = open('filename.txt')
    file.read().split()
    
#Input your file name
openFile(input('Enter file name: '))

for word in openFile(input('Enter file name: ')):
    #check for palindrome
        word = "radar"
        reverse = word[::-1] #write the words backward
        if word == reverse:
            print(word, 'is a palindrome')
        else:
            print(word, 'is not a palindrome')
            
#Solution to number 5: Print all hapaxes in a given file name text

#A function that find all the hapaxes
#given the following text check for the word that appears once
sent = "Life is beautiful and it is life" 
#Changes all capital letters to lowercase and
#Separates the sentence in words
wlist = sent.lower().split() 
newlist = set() #A new set to store words one time
rlist = set() #A set to store all the words that have been removed
#def hapax(openFile(input('Enter file name: ')))
for word in wlist: 
    if word not in newlist:
        newlist.add(word) #Add nonrepeated words to the new set
    else:
        rlist.add(word) #Add all duplicate to remove set
    if word in rlist:
        newlist.remove(word) #Remove words that appear in the 2 sets
print(newlist)

#Solution to number 6: Number lines on the copied version of a specific file
example = '''Love your neighbor as you love yourself
             This is the command from the Lord of Israel 
             Put your trust and whole heart in it '''

#open the desired file
file = openFile(input('Enter file name: ')) 
#make copy from the existing one
nfile = file.copy() 
nlines = len(io.readline(example))  #Get the number of lines
for line in example:
    enumerate(line, start=1)
print(nlines)

#Solution to number 7: Average word length of a text

avgFile = openFile(input('Enter file naem: '))
sep = avgFile.split()#splits the words in order to ignore spaces
newset = set() #Created set that will take all the non repeated words not
total = len(sep) #Count the total number of words 
count = 0
for word in sep: 
    if word not in newset: #counts and adds the word not in the new set
        count += len(word)
        newset.add(word)
    else: #counts the repeated words
        count += len(word)
        
avg = (count)/total # calculates the average word length
    
print(count, total, avg)
    



