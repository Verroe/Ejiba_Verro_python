# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:22:10 2016

@author: verroejiba
"""
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