#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:34:35 2020

@author: sg24x7
"""

name = ''
while not name:
    print('Enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #If numOFGuests is not 0 then the condition is true
    print('Be sure to have enough room for all your guests.')
print('Done')