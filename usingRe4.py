#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:47:22 2020

@author: sg24x7
"""

import re

# Greddy and non Greedy matching

# greedy matching

greedym = re.compile(r'(Ha){3,5}')     # python is greedy by default i.e. it searches for longest string by default.
mo1 = greedym.search('HaHaHaHaHa')
print(mo1.group())

# non-greedy matching
nongreedym = re.compile(r'(Ha){3,5}?')  # we put '?' in the end of searching pattern fr non greedy matching i.e. shortest string search
mo2 = nongreedym.search('HaHaHaHaHa')
print(mo2.group())

# using findall()
# search() returns only the first matched text but findall() returns all such strings
phoneNum = re.compile(r'(\d\d\d-)(\d\d\d-\d\d\d\d)')
mo = phoneNum.search('Phone : 425-555-4242, Cell : 256-859-6648')
print(mo.group())               # group() stops when it searches the first string hat matches the pattern. 
# findall will return a list of strings when no groups have been allocated.
# if there are groups then findall() will return a list of tuples.
x = phoneNum.findall('Phone : 425-555-4242, Cell : 256-859-6648')
print(x)