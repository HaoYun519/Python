# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:57:24 2021

@author: Teacher
"""

# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and 
# count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

import re
filename = input('Enter the filename: ')
regex = input('Enter a regular expression: ')

counter = 0
fhand = open(filename, 'r')
for line in fhand:
    if re.search(regex, line):
        counter += 1
        
print(counter)