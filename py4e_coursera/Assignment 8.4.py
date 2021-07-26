# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:05:09 2021

@author: Teacher
"""

fname = input("Enter file name: ")
fh = open(fname)
data=[]
for each in fh:
    words=each.split()
    for word in words:
        if word not in data:
            data.append(word)
print(sorted(data))