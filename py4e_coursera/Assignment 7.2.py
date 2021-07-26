# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:31:25 2021

@author: Teacher
"""

fname = input('Enter the file name:  ')
fhand = open(fname)
sum = 0.0
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
        sum += float(line[21:])
        count += 1
        print(line)
print('total:',sum,'avarage:',sum/count)