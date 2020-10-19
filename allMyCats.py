#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:19:00 2020

@author: sg24x7
"""

catNames = []
while True:
    print('Enter the name of '+str(len(catNames)+1) + ' (Or nothing to stop)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
print('The cat names are :')
for name in catNames:
    print('' + name)