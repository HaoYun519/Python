# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:43:00 2021

@author: Teacher
"""

fname = input('Enter the file name:  ')
fhand = open(fname)
domains = {}

for line in fhand:
    if line.startswith('From ') :
        email = line.split()[1]
        domain = email.split('@')[1]
        domains[domain] = domains.get(domain, 0) + 1
print(domains)