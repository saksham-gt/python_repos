#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:29:18 2020

@author: sg24x7
"""

# Matching zero or more with a star.
import re

# the group that precedes * (here, wo) can be repeated any number of times or can be completely absent.
batregex = re.compile(r'bat(wo)*man')
mo1 = batregex.search('This is batman.')
mo2 = batregex.search('This is batwoman.')
mo3 = batregex.search('This is batwowowowowoman.')

print(mo1.group())
print(mo2.group())
print(mo3.group())

# Matching one or more with plus

# here it is important for group that precedes + to appear atleast once.
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('This is Batwoman.')
mo2 = batRegex.search('This is Batwowoman.')
mo3 = batRegex.search('This is Batman.')

print(mo1.group())
print(mo2.group())
#print(mo3.group())                  # here it wont show any output as wo is absent feom mo3.

# Matching Specific Repetitions with Braces
# Regex Ha{3} = (Ha)(Ha)(Ha)
# Regex Ha{3, 5} = (Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)(Ha)
haRegex =re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHakjdfj')
mo2 = haRegex.search('Ha')
print(mo1.group())
print(mo2 == None)