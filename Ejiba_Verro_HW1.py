# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:25:15 2016

@author: verroejiba
"""
import os 
import linecache
print(os.getcwd())
os.chdir(input('Enter new directory: '))

#Solution to number 1
#A function to open and read the file to read to be checked for palindrome
def openFile(filename):
    file = open('filename.txt')
    file.read()
    file.split()
    #file.write()
    
#Input your file name
openFile(input('Enter file name: '))

for word in openFile(input('Enter file name: ')):
    #check for palindrome
        word = "radar"
        reverse = word[::-1]
        if word == reverse:
            print(word, 'is a palindrome')
        else:
            print(word, 'is not a palindrome')
            
#Solution to number 5: Print all hapaxes in a given file name text

#A function that find all the hapaxes
#given the following text check for the word that appears once
sent = "Life is beautiful and it is life" 
locase = sent.lower() #writes all the uppercase letters in lowercase
wlist = locase.split() #Separates the sentence in words
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
for line in nfile:
    enumerate(line)
print(nfile)
    
    



