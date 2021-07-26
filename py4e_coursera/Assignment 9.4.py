# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:50:57 2021

@author: Teacher
"""

fname = input('Enter the file name:  ')
fhand = open(fname)
email_addresses = {}

for line in fhand:
    if line.startswith('From ') : 
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1

max_address = None
max_emails=0
for k in email_addresses :
    if email_addresses[k] > max_emails:
        max_address = k
        max_emails = email_addresses[k]

print(max_address,max_emails)