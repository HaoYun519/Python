# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:45:22 2021

@author: Teacher
"""

fname = input('Enter the file name:  ')
fhand = open(fname)
email_addresses = {}

for line in fhand:
    if line.startswith('From ') : 
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1
        # print(email_addresses[email])
print(email_addresses)