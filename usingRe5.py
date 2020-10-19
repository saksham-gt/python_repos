#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:28:25 2020

@author: sg24x7
"""

import re

# Character Class
xmas = re.compile(r'\d+\s\w+')      # one or more numeric digits then one space or sth and then one or more character (by \w)
print(xmas.findall('12 drummers, 11 pipers, 10 lords, 9 maids, 8 ladies, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# making my own character class using square brackets 
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# for creating character classes in a range using hyphen(-)
vowelRegex = re.compile(r'[a-zA-z]')        # also, no need of escape character ., *, (), ? inside the square brackets.
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))

# for negative character class use ^
consonantRegex = re.compile(r'[^AEIOUaeiou]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD'))

# ^ for the string pattern to be at beginning and $ for the string to be at the end of the searching string.
beginwithHello = re.compile(r'^Hello')
reg = beginwithHello.search('Hello, World!')
print(reg.group())

endwithNum = re.compile(r'\d$')
reg = endwithNum.search('Your number is 42')
print(reg.group())

# using ^ and $ both in same example
both = re.compile(r'^\d+$')
reg = both.search('1234567890')
print(reg.group())