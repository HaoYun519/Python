# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:24:55 2021

@author: Teacher
"""
import re

fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    words = re.findall('^From (\S+@\S+)',line)
    count += 1
    print(words)
print('There were ',count,' lines in the file with From as the first word')